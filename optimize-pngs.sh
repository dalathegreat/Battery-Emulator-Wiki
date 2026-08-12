#!/usr/bin/env bash
# Resize oversized PNGs and recompress every PNG in docs/images.
#
#   docs/images/*.png wider than $MAX_TRIGGER  ->  scaled down to $TARGET_W wide
#   then pngquant (lossy palette) -> oxipng (lossless) on every PNG
#
# Usage:   ./optimize-pngs.sh [dir]        default dir: docs/images
#          DRY_RUN=1 ./optimize-pngs.sh    report what would change, touch nothing
#
# Needs: imagemagick, pngquant, oxipng
#   Debian/Ubuntu:  sudo apt install imagemagick pngquant
#   oxipng:         cargo install oxipng
#                   or grab a binary from github.com/shssoichiro/oxipng/releases

set -uo pipefail

DIR="${1:-docs/images}"
MAX_TRIGGER=2000     # only images wider than this get resized
TARGET_W=1200        # resized to this width, aspect ratio kept
QUALITY="65-90"      # pngquant: keeps the original if it can't reach the minimum
DRY_RUN="${DRY_RUN:-0}"

[[ -d "$DIR" ]] || { echo "no such directory: $DIR" >&2; exit 1; }

# ImageMagick 7 ships 'magick', 6 ships 'convert'/'identify'
if command -v magick >/dev/null; then IM="magick"; IDENT="magick identify"
elif command -v convert >/dev/null; then IM="convert"; IDENT="identify"
else echo "imagemagick not found" >&2; exit 1; fi

have_pngquant=1; command -v pngquant >/dev/null || { have_pngquant=0; echo "warning: pngquant not found, skipping palette pass" >&2; }
have_oxipng=1;   command -v oxipng   >/dev/null || { have_oxipng=0;   echo "warning: oxipng not found, skipping lossless pass" >&2; }

size_of() { stat -c%s "$1" 2>/dev/null || stat -f%z "$1"; }
human()   { numfmt --to=iec-i --suffix=B "$1" 2>/dev/null || echo "$1 B"; }

shopt -s nullglob nocaseglob
files=("$DIR"/*.png)
(( ${#files[@]} )) || { echo "no PNGs in $DIR"; exit 0; }

total_before=0 total_after=0 resized=0 n=0

for f in "${files[@]}"; do
    before=$(size_of "$f"); total_before=$((total_before + before)); n=$((n + 1))

    w=$($IDENT -format '%w' "$f[0]" 2>/dev/null) || w=0
    do_resize=0
    (( w > MAX_TRIGGER )) && do_resize=1

    if (( DRY_RUN )); then
        (( do_resize )) && { echo "would resize  ${w}px -> ${TARGET_W}px  $(basename "$f")"; resized=$((resized + 1)); }
        total_after=$((total_after + before))
        continue
    fi

    if (( do_resize )); then
        # -strip drops EXIF/colour profiles; Lanczos keeps screenshot text legible
        $IM "$f" -filter Lanczos -resize "${TARGET_W}x" -strip "$f" && resized=$((resized + 1))
    fi

    (( have_pngquant )) && pngquant --quality="$QUALITY" --speed 1 --strip \
        --skip-if-larger --force --ext .png -- "$f" 2>/dev/null

    (( have_oxipng )) && oxipng -o 4 --strip safe --alpha --quiet "$f" 2>/dev/null

    after=$(size_of "$f"); total_after=$((total_after + after))
    printf '%-58s %9s -> %9s  %s\n' "$(basename "$f")" "$(human "$before")" "$(human "$after")" \
        "$( (( do_resize )) && echo "[${w}px -> ${TARGET_W}px]" )"
done

echo
echo "$n PNGs, $resized resized"
echo "before: $(human "$total_before")"
echo "after:  $(human "$total_after")"
(( total_before > 0 )) && echo "saved:  $(( 100 - total_after * 100 / total_before ))%"
