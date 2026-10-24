#!/usr/bin/env bash
# PreToolUse hook for non-developer agents: they may only write under docs/ or their own memory.
# Exit code 2 blocks the call and shows the reason to Claude.
input="$(cat)"
path="$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n1)"
case "$path" in
  "" ) exit 0 ;;
  */docs/*|docs/*|*/.claude/agent-memory/*|.claude/agent-memory/*) exit 0 ;;
esac
echo "Blocked: this agent may only write under docs/. Hand code and site changes to the developer through docs/status." >&2
exit 2
