#!/usr/bin/env bash
# PreToolUse hook for the project-manager: may write under docs/ (including docs/status/context.json) and its own memory.
input="$(cat)"
path="$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n1)"
case "$path" in
  "" ) exit 0 ;;
  */docs/*|docs/*|*/.claude/agent-memory/*|.claude/agent-memory/*) exit 0 ;;
esac
echo "Blocked: the project-manager writes only under docs/. Assign code or site changes to the developer." >&2
exit 2
