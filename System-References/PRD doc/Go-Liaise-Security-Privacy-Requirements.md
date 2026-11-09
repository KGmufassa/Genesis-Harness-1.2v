# Go Liaise — Security, Privacy, and Compliance Requirements

**Status:** Proposed implementation baseline; legal applicability and public policies pending review  
**Product scope updated:** 2026-11-08 (PRD 1.4); legal/source review remains pending  
**Applies to:** Registered and guest websites at initial launch; backend, media storage, operational tooling, and service providers; native iOS/Android companions at their later release

These requirements support the Go Liaise PRD. They are not final Terms of Service or a Privacy Policy, a security certification, or a determination of legal compliance. Controls reduce risk but cannot guarantee protection from lawsuits. Qualified counsel should review legal applicability and public policies for the actual business and launch markets before release.

---

## Frameworks and Verification Targets

| Framework | Go Liaise use |
|---|---|
| [OWASP ASVS](https://asvs.owasp.org/) | Use ASVS 5.0.0 Level 2 as the proposed web/API verification target. Map applicable controls to implementation and evidence; document exclusions and their rationale. |
| [OWASP MASVS / MASTG](https://mas.owasp.org/MASVS/04-Assessment_and_Certification/) | Before the later native release, verify native storage, authentication, networking, platform interaction, and privacy with relevant mobile tests. Verify backend endpoints separately using ASVS. |
| [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | Structure secure design, code review, dependency management, release protection, and vulnerability response throughout development. |
| [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | Inventory personal data and purposes, assign responsibility, assess privacy risks, and define controls and user choices. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Target Level AA for the full registered and guest website, supported by keyboard and assistive-technology checks; separately verify native accessibility. This is an engineering target, not a legal safe harbor. |

Pin framework versions and applicable control IDs during architecture planning. Record each applicable control as pending, implemented, verified, or not applicable, with owner and evidence. Do not advertise certification or compliance based on adopting a checklist; OWASP does not certify applications.

---

## Product Security and Privacy Requirements

| ID | Required behavior | Acceptance evidence |
|---|---|---|
| SECURITY-GL-001 | Deny access by default; enforce event, role, invitation, and resource authorization on every protected backend request. Solo trips are owner-only, including itinerary, notes, and media. A host cannot access another host's event through identifiers or support tools. Solo-to-group conversion requires an owner-confirmed audience/content review and preserves private notes and unpublished photos; invitation acceptance and membership rules still apply. | Automated cross-event and role-boundary tests for solo/group trips, notes, bulletins, RSVP, itineraries, albums, thumbnails, and photos, including direct URLs and conversion privacy tests. |
| SECURITY-GL-002 | Treat invitation tokens as secrets. Apply expiration, revocation, abuse limits, and guest-session controls. Exclude tokens from analytics, logs, referrers, and third-party embeds; avoid persistent sensitive browser caching. | Expired/revoked links and sessions fail; token-leak and shared-device tests pass. |
| SECURITY-GL-003 | Support website registration/sign-in and later native sign-in to the same account. Preserving an invitation through authentication must not automatically grant membership, bypass host approval, or submit a vote. Use maintained authentication mechanisms, expiring single-use verification codes, retry limits, and secure recovery. Require MFA for production administrators and privileged support access. A shared QR token cannot own all attendees' RSVPs. | Replay, brute-force, session-revocation, recovery, and separate-RSVP-ownership tests. |
| SECURITY-GL-004 | Encrypt transport and managed storage/backups; keep credentials out of clients and source control. Restrict and audit production access. Protect website sessions from unauthorized use and validate session-bound state-changing requests. For the later native release, protect credentials using platform secure storage. | Configuration review, secret scanning, access audit, website session/request-protection tests, and native storage tests for the later mobile release. |
| SECURITY-GL-005 | Keep media private by default. Authorize metadata and image delivery; validate authorized browser uploads at website launch and camera/library uploads at native release, including destination membership, file type/content, and size limits; strip unnecessary location metadata from guest-delivered images. Revocation must stop future protected retrievals, including through caches and existing media links. | Direct-URL, cache, metadata, unsafe-file, and revoked-session tests. Verify that uploading or converting a solo trip does not automatically publish photos. Previously saved copies cannot be recalled. |
| SECURITY-GL-006 | Maintain a data inventory covering registered accounts, solo/group trips, private notes, guest identifiers, RSVPs, photos, event locations, device data, logs, and vendors. Record purpose, access, storage location, retention trigger/duration, deletion method, and lawful basis where applicable. Do not collect sensitive information merely because a form can accept it. | Approved data inventory and field-by-field review before production collection. |
| SECURITY-GL-007 | Provide usable access, correction, export, and deletion request paths for members and accountless guests, with proportionate identity checks. Define treatment of shared content, backups, processor copies, and legally required retention. | End-to-end guest/member request tests and a documented retention/deletion schedule; no indefinite default retention. |
| SECURITY-GL-008 | Default solo trip content to owner-only and guest visibility to unpublished/private until the owner/host explicitly selects the audience. Keep personal notes author-private unless explicitly shared; converting trip mode does not change that choice. Provide notices before collection; distinguish essential processing from optional marketing, analytics, and permissions. No nonessential tracking SDKs until their purposes and consent requirements are reviewed. | Permission and SDK inventory, notice review, and tests that declining optional choices preserves core guest access. |
| SECURITY-GL-009 | Provide photo/content reporting, removal requests, abusive-user controls, and a platform escalation route available to guests without creating an account. Define uploader rights and responsibility for images of other people; host publication is not proof of permission from everyone depicted. | Report-to-resolution walkthrough, responsible operator, and reviewed content/rights policy. |
| SECURITY-GL-010 | Assign incident and vulnerability owners; monitor suspicious access and verification abuse, preserve proportionate audit evidence, rehearse containment and restoration, and define breach-notification decision procedures. | Incident tabletop, backup restoration, and notification/contact runbooks. Determine legal deadlines by jurisdiction, not one universal timer. |
| SECURITY-GL-011 | Review code and dependencies, scan secrets, test authorization, and conduct an independent security review of exposed registered/guest web and API surfaces before website launch, and native surfaces before their later release. | Release-linked findings, remediation/retests, and documented control coverage. Unresolved critical/high exploitable issues block launch. |
| SECURITY-GL-012 | Review cloud, email/SMS, media, analytics, and crash-reporting vendors for actual data handling, access, retention, deletion, subprocessors, and contractual obligations. Keep public disclosures aligned with deployed SDKs and services. | Vendor/data-flow inventory, reviewed contracts, and release disclosure comparison. |

Data minimization, retention, and service-provider controls follow the approach described in the [FTC business security guide](https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business). Where GDPR applies, document the applicable legal basis and principles rather than treating consent as the universal basis; see [EDPB guidance](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en).

---

## Required Policy Deliverables

These are deliverables to draft and review against implemented behavior, not policies already in force. Assign a named person to each owner role before launch.

| Policy / operational document | Minimum coverage | Owner role |
|---|---|---|
| Privacy Notice | Registered users and guests; collected data, purposes, recipients, retention, rights, contact route, and relevant international transfers. Link it before website registration and RSVP/verification and from website settings; include native settings at the later mobile release. Explain solo-trip privacy and reviewed sharing on conversion. | Product + privacy/legal |
| Terms of Service and Acceptable Use | Eligibility, host/guest responsibilities, prohibited conduct, event responsibilities, account suspension, complaints, and locally reviewed contractual terms. Do not assume a blanket disclaimer removes legal duties. | Product + legal |
| Photo and User-Generated Content Policy | Rights to upload/share, audience controls, consent/permissions where needed, reporting, moderation, copyright/takedown handling, and appeals. Address photos of nonusers and minors. | Trust/safety + legal |
| Retention, Deletion, and Rights Procedure | Specific schedules by data category, guest identity verification, request tracking, backups, vendors, legal holds, and deletion completion evidence. | Privacy + engineering |
| Access, Secrets, and Secure Development Policy | Least privilege, administrator MFA, review/release controls, patch triage, secret rotation, and security reporting. | Engineering/security |
| Incident Response and Breach Procedure | Named responders, containment, evidence, recovery, jurisdiction-specific notification assessment, and communication templates. | Security + legal |
| Vendor and Data Processing Procedure | Vendor diligence, agreements, subprocessors, transfers, termination/deletion, and SDK changes. | Operations + privacy/legal |
| Messaging, Tracking, and Permissions Policy | Separate event/verification messages from marketing, applicable consent and opt-out rules, cookies/SDKs, and optional location/media permissions. | Product + privacy/legal |

Website launch requires applicable web/API controls, reviewed public policies, and accurate web/vendor disclosures. Mobile-specific verification and store disclosures are separate gates for the later native release and are not prerequisites for website launch. Review platform requirements as part of native release preparation. Apple addresses user-generated content, privacy, and in-app account deletion in its [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/). Google requires accurate data practices under its [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en), including [in-app and web account-deletion request paths](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en) for covered account-creating apps. Guest deletion/request routes are an additional Go Liaise product requirement.

---

## Applicability Decisions Still Required

| Decision | What must be resolved |
|---|---|
| Operating entity and launch markets | Record company location, target countries/states, users served, vendors, and data-hosting locations. Counsel must identify applicable privacy, consumer, accessibility, breach, and messaging rules. |
| User ages | Decide whether minors may use registered web, guest, and later native experiences, including accountless RSVP. If children may use the service, assess age assurance, guardian involvement, and child-data obligations before enabling that audience. An adults-only label does not by itself settle applicability or handling of children's photos. |
| Expense/payment scope | Distinguish recording balances from accepting payments or holding/transferring funds. Do not enable payment processing until the provider model, payment-security scope, and any financial regulatory obligations are assessed. |
| Live location and tracking | Treat precise/background location as a separate privacy assessment before enabling it; define purpose, audience, permission withdrawal, and retention. Current event venue addresses do not authorize continuous tracking. |
| Advertising/analytics | Document whether data will be used for advertising, cross-app tracking, sale/sharing, or profiling; review each SDK and associated user choices before activation. |

Examples for applicability review, not conclusions: GDPR may apply based on establishment or relevant offering/monitoring activities involving people in the EEA ([EDPB](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en)); California CCPA coverage depends on the business and statutory criteria ([California Attorney General](https://www.oag.ca.gov/privacy/ccpa)); US COPPA covers specified child-directed services and certain actual-knowledge situations involving children under 13 ([FTC](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions)). Other markets and US states may impose additional obligations. Do not assume these three regimes are exhaustive or automatically applicable.

---

## Development and Release Evidence

- **Stages 1–2:** Resolve audience, jurisdictions, monetization, data purposes, and product risks; record legal questions and named owners.
- **Stage 3:** Map `SECURITY-GL-*` requirements to service/data/API decisions; model threats around website accounts, owner-only solo data, solo-to-group conversion, invitation forwarding, guest identity, private media, and administrative access; choose retention and revocation mechanisms.
- **Stage 4:** Include website registration notices, solo privacy and conversion audience/content review, guest rights requests, account deletion, content reporting, verification, consent/permission choices, browser upload failures, and denied/revoked states in individual screen specifications before Stitch review. Include accessibility behavior.
- **Stage 5:** Convert each requirement into traceable tickets and tests with owners. Preserve the requirement IDs rather than considering a policy link sufficient implementation.
- **Stage 6:** Record control-test results, independent review findings, remediation evidence, tested deletion/revocation paths, owner-only solo access, conversion privacy, website sessions, and authorized browser uploads. Validate native storage and camera/library permission/upload paths for the later native release.
- **Stage 7:** Require completed applicability review, reviewed public policies matching the deployed website, web/vendor disclosures (and native/store disclosures for the later native release), resolved launch-blocking vulnerabilities, named incident/moderation contacts, and successful restore/incident exercises. Record the deployed release and approvers. Unresolved applicability or mandatory legal duties cannot be waived by a generic risk acceptance.
- **Stage 8:** Review vendor/SDK changes, vulnerabilities, complaints, access, retention jobs, and changes in markets, audience, features, or applicable rules.

This document defines product requirements and proposed launch criteria. It does not execute a security assessment, implement the controls, approve a stage, or modify the orchestration harness to enforce these new criteria automatically.
