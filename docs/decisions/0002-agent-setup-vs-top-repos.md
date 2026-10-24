# 0002: agent setup compared with well-known repos

Date: 2026-10-24. Status: proposed, founder to approve.

Pages read: Anthropic's [subagent documentation](https://code.claude.com/docs/en/subagents), the [VoltAgent subagent collection](https://github.com/VoltAgent/awesome-claude-code-subagents), [wshobson/agents](https://github.com/wshobson/agents), a [write-up on which of 100 subagents earned their context](https://dev.to/suraj_khaitan_f893c243958/i-built-100-claude-code-subagents-these-are-the-12-that-actually-earn-their-context-10nn), and a [guide to keeping CLAUDE.md short](https://dev.to/iggredible/your-claudemd-is-probably-too-long-17bi). The last three are community sources, not Anthropic's.

| Practice seen | Where | Our setup before | Change made |
| --- | --- | --- | --- |
| Description is a routing rule ("use immediately after...") and does not overlap other agents | write-up, subagent docs | Role summaries | Rewritten as "use when" rules, one per agent |
| Minimal tools per role; reviewers read-only | VoltAgent, write-up | Tool lists, but prose-only limits on writing | Added a PreToolUse hook that limits non-developer agents to writing under docs/ |
| Back important restrictions with a hook, not a prompt | write-up, subagent docs | Hook only for pushes to main | Second hook added; both tested |
| Cheapest adequate model per role | VoltAgent, subagent docs | Already tiered | Unchanged: haiku for research, sonnet elsewhere |
| Agents return a summary, not a long report | write-up | Not stated | Every agent returns at most 150 words plus links; detail goes to docs/status |
| CLAUDE.md under 200 lines, only what Claude cannot guess | CLAUDE.md guide | 12 lines of mixed rules | 21 lines: commands, workflow, approvals, never-list |
| Topic rules load only when relevant | CLAUDE.md guide | In CLAUDE.md | Site copy rules moved to `.claude/rules/site-copy.md`, scoped to `apps/web/**` |
| Reference material loaded on demand | wshobson/agents | None | Report process moved into a `traffic-drop-report` skill |
| Validate agent files automatically | wshobson/agents | None | `scripts/validate_agents.py`, run in CI |
| Curate a small roster | write-up | Seven agents | Kept seven, since each owns a distinct output; review at day 30 and drop any that did not earn its keep |

## Where we differ on purpose

wshobson/agents describes no human approval gates. Faevra keeps founder approval for merges, sending, spending and client data, enforced by deny rules and hooks.

## Known limits

- Hooks restrict the write tools only. An agent with Bash could still change files; testing and developer keep Bash because they must run commands.
- Frontmatter hooks in project agents run only after the folder is trusted.
- Nothing here has run inside Claude Code yet; the first real run is the test.
