#!/usr/bin/env bash
# upstream-diff.sh — summarize new upstream commits since last review
# Usage: bash .agent/scripts/upstream-diff.sh [since-sha]
#
# If since-sha not provided, reads upstream_last_reviewed from CONTEXT.md

set -euo pipefail

UPSTREAM_REMOTE="upstream"
UPSTREAM_BRANCH="main"
BLOCKLIST=(
  "yuanbao" "weixin" "wecom" "qqbot" "dingtalk" "feishu"
  "tencent" "tokenhub" "alibabacloud" "lark-oapi" "dingtalk-stream"
)

# Get baseline SHA
if [[ -n "${1:-}" ]]; then
  SINCE_SHA="$1"
else
  SINCE_SHA=$(grep 'upstream_last_reviewed:' .agent/CONTEXT.md | awk '{print $2}' | tr -d '"' || true)
fi

echo "🔍 Fetching upstream..."
git fetch "$UPSTREAM_REMOTE" --quiet

if [[ -z "${SINCE_SHA:-}" ]]; then
  echo "⚠️  No baseline SHA found. Showing last 30 upstream commits."
  COMMITS=$(git log "$UPSTREAM_REMOTE/$UPSTREAM_BRANCH" --oneline -30)
else
  echo "📌 Baseline: $SINCE_SHA"
  COMMITS=$(git log "$UPSTREAM_REMOTE/$UPSTREAM_BRANCH" --oneline "^${SINCE_SHA}")
fi

TOTAL=$(echo "$COMMITS" | grep -c '[0-9a-f]' || true)

if [[ "$TOTAL" -eq 0 ]]; then
  echo "✅ No new upstream commits since last review."
  exit 0
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  $TOTAL new upstream commits"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

CHINA_COUNT=0
SECURITY_COUNT=0
OTHER_COUNT=0

while IFS= read -r line; do
  SHA=$(echo "$line" | awk '{print $1}')
  MSG=$(echo "$line" | cut -d' ' -f2-)

  # Check blocklist
  IS_CHINA=false
  for kw in "${BLOCKLIST[@]}"; do
    if echo "$MSG" | grep -qi "$kw"; then
      IS_CHINA=true
      break
    fi
    # Also check touched files
    if git diff-tree --no-commit-id -r --name-only "$SHA" 2>/dev/null | grep -qi "$kw"; then
      IS_CHINA=true
      break
    fi
  done

  IS_SECURITY=false
  if echo "$MSG" | grep -qi "security\|vuln\|cve\|patch"; then
    IS_SECURITY=true
  fi

  if $IS_CHINA; then
    echo "  🇨🇳 [SKIP]     $line"
    ((CHINA_COUNT++)) || true
  elif $IS_SECURITY; then
    echo "  🔒 [SECURITY] $line"
    ((SECURITY_COUNT++)) || true
  else
    echo "  📦 [REVIEW]   $line"
    ((OTHER_COUNT++)) || true
  fi
done <<< "$COMMITS"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🇨🇳 Skip (China):  $CHINA_COUNT"
echo "  🔒 Security:       $SECURITY_COUNT"
echo "  📦 Review:         $OTHER_COUNT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [[ "$SECURITY_COUNT" -gt 0 ]]; then
  echo ""
  echo "⚠️  ACTION REQUIRED: $SECURITY_COUNT security commit(s) — review and pull immediately."
fi
