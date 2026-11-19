#!/usr/bin/env bash
# Commit everything in the current gh-pages checkout and push it.
#
# The live site deploy (ci.yml) and the PR previews (pr-preview-deploy.yml)
# all push to gh-pages and touch disjoint paths, so a rejected push is
# resolved by rebasing onto the newer branch tip and trying again.
#
# Usage: push_gh_pages.sh "<commit message>"
set -euo pipefail

message="$1"

git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'

git add -A
if git diff --cached --quiet; then
  echo "gh-pages is already up to date"
  exit 0
fi
git commit --quiet -m "$message"

for attempt in 1 2 3 4 5; do
  if git push --quiet origin HEAD:gh-pages; then
    echo "Pushed: $message"
    exit 0
  fi
  echo "Push rejected, rebasing onto the latest gh-pages (attempt $attempt)"
  sleep $((attempt * 3))
  git pull --quiet --rebase origin gh-pages
done

echo "::error::Could not push to gh-pages after 5 attempts"
exit 1
