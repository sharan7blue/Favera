# QA round 2, 2026-10-24

Not done: project memory not updated (no `.claude/agent-memory`); lint/link CI commands not run (no HTML in the repo yet, draft is markdown only).

## 1. docs/drafts/privacy-and-terms-v2.md: PASS for founder legal check, then developer build, with conditions below

Earlier BLOCK points (docs/status/2026-10-24-qa-tester.md section 1):
1. "Registered in England and Wales" asserted: FIXED (placeholder).
2. "No advertising cookies or trackers": FIXED (narrowed; Tally and Cloudflare flagged). See residual A.
3. Overseas transfer safeguards claim: FIXED (removed; placeholder).
4. Liability cap of nil: FIXED as a proposal (greater of fees or 100 pounds), flagged for adviser.
5. "6 years as tax law requires": FIXED (removed; placeholder).
6. Controller/processor for client data: FIXED in privacy notice (new section, [CONFIRM: roles]). Terms still only say "you confirm they agree"; acceptable.
7. Retention deliverability: FIXED (marked proposals, founder point 1).

ICO URLs, opened 2026-10-24:
- Fee page: supports "including sole traders, unless exempt"; no amounts or exemptions. It does NOT mention self-assessment. The self-assessment page (/self-assessment/) is real and supports it. Draft attributes both to one bullet; harmless, but reword.
- PECR email marketing: all attributed points confirmed (corporate bodies, sole traders/some partnerships as individuals, do-not-email list, no disguised sender, under review for the Data (Use and Access) Act).
- Legitimate interests: three-part test, all before processing: confirmed.
- Storage limitation: no fixed periods, justify, review, erase/anonymise: confirmed.

Remaining issues (none blocks the adviser review):
A. "Our own web pages do not set cookies" is stated as fact. Verified only for index.html source; Cloudflare Pages response headers and the new privacy/terms pages are not checked. Soften or re-verify at build.
B. "We do not collect anything else about your clients" and "We do not sell your data" are promises, unsourced; fine if operations can keep them.
C. "We aim to reply within one month" matches the usual UK GDPR deadline but is unsourced in the draft.
D. Lawful basis "contract" for a free report is for the adviser (consideration question).
E. Every [CONFIRM:...] and [bracket] placeholder must be gone before publication; developer should fail the build on any remaining "[".

## 2. docs/status/2026-10-24-research-analyst-round2.md spot-check

- Blue Array Ltd 09610441: CH matches (Active, private limited, 27 May 2015, Reading address). Site footer shows company number and "Blue Array Ltd". No headcount: "unknown" is correct. MATCH.
- Semetrical Ltd 08728596: CH matches (Active, private limited, 11 October 2013, 64 Southwark Bridge Road). Homepage text I fetched showed no footer, company name or address, so the sheet's site quotes ("© 2026 Semetrical", 124 City Road) are unconfirmed by me; the sheet's own caveat stands. CH PASS, site PARTIAL.
- SDG New Media Ltd 05708841: CH matches (Active, private limited, 14 February 2006, Kingston address). Site footer not opened by me.
No mismatches found on CH facts. Rows 14 (Anicca) and ClickSlice remain unverified, as the analyst states.
