# SSO Supplier Evaluation Template

**Supplier Name:** `[ENTER NAME]`
**Website:** `[ENTER URL]`
**Evaluator:** `[ENTER NAME]`
**Date:** `[YYYY-MM-DD]`

**Source Materials:**
- `[LIST PROPOSAL DOCUMENTS]`

---

## 1. Architecture & Technical Solution
*Focus on the proposed identity system design and technology choices.*

**Proposed Stack:**
- [ ] **Identity Platform/Framework Used:** `[Auth0 / Firebase / Cognito / Custom / etc.]`
- [ ] **Cloud Provider & Region:** `[AWS / GCP / Azure — Region]`
- [ ] **Database for User Identity & PII:** `[PostgreSQL / DynamoDB / etc.]`
- [ ] **Architecture Diagram Provided?** (Yes/No): `[ ]`

**Protocol & Standards Compliance:**
- [ ] **OIDC (OpenID Connect) Support?** (Yes/No): `[ ]`
- [ ] **OAuth 2.0 Support?** (Yes/No): `[ ]`
- [ ] **JWT Token Issuance?** (Yes/No): `[ ]`
- [ ] **Token Format & Claims Configurable?** (Yes/No): `[ ]`

**Authentication Methods:**
- [ ] Email + Password `[ ]`
- [ ] Google Social Login `[ ]`
- [ ] Apple Social Login `[ ]`
- [ ] Facebook Social Login `[ ]`
- [ ] Other: `[DESCRIBE]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 2. LiveLike Integration & Handshake
*Focus on compatibility and readiness to integrate with the LiveLike platform.*

**Integration Readiness:**
- [ ] **SSO Endpoint Available for LiveLike?** (Yes/No): `[ ]`
- [ ] **Token Format Compatible with LiveLike Spec?** (Yes/No): `[ ]`
- [ ] **CazéTV Auth → LiveLike ID Mapping Flow Described?** (Yes/No): `[ ]`
- [ ] **Handshake Certification Plan?** (Yes/No): `[ ]`

**Integration Experience:**
- [ ] **Previous Experience with Federated Identity Handshakes?** (Yes/No): `[ ]`
  > `[DESCRIBE CASES IF YES]`
- [ ] **Estimated Integration Time with LiveLike:** `[ENTER DAYS/WEEKS]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 3. Scalability & Peak Performance
*Focus on ability to handle World Cup registration and authentication spikes.*

**Peak Capacity:**
- [ ] **Stated Peak Capacity (req/sec or req/min):** `[ENTER NUMBER]`
- [ ] **Evidence / Load Test Results Provided?** (Yes/No): `[ ]`
- [ ] **Can Handle 100k+ req/min for Auth?** (Yes/No): `[ ]`
- [ ] **Strategy for Millions of Account Creations in Minutes:**
  > `[DESCRIBE STRATEGY]`

**Infrastructure Resilience:**
- [ ] **Auto-Scaling Configured?** (Yes/No): `[ ]`
- [ ] **Warm-Up / Pre-Scaling Plan for Launch Day?** (Yes/No): `[ ]`
- [ ] **Multi-AZ / Multi-Region Redundancy?** (Yes/No): `[ ]`
- [ ] **Rate Limiting & Abuse Protection?** (Yes/No): `[ ]`

**Reference Evidence:**
- [ ] **Largest B2C Auth Deployment (Users):** `[ENTER NUMBER]`
- [ ] **Highest Concurrent Auth Events Handled:** `[ENTER NUMBER]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 4. Security, LGPD & Compliance
*Focus on data protection, PII handling, and Brazilian regulatory compliance.*

**Data Protection:**
- [ ] **LGPD Compliant?** (Yes/No): `[ ]`
- [ ] **PII Stored in Brazil?** (Yes/No): `[ ]`
- [ ] **Data Processing Agreement (DPA) Provided?** (Yes/No): `[ ]`
- [ ] **Encryption at Rest?** (Yes/No): `[ ]`
- [ ] **Encryption in Transit (TLS)?** (Yes/No): `[ ]`
- [ ] **Credential Hashing Algorithm:** `[bcrypt / Argon2 / PBKDF2 / etc.]`

**Security Posture:**
- [ ] **Certifications (ISO 27001, SOC 2, etc.):** `[LIST]`
- [ ] **Penetration Test Reports Available?** (Yes/No): `[ ]`
- [ ] **WAF / DDoS Protection?** (Yes/No): `[ ]`
- [ ] **MFA Support Available?** (Yes/No): `[ ]`
- [ ] **Brute-Force / Account Takeover Protection?** (Yes/No): `[ ]`

**Age Verification & Consent:**
- [ ] **Age Verification Mechanism?** (Yes/No): `[ ]`
- [ ] **Parental Consent Flow for Minors (13+)?** (Yes/No): `[ ]`
- [ ] **LGPD-Specific Consent Audit Trail?** (Yes/No): `[ ]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 5. Data Ownership, Access & Portability
*Focus on ensuring CazéTV retains full ownership and control of user identity data.*

**Ownership:**
- [ ] **All User Data 100% Owned by CazéTV?** (Yes/No): `[ ]`
- [ ] **Any Restrictions on Data Usage?** (Yes/No): `[ ]`

**Access:**
- [ ] **Direct Database Access Provided?** (Yes/No): `[ ]`
- [ ] **Admin Dashboard for User Management?** (Yes/No): `[ ]`
- [ ] **APIs for Data Extraction?** (Yes/No): `[ ]`

**Exit Scenario:**
- [ ] **Full Data Export Guaranteed on Contract End?** (Yes/No): `[ ]`
- [ ] **Migration Assistance Included?** (Yes/No): `[ ]`
- [ ] **Lock-In Risk Assessment:**
  > `[DESCRIBE — platform dependency, proprietary formats, migration complexity]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 6. Extensibility & Identity Federation
*Focus on future-proofing the architecture for sponsor integration.*

- [ ] **Supports Multiple Identity Providers (IdPs)?** (Yes/No): `[ ]`
- [ ] **Can Add Sponsor as Secondary IdP Without Refactoring?** (Yes/No): `[ ]`
- [ ] **Identity Federation Strategy Described?** (Yes/No): `[ ]`
  > `[DESCRIBE STRATEGY IF YES]`
- [ ] **Account Linking (Social → Sponsor) Supported?** (Yes/No): `[ ]`
- [ ] **Custom Claims / Attributes Extensible?** (Yes/No): `[ ]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 7. Operational Support & SLA
*Focus on ongoing reliability during World Cup operations.*

**SLA Commitments:**
- [ ] **Uptime SLA (%):** `[ENTER %]`
- [ ] **P1 Incident Response Time:** `[ENTER TIME]`
- [ ] **P2 Incident Response Time:** `[ENTER TIME]`
- [ ] **24/7 Monitoring Included?** (Yes/No): `[ ]`
- [ ] **Proactive Alerting?** (Yes/No): `[ ]`

**Support Structure:**
- [ ] **Dedicated Support Team?** (Yes/No): `[ ]`
- [ ] **War-Room During Match Days?** (Yes/No): `[ ]`
- [ ] **Portuguese-Speaking Support?** (Yes/No): `[ ]`
- [ ] **Local Presence in Brazil?** (Yes/No): `[ ]`

**Maintenance:**
- [ ] **Security Patches Included in Contract?** (Yes/No): `[ ]`
- [ ] **Scheduled Maintenance Windows Defined?** (Yes/No): `[ ]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 8. Registration & User Experience
*Focus on the end-user registration and login flow.*

**Registration Flow:**
- [ ] **Frictionless Registration? (Minimal Fields)**  (Yes/No): `[ ]`
- [ ] **Email Verification Flow?** (Yes/No): `[ ]`
- [ ] **Password Recovery / Reset Flow?** (Yes/No): `[ ]`
- [ ] **Account Deduplication Strategy?** (Yes/No): `[ ]`

**User Management:**
- [ ] **Self-Service Profile Edit?** (Yes/No): `[ ]`
- [ ] **Account Deletion (LGPD Right)?** (Yes/No): `[ ]`
- [ ] **Session Management (Multi-Device)?** (Yes/No): `[ ]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 9. Documentation & Knowledge Transfer
*Focus on ensuring no vendor lock-in through complete documentation.*

- [ ] **Full Architecture Documentation Provided?** (Yes/No): `[ ]`
- [ ] **API Documentation Provided?** (Yes/No): `[ ]`
- [ ] **Runbook / Ops Documentation?** (Yes/No): `[ ]`
- [ ] **Knowledge Transfer Sessions Included?** (Yes/No): `[ ]`
- [ ] **Source Code Delivered (if custom)?** (Yes/No): `[ ]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 10. Timeline & Delivery
*Focus on ability to meet the aggressive delivery window.*

- [ ] **Proposed Kick-Off Date:** `[ENTER DATE]`
- [ ] **Proposed Go-Live Date:** `[ENTER DATE]`
- [ ] **LiveLike Integration Complete By:** `[ENTER DATE]`
- [ ] **Timeline Breakdown Provided?** (Yes/No): `[ ]`

**Milestone Plan:**
| Phase | Description | Duration | Date |
|---|---|---|---|
| Kick-Off | `[DESCRIBE]` | `[ ]` | `[ ]` |
| Development | `[DESCRIBE]` | `[ ]` | `[ ]` |
| Integration & Testing | `[DESCRIBE]` | `[ ]` | `[ ]` |
| Go-Live | `[DESCRIBE]` | `[ ]` | `[ ]` |

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 11. Commercial, Contractual & Financial
*Focus on cost structure, payment terms, and financial predictability.*

**Cost Structure:**
- [ ] **Implementation Cost (Phase 1):** `[ENTER VALUE]`
- [ ] **Monthly Operations Cost (Phase 2):** `[ENTER VALUE]`
- [ ] **Pricing Model:** `[Fixed / Usage-Based / Hybrid]`

**Cost Variability:**
- [ ] **Costs Increase with User Volume?** (Yes/No): `[ ]`
- [ ] **Costs Increase with Auth Request Volume?** (Yes/No): `[ ]`
- [ ] **Hidden Costs Identified:** `[LIST — infra, licenses, overages, etc.]`

**Contract Terms:**
- [ ] **Minimum Contract Duration (Months):** `[ENTER NUMBER]`
- [ ] **Early Termination Penalties?** (Yes/No): `[ ]`
  > `[DESCRIBE IF YES]`
- [ ] **Payment Terms:** `[DESCRIBE]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

## 12. Team, Experience & References
*Focus on supplier maturity in identity/auth at scale.*

- [ ] **Years in Market:** `[ENTER NUMBER]`
- [ ] **B2C Identity System Cases at Scale:** `[ENTER NUMBER & DESCRIBE]`
- [ ] **Largest Auth Deployment (Users):** `[ENTER NUMBER]`
- [ ] **Sports / Entertainment / Media Cases?** (Yes/No): `[ ]`
  > `[DESCRIBE IF YES]`
- [ ] **Reference Contacts Provided?** (Yes/No): `[ ]`
- [ ] **Team Size Dedicated to This Project:** `[ENTER NUMBER]`

- **Observations:**
  > `[ENTER QUALITATIVE NOTES]`
- **Block Rating (1-5):** `[ ]`

---

# Executive Summary & Recommendation

## Block Ratings Summary
| Block | Rating | Status |
| :--- | :--- | :--- |
| 1. Architecture & Technical Solution | **/5** | |
| 2. LiveLike Integration & Handshake | **/5** | |
| 3. Scalability & Peak Performance | **/5** | |
| 4. Security, LGPD & Compliance | **/5** | |
| 5. Data Ownership, Access & Portability | **/5** | |
| 6. Extensibility & Identity Federation | **/5** | |
| 7. Operational Support & SLA | **/5** | |
| 8. Registration & User Experience | **/5** | |
| 9. Documentation & Knowledge Transfer | **/5** | |
| 10. Timeline & Delivery | **/5** | |
| 11. Commercial, Contractual & Financial | **/5** | |
| 12. Team, Experience & References | **/5** | |
| **Average (all blocks)** | **/5** | |

## Automated Risk Flags
| Category | Flag Condition | Risk Level | Alert |
| :--- | :--- | :--- | :--- |
| | | | |

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| | | |

## Key Strengths
| Strength Area | Rating | Description |
| :--- | :--- | :--- |
| | | |

## Final Recommendation
`[PROCEED / PROCEED WITH CAUTION / DISCARD — with rationale]`
