# DRAFT - not legal advice. Founder has declined an external check (24 Oct 2026) and accepts the wording himself.

Status: revision 4 of the privacy notice only (terms later), from docs/drafts/privacy-and-terms-v3.md and the founder decisions of 24 Oct 2026. HTML is body content only; the developer places it in `apps/web/privacy.html`. The build should fail on any remaining "[".

## Placeholders still open

1. [CONTACT EMAIL] - add once the mailbox exists (board #3).
2. [LAST UPDATED DATE] - date of publication.
3. [CONFIRM: Cloudflare Web Analytics cookie-free] - developers.cloudflare.com/web-analytics/ could not be opened (WebFetch permission not granted, 2026-10-24), so the "no cookies" claim is left out.
4. [CONFIRM: Tally cookies: check Tally form cookies in a private window]
5. [CONFIRM: cookies check] - re-verify live pages and Cloudflare Pages headers set no cookies.
6. [CONFIRM: Cloudflare logging] - what request data Cloudflare Pages records.
7. [CONFIRM: Cloudflare data and country], [CONFIRM: Google Workspace data and country], [CONFIRM: Tally data and country] - none of the providers' own privacy or data-location pages were opened.

Resolved: England and Wales; retention now the founder's policy; roles written; tax-record placeholder replaced by "if and when we issue invoices".

## Privacy notice (HTML body)

```html
<h1>Privacy notice</h1>
<p class="note">Last updated: [LAST UPDATED DATE]</p>

<h2>Who we are</h2>
<p>FAEVRA LTD ("Faevra", "we") is a company registered in England and Wales, company number 17534431, with its registered office at 66 Paul Street, London, England, United Kingdom, EC2A 4NA. Contact us at [CONTACT EMAIL].</p>

<h2>What we collect</h2>
<ul>
  <li><strong>Request form answers.</strong> What you type into our Tally form, such as your name, business name, website and what you want from a report.</li>
  <li><strong>Your email address</strong> and anything you write to us in emails.</li>
  <li><strong>Search Console data, only if you or your client grants access or gives us an export.</strong> We use it only to build the report you asked for.</li>
</ul>
<p>We ask only for what is listed above, and we do not set out to collect personal data about your clients beyond what appears in the Search Console data you choose to share.</p>

<h2>Our role: controller and processor</h2>
<p>For your form answers and emails, Faevra is the "controller" under UK GDPR: we decide how and why that data is used.</p>
<p>For a client's Search Console export that an agency gives us, Faevra is the agency's "processor" and the agency is the controller. In that case we:</p>
<ul>
  <li>use the data only on the agency's instructions, to produce the report;</li>
  <li>delete or return it on request;</li>
  <li>keep it secure; and</li>
  <li>use no sub-processors beyond those listed in "Who else handles your data" below.</li>
</ul>

<h2>Cookies and tracking</h2>
<p>When we last checked, our own web pages did not set cookies and did not run advertising or tracking scripts. [CONFIRM: cookies check] We plan to use Cloudflare Web Analytics to count visits. [CONFIRM: Cloudflare Web Analytics cookie-free] We will update this notice before it is switched on. [CONFIRM: Cloudflare logging] Our hosting provider may keep ordinary server logs. Our request form is run by Tally on its own website, and Tally may set its own cookies. [CONFIRM: Tally cookies: check Tally form cookies in a private window]</p>

<h2>Why we use it, and our lawful basis</h2>
<table>
  <thead><tr><th>Purpose</th><th>Lawful basis (UK GDPR Article 6)</th></tr></thead>
  <tbody>
    <tr><td>Answering your request and building your report</td><td>Contract, or steps you ask us to take before a contract (6(1)(b))</td></tr>
    <tr><td>Reading your Search Console data</td><td>Contract (6(1)(b)); you choose to grant access and can remove it at any time</td></tr>
    <tr><td>Emailing limited companies about our service (see below)</td><td>Legitimate interests (6(1)(f))</td></tr>
    <tr><td>Keeping invoice and tax records, if and when we issue invoices</td><td>Legal obligation (6(1)(c))</td></tr>
  </tbody>
</table>

<h2>Business email and your right to opt out</h2>
<p>We may email business contacts at limited companies and LLPs about our service. The Privacy and Electronic Communications Regulations (PECR) allow this for corporate bodies, and we do not email sole traders or ordinary partnerships this way. Every such email says who we are and how to stop them. Reply "stop" or write to [CONTACT EMAIL] and we will not email you again. We keep a short do-not-email list so that we remember. You can also object under data protection law at any time.</p>

<h2>Data you pass on from your clients</h2>
<p>If you give us Search Console access or exports that belong to your client, you tell us you are allowed to. We act as your processor for that data, as set out above, and we will not use it for our own purposes.</p>

<h2>How long we keep it</h2>
<ul>
  <li>Form answers and emails: up to 12 months.</li>
  <li>Search Console exports: deleted 30 days after the report is delivered.</li>
  <li>Do-not-email records: kept so we honour your request.</li>
  <li>Invoice and tax records, if and when we issue invoices: for as long as the law requires.</li>
</ul>

<h2>Who else handles your data</h2>
<p>These are our processors. We use no others.</p>
<ul>
  <li><strong>Cloudflare</strong> hosts this website. [CONFIRM: Cloudflare data and country]</li>
  <li><strong>Google Workspace</strong> provides our email and file storage. [CONFIRM: Google Workspace data and country]</li>
  <li><strong>Tally</strong> runs our request form. [CONFIRM: Tally data and country]</li>
</ul>
<p>We do not sell your data. If a provider processes data outside the UK, we rely on safeguards that UK data protection law accepts for such transfers.</p>

<h2>Your rights</h2>
<p>You can ask us to give you a copy of your data, correct it, delete it, restrict or object to how we use it, or move it to another service. You can object to business email at any time and we will stop.</p>

<h2>How to ask for deletion</h2>
<p>Email [CONTACT EMAIL] with the subject "Delete my data" and the email address you used. We will reply in writing and delete your data, except records we must keep by law. The law requires us to respond without undue delay and at the latest within one month. If your request is complex we may extend that by up to two further months, and if so we will tell you within the first month and explain why. If you granted Search Console access, you can also remove our access yourself in your Google account settings.</p>

<h2>Complaints</h2>
<p>Please tell us first so we can put it right. You can also complain to the Information Commissioner's Office at <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>.</p>
```

## Sources

- Companies House: https://find-and-update.company-information.service.gov.uk/company/17534431 (as of 2026-10-24, context.json); jurisdiction confirmed by founder 24 Oct 2026.
- ICO erasure, PECR and other pages: as cited in v3 (opened 2026-10-24 there).
- Not opened, so not stated: Cloudflare Web Analytics page (https://developers.cloudflare.com/web-analytics/, blocked), and Cloudflare, Google Workspace and Tally privacy or data-location pages.
