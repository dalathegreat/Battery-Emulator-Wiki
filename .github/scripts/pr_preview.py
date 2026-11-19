#!/usr/bin/env python3
"""
Publish, announce and remove pull request previews of the MkDocs site.

Previews live on the gh-pages branch under pr-preview/pr-<N>/, next to the
published site. Called from .github/workflows/pr-preview-deploy.yml. The
built site handed to `publish` comes from an untrusted PR build and is
treated strictly as data: it is copied, compared and text-rewritten, never
executed.

Subcommands
  publish  Copy a built preview into a gh-pages checkout. Media files that
           are byte-identical to the published site are not copied again;
           the preview's pages link to the published copy instead. A preview
           then costs ~15 MiB instead of the full ~200 MiB site, which keeps
           gh-pages well under the 1 GB GitHub Pages limit.
  comment  Create or update the single preview comment on the PR.
  remove   Delete one preview, or every preview whose PR is no longer open.
  rebuild  Restart the PR's latest preview build, once it is finished.
           Used by the image normalizer when it is done and by the
           `/preview` comment command; a restarted build always builds the
           PR's latest commit.
"""

from __future__ import annotations

import argparse
import filecmp
import json
import os
import posixpath
import re
import shutil
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote, urlparse

PREVIEW_ROOT = "pr-preview"
BUILD_WORKFLOW = "pr-preview-build.yml"
COMMAND = "/preview"
MARKER = "<!-- pr-preview -->"
LIVE_MARKER = "<!-- pr-preview: live -->"   # a preview is currently published

# Only static attachments are shared with the live site. Pages, theme assets,
# the search index and the sitemap always come from the preview build.
SHARED_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg", ".bmp",
    ".ico", ".tif", ".tiff", ".pdf", ".drawio", ".excalidraw", ".zip",
    ".7z", ".gz", ".mp4", ".webm", ".mov", ".mp3", ".wav", ".bin",
}
NEVER_SHARED_DIRS = ("assets/", PREVIEW_ROOT + "/")

URL_ATTR_RE = re.compile(
    r"""(\s(?:src|href|poster|data-src)\s*=\s*)(["'])([^"'<>]*)\2""", re.I)
SRCSET_RE = re.compile(r"""(\ssrcset\s*=\s*)(["'])([^"'<>]*)\2""", re.I)
HEAD_RE = re.compile(r"<head(?:\s[^>]*)?>", re.I)
ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
NOINDEX = '<meta name="robots" content="noindex, nofollow">'


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def preview_url(site_url: str, pr: int) -> str:
    return f"{site_url.rstrip('/')}/{PREVIEW_ROOT}/pr-{pr}/"


def mib(n: int) -> str:
    return f"{n / 1048576:.1f} MiB"


def github(method: str, path: str, body: dict | None = None):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "pr-preview",
        },
    )
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    return json.loads(data) if data else None


def github_list(path: str) -> list:
    items, page = [], 1
    sep = "&" if "?" in path else "?"
    while True:
        batch = github("GET", f"{path}{sep}per_page=100&page={page}")
        items += batch
        if len(batch) < 100:
            return items
        page += 1


# --------------------------------------------------------------------------
# publish
# --------------------------------------------------------------------------

def is_shared(rel: str, src: Path, live_root: Path) -> bool:
    """True when the published site already serves an identical copy."""
    if Path(rel).suffix.lower() not in SHARED_EXT:
        return False
    if rel.startswith(NEVER_SHARED_DIRS):
        return False
    live = live_root / rel
    if live.is_symlink() or not live.is_file():
        return False
    if live.stat().st_size != src.stat().st_size:
        return False
    return filecmp.cmp(live, src, shallow=False)


def rewrite_html(text: str, page_dir: str, shared: set[str], live_base: str) -> str:
    """Point links to shared files at the published copy and add noindex."""

    def relink(url: str) -> str:
        if (not url or url.startswith(("#", "/", "data:", "mailto:", "javascript:"))
                or "://" in url):
            return url
        cut = min((i for i in (url.find("?"), url.find("#")) if i >= 0),
                  default=len(url))
        path, suffix = url[:cut], url[cut:]
        target = posixpath.normpath(posixpath.join(page_dir, path))
        if target.startswith("..") or unquote(target) not in shared:
            return url
        return live_base + target + suffix

    def attr(m: re.Match) -> str:
        return f"{m.group(1)}{m.group(2)}{relink(m.group(3))}{m.group(2)}"

    def srcset(m: re.Match) -> str:
        parts = []
        for candidate in m.group(3).split(","):
            bits = candidate.strip().split(None, 1)
            if bits:
                bits[0] = relink(bits[0])
            parts.append(" ".join(bits))
        return f"{m.group(1)}{m.group(2)}{', '.join(parts)}{m.group(2)}"

    text = URL_ATTR_RE.sub(attr, text)
    text = SRCSET_RE.sub(srcset, text)
    return HEAD_RE.sub(lambda m: m.group(0) + NOINDEX, text, count=1)


def cmd_publish(args) -> int:
    src_root = Path(args.preview).resolve()
    live_root = Path(args.pages).resolve()
    dest = live_root / PREVIEW_ROOT / f"pr-{args.pr}"
    live_base = urlparse(args.site_url).path.rstrip("/") + "/"

    files: list[tuple[str, Path]] = []
    for dirpath, dirnames, filenames in os.walk(src_root, followlinks=False):
        for name in filenames:
            path = Path(dirpath) / name
            if path.is_symlink() or not path.is_file():
                print(f"::warning::Skipping non-regular file {path.relative_to(src_root)}")
                continue
            files.append((path.relative_to(src_root).as_posix(), path))
    if not any(rel == "index.html" for rel, _ in files):
        print("::error::The preview artifact has no index.html")
        return 1

    shared = {rel for rel, path in files if is_shared(rel, path, live_root)}

    if dest.exists():
        shutil.rmtree(dest)
    copied = shared_bytes = 0
    for rel, path in files:
        if rel in shared:
            shared_bytes += path.stat().st_size
            continue
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        if rel.endswith(".html"):
            text = path.read_text(encoding="utf-8", errors="surrogateescape")
            page_dir = posixpath.dirname(rel)
            out.write_text(rewrite_html(text, page_dir, shared, live_base),
                           encoding="utf-8", errors="surrogateescape")
        else:
            shutil.copyfile(path, out)
        copied += out.stat().st_size

    summary = (f"Preview pr-{args.pr}: {len(files) - len(shared)} files, "
               f"{mib(copied)} published; {len(shared)} unchanged files "
               f"({mib(shared_bytes)}) served from the live site")
    print(summary)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as fh:
            fh.write(summary + "\n")
    return 0


# --------------------------------------------------------------------------
# comment
# --------------------------------------------------------------------------

def changed_pages(repo: str, pr: int) -> list[tuple[str, str]]:
    """(docs-relative .md path, preview-relative URL) of the PR's pages."""
    pages = []
    for f in github_list(f"/repos/{repo}/pulls/{pr}/files"):
        name = f["filename"]
        if (f["status"] == "removed" or not name.startswith("docs/")
                or not name.endswith(".md") or name.startswith("docs/overrides/")):
            continue
        rel = name[len("docs/"):]
        stem = rel[:-len(".md")]
        if posixpath.basename(stem) in ("index", "README"):
            url = posixpath.dirname(stem)
            url = url + "/" if url else ""
        else:
            url = stem + "/"
        pages.append((rel, url))
    return sorted(pages)


def clean_log_line(line: str) -> str:
    line = ANSI_RE.sub("", line).rstrip()
    return line.replace("```", "'''")[:400]


def log_excerpt(log: Path | None, wanted: list[str] | None, limit: int = 20) -> list[str]:
    """Warnings mentioning one of `wanted`, or the log tail when None."""
    if not log or not log.is_file():
        return []
    lines = [clean_log_line(l) for l in log.read_text(errors="replace").splitlines()]
    if wanted is None:
        picked = [l for l in lines if re.match(r"(ERROR|WARNING|Error|Traceback)", l)]
        return (picked or lines)[-limit:]
    return [l for l in lines
            if l.startswith("WARNING") and any(f"'{w}'" in l for w in wanted)][:limit]


def find_comment(repo: str, pr: int) -> dict | None:
    for c in github_list(f"/repos/{repo}/issues/{pr}/comments"):
        if c["user"]["login"] == "github-actions[bot]" and MARKER in (c["body"] or ""):
            return c
    return None


def cmd_comment(args) -> int:
    repo = os.environ["GITHUB_REPOSITORY"]
    url = preview_url(args.site_url, args.pr)
    sha = (args.sha or "")[:7]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    log = Path(args.log) if args.log else None
    existing = find_comment(repo, args.pr)

    body = [MARKER, "### 📖 Documentation preview", ""]
    if args.state == "deployed":
        pages = changed_pages(repo, args.pr)
        body += [LIVE_MARKER, f"**{url}**", "",
                 f"Built from {sha} · {now} · [build log]({args.run_url})", ""]
        if pages:
            body.append("Changed pages:")
            for rel, page_url in pages[:15]:
                body.append(f"- [{rel}]({url}{quote(page_url)})")
            if len(pages) > 15:
                body.append(f"- … and {len(pages) - 15} more")
            body.append("")
        warnings = log_excerpt(log, [rel for rel, _ in pages])
        if warnings:
            body += [f"<details><summary>⚠️ {len(warnings)} build warning(s) "
                     "in changed pages</summary>", "", "```text", *warnings,
                     "```", "</details>", ""]
        body += [f"🔁 Comment `{COMMAND}` to rebuild the preview from the "
                 "latest commit.", "",
                 "<sub>Also rebuilt on every push, after the image normalizer, "
                 "and removed when the PR is closed. GitHub Pages may take a "
                 "minute or two to show a new version.</sub>"]
    elif args.state == "failed":
        body += [f"❌ The preview build failed for {sha} — see the "
                 f"[build log]({args.run_url}). Push a fix, or comment "
                 f"`{COMMAND}` to retry.", ""]
        if existing and LIVE_MARKER in existing["body"]:
            body += [LIVE_MARKER, f"The last successful preview is still at {url}", ""]
        tail = log_excerpt(log, None)
        if tail:
            body += ["<details><summary>Build output</summary>", "", "```text",
                     *tail, "```", "</details>"]
    else:  # removed
        if not existing:
            return 0
        body.append("🧹 The preview was removed because the pull request was closed.")

    text = "\n".join(body) + "\n"
    if existing:
        github("PATCH", f"/repos/{repo}/issues/comments/{existing['id']}", {"body": text})
    else:
        github("POST", f"/repos/{repo}/issues/{args.pr}/comments", {"body": text})
    print(f"Preview comment {'updated' if existing else 'created'} on #{args.pr}")
    return 0


# --------------------------------------------------------------------------
# remove
# --------------------------------------------------------------------------

def cmd_remove(args) -> int:
    root = Path(args.pages) / PREVIEW_ROOT
    if args.pr is not None:
        targets = [args.pr]
    else:
        repo = os.environ["GITHUB_REPOSITORY"]
        targets = []
        for d in sorted(root.glob("pr-*")) if root.is_dir() else []:
            m = re.fullmatch(r"pr-(\d+)", d.name)
            if m and github("GET", f"/repos/{repo}/pulls/{m.group(1)}")["state"] != "open":
                targets.append(int(m.group(1)))
    removed = []
    for pr in targets:
        d = root / f"pr-{pr}"
        if d.is_dir():
            shutil.rmtree(d)
            removed.append(pr)
    print("Removed previews: " + (", ".join(f"#{n}" for n in removed) or "none"))
    set_output(removed=" ".join(map(str, removed)))
    return 0


# --------------------------------------------------------------------------
# rebuild
# --------------------------------------------------------------------------

def set_output(**values: str) -> None:
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            for key, value in values.items():
                fh.write(f"{key}={value}\n")


def cmd_rebuild(args) -> int:
    repo = os.environ["GITHUB_REPOSITORY"]

    def done(result: str, message: str) -> int:
        print(("::notice::" if result != "restarted" else "") + message)
        set_output(result=result, message=message)
        return 0

    pr = github("GET", f"/repos/{repo}/pulls/{args.pr}")
    if pr["state"] != "open":
        return done("closed", f"PR #{args.pr} is closed, no preview to rebuild.")
    head_repo = (pr["head"]["repo"] or {}).get("full_name")
    head_ref = pr["head"]["ref"]

    runs = github("GET", f"/repos/{repo}/actions/workflows/{BUILD_WORKFLOW}/runs"
                         f"?event=pull_request&branch={quote(head_ref, safe='')}"
                         "&per_page=50")["workflow_runs"]
    runs = [r for r in runs
            if (r.get("head_repository") or {}).get("full_name") == head_repo]
    if not runs:
        return done("none", "There is no preview build to restart yet: it starts "
                            "with the first push that changes `docs/`, "
                            "`snippets/` or `mkdocs.yml`.")

    run = runs[0]                            # newest first
    deadline = time.monotonic() + args.wait
    while run["status"] != "completed" and time.monotonic() < deadline:
        print(f"Waiting for {run['html_url']} ({run['status']})")
        time.sleep(10)
        run = github("GET", f"/repos/{repo}/actions/runs/{run['id']}")
    if run["status"] != "completed":
        return done("busy", "The preview build is still running; try again when "
                            f"it has finished: {run['html_url']}")
    if run["conclusion"] == "action_required":
        return done("approval", "The preview build is waiting for a maintainer to "
                                "approve workflows for this PR; it builds the "
                                f"latest commit once approved: {run['html_url']}")

    github("POST", f"/repos/{repo}/actions/runs/{run['id']}/rerun")
    return done("restarted", f"Restarted the preview build: {run['html_url']}")


# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("publish")
    p.add_argument("--preview", required=True, help="built preview site")
    p.add_argument("--pages", required=True, help="gh-pages checkout")
    p.add_argument("--pr", type=int, required=True)
    p.add_argument("--site-url", required=True, help="site_url of the live site")
    p.set_defaults(func=cmd_publish)

    p = sub.add_parser("comment")
    p.add_argument("--pr", type=int, required=True)
    p.add_argument("--state", choices=["deployed", "failed", "removed"], required=True)
    p.add_argument("--site-url", required=True)
    p.add_argument("--sha")
    p.add_argument("--run-url")
    p.add_argument("--log", help="mkdocs build log")
    p.set_defaults(func=cmd_comment)

    p = sub.add_parser("remove")
    p.add_argument("--pages", required=True)
    p.add_argument("--pr", type=int, help="omit to remove all previews of closed PRs")
    p.set_defaults(func=cmd_remove)

    p = sub.add_parser("rebuild")
    p.add_argument("--pr", type=int, required=True)
    p.add_argument("--wait", type=int, default=300,
                   help="seconds to wait for a running build to finish")
    p.set_defaults(func=cmd_rebuild)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
