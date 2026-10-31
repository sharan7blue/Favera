# Research note: how people use MiroFish (Mirrorfish) for product validation

Owner: research-analyst (Rhea)
Date of research: 2026-10-28
Task source: project-manager task message (research request). Done-when was not stated as a separate field; the request's own output spec (per-source URL, quote, date; gaps; verified vs unverified) was treated as done-when.
Scope: public web only. No client data, no prospect data, no personal profiles. Nothing sent or posted.

## Bottom line

- MiroFish is large on GitHub (about 80K stars) and widely covered in blogs, vendor pages and X posts from March to October 2026.
- I found no real Reddit thread, no Hacker News thread about MiroFish, and no official Product Hunt launch. Reddit, HN and Product Hunt were the sources the request named, and none turned up.
- The only "product validation" write-ups I could open are blogs and vendor pages. None shows a measured outcome (did a real product sell, or did simulated reactions match real buyers?). Several authors say so themselves.
- Two case-style posts exist: a 44-agent SaaS launch test (qualitative findings, no real-world check) and a vendor-hosted ThumbAI example (labelled illustrative). Neither is evidence of validity.
- The most useful practitioner guidance is the seed-document advice and the cost and pitfall warnings. These are consistent across sources.

## Source table (figures and claims)

"Accessed" is 2026-10-28 for every row. "Published" is the date shown on the page, or "undated" if none.

| # | Source (link) | Published / as-of | What it says (key quote or finding) | Type / reliability |
|---|---|---|---|---|
| S1 | [gittrend.io repo page](https://gittrend.io/repo/666ghj/MiroFish) | No as-of date on page; chart ends 28 Oct, one line cites 27 Sep 2026 | 82.4k stars, 12.5k forks, AGPL-3.0, created 26 Nov 2025, Python. Tagline "A Simple and Universal Swarm Intelligence Engine, Predicting Anything." | Third-party mirror of GitHub. Figures not checked against GitHub directly. |
| S2 | [OSSInsight analysis](https://ossinsight.io/analyze/666ghj/MiroFish) | Contributor rankings 2026/09 | 80,363 stars, 12,193 forks (share text). Issue and PR cells blank. | Third-party analytics. |
| S3 | [36Kr Europe (repost of 新智元)](https://eu.36kr.com/en/p/3715147673006213) | 9 Mar 2026 | Shanda Group (Chen Tianqiao) to invest "30 million yuan" in MiroFish; decision came within 24 hours of a demo video. Meta description says "$30 million", which conflicts with body text. Star count then: 5.7K. Benchmark claim vs OpenAI, Google, Microsoft given with no source. | Press (secondary). Funding date not given. Treat "$4M in 24 hours" as a press claim. |
| S4 | [Woshipm, 张艾拉 (Chinese)](https://www.woshipm.com/ai/6365813.html) | 31 Mar 2026 | "至少现在还不能这么下结论" (at least for now, one cannot conclude it can predict the future). "能模拟，不等于已经证明能高精度预测" (being able to simulate is not proof of high-precision prediction). Cites 30M RMB from Chen Tianqiao. Says no solid, reproducible evaluation exists. | Opinion, Chinese. Useful critical view. |
| S5 | [Blocmates article (Lavina)](https://www.blocmates.com/articles/what-is-mirofish-the-agent-engine-that-can-predict-anything-and-everything) | 18 Mar 2026 | "A simulation can produce very convincing output without being predictively accurate." Says "over 28k stars and 3.4k forks". Calls validation "the most significant challenge". Cost: 800 to 1,200 agents over 30 to 50 rounds "costs real money in API tokens." | Explainer. Star figure undated in the piece. |
| S6 | [Starlog article](https://starlog.is/articles/ai-agents/666ghj-mirofish) | 7 May 2026 | Star count 59.5k next to the date. "MiroFish provides no built-in evaluation framework, no backtesting methodology, no confidence intervals." "agent-based predictions are fundamentally difficult to verify until the future actually happens." Warns against sending sensitive data to third-party services. | Explainer / review. |
| S7 | [Mayhemcode: How to Use MiroFish for AI-Powered Product Launch Testing](https://www.mayhemcode.com/2026/10/how-to-use-mirofish-for-ai-powered.html) | 13 Oct 2026 | Method: upload launch post, pricing page or reviews as seed; knowledge graph extracts people and groups; personas generated; two platforms run in parallel; ReportAgent writes report; "God's-eye view" lets you inject events. Brief advice: treat seed as config file; write income, devices, spend and frustrations per group; ask one specific question. Pitfall: README says consumption is high, try fewer than 40 rounds. Says no validated results are shown. | How-to guide. Closest match to the product-launch use. No real results. |
| S8 | [Caminho Solo: MiroFish Offline to validate a product idea](https://caminhosolo.com.br/en/2026/04/mirofish-offline-validate-product-idea-before-building/) | 7 Apr 2026 | Five-stage local setup (Docker, Ollama, Neo4j). Recommends simulation then "5 to 10 real conversations" then MVP. "A vague seed produces vague results." Spend 15 to 30 minutes on the seed. ThumbAI example: 58% positive, 28% neutral, 14% negative; price acceptance 74% at $19, 58% at $29, 31% at $49; 91% want a free trial. Article says these are example outputs with no methodology. "Simulation signals risk, not proof of market fit." | Blog with a commercial angle (monetisation projections in the piece). Example figures are illustrative, not measured. |
| S9 | [Sanjay Shankar: AI Market Simulation, tested a SaaS launch with 44 agents](https://sanjayshankar.me/ai-market-simulation-mirofish-startup-launch/) | Published 25 Mar 2026; updated 10 Sep 2026 | Product not named. Seed: 6 to 8 page market brief (users, jobs, positioning, pricing, competitors). 44 agents, 10 rounds. Qualitative findings: solo builders adopted first; main objection "team adoption friction"; two highly connected agents drove awareness. Cost about $0.01 to $0.03 per run. No comparison with real customer behaviour. "decision support, not truth." | Closest to a real case study. Single author, one run, no outcome check. |
| S10 | [Nervegna Substack: AutoResearchClaw + MiroFish + Claude Code](https://nervegna.substack.com/p/autoresearchclaw-mirofish-claude) | 27 Mar 2026 | Installation guide. Suggests 40 to 100 agents and 20 to 30 rounds. Author did not show a run. Says "This is not a replacement for user research." Repeats "$4.1M in 24 hours" and a trading-bot claim without checking them. | Guide. No results. |
| S11 | [Mirofish.us concept-testing page](https://mirofish.us/use-cases/concept-testing) | Undated (footer "© 2026") | Vendor page ("independent AI simulation service"). Says "It estimates reaction, not demand — only real buyers measure demand." "Use it to kill weak concepts and sharpen strong ones, not to green-light a build." Example "70% estimated confidence" marked "Illustrative output". Prices and speed stated with no source. | Commercial vendor. Not the official project. Useful as a disclaimer-style reference. |
| S12 | [Mirofish.my use cases](https://mirofish.my/use-cases) | © 2026, undated | Vendor site (support@mirofish.my). About 90 use cases including "AI Demand Validation", "Value Proposition Validation", "Concept Testing". No numbers on any use case. Disclaimer: "Forecasts are exploratory outputs and should be reviewed before operational, financial, or policy decisions." | Commercial vendor. Shows the range of marketed uses; no evidence of outcomes. |
| S13 | [TheAIWay review](https://theaiway.net/products/mirofish/) | "Review updated June 2026" | Pros: "staged simulation instead of a one-shot answer"; can keep chatting with the simulated world. Cons: hosted version "still framed as waitlist-stage"; "Public materials do not prove forecast accuracy for high-stakes decisions." Pricing: "Public pricing is not confirmed." | Review site. Pricing not verified. |
| S14 | [Medium, Mohit Sewak (PhD)](https://medium.com/a-microbiome-scientist-at-large/mirofish-ce7aef53f196) | 3 Apr 2026 (per page) | Critical view: "they don't predict the future — they invent a highly plausible fake one." Cites a Polymarket bot test (lost 73% of opinion variance in 8 rounds) and other papers. Advises treating report as "a creative writing exercise, not a business strategy." Several citations ("IEEE, 2026", "Moltbook Authors, 2026") cannot be verified from the page. | Opinion with citations. Some figures unverifiable; flagged. |
| S15 | [Medium, "The Truth About MiroFish"](https://medium.com/a-microbiome-scientist-at-large/mirofish-ce7aef53f196) (see note on mapping) | "mid-March" (no year) | "There are no widely available independent studies proving that Mirofish's simulations match real-world outcomes." Funding "around 30 million yuan... not officially confirmed". | Opinion. Date weak. |
| S16 | [Hunted.space listing for MiroFish](https://www.hunted.space/product/mirofish-4) | Date not shown | Launch-style listing, "Hunted by ce zhang", 0 upvotes, 1 comment, ranked #50 of the day, not featured. Description: "Upload reports, build graph memory, run parallel simulations, generate prediction reports." | Directory listing, not Product Hunt. Low signal. |
| S17 | [HuntScreens MiroFish page](https://huntscreens.com/ja/products/mirofish) | Date not shown | Description: "MiroFishは、AIを活用したシナリオ予測チャットです。" No votes or maker. | Aggregator. Low signal. |
| S18 | X posts (search snippets only): e.g. [slash1s post on 4M funding and 23k stars](https://x.com/slash1sol/status/2032843221710078329); [socialwithaayan post on "scarily accurate" demos](https://x.com/socialwithaayan/status/2032054540166648115) | March 2026 (per snippet) | Claims: "scarily accurate" live demos; "$4.1M in 24 hours"; "23k+ stars". | Could not open: X blocked the fetch (robots disallowed). Not used for any figure. |

Notes on sources:
- S15: the fetch results were mapped to URLs by call order, so the attribution of the "mid-March" and "April 3" pages to their URLs should be re-checked before quoting either.
- [Pasquale Pillitteri, "Does MiroFish Really Work?"](https://pasqualepillitteri.it/en/news/21443/does-mirofish-really-work-agent-swarm-alternatives) was blocked by an anti-bot page (Anubis). I could not read it. It is not used for any claim.
- [Emelia hub](https://emelia.io/hub/mirofish-ai-swarm-prediction) returned a blog index, not the article. The "$4M in 24 hours" headline on that page is unverified there. The same claim is repeated from S3.
- Star counts over time (all third-party, not checked on GitHub): 5.7K (S3, Mar 2026), 23K+ (X snippet, Mar 2026), 28K (S5, 18 Mar 2026), 59.5K (S6, 7 May 2026), 80,363 (S2, Sep 2026 chart), 82.4K (S1, undated). Growth is real in the sources but the exact numbers are not verified against GitHub.

## Method and brief-writing guidance found (consistent across S7, S8, S9, S10, S11)

- Seed material is the main input. The engine builds personas from it, so a vague seed gives vague personas (S8).
- Write a concrete paragraph per audience group: income, devices, current spend, frustrations (S7).
- Ask one specific question per run, such as "how will people react to this price in the first two weeks" (S7).
- Vary one thing at a time and compare runs (S7).
- Start small: under 40 rounds and 40 to 100 agents (S7, S10).
- Validate with real conversations afterwards: 5 to 10 real people (S8), "talk to real prospects" (S11).

## Pitfalls reported (with source)

- Simulated enthusiasm is not demand. Simulated agents have no budget and nothing at stake (S11).
- LLM personas polarise faster than humans and can converge on a false consensus (S10, S14, S15). The OASIS paper is cited as showing agents follow the crowd more than humans do (S7, secondary).
- Persona stereotypes; output can look convincing without being accurate (S5, S4).
- No backtesting, no confidence intervals, no built-in evaluation (S6).
- Repeat runs can differ because the model is probabilistic (S15).
- Cost: API tokens can be significant at scale (S5, S7). Per-run cost of $0.01 to $0.03 reported for a 44-agent, 10-round run (S9), so the cost depends on setup.
- Setup is technical: Docker, Ollama or cloud keys, Zep Cloud memory, Python 3.11 or 3.12 (S7, S8, S10). Windows support was said to be in testing (S5).
- Data privacy: no fully self-hosted hosted version, so scenario data goes to third parties (S6).
- Licence AGPL-3.0 (S1, S7). Relevant if the tool is used in a product.
- Model quality changes results: a local 12B model gave flatter personas than GPT-4 or Gemini in S9.

## Products reported as validated with MiroFish

- A 44-agent test of an unnamed B2B-style SaaS launch (S9). Qualitative only.
- A ThumbAI example (YouTube thumbnail SaaS) (S8). Illustrative numbers only. This is an example, not a result.
- A "Pune budgeting app at Rs 199/month" scenario (S7, referred to as hypothetical in a secondary summary).
- Public-opinion and novel-ending examples in the README (S7, secondary).
- Trading and quant use, including a claimed $4,266 profit over 338 trades (S10, secondary). Not verified.

No source I could open reported a validated product outcome (sales, retention, or a prediction that matched a later real result) that was measured against real customers.

## What did NOT come up (search gaps)

- Reddit (r/SaaS, r/Entrepreneur, r/ProductManagement, r/MachineLearning): no MiroFish thread surfaced in four searches, including a site-restricted search that the proxy rejected. Treat as "none found", not "none exist".
- Hacker News: no MiroFish-specific discussion surfaced. Search results for "MiroFish" returned unrelated HN threads (Miro whiteboard, Bending Spoons buying Miro).
- Product Hunt: no official launch found. Only directory mirrors (S16, S17).
- Official GitHub README and issues: not opened directly. Their content is taken from secondary summaries (S7, S5, S6). Worth opening before relying on any detail.
- Independent accuracy study or backtest: none found. Several sources say none exists (S6, S14, S15).
- Pricing for the hosted product: not confirmed (S13).
- Failed or negative product-validation stories: none found. Critical sources exist (S4, S6, S14), but none reports a specific failed product test.
- Twitter/X threads with real simulation outputs: only snippets. X content could not be opened (S18).

## Could and could not verify

Verified by opening the page (dated): S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S16, S17.
Not verified (could not open or claims unsourced): X posts (S18), Pasquale Pillitteri (blocked), Emelia "$4M" article (not reached), $4.1M / "24 hours" funding (press only, repeated, not confirmed by a primary source), "beats OpenAI/Google/Microsoft" benchmark (no source, S3), "scarily accurate" demos (no output shown).

## Implications for Faevra (for project-manager)

- Do not use MiroFish-based claims in site copy or outreach. No source shows its outputs match real buyer behaviour, and the copy rules require a sourced, dated claim.
- If a MiroFish-style experiment is ever run for Faevra's own positioning, it would be a low-cost pre-filter only, followed by real conversations (S8, S11). It does not replace the Gate 1 and Gate 2 evidence.
- This is a market-context note, so no client or prospect data was used and nothing was sent.

## Memory

No memory tool was available to this agent in this session (no mcp__memory__ functions in my tool list), so I could not update project memory. Suggested memory entry for the main session: "MiroFish research 2026-10-28: 80K stars (OSSInsight, Sep 2026); no Reddit, HN or Product Hunt threads found; no measured product-validation outcomes found; treat as exploratory only. Full table in docs/status/2026-10-28-research-analyst.md."

## Status

Done. Not blocked. Gaps listed above. No repo writes other than this note. No client data, prospect data or personal profiles used.
