# Supplier Evaluation Template

**Supplier Name:** `Fan Arena`
**Website:** `[Not Specified in text]`
**Evaluator:** `Rodrigo`
**Date:** `2026-01-22`

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic.*

- [ ] **Highest Participants Record (Single Game):** `~300,000 (Admitted largest database). Claims architecture scales, but no proven 1M+ case.`
- [ ] **Strategy for 10M Concurrent Users (5 mins before game):**
  > `Serverless / Cloud Functions on AWS & Digital Ocean. Claims "scale by design" where more users trigger more instances. But untested at this volume.`
- [ ] **Platforms Supported:**
    - [x] Web Desktop
    - [x] Web Mobile
    - [ ] App iOS `(Via WebView / Native Shell)`
    - [ ] App Android `(Via WebView / Native Shell)`
- [ ] **Uptime SLA (%):** `[Not Specified]`
- [ ] **Support SLA 24/7?** (Yes/No): `[Implied Yes for WC window, but need to hire/train local team]`
- [ ] **Local Support in Brazil?** (Yes/No): `No (Europe based. Suggests training 2 local people for end-user support).`
- [x] **Auto-scaling Infrastructure?** (Yes/No): `Yes (AWS Cloud Functions)`
- [ ] **Recent Load Test Evidence Provided?** (Yes/No): `No (Claims familiarity with 10k-100k scale, acknowledges 10M is different but doable).`
- **Observations:**
  > `Major Risk: They have NEVER done a project of this size. Their largest is 300k. They claim their architecture (Cloud Functions) handles it, but it's a theoretical claim vs. Easypromos' proven volume.`
- **Block Rating (1-5):** `[ ]`

---

## 2. Security, LGPD & Governance
*Focus on legal compliance and data safety.*

- [x] **LGPD/GDPR Compliant?** (Yes/No): `Yes (GDPR native, assumes coverage for LGPD)`
- [ ] **Data Residency Country:** `Europe (Likely AWS/Digital Ocean regions)`
- [ ] **Certifications (ISO, SOC, etc.):** `[Not Specified]`
- [ ] **Penetration Test Report Available?** (Yes/No): `[Not Specified]`
- **Observations:**
  > `Standard EU GDPR compliance. SSO/Auth via OIDC supported to minimize PII storage.`
- **Block Rating (1-5):** `[ ]`

---

## 3. Core Product Features
*Focus on the betting/prediction mechanics.*

**Prediction Types:**
- [x] Match Result (1x2)
- [x] Exact Score
- [ ] Special Predictions `(Implied - "custom rules available")`
- [ ] Live Predictions `[Not Specified]`

**Rankings:**
- [x] Global
- [x] Public Leagues
- [x] Private Leagues `(Yes - Core feature of their Fantasy engine, transferable to Prediction)`
- [x] By Period (Day/Round/Tournament)

**Private Leagues:**
- [x] Free Creation? `(Yes)`
- [x] Invite via Link? `(Yes)`
- [x] Participant Limit Config? `(Yes)`

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No)
- [x] Multiple Rules Supported? (Yes/No)
- [x] Missions / Challenges? (Yes/No - "Boosters" mentioned, flexible dev)`
- [x] Badges / Achievements? (Yes/No - "Custom badges" mentioned)`
- [x] Prizes: `Ranking / Raffles / Tiers`

**Real-time API:**
- [x] API for Live Data Display? (Yes/No) `(Real-time calculation mentioned)`
- [ ] Real-time Prediction Counts? (Yes/No)

- **Observations:**
  > `Strong on Gamification Mechanics. Unlike Easypromos, they support Private Leagues, VIP Leagues, and complex scoring natively. Prototype-first approach means high flexibility.`
- **Block Rating (1-5):** `[ ]`

---

## 4. Customization, UX & Front-end
*Focus on white-label depth and user experience.*

- [x] **Full CSS/Theme Customization:** (Yes/No): `Yes (Turnkey solution - built from scratch/components)`
- [x] **Custom Domain (CNAME):** (Yes/No): `Yes`
- [x] **Mobile Responsive Score (1-10):** `[High] (Mobile-first web view)`
- **Observations:**
  > `They build the UI for the client (Turnkey). "We deliver turnkey from A to Z". High customization potential (Frankenstein risk mentioned but manageable).`
- **Block Rating (1-5):** `[ ]`

---

## 5. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [x] **Can close Dedicated Roadmap for Cup?** (Yes/No): `Yes (Project-based approach)`
- [x] **Open to Partner-Specific Features?** (Yes/No): `Yes (Very open - "We build 20 features if you want")`
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Medium] (Smaller team, but dedicated project focus)`
- **Timelines (Avg Days):**
    - Setup Technical: `[N/A]`
    - Customization: `2 Weeks Design + 4 Weeks Dev (Approx 2 months total)`
    - Go-Live: `May (for June event)`
- **Update Frequency (Weeks):** `[Project based]`
- **Observations:**
  > `Agile custom dev shop model. They define scope -> prototype -> build. Timeline is tight (2 months) but feasible.`
- **Block Rating (1-5):** `[ ]`

---

## 6. Integration Ecosystem
*Focus on connecting with existing client tech.*

- [x] **Documented APIs:**
    - [x] Login/SSO `(OIDC/OAuth supported)`
    - [ ] Partners
- **Partner Integration:**
    - [x] Partner Benefits? (Yes/No)
    - [x] Subscription Status? (Yes/No)
    - [x] External Rewards? (Yes/No)
- **Experience:**
    - [x] Co-branding Support? (Yes/No)
    - [x] Exclusive Partner Areas? (Yes/No)
    - [ ] Track Record with Media/Sponsors? (Yes/No)
- [ ] **Analytics (GA4/GTM) Integration:** (Yes/No): `[Likely Yes]`
- **Observations:**
  > `SSO capable. Can integrate Loyalty data to create specific segments/leagues.`
- **Block Rating (1-5):** `[ ]`

---

## 7. Channels & Notifications
*Focus on user re-engagement.*

- [ ] **Official WhatsApp API Integration:** (Yes/No): `[Not Specified]`
- [x] **Customizable Transactional Emails:** (Yes/No): `Yes`
- [ ] **Web Push Notifications:** (Yes/No): `[Not Specified]`
- **Observations:**
  > `Focus on in-game retention logic (revealing games slowly). No specific mention of WhatsApp or Push, but custom dev nature suggests it's possible.`
- **Block Rating (1-5):** `[ ]`

---

## 8. Social Sharing & Virality
*Focus on organic growth.*

- [ ] **Dynamic Ranking Image Generation:** (Yes/No): `[Not Specified]`
- [x] **Referral System (Invite Links):** (Yes/No): `Yes (Private Leagues)`
- [ ] **Deep Linking Support:** (Yes/No): `[Not Specified]`
- **Observations:**
  > `Private Leagues are the main viral driver here.`
- **Block Rating (1-5):** `[ ]`

---

## 9. Commercial & Contractual
*Focus on cost structure and lock-in.*

- [x] **Setup Fee Range:** `~€100k ballpark for 10M users (includes setup + license)`
- [x] **Pricing Model (Flat/User/RevShare):** `License/Project Fee`
- [ ] **Contract Min Duration (Months):** `[Project based]`
- **Observations:**
  > `Significant upfront cost (~€100k) compared to simpler SaaS, but includes full turnkey delivery.`
- **Block Rating (1-5):** `[ ]`

---

## 10. Team, Experience & References
*Focus on supplier maturity.*

- [x] **Years in Market:** `~10 years`
- [ ] **Previous World Cup/Massive Event Cases:** `No (Did Euros, but smaller scale)`
- [ ] **Reference Contacts Provided?** (Yes/No): `Yes (Mentioned providing testimonials)`
- **Observations:**
  > `Experienced in Fantasy/Prediction, but NOT at this scale (Brazil/World Cup). European focus.`
- **Block Rating (1-5):** `[ ]`

---

# Executive Summary & Recommendation

## Executive Summary
Fan Arena acts as a **Turnkey/Boutique Development Partner** rather than a pure SaaS. They offer high flexibility, allowing for **tailor-made gamification**, **Private Leagues**, and specific loyalty integrations that Easypromos lacks. 

However, they represent a **Critical Operational Risk** regarding scale. They have **never** handled a project of this magnitude (10M-20M users); their largest reference is ~300k. While they claim a scalable serverless architecture, they are essentially unproven at the "Brazil World Cup" level. They also lack local support.

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| **Scale / Reliability** | **CRITICAL** | **Unproven at Scale.** Jumping from 300k to 20M users is a massive leap. "Theoretical" cloud scaling often breaks in practice under load (DB locks, race conditions). |
| **Operations** | **HIGH** | **No Local Support.** Time zone differences and lack of Portuguese speakers mean we need to build our own support layer. |
| **Delivery** | **MEDIUM** | **Custom Dev Timeline.** 2 months is tight for a full turnkey build + UAT. Any delay is fatal for a fixed event like WC. |
| **Cost** | **MEDIUM** | **~€100k Upfront.** Higher initial CAPEX than monthly SaaS. |

## Final Recommendation
**⚠️ GO WITH EXTREME CAUTION (High Reward / High Risk)**

Fan Arena offers the **superior product vision** (Private Leagues, Customer engagement) which fits the "viral" business goal much better than Easypromos. However, the **technical risk is massive**.

**Next Steps / Mitigations:**
1.  **Technical Due Diligence:** We MUST audit their architecture. Access to their AWS topology to verify "Serverless" claims.
2.  **Load Testing:** Contract MUST be contingent on passing a synthetic load test of 1M - 5M concurrents (simulating the WC spike).
3.  **SLA Penalties:** Heavy penalties for downtime.
4.  **Reference Check:** Call the "betting company" or "DPG Media" they mentioned to verify stability.
