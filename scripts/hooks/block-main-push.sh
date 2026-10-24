#!/usr/bin/env bash
# PreToolUse hook: exit code 2 blocks the command and shows the reason to Claude.
input="$(cat)"
if printf '%s' "$input" | grep -Eq 'git +push[^"]*[ :](main|master)([^A-Za-z0-9_-]|$)'; then
  echo "Blocked: pushing to main needs the founder's approval. Push a branch instead." >&2
  exit 2
fi
exit 0
