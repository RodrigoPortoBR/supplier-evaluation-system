# Supplier Evaluation Template

**Supplier Name:** `Genius Sports`
**Website:** `https://www.geniussports.com`
**Evaluator:** `Rodrigo`
**Date:** `2026-02-19`

**Source Materials:**
- Meeting Notes Summary (Gemini) – Feb 12, 2026 (4 pages)
- Full Meeting Transcript – Feb 12, 2026 (21 pages)
- Participants: Rodrigo Porto, Christian Abbonizio (Genius Sports)

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic and proven load capacity.*

**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `Millions (FIFA PlayZone – millions of users playing their FIFA games)` `[Promise]`
- [x] **Strategy for 10M Concurrent Users (5 mins before game):**
  > `Genius confirmed they can accommodate stress tests for high concurrent user peaks, specifically mentioning 10 million concurrent users before a game starts (00:19:46). Exact infrastructure strategy not detailed in this call.` `[Promise]`
- [ ] **Maximum Simultaneous Users Tested:** `[Not Informed]`

**Infrastructure & Platforms:**
- [ ] **Auto-scaling Infrastructure?** (Yes/No): `[Not Informed] – Infrastructure details not discussed, but implied by FIFA-scale operations`
- [ ] **Uptime SLA (%):** `Standard SLAs for uptime confirmed (00:22:24), exact % not specified`
- [x] **Platforms Supported:**
    - [x] Web Desktop `(Native web development confirmed)`
    - [x] Web Mobile `(Mobile web view – recommended approach, used with FIFA and most partners)`
    - [x] App iOS `(React Native app development available; however, Genius generally advises mobile web view in app instead – 00:08:37)`
    - [x] App Android `(Same as iOS – React Native available, web view recommended)`

- **Observations:**
  > `Strong signal: Genius runs FIFA PlayZone at massive scale with millions of users. They explicitly confirmed ability to handle 10M concurrent users. However, specific load test reports or infrastructure architecture details (auto-scaling, cloud provider, etc.) were not discussed in this meeting. The claims are credible given FIFA reference, but concrete evidence (load test results, architecture docs) should be requested. They recommend mobile web view over native React Native builds for lower friction and easier execution.`
- **Block Rating (1-5):** `4 [Promise – credible due to FIFA, but unverified with hard data]`

---

## 2. Local Support & Operational Coverage
*Focus on the vendor's ability to provide reliable, real-time operational support during a high-stakes global event.*

**Local Presence & Timezone Alignment:**
- [x] **Local Support in Brazil?** (Yes/No): `Yes – Portuguese-speaking support is available (00:21:05)`
- [x] **Portuguese-Speaking Support Team?** (Yes/No): `Yes (00:21:05)`
- [ ] **Timezone Coverage Strategy for Brazil:**
  > `[Not Informed] – Not explicitly discussed, but Portuguese-speaking support availability implies coverage`
- [ ] **Dedicated Local Account Managers?** (Yes/No): `[Not Informed]`

**Support Availability:**
- [x] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `Yes – Genius provides 24/7 support (00:22:24)`
- [ ] **SLA Response Times for Critical Incidents:** `Standard SLAs for uptime confirmed, specific response times not detailed`
- [ ] **Dedicated War-Room Structure During Major Events?** (Yes/No): `[Not Informed]`

**Operational Escalation Flow:**
- [ ] **L1 Support (User Issues) – Handled by:** `Genius can handle support entirely or create a bridge to the partner's support team (00:21:05)`
- [ ] **L2 Technical Issues – Handled by:** `Full escalation pathways for bug triage confirmed (00:22:24)`
- [ ] **L3 Infrastructure Failures – Handled by:** `[Not Informed – implied Genius handles]`

- **Observations:**
  > `Strong: Genius offers flexible support models – they can handle it entirely or bridge to the client's team. 24/7 support with Portuguese speakers is a significant advantage over Fan Arena (who has no local support). Full escalation pathways exist. Specific SLAs and war-room structure should be clarified in the proposal.`
- **Block Rating (1-5):** `4 [Strong indicators, but specific SLA details needed]`

---

## 3. User Support & Incident Management
*Focus on operational ownership of user issues and incident resolution.*

**Support Ownership:**
- [x] **Who Handles User Complaints?** `Genius can handle support entirely or create a bridge to the partner's team (00:21:05)`
- [x] **Who Handles Technical Bug Reports?** `Full escalation pathways for bug triage (00:22:24)`

**Escalation Process:**
- [x] **Defined Workflow for Critical Bugs?** (Yes/No): `Yes – Full escalation pathways for bug triage confirmed (00:22:24)`
- [ ] **Defined Workflow for Mass User Incidents?** (Yes/No): `[Not Informed – implied by FIFA-scale operations]`

- **Observations:**
  > `Genius confirmed structured escalation paths and 24/7 support. The support model is flexible (fully managed or hybrid). However, specific incident management procedures for mass user events were not detailed. Their experience with FIFA suggests robust incident management processes exist.`
- **Block Rating (1-5):** `4 [Promise – credible due to FIFA ops experience]`

---

## 4. Security, LGPD, Governance & Compliance
*Focus on legal compliance, data safety, and youth participation regulations.*

**Data Protection & Compliance:**
- [ ] **LGPD/GDPR Compliant?** (Yes/No): `[Not Informed]`
- [ ] **Data Residency Country:** `[Not Informed]`
- [ ] **Certifications (ISO, SOC, etc.):** `[Not Informed]`

**Age Verification & Youth Safety (13+ Users):**
- [ ] **Age Verification Flow:**
  > `[Not Informed]`
- [ ] **Consent Mechanisms for Minors:**
  > `[Not Informed]`
- [ ] **Special Data Protection Policies for Under-18 Users?** (Yes/No): `[Not Informed]`
- [ ] **Parental Consent Options Available?** (Yes/No): `[Not Informed]`

- **Observations:**
  > `⚠️ Major gap: Security, LGPD compliance, and age verification were NOT discussed in this meeting. Given the Brazilian market (LGPD) and likely youth audience, this is CRITICAL to address in follow-up. Genius works with FIFA (global compliance requirements), which is a positive signal, but explicit confirmation is needed.`
- **Block Rating (1-5):** `[Not Assessed – Insufficient Data]`

---

## 5. Data Ownership, Access & Portability
*Focus on guaranteeing full strategic control over user data and long-term usability.*

**Data Ownership:**
- [x] **All User Data Fully Owned by Client?** (Yes/No): `No – Co-controller status. Both the client and Genius share privileges and unrestricted access to user data (00:23:39)`
- [ ] **Any Restrictions on Data Usage?** (Yes/No): `No restrictions – both parties have unrestricted access`
  > `Co-controller model: data lives in Genius's databases, both parties co-own and have full access`

**Data Access:**
- [x] **Access to Full User Database?** (Yes/No): `Yes – Full unobstructed access (00:23:39)`
- [ ] **Access to Behavioral Event Data?** (Yes/No): `Yes – Genius handles all data collection and analytics and shares back with partner (00:07:18)`
- [ ] **Access to Prediction History?** (Yes/No): `[Not Informed – implied by full access]`

**Data Extraction Methods:**
- [ ] **Direct Platform Exports?** (Yes/No): `[Not Informed]`
- [ ] **APIs for Real-Time Extraction?** (Yes/No): `[Not Informed]`
- [x] **Scheduled Automated Data Dumps?** (Yes/No): `Yes – File transfer protocols to share data into client's databases, CRM systems, email marketing systems (00:24:55)`

**Exit Scenario (Critical):**
- [x] **If Partnership Ends – What Happens to User Accounts?**
  > `Data can be safely stored in the client's database at contract end (00:24:55)`
- [x] **If Partnership Ends – What Happens to Historical Data?**
  > `Full data transfer confirmed – "in whatever way they prefer it to be transferred over" (00:24:55)`
- [ ] **If Partnership Ends – What Happens to Behavioral Insights?**
  > `[Not Informed – implied covered by full data transfer]`
- [x] **Full Data Export Guaranteed on Exit?** (Yes/No): `Yes (00:24:55)`

- **Observations:**
  > `Data model is Co-Controller (not sole ownership). This is a ⚠️ WARNING: the client does NOT have exclusive ownership. However, there are no restrictions on client access, and full data export at contract end is confirmed. Genius collects all analytics and shares them back. The co-controller model is standard for managed service providers but should be clearly defined in the contract to protect client interests.`
- **Block Rating (1-5):** `3 [Co-controller not sole ownership – contractual clarity needed]`

---

## 6. Core Product Features & Functional Readiness
*Focus on prediction mechanics, feature coverage, and how much of the desired product vision already exists.*

**Feature Coverage Assessment:**
- [x] **Which Core Features Are Ready Out-of-the-Box?**
  > `Prediction games, bracket challenges, trivia/quiz (always-on), leaderboards, sponsor activations, private leagues – all built before for FIFA PlayZone (00:12:03, 00:42:49)`
- [x] **Which Core Features Are Customizable?**
  > `Full custom builds – "we take different code and pieces of inspiration from existing products and use them to create this new one" (00:42:49). Private leagues, daily missions/trivia, lucky numbers/draw, premium vs. free leaderboards all confirmed feasible`
- [ ] **Which Core Features Are Not Available?**
  > `Prize fulfillment – handled by client, not Genius (00:06:06)`

**Prediction Types:**
- [x] Match Result (1x2) `(Prediction game confirmed)`
- [x] Exact Score `(Prototype showed exact score input – 00:32:50)`
- [x] Special Predictions `(Layered experiences – trivia, quiz, daily missions – 00:13:21)`
- [ ] Live Predictions `[Not Informed]`
- [x] **Multiple Prediction Types Supported?** (Yes/No): `Yes`
- [ ] **Configurable Scoring Logic?** (Yes/No): `[Not Informed – implied by custom builds]`

**Rankings:**
- [x] Global `(Implied by leaderboards)`
- [x] Public Leagues `(Free-to-play basic leaderboard – 00:00:00)`
- [x] Private Leagues `(Standard part of product builds – 00:02:16)`
- [ ] By Period (Day/Round/Tournament) `[Not Informed]`

**Scoring & Engagement:**
- [ ] Configurable Scoring System? (Yes/No) `[Not Informed – implied]`
- [ ] Multiple Rules Supported? (Yes/No) `[Not Informed – implied by custom builds]`
- [x] Missions / Challenges? (Yes/No) `Yes – daily quiz/trivia missions confirmed (00:13:21, 00:30:14)`
- [x] Badges / Achievements? (Yes/No) `Yes – prototype included badges (00:39:52)`
- [x] Prizes: `Ranking (premium leaderboard) / Lucky Draw (weekly – 00:39:52) / Tiers (free vs premium)`

**Real-time API:**
- [ ] API for Live Data Display? (Yes/No) `[Not Informed]`

- **Observations:**
  > `Extremely strong: Christian confirmed "almost all features in the prototype have been built before" (00:42:49). Genius has proven delivery of prediction games, bracket challenges, trivia, leaderboards, and sponsor activations through FIFA PlayZone. Daily missions/quiz with lucky numbers accumulation and weekly draws are all feasible. The product vision alignment is excellent. The only gap is prize fulfillment (handled by client). Custom builds mean high flexibility but longer timelines.`
- **Block Rating (1-5):** `5 [Proven feature set via FIFA, near-complete alignment with prototype]`

---

## 7. League Management & Premium Infrastructure
*Focus on private and premium league scalability, creation, and administration.*

**Private Leagues:**
- [x] **Free Creation?** (Yes/No): `Yes – standard feature (00:02:16)`
- [ ] **Invite via Link?** (Yes/No): `[Not Informed – implied by private league feature]`
- [ ] **Participant Limit Config?** (Yes/No): `Yes – common user: up to 5 private leagues, premium: up to 100 (00:01:01)`
- [ ] **How Scalable Is Private League Creation?**
  > `Standard part of their product builds, used in FIFA PlayZone`
- [ ] **Maximum Number of Private Leagues Supported:** `[Not Informed]`

**Premium League Logic:**
- [x] **League Access Restricted by Subscription Status?** (Yes/No): `Yes – users with existing paid subscriptions from sponsors can log in as premium users via SSO (00:09:50, 00:27:33)`
- [x] **League Access Restricted by External Partner Eligibility?** (Yes/No): `Yes – sponsor-based gating via SSO (00:09:50)`
- [x] **Support for Public Leagues?** (Yes/No): `Yes – free-to-play basic leaderboard (00:00:00)`
- [x] **Support for Private Leagues?** (Yes/No): `Yes – standard part of builds (00:02:16)`
- [x] **Support for Premium Leagues?** (Yes/No): `Yes – premium leaderboard with better prizes (00:00:00)`

**Administration Controls:**
- [ ] **League Moderation Tools?** (Yes/No): `[Not Informed]`
- [ ] **Anti-Fraud Mechanisms?** (Yes/No): `[Not Informed]`

- **Observations:**
  > `Strong league infrastructure: free, premium, and private leagues are all standard. Premium access gated by sponsor subscription via SSO is exactly the model needed. The concept supports multiple sponsored leaderboards based on number of sponsors. Moderation and anti-fraud details should be requested.`
- **Block Rating (1-5):** `5 [Excellent alignment with league model requirements]`

---

## 8. Game Operation & Scoring Process
*Focus on reliability and transparency of scoring updates.*

**Score Update Timing:**
- [ ] **Real-Time Updates?** (Yes/No): `[Not Informed]`
- [ ] **End-of-Match Updates?** (Yes/No): `[Not Informed]`
- [ ] **Daily Batch Updates?** (Yes/No): `[Not Informed]`

**Data Source Reliability:**
- [x] **Official Match Data Providers Used:** `Genius Sports IS a sports data provider – they own their data pipeline`

- **Observations:**
  > `Unique advantage: Genius Sports is itself a leading sports data provider. Unlike other suppliers who depend on third-party data feeds, Genius owns the data pipeline end-to-end. This should eliminate data latency and reliability concerns. Specific scoring update timing was not discussed but is likely real-time given their data infrastructure.`
- **Block Rating (1-5):** `5 [Genius IS the data provider – unmatched advantage]`

---

## 9. Customization, UX & Front-End Design
*Focus on white-label depth, user experience, and design responsibility.*

**Customization Depth:**
- [x] **Full CSS/Theme Customization:** (Yes/No): `Yes – fully custom builds, not white-label templates (00:03:14)`
- [x] **Full UI Customization or Limited Branding?**
  > `Full custom UI – "Genius does not use white-label solutions, opting for custom builds to provide full flexibility over features and creative control" (00:03:14)`
- [x] **Custom Domain (CNAME):** (Yes/No): `Yes – implied by custom builds (FIFA PlayZone sits as micro-site within FIFA.com)`
- [ ] **Mobile Responsive Score (1-10):** `[Not Assessed – mobile web view is recommended approach]`

**Design Ownership:**
- [x] **Vendor Provides UI/UX Designers?** (Yes/No): `Yes – end-to-end managed service includes design (00:06:06)`
- [x] **Vendor Provides Front-End Development Support?** (Yes/No): `Yes – full development capability (React Native, native web – 00:08:37)`
- [ ] **Client Must Supply Design Resources?** (Yes/No): `No – Genius handles "the entire end-to-end experience of building it" including design; client provides branding guides`

- **Observations:**
  > `Premium offering: Genius provides full end-to-end design and development. Client only needs to provide branding guidelines (or even just a YouTube channel or reference material). Christian offered to brand mockups to a potential sponsor for the client presentation. This is a significant advantage – no need to hire external designers or front-end developers.`
- **Block Rating (1-5):** `5 [Full creative and development ownership by Genius]`

---

## 10. Integration Ecosystem & Partner Connectivity
*Focus on connecting with existing client tech, third-party data sources, and membership systems.*

**Documented APIs:**
- [x] Login/SSO `(Single sign-on with multiple third-party providers confirmed – 00:09:50, 00:10:59)`
- [ ] Partners `[Not Informed – specific API docs not discussed]`

**Partner Integration:**
- [x] Partner Benefits? (Yes/No) `Yes – sponsor activations layered into games (00:12:03)`
- [x] Subscription Status? (Yes/No) `Yes – premium access via existing sponsor subscription (00:09:50)`
- [ ] External Rewards? (Yes/No) `[Not Informed]`

**External Database Integration:**
- [x] **Can Connect to Loyalty Programs (e.g., iFood Club)?** (Yes/No): `Yes – integrates with CRM systems, email marketing systems, various databases (00:07:18, 00:24:55)`
- [x] **Can Connect to Subscription Databases?** (Yes/No): `Yes – SSO with sponsor subscription verification (00:09:50)`

**Access Authorization:**
- [x] **Entry to Premium Leagues Gated by Partner Status?** (Yes/No): `Yes (00:09:50)`
- [x] **Entry to Premium Leagues Gated by Subscription Verification?** (Yes/No): `Yes – user with active subscription logs in directly as premium (00:27:33)`
- [ ] **Entry to Premium Leagues Gated by External APIs?** (Yes/No): `[Implied Yes via SSO]`

**Experience:**
- [x] Co-branding Support? (Yes/No) `Yes – offered to brand proposal to potential sponsor (00:45:09)`
- [x] Exclusive Partner Areas? (Yes/No) `Yes – sponsor activations and premium leagues (00:12:03)`
- [x] Track Record with Media/Sponsors? (Yes/No) `Yes – FIFA, Major League Baseball, major sports organizations worldwide (00:12:03)`

- **Observations:**
  > `Exceptional integration capabilities. SSO with multiple third-party providers is proven (FIFA). Sponsor-based premium gating works exactly as needed. CRM/notification/analytics integrations included. Multi-sponsor SSO requires data consistency (email, name, etc.) across providers. The FIFA and MLB references demonstrate real track record with major media/sports organizations.`
- **Block Rating (1-5):** `5 [Proven integration ecosystem with FIFA/MLB]`

---

## 11. Channels, Notifications & User Communication
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [ ] **Web Push Notifications:** (Yes/No): `[Not Informed]`
- [ ] **Email Automation:** (Yes/No): `[Not Informed – CRM integration mentioned, implies capability]`

**Communication Ownership:**
- [ ] **Who Manages Messaging Templates?** `[Not Informed]`
- [ ] **Who Manages Campaign Scheduling?** `[Not Informed]`

- **Observations:**
  > `Notification specifics were not discussed. However, Genius mentioned integration with CRM and notification systems (00:07:18), suggesting capability exists. Specific channel support (push, email, WhatsApp) should be clarified in follow-up.`
- **Block Rating (1-5):** `[Not Assessed – Insufficient Data]`

---

## 12. Social Sharing & Virality
*Focus on organic growth and viral content generation.*

- [x] **Native Sharing Features?** (Yes/No): `Yes – prototype included social sharing of lucky numbers to double rewards (00:31:30)`
- [ ] **Social Platforms Supported for Sharing User Answers / Status:** `[Not Informed – prototype showed social media sharing]`

- **Observations:**
  > `Prototype included a viral mechanic: sharing quiz results on social media doubles lucky numbers earned. This incentivized sharing is a strong engagement driver. Specific platform support details not discussed.`
- **Block Rating (1-5):** `4 [Sharing mechanic exists with incentive structure]`

---

## 13. Geo-Restriction Capabilities
*Focus on control over geographic participation.*

- [ ] **Registration Restricted to Brazilian Users Only?** (Yes/No): `[Not Informed]`
- [ ] **Restriction by Specific IP Ranges?** (Yes/No): `[Not Informed]`

- **Observations:**
  > `Not discussed. Should be clarified given the Brazil-specific nature of the project.`
- **Block Rating (1-5):** `[Not Assessed – Insufficient Data]`

---

## 14. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [x] **Can Close Dedicated Roadmap for Cup?** (Yes/No): `Yes – custom build dedicated to this project`
- [x] **Open to Partner-Specific Features?** (Yes/No): `Yes – custom development is their model. "Almost all features in the prototype have been built before" (00:42:49). Also open to live triggers and influencer-driven missions (00:38:00)`
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Low] – custom builds, not shared platform` `[Promise]`
- **Timelines (Avg Days):**
    - Setup Technical: `[Not Informed]`
    - Customization: `Custom build – leveraging existing technology`
    - Go-Live: `Mid-May 2026 target. Christian said "if we get sign-off within the next couple weeks, we can probably make it work" (00:42:49). Proposal with mockups promised before Feb 20 meeting.`

- **Observations:**
  > `⚠️ Timeline is the #1 concern expressed by Genius. Mid-May go-live requires signing off within ~2 weeks of the meeting (by end of Feb 2026). Christian explicitly flagged timing as "the biggest concern" – not capability. Custom build nature means dedicated resources with no conflict risk from other clients. The feature scope is highly flexible and can be adjusted to fit budget/timeline.`
- **Block Rating (1-5):** `4 [Capable, but May deadline is tight and timing-critical]`

---

## 15. Commercial, Contractual & Financial Risk
*Focus on cost structure, lock-in risks, and financial predictability.*

**Cost Structure:**
- [ ] **Setup Fee Range:** `[Not Informed – explicitly described as "expensive" and "not the cheap provider"] (00:14:29)`
- [ ] **Pricing Model:** `[Custom/Project-based] – built for large enterprise clients with significant budgets`

**Cost Variability & Budget Risk:**
- [ ] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `[Not Informed]`
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `[Not Informed]`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `Yes – scope can be adjusted by removing features if budget is too high (00:15:26)`

**Contract Terms:**
- [ ] **Minimum Contract Duration (Months):** `[Not Informed – project-based]`
- [ ] **Early Termination Penalties?** (Yes/No): `[Not Informed]`
  > `[Not Discussed]`

**Platform Dependency & Exit Risks:**
- [ ] **Migration Complexity:**
  > `Custom build – full data export confirmed, but platform code is Genius proprietary`
- [x] **Data Portability Guarantees?** (Yes/No): `Yes – full data export confirmed at contract end (00:24:55)`

- **Observations:**
  > `⚠️ HIGH COST: Genius explicitly positioned themselves as the premium, expensive option. "We are not the cheap provider in the space" (00:14:29). Rodrigo acknowledged this would "likely be the most expensive" option. Specific pricing was not shared in the call – awaiting proposal. The scope-flexibility is a mitigating factor (features can be removed to fit budget). Full proposal with pricing expected before Feb 20.`
- **Block Rating (1-5):** `3 [High cost expected, specific numbers pending proposal]`

---

## 16. Team, Experience & References
*Focus on supplier maturity.*

- [x] **Years in Market:** `[Established – Genius Sports is a publicly traded company (NYSE: GENI)]`
- [x] **Previous World Cup/Massive Event Cases:** `Yes – Built FIFA PlayZone (includes prediction games, bracket challenges, trivia). Millions of users (00:04:57, 00:12:03, 00:19:46)`
- [ ] **Reference Contacts Provided?** (Yes/No): `Case studies deck promised (to be sent) (00:47:23)`

- **Observations:**
  > `Genius Sports is the strongest reference in this evaluation: publicly traded company, official FIFA partner, built FIFA PlayZone used by millions, works with Major League Baseball and major sports organizations worldwide. This is not a small shop – it's an enterprise-grade organization with proven massive-scale event experience. Case studies deck to be provided.`
- **Block Rating (1-5):** `5 [FIFA partner, publicly traded, proven at World Cup scale]`

---

# Executive Summary & Recommendation

## Executive Summary
Genius Sports is a **premium, enterprise-grade gamiﬁcation partner** with the strongest pedigree in this evaluation – they are the official technology partner behind **FIFA's PlayZone**, handling millions of users at World Cup scale. Unlike Fan Arena or Easypromos, Genius offers **fully custom builds** (not white-label), providing complete creative and technical control. They deliver an **end-to-end managed service** covering design, development, operations, and 24/7 Portuguese-speaking support.

The product vision alignment is **near-perfect**: prediction games, private/premium/public leagues, daily missions, trivia, lucky draws, sponsor-gated premium access via SSO, and social sharing incentives are all confirmed as previously built features. Genius also uniquely owns their sports data pipeline, eliminating third-party data dependency.

The two primary concerns are **cost** (explicitly premium pricing, likely the most expensive option) and **timeline** (mid-May go-live requires fast sign-off and execution).

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| **Commercial / Cost** | **HIGH** | **Premium Pricing.** Genius explicitly stated they are "not the cheap provider." Custom enterprise builds require "significant budgets." Concrete pricing awaiting proposal. |
| **Timeline** | **HIGH** | **Mid-May Deadline is Tight.** Christian flagged timing as the #1 concern. Requires contract sign-off within ~2 weeks of meeting to make the deadline work. |
| **Data Ownership** | **MEDIUM** | **Co-Controller Model.** Data is co-owned by Genius and client. While client has unrestricted access and full export rights, this is NOT sole ownership. Contract must clearly define co-controller boundaries. |
| **Security / LGPD** | **⚠️ UNKNOWN** | **Not Discussed.** LGPD compliance, data residency, certifications, age verification, and penetration testing were NOT addressed in this call. MUST be clarified. |
| **Notifications** | **LOW** | **Not Detailed.** Push, email, and campaign channels not explicitly discussed (CRM integration exists). |

## Key Strengths
| Strength Area | Rating | Description |
| :--- | :--- | :--- |
| **Experience & References** | ⭐⭐⭐⭐⭐ | FIFA PlayZone, MLB, publicly traded (NYSE: GENI). Unmatched pedigree. |
| **Product Feature Alignment** | ⭐⭐⭐⭐⭐ | "Almost all features in the prototype have been built before." Near-complete match. |
| **Data Pipeline** | ⭐⭐⭐⭐⭐ | Genius IS the sports data provider. No third-party dependency. |
| **Design & Development** | ⭐⭐⭐⭐⭐ | Full end-to-end managed service including design, dev, and operations. |
| **Integration / SSO** | ⭐⭐⭐⭐⭐ | Multi-sponsor SSO proven with FIFA. Premium gating by subscription status. |
| **Support** | ⭐⭐⭐⭐ | 24/7, Portuguese speaking, flexible model (fully managed or hybrid). |

## Final Recommendation
**✅ GO – Best-in-Class Option (Contingent on Budget & Timeline)**

Genius Sports is the **clear technical and operational leader** in this evaluation. They have **proven World Cup-scale delivery** (FIFA PlayZone), the deepest feature set, and a fully managed service model that minimizes client-side resource requirements.

**The decision hinges on two factors:**
1. **Budget:** Can the project accommodate premium pricing? If the proposal is within range, Genius is the obvious choice.
2. **Speed:** Contract must be signed rapidly (within ~2 weeks) to hit the mid-May deadline.

**Immediate Next Steps:**
1. **Review Proposal** (expected before Feb 20, 2026) – evaluate pricing vs. budget.
2. **Clarify Security & LGPD** – request LGPD/GDPR compliance confirmation, data residency details, certifications, age verification capabilities.
3. **Clarify Data Ownership Contract Terms** – ensure co-controller model has clear boundaries protecting client interests.
4. **Request Load Test Documentation** – obtain concrete evidence of FIFA PlayZone scale (concurrent users, architecture).
5. **Define Timeline Milestones** – get detailed delivery schedule with checkpoints from design → build → UAT → go-live.
