# DRAFT - not legal advice, founder to have checked

Status: revision 3 of docs/drafts/privacy-and-terms-v2.md, answering the non-blocking points in docs/status/2026-10-24-qa-tester-round2.md. Not to be published until the founder has had it checked. The HTML is body content only; the developer places it in `apps/web/privacy.html` and `apps/web/terms.html` using the existing page shell and `styles.css`. Nothing here is a statement that the wording is legally valid.

## Placeholders still open (all must be resolved before publishing; the build should fail on any remaining "[")

| Placeholder | What is needed |
| --- | --- |
| [CONFIRM: England and Wales] (country of registration) | Founder to confirm. Companies House page does not state jurisdiction; the 8-digit number with no prefix indicates England and Wales (context.json, as of 2026-10-24) |
| [CONTACT EMAIL] | Privacy mailbox; add only once it exists (board #3) |
| [LAST UPDATED DATE] | Date of publication |
| [CONFIRM: ICO fee] | Whether Faevra must pay the ICO data protection fee (take the ICO self-assessment) and, if so, the registration number to show (optional) |
| [CONFIRM: analytics] | Cloudflare Web Analytics is planned (described as cookie-free); confirm before it is switched on and keep this page in step |
| [CONFIRM: cookies check] | Re-verify at build that the live pages (including privacy and terms) and Cloudflare Pages response headers set no cookies |
| [CONFIRM: Tally cookies] | What cookies or trackers the Tally form sets; check Tally's own policy and the live form |
| [CONFIRM: Cloudflare logging] | What request data Cloudflare Pages records for us |
| [CONFIRM: transfers] | Whether Cloudflare, Google Workspace or Tally process data outside the UK, and the transfer mechanism each uses |
| [CONFIRM: roles] | Controller/processor split for client Search Console data passed on by an agency |
| [CONFIRM: tax records] | Required retention for accounting records, from HMRC or Companies House guidance, once there are any |
| [CONFIRM: liability cap] | Adviser to decide the cap and whether it is reasonable |
| [CONFIRM: governing law] | Governing law and courts, with adviser (the terms still carry this from v2) |

Filled in v3 (source: https://find-and-update.company-information.service.gov.uk/company/17534431 , as of 2026-10-24): company name FAEVRA LTD, company number 17534431, registered office 66 Paul Street, London, England, United Kingdom, EC2A 4NA.

## Changes from v2, by QA point

- Non-blocking, ICO bullet: the self-assessment is now cited to its own page (ICO self-assessment), opened 2026-10-24. That page says it helps you decide if you need to pay the fee and how much, and that organisations (including sole traders) using personal information need to pay unless exempt. The fee page is cited separately for the general rule.
- A (cookies stated as fact): softened to what has been checked, with [CONFIRM: cookies check] for the live pages and headers.
- B ("We do not collect anything else about your clients", "We do not sell your data"): the first is reworded to describe what we ask for rather than a blanket promise. "We do not sell your data" is kept as a commitment the founder must be able to keep.
- C (one-month reply): now sourced. The ICO erasure page (opened 2026-10-24) says: "You must respond to a request for erasure without undue delay and at the latest within one month", extendable by two further months if the request is complex, with notice in the first month. The notice now says this, not just "we aim".
- D (contract basis for a free report): left unchanged, for the adviser.
- Company details filled; country of registration kept as [CONFIRM: England and Wales].

## Points for the founder and adviser

1. Retention periods are proposals. The ICO says the UK GDPR sets no fixed periods and that you must be able to justify them. Only promise a period you can carry out by hand.
2. ICO fee: take the ICO self-assessment; do not assume either way.
3. PECR and legitimate interests: ICO guidance is under review because of the Data (Use and Access) Act, so re-check before the first outreach email. Keep a written legitimate-interests assessment.
4. Corporate-subscriber marketing: check each recipient really is a limited company or LLP; never email sole traders or ordinary partnerships this way. A named person at a company address can still raise data protection issues; keep a do-not-email list.
5. Whether the free report needs other liability wording, and whether "contract" is the right lawful basis for a free report.
6. Founder to confirm the country of registration, then replace [CONFIRM: England and Wales].

---

## Privacy notice (HTML body)

```html
<h1>Privacy notice</h1>
<p class="note">Last updated: [LAST UPDATED DATE]</p>

<h2>Who we are</h2>
<p>FAEVRA LTD ("Faevra", "we") is a company registered in [CONFIRM: England and Wales], company number 17534431, with its registered office at 66 Paul Street, London, England, United Kingdom, EC2A 4NA. We decide how and why your personal data is used, so we are the "controller" under UK GDPR. Contact us at [CONTACT EMAIL].</p>

<h2>What we collect</h2>
<ul>
  <li><strong>Request form answers.</strong> What you type into our Tally form, such as your name, business name, website and what you want from a report.</li>
  <li><strong>Your email address</strong> and anything you write to us in emails.</li>
  <li><strong>Search Console data, only if you or your client grants access.</strong> We ask for read-only access to a Search Console property, or a data export. We use it only to build the report you asked for.</li>
</ul>
<p>We ask only for what is listed above, and we do not set out to collect personal data about your clients beyond what appears in the Search Console data you choose to share.</p>

<h2>Cookies and tracking</h2>
<p>When we last checked, our own web pages did not set cookies and did not run advertising or tracking scripts. [CONFIRM: cookies check] [CONFIRM: Cloudflare Web Analytics] We plan to add Cloudflare Web Analytics, which is designed to count visits without cookies; if we do, we will update this notice first. Our request form is run by Tally on its own website, and Tally may set its own cookies; see Tally's privacy policy. [CONFIRM: Tally cookies] [CONFIRM: Cloudflare logging] Our hosting provider may keep ordinary server logs.</p>

<h2>Why we use it, and our lawful basis</h2>
<table>
  <thead><tr><th>Purpose</th><th>Lawful basis (UK GDPR Article 6)</th></tr></thead>
  <tbody>
    <tr><td>Answering your request and building your report</td><td>Contract, or steps you ask us to take before a contract (6(1)(b))</td></tr>
    <tr><td>Reading your Search Console data</td><td>Contract (6(1)(b)); you choose to grant access and can remove it at any time</td></tr>
    <tr><td>Emailing limited companies about our service (see below)</td><td>Legitimate interests (6(1)(f))</td></tr>
    <tr><td>Keeping any accounting records we are required to keep</td><td>Legal obligation (6(1)(c)) [CONFIRM: tax records]</td></tr>
  </tbody>
</table>

<h2>Business email and your right to opt out</h2>
<p>We may email business contacts at limited companies and LLPs about our service. The Privacy and Electronic Communications Regulations (PECR) allow this for corporate bodies, and we do not email sole traders or ordinary partnerships this way. Every such email says who we are and how to stop them. Reply "stop" or write to [CONTACT EMAIL] and we will not email you again. We keep a short do-not-email list so that we remember. You can also object under data protection law at any time.</p>

<h2>Data you pass on from your clients</h2>
<p>[CONFIRM: roles] If you give us Search Console access or exports that belong to your client, you tell us you are allowed to. We use that data only to produce your report, and we will not use it for our own purposes. Who is the "controller" of that data, and whether we act as your processor, depends on your arrangement with your client; we will confirm this in writing before any access is requested.</p>

<h2>How long we keep it (proposed)</h2>
<p>These are our proposed periods and may change before launch. We keep personal data only as long as we need it for the reasons above.</p>
<ul>
  <li>Form answers and emails: up to 12 months after our last contact with you (proposal).</li>
  <li>Search Console data: deleted within 30 days after the report is delivered, unless you ask us to keep it for a follow-up (proposal).</li>
  <li>Do-not-email records: kept so we honour your request.</li>
  <li>Customer and invoice records, if we have any: for the period the law requires [CONFIRM: tax records].</li>
</ul>

<h2>Who else handles your data</h2>
<ul>
  <li><strong>Cloudflare</strong> hosts this website.</li>
  <li><strong>Google Workspace</strong> provides our email and file storage.</li>
  <li><strong>Tally</strong> runs our request form.</li>
</ul>
<p>We do not sell your data. [CONFIRM: transfers] Some of these providers may process data outside the UK. We will list where, and the safeguards each relies on, before launch.</p>

<h2>Your rights</h2>
<p>You can ask us to give you a copy of your data, correct it, delete it, restrict or object to how we use it, or move it to another service. You can object to business email at any time and we will stop.</p>

<h2>How to ask for deletion</h2>
<p>Email [CONTACT EMAIL] with the subject "Delete my data" and the email address you used. We will reply in writing and delete your data, except records we must keep by law. The law requires us to respond without undue delay and at the latest within one month. If your request is complex we may extend that by up to two further months, and if so we will tell you within the first month and explain why. If you granted Search Console access, you can also remove our access yourself in your Google account settings.</p>

<h2>Complaints</h2>
<p>Please tell us first so we can put it right. You can also complain to the Information Commissioner's Office at <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>.</p>
```

---

## Short terms (HTML body)

```html
<h1>Terms</h1>
<p class="note">Last updated: [LAST UPDATED DATE]</p>

<h2>Who these terms are with</h2>
<p>These terms are between you and FAEVRA LTD, company number 17534431, registered office 66 Paul Street, London, England, United Kingdom, EC2A 4NA. By requesting a report you agree to them. They are for businesses, not consumers.</p>

<h2>What we provide</h2>
<p>A plain-English report explaining a drop in search traffic, based on the Search Console data you give us. The report is our analysis. It is information, not a guarantee of any result, ranking or recovery in traffic.</p>

<h2>What you must do</h2>
<ul>
  <li>Only share data you are allowed to share. If it belongs to a client, you confirm they agree.</li>
  <li>Give accurate information.</li>
</ul>

<h2>Search Console access</h2>
<p>Any access is read-only and used only to build your report. You can remove it at any time in your Google account. We do not change anything in your or your client's account.</p>

<h2>Price</h2>
<p>The first report for one client site is free while we are starting out. We will agree any paid work with you in writing before it begins.</p>

<h2>Using the report</h2>
<p>You may share the report with your own clients. Please do not present it as an official Google document.</p>

<h2>Our responsibility</h2>
<p>We take care over our reports, but we cannot promise they are error-free, so please check important decisions yourself. Nothing in these terms limits liability for death or personal injury caused by negligence, for fraud, or for anything else the law does not allow us to limit. [CONFIRM: liability cap] Otherwise, our total liability to you for anything connected with a report is limited to the greater of the fees you paid us for it and &pound;100. We are not liable for lost profit or indirect loss.</p>

<h2>Privacy</h2>
<p>How we use personal data is in our <a href="privacy.html">privacy notice</a>.</p>

<h2>Changes and law</h2>
<p>We may update these terms and will change the date above. These terms are governed by the law of [CONFIRM: England and Wales; governing law and courts to be settled with adviser]; its courts have jurisdiction.</p>
```

The liability wording (greater of fees paid or 100 pounds) is a proposal only, for the founder's adviser to assess for reasonableness. No claim is made that it is legally valid.

---

## Sources (opened 2026-10-24 unless stated)

- Companies House, FAEVRA LTD: https://find-and-update.company-information.service.gov.uk/company/17534431 (as of 2026-10-24, via docs/status/context.json). Name, number, registered office. Page does not state jurisdiction.
- ICO, data protection fee: https://ico.org.uk/for-organisations/data-protection-fee/ . Organisations, including sole traders, that use personal information need to pay the fee unless exempt. No amounts or exemption list on this page.
- ICO, data protection fee self-assessment: https://ico.org.uk/for-organisations/data-protection-fee/self-assessment/ . Helps you decide if you need to pay the fee and how much; takes about 10 minutes.
- ICO, right to erasure: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-erasure/ . Respond without undue delay and at the latest within one month; extendable by a further two months if complex, with notice in the first month.
- ICO, electronic mail marketing (PECR): https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/ . Corporate bodies may be emailed without prior consent; sole traders and some partnerships count as individuals; keep a do-not-email list; do not hide the sender; guidance under review for the Data (Use and Access) Act.
- ICO, legitimate interests: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/what-is-the-legitimate-interests-basis/ . Purpose, necessity and balancing tests, all before processing starts.
- ICO, storage limitation: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/ . No fixed periods; justify retention; review; erase or anonymise.
- Site check: `apps/web/index.html` read 2026-10-24 for v2 (no scripts other than JSON-LD; one external link, `tally.so`). Not re-checked in v3.
- Not sourced and so not stated: tax-record retention period, international transfer safeguards, Tally and Cloudflare cookie behaviour.
