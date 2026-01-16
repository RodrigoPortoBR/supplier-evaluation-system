# Supplier Evaluation Template

**Supplier Name:** GPT
**Website:** `[Not Provided]`
**Evaluator:** Antigravity (Agent)
**Date:** 2025-09-18

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic.*

- [ ] **Highest Participants Record (Single Game):** `~300k / 10 min` (Evidence: Campaign TV LatAm)
- [ ] **Strategy for 10M Concurrent Users (5 mins before game):**
  > **[PROMISE]** Claims architecture scales, but admitted "never tested exactly this scenario".
  > **[MITIGATION]** Uses palpite buffer and asynchronous queues.
- [ ] **Platforms Supported:**
    - [x] Web Desktop
    - [x] Web Mobile
    - [ ] App iOS (Not mentioned explicitly as native, inferred Web focus)
    - [ ] App Android (Not mentioned explicitly as native)
- [ ] **Uptime SLA (%):** `99.5%` (Standard Enterprise)
- [ ] **Support SLA 24/7?** (Yes/No): `No` (Requires extra fee for on-call)
- [ ] **Local Support in Brazil?** (Yes/No): `Yes` (Team in BR, PT, ES)
- [ ] **Auto-scaling Infrastructure?** (Yes/No): `Yes` (AWS EKS + ASG)
- [ ] **Recent Load Test Evidence Provided?** (Yes/No): `No` (Internal only, no report shared)
- **Observations:**
  > **[RISK]** Huge gap between proven scale (300k) and target (10M).
  > **[RISK]** No dedicated SRE by default.
- **Block Rating (1-5):** `2`

---

## 2. Security, LGPD & Governance
*Focus on legal compliance and data safety.*

- [ ] **LGPD/GDPR Compliant?** (Yes/No): `Yes` (Self-declared)
- [ ] **Data Residency Country:** `AWS South America or Europe`
- [ ] **Certifications (ISO, SOC, etc.):** `None` (ISO 27001 in process)
- [ ] **Penetration Test Report Available?** (Yes/No): `No` (Claims done in other projects)
- **Observations:**
  > **[MISSING]** No physical evidence of security audits.
- **Block Rating (1-5):** `3`

---

## 3. Core Product Features
*Focus on the betting/prediction mechanics.*

**Prediction Types:**
- [x] Match Result (1x2)
- [x] Exact Score
- [x] Special Predictions
- [ ] Live Predictions (Roadmap only)

**Rankings:**
- [x] Global
- [x] Public Leagues
- [x] Private Leagues
- [x] By Period (Day/Round/Tournament)

**Private Leagues:**
- [x] Free Creation?
- [x] Invite via Link?
- [x] Participant Limit Config?

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No) (Not self-service)
- [x] Multiple Rules Supported? (Yes/No)
- [x] Missions / Challenges? (Yes/No) (Simple)
- [x] Badges / Achievements? (Yes/No) (Basic)
- [ ] Prizes: `Ranking`

**Real-time API:**
- [ ] API for Live Data Display? (Yes/No): `No` (No guarantee for live broadcast)
- [ ] Real-time Prediction Counts? (Yes/No)

- **Observations:**
  > **[LIMITATION]** Configuration depends on GPT team (not self-service).
- **Block Rating (1-5):** `4`

---

## 4. Customization, UX & Front-end
*Focus on white-label depth and user experience.*

- [x] **Full CSS/Theme Customization:** (Yes/No): `Yes`
- [x] **Custom Domain (CNAME):** (Yes/No): `Yes`
- [ ] **Mobile Responsive Score (1-10):** `N/A` (No demo provided)
- **Observations:**
  > **[MISSING]** No demo link available.
- **Block Rating (1-5):** `3`

---

## 5. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [x] **Can close Dedicated Roadmap for Cup?** (Yes/No): `Yes`
- [ ] **Open to Partner-Specific Features?** (Yes/No): `Maybe` (Depends on core)
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `High` (If shared infra)
- **Timelines (Avg Days):**
    - Setup Technical: `30`
    - Customization: `20`
    - Go-Live: `60-90`
- **Update Frequency (Weeks):** `[Not Informed]`
- **Observations:**
  > **[CRITICAL]** Admitted risk of conflict if not on dedicated environment.
- **Block Rating (1-5):** `3`

---

## 6. Integration Ecosystem
*Focus on connecting with existing client tech.*

- [ ] **Documented APIs:**
    - [x] Login/SSO
    - [ ] Partners
- **Partner Integration:**
    - [ ] Partner Benefits? (Yes/No)
    - [ ] Subscription Status? (Yes/No)
    - [ ] External Rewards? (Yes/No)
- **Experience:**
    - [x] Co-branding Support? (Yes/No)
    - [ ] Exclusive Partner Areas? (Yes/No) (Custom dev needed)
    - [x] Track Record with Media/Sponsors? (Yes/No)
- [x] **Analytics (GA4/GTM) Integration:** (Yes/No): `Yes`
- **Observations:**
  > No widespread partner ecosystem pre-built.
- **Block Rating (1-5):** `3`

---

## 7. Channels & Notifications
*Focus on user re-engagement.*

- [ ] **Official WhatsApp API Integration:** (Yes/No): `No`
- [x] **Customizable Transactional Emails:** (Yes/No): `Yes`
- [x] **Web Push Notifications:** (Yes/No): `Yes`
- **Observations:**
  > **[WEAKNESS]** Lack of WhatsApp is a major engagement miss for Brazil.
- **Block Rating (1-5):** `2`

---

## 8. Social Sharing & Virality
*Focus on organic growth.*

- [ ] **Dynamic Ranking Image Generation:** (Yes/No): `No`
- [x] **Referral System (Invite Links):** (Yes/No): `Yes` (Simple)
- [ ] **Deep Linking Support:** (Yes/No): `Depends on App`
- **Observations:**
  > Viral features are very basic.
- **Block Rating (1-5):** `2`

---

## 9. Commercial & Contractual
*Focus on cost structure and lock-in.*

- [ ] **Setup Fee Range:** `[Not Informed]`
- [ ] **Pricing Model (Flat/User/RevShare):** `Setup + Monthly` (No RevShare)
- [ ] **Contract Min Duration (Months):** `12`
- **Observations:**
  > Model is safer (predictable cost) but high lock-in (12m).
- **Block Rating (1-5):** `4`

---

## 10. Team, Experience & References
*Focus on supplier maturity.*

- [ ] **Years in Market:** `8`
- [ ] **Previous World Cup/Massive Event Cases:** `0` (Only regional tournaments)
- [ ] **Reference Contacts Provided?** (Yes/No): `Yes` (2-3 enterprise clients)
- **Observations:**
  > **[RISK]** Never operated a World Cup.
- **Block Rating (1-5):** `2`
