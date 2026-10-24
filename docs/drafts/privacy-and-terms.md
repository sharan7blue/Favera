# DRAFT - not legal advice, founder to have checked

Status: draft for board #8. Not to be published until the founder has had it checked. The HTML below is body content only; the developer places it in new pages (suggested: `apps/web/privacy.html` and `apps/web/terms.html`, linked from the footer) using the existing page shell and `styles.css`.

## Placeholders to fill before publishing

| Placeholder | What is needed |
| --- | --- |
| [COMPANY NUMBER] | Companies House number for Faevra Ltd |
| [REGISTERED ADDRESS] | Registered office address |
| [CONTACT EMAIL] | Privacy mailbox. Per site rules, add only once the mailbox exists (board #3) |
| [LAST UPDATED DATE] | Date of publication |

## Points for the founder and your adviser to confirm

1. Retention periods below are proposals, not facts; confirm or change them.
2. Whether you need to register with the ICO (fee) and whether to name the ICO registration number.
3. Cloudflare, Google Workspace and Tally data-transfer terms and whether any processing happens outside the UK/EEA; the text says only that safeguards apply, so confirm that is true.
4. The legitimate-interests assessment for B2B email (PECR).
5. Whether the free report needs any liability wording beyond the terms below.

---

## Privacy notice (HTML body)

```html
<h1>Privacy notice</h1>
<p class="note">Last updated: [LAST UPDATED DATE]</p>

<h2>Who we are</h2>
<p>Faevra Ltd ("Faevra", "we") is a company registered in England and Wales, company number [COMPANY NUMBER], with its registered office at [REGISTERED ADDRESS]. We decide how and why your personal data is used, so we are the "controller" under UK GDPR. Contact us at [CONTACT EMAIL].</p>

<h2>What we collect</h2>
<ul>
  <li><strong>Request form answers.</strong> What you type into our Tally form, such as your name, business name, website and what you want from a report.</li>
  <li><strong>Your email address</strong> and anything you write to us in emails.</li>
  <li><strong>Search Console data, only if you or your client grants access.</strong> We ask for read-only access to a Search Console property. We use it only to build the report you asked for. We do not ask for any other client data.</li>
</ul>
<p>We do not collect anything else about your clients. We do not use advertising cookies or trackers on this site.</p>

<h2>Why we use it, and our lawful basis</h2>
<table>
  <thead><tr><th>Purpose</th><th>Lawful basis (UK GDPR Article 6)</th></tr></thead>
  <tbody>
    <tr><td>Answering your request and building your report</td><td>Contract, or steps you ask us to take before a contract (6(1)(b))</td></tr>
    <tr><td>Reading your Search Console data</td><td>Contract (6(1)(b)), and your consent when you grant access. You can withdraw it at any time</td></tr>
    <tr><td>Emailing limited companies about our service (see below)</td><td>Legitimate interests (6(1)(f))</td></tr>
    <tr><td>Keeping records for tax and accounts</td><td>Legal obligation (6(1)(c))</td></tr>
  </tbody>
</table>

<h2>Business email and your right to opt out</h2>
<p>We may email business contacts at limited companies about our service. We do this under the Privacy and Electronic Communications Regulations (PECR), which allow it for limited companies, and we do not email sole traders or ordinary partnerships this way. Every such email says who we are and how to stop them. Reply "stop" or write to [CONTACT EMAIL] and we will not email you again. We keep a short suppression record so that we remember not to.</p>

<h2>How long we keep it</h2>
<ul>
  <li>Form answers and emails: up to 12 months after our last contact with you, then deleted.</li>
  <li>Search Console data: deleted within 30 days after your report is delivered, unless you ask us to keep it for a follow-up report.</li>
  <li>Opt-out records: kept so we honour your request.</li>
  <li>Customer and invoice records: 6 years, as tax law requires.</li>
</ul>

<h2>Who else handles your data</h2>
<p>These providers process data for us under their own data-protection terms:</p>
<ul>
  <li><strong>Cloudflare</strong> hosts this website.</li>
  <li><strong>Google Workspace</strong> provides our email and file storage.</li>
  <li><strong>Tally</strong> runs our request form.</li>
</ul>
<p>We do not sell your data. Where a provider processes data outside the UK, it must use approved safeguards.</p>

<h2>Your rights</h2>
<p>You can ask us to give you a copy of your data, correct it, delete it, restrict or object to how we use it, or move it to another service. You can withdraw consent at any time. You can object to business email at any time and we will stop.</p>

<h2>How to ask for deletion</h2>
<p>Email [CONTACT EMAIL] with the subject "Delete my data" and the email address you used. We will confirm in writing and delete your data, except records we must keep by law. We aim to reply within one month. If you granted Search Console access, you can also remove our access yourself in your Google account settings.</p>

<h2>Complaints</h2>
<p>Please tell us first so we can put it right. You can also complain to the Information Commissioner's Office at <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>.</p>
```

---

## Short terms (HTML body)

```html
<h1>Terms</h1>
<p class="note">Last updated: [LAST UPDATED DATE]</p>

<h2>Who these terms are with</h2>
<p>These terms are between you and Faevra Ltd, company number [COMPANY NUMBER], registered office [REGISTERED ADDRESS]. By requesting a report you agree to them. They are for businesses, not consumers.</p>

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
<p>We take care over our reports, but we cannot promise they are error-free, so please check important decisions yourself. We do not limit liability for death or personal injury caused by negligence, fraud, or anything the law does not let us limit. Otherwise our total liability to you is limited to the amount you paid us for the report in question, and we are not liable for lost profit or indirect loss.</p>

<h2>Privacy</h2>
<p>How we use personal data is in our <a href="privacy.html">privacy notice</a>.</p>

<h2>Changes and law</h2>
<p>We may update these terms and will change the date above. These terms are governed by the law of England and Wales, and its courts have jurisdiction.</p>
```
