#!/usr/bin/env python3
"""
Normalize external images referenced from Markdown files in a pull request.

For every changed .md file in the PR:
  * find image references pointing at an external URL
    (GitHub user-attachments, raw.githubusercontent, any http(s) image)
  * download it
  * downscale to MAX_WIDTH if it is wider
  * store it in IMAGES_DIR under a name derived from the .md file name,
    numbered in sequence, never overwriting an existing file
  * rewrite the reference in the .md to a relative link to the new file

The result is committed to the PR branch and summarized in a PR comment.
"""

from __future__ import annotations

import hashlib
import io
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
from PIL import Image

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

API = "https://api.github.com"
TOKEN = os.environ["GITHUB_TOKEN"]
BASE_REPO = os.environ["BASE_REPO"]
PR_NUMBER = os.environ["PR_NUMBER"]
HEAD_REF = os.environ["HEAD_REF"]

MAX_WIDTH = int(os.environ.get("MAX_WIDTH", "1200"))
IMAGES_DIR = Path(os.environ.get("IMAGES_DIR", "docs/images"))
SKIP_HOSTS = {
    h.strip().lower()
    for h in os.environ.get("SKIP_HOSTS", "").split(",")
    if h.strip()
}

MAX_DOWNLOAD_BYTES = 40 * 1024 * 1024
COMMENT_MARKER = "<!-- pr-image-normalizer -->"

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "battery-emulator-wiki-image-normalizer"})

GH = requests.Session()
GH.headers.update(
    {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "battery-emulator-wiki-image-normalizer",
    }
)

# --------------------------------------------------------------------------
# Reference patterns
# --------------------------------------------------------------------------

# ![alt](url "title")
RE_MD_IMAGE = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\(\s*<?(?P<url>[^)>\s]+)>?"
    r"(?P<title>\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
# <img src="url" ...>
RE_HTML_IMAGE = re.compile(
    r"<img\b[^>]*?\bsrc\s*=\s*(?P<q>[\"'])(?P<url>.*?)(?P=q)[^>]*?>",
    re.IGNORECASE | re.DOTALL,
)
# [label]: url  (reference definitions)
RE_REF_DEF = re.compile(
    r"^(?P<lead>[ \t]{0,3}\[(?P<label>[^\]]+)\]:[ \t]*)(?P<url>\S+)",
    re.MULTILINE,
)
# A bare attachment URL on its own — GitHub renders these as images
RE_BARE_ATTACHMENT = re.compile(
    r"https://github\.com/user-attachments/assets/[0-9A-Za-z._-]+"
)

IMAGE_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg", ".avif", ".tif", ".tiff",
}

PIL_EXT = {
    "PNG": ".png",
    "JPEG": ".jpg",
    "GIF": ".gif",
    "WEBP": ".webp",
    "BMP": ".bmp",
    "TIFF": ".tiff",
}


@dataclass
class Change:
    md_file: str
    url: str
    new_path: str
    original_size: tuple[int, int] | None
    new_size: tuple[int, int] | None
    resized: bool
    reused: bool = False


@dataclass
class State:
    reserved: set[str] = field(default_factory=set)
    by_url: dict[str, str] = field(default_factory=dict)
    by_hash: dict[str, str] = field(default_factory=dict)
    changes: list[Change] = field(default_factory=list)
    failures: list[tuple[str, str, str]] = field(default_factory=list)


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------


def log(msg: str) -> None:
    print(msg, flush=True)


def run(*args: str) -> str:
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout.strip()


def changed_markdown_files() -> list[str]:
    files: list[str] = []
    page = 1
    while True:
        response = GH.get(
            f"{API}/repos/{BASE_REPO}/pulls/{PR_NUMBER}/files",
            params={"per_page": 100, "page": page},
            timeout=30,
        )
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break
        for item in batch:
            if item.get("status") == "removed":
                continue
            name = item.get("filename", "")
            if name.lower().endswith(".md"):
                files.append(name)
        if len(batch) < 100:
            break
        page += 1
    return files


def is_external(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False
    if parsed.netloc.lower() in SKIP_HOSTS:
        return False
    return True


def looks_like_image(url: str) -> bool:
    parsed = urlparse(url)
    if "user-attachments/assets" in parsed.path:
        return True
    return Path(unquote(parsed.path)).suffix.lower() in IMAGE_EXTS


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value or "image"


def download(url: str) -> bytes:
    last_error: Exception | None = None
    for _ in range(3):
        try:
            response = SESSION.get(url, timeout=60, stream=True)
            response.raise_for_status()
            buffer = io.BytesIO()
            for chunk in response.iter_content(64 * 1024):
                buffer.write(chunk)
                if buffer.tell() > MAX_DOWNLOAD_BYTES:
                    raise RuntimeError("file larger than 40 MB")
            return buffer.getvalue()
        except Exception as error:  # noqa: BLE001 - retried below
            last_error = error
    raise RuntimeError(str(last_error))


def process_image(data: bytes) -> tuple[bytes, str, tuple[int, int] | None, tuple[int, int] | None, bool]:
    """Return (bytes, extension, original size, new size, resized)."""
    head = data[:400].lstrip()
    if head.startswith(b"<?xml") or head.startswith(b"<svg") or b"<svg" in head:
        return data, ".svg", None, None, False

    with Image.open(io.BytesIO(data)) as image:
        fmt = (image.format or "").upper()
        extension = PIL_EXT.get(fmt)
        original = image.size
        animated = getattr(image, "n_frames", 1) > 1

        if extension is None:
            raise RuntimeError(f"unsupported image format: {fmt or 'unknown'}")
        if original[0] <= MAX_WIDTH or animated:
            return data, extension, original, original, False

        height = max(1, round(original[1] * MAX_WIDTH / original[0]))
        resized = image.convert("RGBA") if fmt == "PNG" and image.mode == "P" else image.copy()
        resized = resized.resize((MAX_WIDTH, height), Image.LANCZOS)

        output = io.BytesIO()
        if fmt == "JPEG":
            resized.convert("RGB").save(output, "JPEG", quality=88, optimize=True, progressive=True)
        elif fmt == "PNG":
            resized.save(output, "PNG", optimize=True)
        elif fmt == "WEBP":
            resized.save(output, "WEBP", quality=88, method=4)
        else:
            resized.save(output, fmt)
        return output.getvalue(), extension, original, (MAX_WIDTH, height), True


def allocate_name(md_file: str, extension: str, state: State) -> Path:
    """Sequential name derived from the .md file, never colliding with an
    existing file — the sequence is shared across extensions."""
    stem = slugify(Path(md_file).stem)
    index = 1
    while True:
        base = f"{stem}-{index:02d}"
        taken = base.lower() in state.reserved or any(
            IMAGES_DIR.glob(f"{base}.*")
        )
        if not taken:
            state.reserved.add(base.lower())
            return IMAGES_DIR / f"{base}{extension}"
        index += 1


def relative_link(target: Path, md_file: str) -> str:
    relative = os.path.relpath(target, Path(md_file).parent)
    return Path(relative).as_posix()


# --------------------------------------------------------------------------
# Core
# --------------------------------------------------------------------------


def collect_urls(text: str) -> list[tuple[int, int, str, str]]:
    """Collect (start, end, url, kind) spans of external image references."""
    spans: list[tuple[int, int, str, str]] = []

    def add(match: re.Match, kind: str) -> None:
        url = match.group("url").strip()
        if is_external(url) and looks_like_image(url):
            spans.append((match.start("url"), match.end("url"), url, kind))

    for match in RE_MD_IMAGE.finditer(text):
        add(match, "markdown")
    for match in RE_HTML_IMAGE.finditer(text):
        add(match, "html")
    for match in RE_REF_DEF.finditer(text):
        add(match, "reference")
    for match in RE_BARE_ATTACHMENT.finditer(text):
        spans.append((match.start(), match.end(), match.group(0), "bare"))

    # Drop overlaps — a bare URL already covered by a markdown or HTML tag
    # keeps the richer match, which is added first and wins on a stable sort.
    spans.sort(key=lambda item: (item[0], -item[1]))
    result: list[tuple[int, int, str, str]] = []
    last_end = -1
    for span in spans:
        if span[0] >= last_end:
            result.append(span)
            last_end = span[1]
    return result


def fetch_and_store(url: str, md_file: str, state: State) -> str:
    """Download/process an image and return its repository-relative path."""
    if url in state.by_url:
        return state.by_url[url]

    data = download(url)
    data, extension, original, new_size, resized = process_image(data)

    digest = hashlib.sha256(data).hexdigest()
    if digest in state.by_hash:
        target = state.by_hash[digest]
        state.by_url[url] = target
        state.changes.append(
            Change(md_file, url, target, original, new_size, resized, reused=True)
        )
        return target

    target_path = allocate_name(md_file, extension, state)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_bytes(data)

    target = target_path.as_posix()
    state.by_url[url] = target
    state.by_hash[digest] = target
    state.changes.append(Change(md_file, url, target, original, new_size, resized))
    log(f"  {url} -> {target}")
    return target


def process_markdown(md_file: str, state: State) -> bool:
    path = Path(md_file)
    if not path.is_file():
        return False

    text = path.read_text(encoding="utf-8")
    spans = collect_urls(text)
    if not spans:
        return False

    log(f"{md_file}: {len(spans)} external image reference(s)")
    pieces: list[str] = []
    cursor = 0
    changed = False

    for start, end, url, kind in spans:
        try:
            target = fetch_and_store(url, md_file, state)
        except Exception as error:  # noqa: BLE001 - reported in the PR comment
            log(f"  !! {url}: {error}")
            state.failures.append((md_file, url, str(error)))
            continue

        link = relative_link(Path(target), md_file)
        # Only a standalone URL needs image syntax added around it; every
        # other kind is already inside a link or tag.
        replacement = f"![]({link})" if kind == "bare" else link

        pieces.append(text[cursor:start])
        pieces.append(replacement)
        cursor = end
        changed = True

    if not changed:
        return False

    pieces.append(text[cursor:])
    path.write_text("".join(pieces), encoding="utf-8")
    return True


def build_comment(state: State) -> str:
    lines = [
        COMMENT_MARKER,
        "### 🖼️ Images normalized",
        "",
        f"External images referenced from the changed Markdown files were downloaded, "
        f"downscaled to max **{MAX_WIDTH}px** wide where needed, moved to `{IMAGES_DIR}/` "
        f"and relinked. The changes are pushed to this branch.",
        "",
        "| Markdown file | Source | New file | Size |",
        "| --- | --- | --- | --- |",
    ]
    for change in state.changes:
        source = urlparse(change.url).path.rsplit("/", 1)[-1] or urlparse(change.url).netloc
        source = f"[{source[:40]}]({change.url})"
        if change.original_size and change.new_size:
            if change.resized:
                size = f"{change.original_size[0]}×{change.original_size[1]} → {change.new_size[0]}×{change.new_size[1]}"
            else:
                size = f"{change.original_size[0]}×{change.original_size[1]} (unchanged)"
        else:
            size = "vector (unchanged)"
        if change.reused:
            size += " · deduplicated"
        lines.append(f"| `{change.md_file}` | {source} | `{change.new_path}` | {size} |")

    if state.failures:
        lines += ["", "#### ⚠️ Could not be processed", ""]
        for md_file, url, error in state.failures:
            lines.append(f"- `{md_file}`: {url} — {error}")
        lines.append("")
        lines.append("Please attach these manually under `docs/images/`.")

    lines += [
        "",
        "<sub>If anything looks wrong, just amend the commit — this check only touches "
        "images that still point outside the repository.</sub>",
    ]
    return "\n".join(lines)


def upsert_comment(body: str) -> None:
    response = GH.get(
        f"{API}/repos/{BASE_REPO}/issues/{PR_NUMBER}/comments",
        params={"per_page": 100},
        timeout=30,
    )
    response.raise_for_status()
    for comment in response.json():
        if COMMENT_MARKER in (comment.get("body") or ""):
            GH.patch(
                f"{API}/repos/{BASE_REPO}/issues/comments/{comment['id']}",
                json={"body": body},
                timeout=30,
            ).raise_for_status()
            return
    GH.post(
        f"{API}/repos/{BASE_REPO}/issues/{PR_NUMBER}/comments",
        json={"body": body},
        timeout=30,
    ).raise_for_status()


def commit_and_push() -> None:
    run("git", "config", "user.name", "github-actions[bot]")
    run(
        "git",
        "config",
        "user.email",
        "41898282+github-actions[bot]@users.noreply.github.com",
    )
    run("git", "add", "-A")
    if not subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode:
        log("Nothing staged.")
        return
    run("git", "commit", "-m", "docs: move external images to docs/images and relink")
    run("git", "push", "origin", f"HEAD:refs/heads/{HEAD_REF}")


def main() -> int:
    md_files = changed_markdown_files()
    if not md_files:
        log("No Markdown files changed.")
        return 0

    log(f"Changed Markdown files: {len(md_files)}")
    state = State()
    touched = [name for name in md_files if process_markdown(name, state)]

    if not state.changes and not state.failures:
        log("No external images found.")
        return 0

    if touched:
        try:
            commit_and_push()
        except RuntimeError as error:
            log(f"Push failed: {error}")
            upsert_comment(
                f"{COMMENT_MARKER}\n### 🖼️ Images could not be normalized\n\n"
                f"{len(state.changes)} external image(s) were found, but the changes "
                f"could not be pushed to this branch.\n\n"
                f"Enable **Allow edits by maintainers** on this PR, or move the images "
                f"to `{IMAGES_DIR}/` manually.\n\n<details><summary>Details</summary>\n\n"
                f"```\n{error}\n```\n\n</details>"
            )
            return 1

    upsert_comment(build_comment(state))
    return 0


if __name__ == "__main__":
    sys.exit(main())
