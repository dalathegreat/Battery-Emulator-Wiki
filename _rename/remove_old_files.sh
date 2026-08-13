#!/usr/bin/env bash
# Remove the old numbered directories after unzipping the new tree over docs/.
# docs/images/ is untouched by this.
#   bash _rename/remove_old_files.sh && rm -rf _rename

set -e
cd "$(dirname "$0")/.."

git rm -rq --ignore-unmatch -- "docs/10-inverters"
git rm -rq --ignore-unmatch -- "docs/20-battery"
git rm -rq --ignore-unmatch -- "docs/30-hardware"
git rm -rq --ignore-unmatch -- "docs/40-setup"

echo "old numbered directories removed"
