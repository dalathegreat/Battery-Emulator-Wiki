#!/usr/bin/env python3
"""
Rename every docs/**.md to [a-z0-9_]+.md, keep the menus correct, fix all links.
Idempotent: safe to re-run against a freshly pulled clone.

    python3 reapply.py <repo-root>
"""
import json, os, re, subprocess, sys, unicodedata
from urllib.parse import unquote

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
DOCS = os.path.join(ROOT, 'docs')

# folders where a filename prefix just repeats what the folder already says
STRIP_PREFIX = {
    '20-battery': ('battery_',),
    '40-setup/30-chargers': ('charger_',),
    '40-setup/20-software': ('feature_',),
}


def md_files():
    for r, _, fs in os.walk(DOCS):
        rel = os.path.relpath(r, DOCS).replace(os.sep, '/')
        for f in sorted(fs):
            if f.endswith('.md'):
                yield (f if rel == '.' else f'{rel}/{f}')


def slug(stem):
    s = unicodedata.normalize('NFKD', stem)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('&', ' and ')
    s = re.sub(r'[^A-Za-z0-9]+', '_', s)
    return re.sub(r'_+', '_', s).strip('_').lower()


def build_map():
    m = {}
    for old in md_files():
        d, base = os.path.split(old)
        new_stem = slug(base[:-3])
        for pref in STRIP_PREFIX.get(d, ()):
            if new_stem.startswith(pref) and len(new_stem) > len(pref):
                new_stem = new_stem[len(pref):]
        m[old] = f'{d}/{new_stem}.md' if d else f'{new_stem}.md'
    dupes = [v for v in m.values() if list(m.values()).count(v) > 1]
    if dupes:
        sys.exit(f'name collisions: {sorted(set(dupes))}')
    return m


def nav_labels(site):
    """menu label per source path, read from a built site"""
    s = open(os.path.join(site, 'index.html'), encoding='utf-8').read()
    out = {}
    for href, inner in re.findall(
            r'<a href="([^"]+)"\s+class="md-nav__link[^"]*"[^>]*>(.*?)</a>', s, re.S):
        lab = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', inner)).strip().replace('&amp;', '&')
        if href.startswith('#') or not lab:
            continue
        h = unquote(href).strip('/')
        src = 'index.md' if h in ('', '.') else h + '.md'
        if not os.path.exists(os.path.join(DOCS, src)):
            src = h + '/index.md'
        out.setdefault(src, lab)
    return out


def title_from_stem(stem):
    """reconstruct the human title a GitHub-wiki filename encodes"""
    t = stem.replace('\u2010', '\x00')      # U+2010 was a real hyphen
    t = re.sub(r'-{2,}', ' \x01 ', t)       # '---' was space-hyphen-space
    t = t.replace('-', ' ').replace('\x00', '-').replace('\x01', '-')
    t = re.sub(r'^(Battery|Charger|Feature|Shunt)_\s*-?\s*', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def front_matter(text):
    return re.match(r'\A(---\r?\n)(.*?)(\r?\n---\r?\n)', text, re.S)


def add_titles(mapping, labels):
    """give every page an explicit, quoted title so renaming can't change the menus"""
    added = quoted = 0
    for src in mapping:
        p = os.path.join(DOCS, src)
        s = open(p, encoding='utf-8').read()
        fm = front_matter(s)
        tm = re.search(r'^title:[ \t]*(.*)$', fm.group(2), re.M) if fm else None

        if tm is None:
            lab = labels.get(src)
            derived = title_from_stem(os.path.basename(src)[:-3])
            # a label sharing no word with the filename came from a stray heading
            overlap = set(re.findall(r'[a-z0-9]+', (lab or '').lower())) & \
                      set(re.findall(r'[a-z0-9]+', derived.lower()))
            title = lab if (lab and overlap) else derived
            if not title:
                continue
            block = f'title: "{title.replace(chr(92), chr(92)*2).replace(chr(34), chr(39))}"'
            s = (s[:fm.end(2)] + '\n' + block + s[fm.end(2):]) if fm \
                else f'---\n{block}\n---\n\n' + s.lstrip('\n')
            added += 1
        else:
            val = tm.group(1).strip()
            if (val.startswith('"') and val.endswith('"')) or \
               (val.startswith("'") and val.endswith("'")):
                continue
            # unquoted YAML: a colon in the title makes MkDocs discard it silently
            esc = val.replace('\\', '\\\\').replace('"', '\\"')
            s = s[:fm.start(2)] + fm.group(2)[:tm.start(1)] + f'"{esc}"' + \
                fm.group(2)[tm.end(1):] + s[fm.end(2):]
            quoted += 1
        open(p, 'w', encoding='utf-8').write(s)
    return added, quoted


def rename(mapping):
    n = 0
    for old, new in mapping.items():
        if old == new:
            continue
        subprocess.run(['git', 'mv', '-f', f'docs/{old}', f'docs/{new}'],
                       cwd=ROOT, check=True, capture_output=True)
        n += 1
    return n


def dest_spans(s):
    """paren-balanced spans of every markdown link destination"""
    out = []
    for m in re.finditer(r'\]\(', s):
        i, d = m.end(), 1
        while i < len(s) and d:
            d += (s[i] == '(') - (s[i] == ')')
            i += 1
        out.append((m.end(), i - 1))
    return out


def fix_links(mapping):
    import posixpath
    inv = {n: o for o, n in mapping.items()}
    changed = unresolved = 0
    for page_new in md_files():
        p = os.path.join(DOCS, page_new)
        page_old = inv.get(page_new, page_new)
        s = open(p, encoding='utf-8').read()

        def remap(dest):
            nonlocal changed, unresolved
            d = dest.strip()
            if not d or d.startswith(('http://', 'https://', 'mailto:', '#')):
                return None
            path, sep, frag = d.partition('#')
            if not path.endswith('.md'):
                return None
            tgt = posixpath.normpath(
                posixpath.join(posixpath.dirname(page_old), unquote(path)))
            if tgt not in mapping:
                unresolved += 1
                return None
            rel = posixpath.relpath(mapping[tgt], posixpath.dirname(page_new) or '.')
            changed += 1
            return rel + sep + frag if sep else rel

        out, last = [], 0
        for a, b in dest_spans(s):
            new = remap(s[a:b])
            if new is None:
                continue
            out.append(s[last:a]); out.append(new); last = b
        out.append(s[last:])
        s2 = re.sub(r'(href=")([^"]+)(")',
                    lambda m: m.group(0) if remap(m.group(2)) is None
                    else m.group(1) + remap(m.group(2)) + m.group(3),
                    ''.join(out))
        if s2 != s:
            open(p, 'w', encoding='utf-8').write(s2)
    return changed, unresolved


def fix_redirects(mapping):
    p = os.path.join(ROOT, 'mkdocs.yml')
    s = open(p, encoding='utf-8').read()
    n = 0
    for old, new in mapping.items():
        if old != new and old in s:
            s = s.replace(old, new); n += 1
    if n:
        open(p, 'w', encoding='utf-8').write(s)
    return n


if __name__ == '__main__':
    mapping = build_map()
    json.dump(mapping, open('/home/claude/rename_map.json', 'w'), indent=0)
    print(f'files: {len(mapping)}  to rename: {sum(o != n for o, n in mapping.items())}')
    labels = json.load(open('/home/claude/nav_before.json'))
    print('titles added / quoted: %d / %d' % add_titles(mapping, labels))
    print('renamed: %d' % rename(mapping))
    c, u = fix_links(mapping)
    print(f'links rewritten: {c}   unresolved: {u}')
    print('mkdocs.yml paths updated: %d' % fix_redirects(mapping))
