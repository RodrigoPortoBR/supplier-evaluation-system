# Supplier Evaluation Template

**Supplier Name:** `Easypromos`
**Website:** `[Not Specified]`
**Evaluator:** `Rodrigo`
**Date:** `2026-01-20`

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic.*

- [x] **Highest Participants Record (Single Game):** `Millions (Cumulative), >1M (Single Project, e.g. Real Madrid)`
- [ ] **Strategy for 10M Concurrent Users (5 mins before game):**
  > `Dedicated infrastructure, Predefined rate-limiting and queueing strategies, Pre-match submission windows. (Only for enterprise setups)`
- [ ] **Platforms Supported:**
    - [x] Web Desktop
    - [x] Web Mobile
    - [ ] App iOS `(Via WebView)`
    - [ ] App Android `(Via WebView)`
- [ ] **Uptime SLA (%):** `[Not Specified]`
- [x] **Support SLA 24/7?** (Yes/No): `Yes (For live events in enterprise agreement)`
- [ ] **Local Support in Brazil?** (Yes/No): `No (Centralized, but experienced with Brazil)`
- [x] **Auto-scaling Infrastructure?** (Yes/No): `Yes (Google Cloud)`
- [x] **Recent Load Test Evidence Provided?** (Yes/No): `Yes (Regular stress testing, custom load tests for large events)`
- **Observations:**
  > `Standard SaaS platform on GCP. For >5M users, they require custom enterprise setups with defined traffic patterns. No native apps, only WebView.`
- **Block Rating (1-5):** `[ ]`

---

## 2. Security, LGPD & Governance
*Focus on legal compliance and data safety.*

- [x] **LGPD/GDPR Compliant?** (Yes/No): `Yes`
- [ ] **Data Residency Country:** `Google Cloud (Location not specified)`
- [ ] **Certifications (ISO, SOC, etc.):** `Security Work Paper mentioned`
- [ ] **Penetration Test Report Available?** (Yes/No): `[See Security Work Paper]`
- **Observations:**
  > `Platform is LGPD-compliant with explicit consent management. Client is Data Controller, Easypromos is Data Processor.`
- **Block Rating (1-5):** `[ ]`

---

## 3. Core Product Features
*Focus on the betting/prediction mechanics.*

**Prediction Types:**
- [x] Match Result (1x2)
- [x] Exact Score
- [x] Special Predictions
- [ ] Live Predictions `(Explicitly stated as "No" in answers, possibly typo but unlikely given context)`

**Rankings:**
- [x] Global
- [ ] Public Leagues `(No)`
- [ ] Private Leagues `(No - but discussed as potential quick win or temporary view)`
- [x] By Period (Day/Round/Tournament)

**Private Leagues:**
- [ ] Free Creation? `(No)`
- [ ] Invite via Link? `(No)`
- [ ] Participant Limit Config? `(No)`

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No)
- [x] Multiple Rules Supported? (Yes/No)
- [x] Missions / Challenges? (Yes/No - via virtual currency/segments)
- [x] Badges / Achievements? (Yes/No - via virtual currency)
- [ ] Prizes: `Ranking / Raffles / Tiers`

**Real-time API:**
- [ ] API for Live Data Display? (Yes/No) `(Unclear)`
- [ ] Real-time Prediction Counts? (Yes/No) `(Unclear)`

- **Observations:**
  > `Weak on "Leagues" (Public/Private). Strong on gamification (quizzes, scratch cards, virtual currency). Private leagues are a major missing feature for the "social" aspect, though they mention "temporary views" or custom dev "quick wins".`
- **Block Rating (1-5):** `[ ]`

---

## 4. Customization, UX & Front-end
*Focus on white-label depth and user experience.*

- [x] **Full CSS/Theme Customization:** (Yes/No): `Yes (Design guide available)`
- [ ] **Custom Domain (CNAME):** (Yes/No): `[Likely Yes, "Fully white-label"]`
- [ ] **Mobile Responsive Score (1-10):** `[High]`
- **Observations:**
  > `Fully white-label front-end. Self-service editor relative to looking and feel.`
- **Block Rating (1-5):** `[ ]`

---

## 5. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [ ] **Can close Dedicated Roadmap for Cup?** (Yes/No): `No (SaaS platform)`
- [x] **Open to Partner-Specific Features?** (Yes/No): `limited (Open to "quick wins" or discussing existing roadmap, but no custom dev from scratch)`
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Low/Med] (SaaS shared environment usually, but dedicated infra for enterprise)`
- **Timelines (Avg Days):**
    - Setup Technical: `Immediate (Self-service)`
    - Customization: `[Depends on client]`
    - Go-Live: `[Fast]`
- **Update Frequency (Weeks):** `[Not Specified]`
- **Observations:**
  > `They do NOT do custom development. They are a product company. They can fast-track roadmap items if aligned, but wont build bespoke features easily.`
- **Block Rating (1-5):** `[ ]`

---

## 6. Integration Ecosystem
*Focus on connecting with existing client tech.*

- [x] **Documented APIs:**
    - [x] Login/SSO
    - [x] Partners
- **Partner Integration:**
    - [x] Partner Benefits? (Yes/No)
    - [x] Subscription Status? (Yes/No)
    - [x] External Rewards? (Yes/No)
- **Experience:**
    - [x] Co-branding Support? (Yes/No)
    - [x] Exclusive Partner Areas? (Yes/No)
    - [x] Track Record with Media/Sponsors? (Yes/No)
- [ ] **Analytics (GA4/GTM) Integration:** (Yes/No): `Yes (Integrations with marketing tools mentioned)`
- **Observations:**
  > `Strong integration capabilities via API/Webhooks. Can handle complex multi-partner ecosystems (sponsors, media) with exclusive areas.`
- **Block Rating (1-5):** `[ ]`

---

## 7. Channels & Notifications
*Focus on user re-engagement.*

- [ ] **Official WhatsApp API Integration:** (Yes/No): `No`
- [x] **Customizable Transactional Emails:** (Yes/No): `Yes (Native platform)`
- [ ] **Web Push Notifications:** (Yes/No): `[Not Specified]`
- **Observations:**
  > `No WhatsApp integration. Relies on email.`
- **Block Rating (1-5):** `[ ]`

---

## 8. Social Sharing & Virality
*Focus on organic growth.*

- [ ] **Dynamic Ranking Image Generation:** (Yes/No): `[Not Specified]`
- [x] **Referral System (Invite Links):** (Yes/No): `Yes ("Virality system 100% configurable")`
- [ ] **Deep Linking Support:** (Yes/No): `[Not Specified]`
- **Observations:**
  > `Virality system mentioned but details sparse in documents.`
- **Block Rating (1-5):** `[ ]`

---

## 9. Commercial & Contractual
*Focus on cost structure and lock-in.*

- [ ] **Setup Fee Range:** `[Not Specified] (Mention of $399 for base, but Enterprise separate)`
- [ ] **Pricing Model (Flat/User/RevShare):** `License/Subscription (Mention of "each license")`
- [ ] **Contract Min Duration (Months):** `[Not Specified]`
- **Observations:**
  > `pay-per-use/license model. Email overages cost extra.`
- **Block Rating (1-5):** `[ ]`

---

## 10. Team, Experience & References
*Focus on supplier maturity.*

- [ ] **Years in Market:** `[Not Specified]`
- [ ] **Previous World Cup/Massive Event Cases:** `[Not Specified] (Reference to Real Madrid, but not WC specifically)`
- [ ] **Reference Contacts Provided?** (Yes/No): `[Not Specified]`
- **Observations:**
  > `Mature SaaS product, but specific World Cup references not detailed in text.`
- **Block Rating (1-5):** `[ ]`

---

# Executive Summary & Recommendation

## Executive Summary
Easypromos is a mature, robust **SaaS platform** that excels in **gamification** (Quizzes, Scratch & Win, sophisticated scoring) and reliability (>1M users/campaign). It runs on Google Cloud with auto-scaling, making it technically safe for high volumes given their Enterprise setup.

However, it is **NOT a custom development shop**. They are a product company. This means significant limitations in flexibility for bespoke features. Two critical gaps identified for a Brazilian World Cup context are **Private Leagues** (they do not support them, only "temporary views") and **WhatsApp Integration** (non-existent natively).

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| **Social / Virality** | **HIGH** | **No Private Leagues.** This is a major engagement blocker for World Cup predictions where "beating friends" is a core loop. |
| **Channels** | **HIGH** | **No native WhatsApp.** Critical channel for re-engagement in Brazil. |
| **Customization** | **MEDIUM** | **No Custom Dev.** If the client needs a specific feature not in the "Quick Wins" scope, it won't happen. |
| **Product** | **MEDIUM** | **Live Predictions.** Conflicting info, but likely not supported or limited. |

## Final Recommendation
**⚠️ GO WITH RISKS (or NO-GO if Private Leagues are mandatory)**

Easypromos is a safe technical choice for a *standard* promotional campaign. If the project requires deep social mechanics (users creating their own leagues, inviting friends via specific links, group chats) which are viral drivers, **Easypromos is likely a mismatch**.

**Next Steps / Mitigations:**
1.  **Clarify "Private Leagues" workaround:** Can the "temporary view" be saved? (Miquel mentioned "we could add the option to save that ranking"). Is this guaranteed?
2.  **WhatsApp:** Confirm if we can use an external provider (e.g., Twilio/Zenvia) triggered by Easypromos Webhooks (which they support).
