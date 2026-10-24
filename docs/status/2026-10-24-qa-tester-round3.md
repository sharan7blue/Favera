# QA round 3, 2026-10-24

Not done: project memory not updated (no `.claude/agent-memory`); lint/link CI commands not run (draft is markdown, no HTML yet). Companies House was fetched via WebFetch because curl was blocked by the proxy (403).

Draft: docs/drafts/privacy-and-terms-v3.md

## Verdict: PASS for building privacy.html now on a non-live branch with visible [CONFIRM] markers. Not publishable yet (see 3).

## 1. Companies House (opened 2026-10-24)
https://find-and-update.company-information.service.gov.uk/company/17534431
- Name FAEVRA LTD: MATCH.
- Number 17534431: MATCH.
- Registered office 66 Paul Street, London, England, United Kingdom, EC2A 4NA: MATCH.
- Status Active, incorporated 21 October 2026. Page does not state jurisdiction, so [CONFIRM: England and Wales] correctly stays.

## 2. Earlier non-blocking points
- ICO bullet: FIXED. Self-assessment page (https://ico.org.uk/for-organisations/data-protection-fee/self-assessment/) opened: helps decide whether to pay and how much, "about 10 minutes", organisations including sole traders pay unless exempt. Matches draft. Fee page is cited separately.
- A (cookies as fact): FIXED, softened to "when we last checked" plus markers. Still not re-verified in v3.
- B (promises): FIXED for "collect anything else"; "We do not sell your data" kept as a commitment, acceptable.
- C (one month): FIXED. Erasure page opened: "without undue delay and at the latest within one month"; extendable by a further two months if complex, with notice and reasons within one month. Draft matches. Draft omits that the extension also applies to multiple requests; harmless.
- D (contract basis for free report): unchanged, for the adviser.

## 3. Privacy notice: publication readiness
Blocks publishing (must be resolved or the text removed/reworded):
- [CONFIRM: England and Wales]
- [CONTACT EMAIL] (three uses; the rights and opt-out routes depend on it)
- [LAST UPDATED DATE]
- [CONFIRM: cookies check] (live pages and headers)
- [CONFIRM: Cloudflare Web Analytics] (or delete the sentence if not adopted)
- [CONFIRM: Tally cookies]
- [CONFIRM: Cloudflare logging]
- [CONFIRM: transfers] (notice promises a list of locations and safeguards "before launch")
- [CONFIRM: roles]
- Also remove "(proposed)", "(proposal)" and "may change before launch" wording once retention periods are decided.

Optional or conditional:
- [CONFIRM: tax records]: blocks only if the notice still mentions accounting records; drop that row and bullet if there are none.

Not in the privacy notice (terms only, or not in the notice at all):
- [CONFIRM: ICO fee]: no marker appears in the notice. It is a legal question for the founder, not a page blocker.
- [CONFIRM: liability cap], [CONFIRM: governing law]: terms only.

Defect for the author: the placeholder table lists "[CONFIRM: analytics]" but the notice uses "[CONFIRM: Cloudflare Web Analytics]"; "[CONFIRM: ICO fee]" is in the table but not the notice. Align the names so the build check ("[" fails build) and the table agree.

Unchanged limits: "contract" lawful basis and PECR/legitimate-interests wording are for the adviser. The make-a-complaint link was not opened by me.

## 4. Day job and personal profiles
Searched the draft for employer names, LinkedIn, GitHub and personal names: none found. PASS.
