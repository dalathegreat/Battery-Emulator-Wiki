#!/usr/bin/env python3
"""
Report image files that nothing in the repository references.

Runs manually. It scans every text file in the repository for mentions of
each image, so an image is only called orphaned when its name appears
nowhere — in Markdown, in mkdocs.yml, in theme overrides or in CSS.

The scan deliberately errs towards under-reporting: a file that is
mentioned anywhere at all is treated as used.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

IMAGES_DIR = Path(os.environ.get("IMAGES_DIR", "docs/images"))
DOCS_DIR = Path(os.environ.get("DOCS_DIR", "docs"))

IMAGE_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg", ".avif", ".ico",
    ".tif", ".tiff",
}
# Files that can plausibly reference an image
TEXT_EXTS = {
    ".md", ".markdown", ".yml", ".yaml", ".html", ".htm", ".css", ".js",
    ".json", ".txt", ".toml", ".cfg", ".ini",
}
SKIP_DIRS = {".git", ".github", "node_modules", "site", "venv", ".venv"}
# The report this script writes must never become part of its own corpus
ORPHAN_LIST = Path(os.environ.get("ORPHAN_LIST", "orphans.txt"))

RE_MD_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)>\s]+)>?(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)")
RE_HTML_SRC = re.compile(r"<img\b[^>]*?\bsrc\s*=\s*([\"'])(.*?)\1", re.IGNORECASE | re.DOTALL)


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.resolve() == ORPHAN_LIST.resolve():
            continue
        if path.is_file():
            yield path


def build_corpus() -> str:
    """Every text file in the repo, concatenated, excluding the image dir."""
    chunks: list[str] = []
    for path in iter_files(Path(".")):
        if path.suffix.lower() not in TEXT_EXTS:
            continue
        try:
            chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
    return "\n".join(chunks)


def name_variants(name: str) -> set[str]:
    """A file may be written plainly or percent-encoded."""
    return {name, name.replace(" ", "%20"), name.replace(" ", "+")}


def find_orphans(corpus: str) -> list[tuple[Path, int]]:
    images = [
        path
        for path in iter_files(IMAGES_DIR)
        if path.suffix.lower() in IMAGE_EXTS
    ]
    # Duplicate basenames need a longer needle to stay unambiguous
    seen: dict[str, int] = {}
    for image in images:
        seen[image.name] = seen.get(image.name, 0) + 1

    orphans: list[tuple[Path, int]] = []
    for image in sorted(images):
        if seen[image.name] > 1:
            needles = name_variants(f"{image.parent.name}/{image.name}")
        else:
            needles = name_variants(image.name)
        if not any(needle in corpus for needle in needles):
            orphans.append((image, image.stat().st_size))
    return orphans


def find_broken(md_files: list[Path]) -> list[tuple[Path, str]]:
    """Markdown pointing at a local image that does not exist."""
    broken: list[tuple[Path, str]] = []
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        targets = [match.group(1) for match in RE_MD_IMAGE.finditer(text)]
        targets += [match.group(2) for match in RE_HTML_SRC.finditer(text)]
        for target in targets:
            if urlparse(target).scheme in ("http", "https", "data", "mailto"):
                continue
            clean = unquote(target.split("#")[0].split("?")[0]).strip()
            if not clean:
                continue
            if clean.startswith("/"):
                resolved = DOCS_DIR / clean.lstrip("/")
            else:
                resolved = md_file.parent / clean
            if not resolved.exists():
                broken.append((md_file, target))
    return broken


def human(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB"):
        if value < 1024 or unit == "MB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} MB"


def main() -> int:
    if not IMAGES_DIR.is_dir():
        print(f"No such directory: {IMAGES_DIR}")
        return 0

    corpus = build_corpus()
    orphans = find_orphans(corpus)
    md_files = [
        path for path in iter_files(DOCS_DIR) if path.suffix.lower() == ".md"
    ]
    broken = find_broken(md_files)

    lines = [f"## Orphaned image scan — `{IMAGES_DIR}`", ""]

    if orphans:
        total = sum(size for _, size in orphans)
        lines += [
            f"**{len(orphans)} image(s) not referenced anywhere** "
            f"({human(total)} reclaimable).",
            "",
            "| Image | Size |",
            "| --- | --- |",
        ]
        lines += [f"| `{path.as_posix()}` | {human(size)} |" for path, size in orphans]
    else:
        lines.append("✅ Every image is referenced.")

    if broken:
        lines += [
            "",
            f"### ⚠️ {len(broken)} reference(s) to a missing file",
            "",
            "| Markdown file | Target |",
            "| --- | --- |",
        ]
        lines += [f"| `{md.as_posix()}` | `{target}` |" for md, target in broken]

    lines += [
        "",
        f"<sub>Scanned {len(md_files)} Markdown file(s). An image counts as used "
        f"if its filename appears in any text file, so anything referenced from "
        f"`mkdocs.yml`, theme overrides or CSS is kept.</sub>",
    ]

    report = "\n".join(lines)
    print(report)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        Path(summary).write_text(report + "\n", encoding="utf-8")

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"orphan_count={len(orphans)}\n")
            handle.write(f"broken_count={len(broken)}\n")

    ORPHAN_LIST.write_text(
        "\n".join(path.as_posix() for path, _ in orphans), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
