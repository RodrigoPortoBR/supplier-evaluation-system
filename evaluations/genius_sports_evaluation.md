# Supplier Evaluation Template

**Supplier Name:** `Genius Sports`
**Website:** `https://www.geniussports.com`
**Evaluator:** `Rodrigo`
**Date:** `2026-02-19`

**Source Materials:**
- Meeting Notes Summary (Gemini) – Feb 12, 2026 (4 pages)
- Full Meeting Transcript – Feb 12, 2026 (21 pages)
- **Genius Sports – World Cup Predictor Proposal** (Formal Proposal, 3 pages, received Feb 20, 2026)
- Participants: Rodrigo Porto, Christian Abbonizio (Genius Sports)

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic and proven load capacity.*

**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `Millions (FIFA PlayZone – millions of users playing their FIFA games)` `[Promise]`
- [x] **Strategy for 10M Concurrent Users (5 mins before game):**
  > `Genius confirmed they can accommodate stress tests for high concurrent user peaks, specifically mentioning 10 million concurrent users before a game starts (00:19:46). Proposal confirms "stress-tested infrastructure and dedicated hosting environments" for peak matchday traffic. Targeting up to 15 million registrations.` `[Promise → Proposal Confirmed]`
- [ ] **Maximum Simultaneous Users Tested:** `[Not Informed – proposal references stress-tested infrastructure but no specific numbers]`

**Infrastructure & Platforms:**
- [ ] **Auto-scaling Infrastructure?** (Yes/No): `[Not Informed explicitly] – Proposal confirms "dedicated hosting environments" and "stress-tested infrastructure" handling millions of users. Implies auto-scaling but not stated verbatim.`
- [ ] **Uptime SLA (%):** `Standard SLAs for uptime confirmed (00:22:24), exact % not specified in proposal`
- [x] **Platforms Supported:**
    - [x] Web Desktop `(Proposal confirms: "responsive web" – primary platform)`
    - [x] Web Mobile `(Proposal confirms: "responsive web, with the option to embed... into existing mobile applications through web view")`
    - [x] App iOS `(Web view embed into existing app – confirmed in proposal)`
    - [x] App Android `(Web view embed into existing app – confirmed in proposal)`

- **Observations:**
  > `Strong signal reinforced by formal proposal: Genius runs FIFA PlayZone at massive scale with millions of users. Proposal targets "up to 15 million registrations" and confirms "enterprise-scale engagement ecosystem that supports millions of users." Infrastructure described as "stress-tested" with "dedicated hosting environments" for peak matchday traffic. Primary platform is responsive web with web view embed for mobile apps. Still missing: specific load test numbers, cloud provider details, auto-scaling architecture documentation.`
- **Block Rating (1-5):** `4 [Promise reinforced by proposal – credible due to FIFA + enterprise positioning, but load test evidence still pending]`

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
  > `Proposal confirms: Match score predictions (group + knockout), tournament-level predictions (winner, Golden Boot, Brazil progression), bracket challenges, daily trivia/quiz with lucky numbers, weekly prize draws, private leagues (5 free / 100 premium), public + premium leaderboards, sponsor activations, social sharing (double rewards). All built before for FIFA PlayZone.`
- [x] **Which Core Features Are Customizable?**
  > `Full custom builds. Proposal: "We will build an enterprise-scale engagement ecosystem." Premium weekly missions tied to live broadcast moments, influencer prompts, or sponsor activations. Experiential rewards for premium users.`
- [x] **Which Core Features Are Not Available?**
  > `Prize fulfillment – client responsibility. Proposal: "The client will manage prize fulfillment. We will manage all technical and operational components."`

**Prediction Types:**
- [x] Match Result (1x2) `(Proposal confirmed: "predict match scores across the group stage and knockout rounds")`
- [x] Exact Score `(Proposal confirmed: "predict match scores" – exact score input)`
- [x] Special Predictions `(Proposal confirmed: "tournament-level predictions, including overall winner, Golden Boot winner, and Brazil's progression")`
- [ ] Live Predictions `[Not Informed in proposal]`
- [x] **Multiple Prediction Types Supported?** (Yes/No): `Yes – match predictions, tournament predictions, daily trivia`
- [x] **Configurable Scoring Logic?** (Yes/No): `Yes – Proposal: "Both tiers will use identical scoring mechanics to preserve fairness" implies configurable scoring system`

**Rankings:**
- [x] Global `(Implied by leaderboards)`
- [x] Public Leagues `(Free-to-play basic leaderboard – 00:00:00)`
- [x] Private Leagues `(Standard part of product builds – 00:02:16)`
- [ ] By Period (Day/Round/Tournament) `[Not Informed]`

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No) `Yes – Proposal: "identical scoring mechanics" between tiers, premium gets "enhanced rewards"`
- [ ] Multiple Rules Supported? (Yes/No) `[Not Informed – implied by custom builds]`
- [x] Missions / Challenges? (Yes/No) `Yes – Proposal confirms: "exclusive weekly missions" for premium users, daily trivia quiz`
- [x] Badges / Achievements? (Yes/No) `Yes – prototype included badges (00:39:52)`
- [x] Prizes: `Proposal confirms: "standard prizing" (free), "enhanced rewards" (premium), weekly lucky number prize draws, experiential rewards for premium missions`

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
- [x] **Participant Limit Config?** (Yes/No): `Yes – Proposal confirms: Free users join up to 5 private leagues, Premium users create and join up to 100`
- [x] **How Scalable Is Private League Creation?**
  > `Proposal: "The private league engine will serve as a core differentiator." Positioned as national hub for friend-based competition. "Brazil's strong culture of social prediction" referenced.`
- [ ] **Maximum Number of Private Leagues Supported:** `[Not Informed – but designed for national scale with 15M registrations target]`

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
- [ ] **Web Push Notifications:** (Yes/No): `[Not Informed explicitly – proposal mentions "notification infrastructure" integration]`
- [x] **Email Automation:** (Yes/No): `Yes – Proposal confirms: "We will integrate CRM systems, analytics tracking, notification infrastructure"`

**Communication Ownership:**
- [ ] **Who Manages Messaging Templates?** `[Not Informed – implied shared via CRM integration]`
- [ ] **Who Manages Campaign Scheduling?** `[Not Informed – implied shared via CRM integration]`

- **Observations:**
  > `Proposal confirms integration with CRM systems, analytics tracking, and notification infrastructure. This means the notification tooling connects to the client's existing stack rather than being a standalone feature. Still unclear if Genius provides native push notifications or if it's fully dependent on client CRM. Daily engagement mechanic (trivia → lucky numbers) naturally drives return visits and reduces dependency on push notifications.`
- **Block Rating (1-5):** `3 [CRM/notification integration confirmed, but no native notification engine detailed]`

---

## 12. Social Sharing & Virality
*Focus on organic growth and viral content generation.*

- [x] **Native Sharing Features?** (Yes/No): `Yes – Proposal confirms: "Social sharing will increase rewards" as part of the lucky numbers mechanic`
- [ ] **Social Platforms Supported for Sharing User Answers / Status:** `[Not Informed – specific platforms not listed in proposal]`

- **Observations:**
  > `Proposal confirms viral mechanic: sharing trivia results on social media increases lucky number rewards. Proposal: "Social sharing will increase rewards." Combined with weekly prize draws, this creates a strong viral loop. Specific social platform support not listed but implied (standard social media integration).`
- **Block Rating (1-5):** `4 [Sharing mechanic confirmed with incentive structure in proposal]`

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
    - Setup Technical: `[Not Informed – part of custom build timeline]`
    - Customization: `Custom build – leveraging existing technology ("proven tournament-scale architecture")`
    - Go-Live: `Mid-May 2026. Proposal: "If we confirm scope quickly and align on design decisions, we can achieve a mid-May go-live. Early approval will allow us to deliver the complete feature set without reducing scope."`

- **Observations:**
  > `⚠️ Timeline is the #1 concern expressed by Genius. Mid-May go-live requires signing off within ~2 weeks of the meeting (by end of Feb 2026). Christian explicitly flagged timing as "the biggest concern" – not capability. Custom build nature means dedicated resources with no conflict risk from other clients. The feature scope is highly flexible and can be adjusted to fit budget/timeline.`
- **Block Rating (1-5):** `4 [Capable, but May deadline is tight and timing-critical]`

---

## 15. Commercial, Contractual & Financial Risk
*Focus on cost structure, lock-in risks, and financial predictability.*

**Cost Structure:**
- [x] **Setup Fee Range:** `$150,000 – $225,000 USD (Annual License Fee) [Proposal Confirmed]`
- [x] **Pricing Model:** `Annual License Fee – fixed range. Proposal: "World Cup Predictor – Annual License Fee – $150,000 - $225,000 USD"`

**Cost Variability & Budget Risk:**
- [ ] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `[Not Informed – annual license suggests fixed cost regardless of traffic]`
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `[Not Informed – annual license suggests inclusive]`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `Yes – scope can be adjusted by removing features if budget is too high (00:15:26). Range ($150k-$225k) likely reflects different scope levels.`

**Contract Terms:**
- [ ] **Minimum Contract Duration (Months):** `Annual license – implies 12 months minimum`
- [ ] **Early Termination Penalties?** (Yes/No): `[Not Informed]`
  > `[Not Discussed in proposal]`

**Platform Dependency & Exit Risks:**
- [ ] **Migration Complexity:**
  > `Custom build – full data export confirmed, but platform code is Genius proprietary. Proposal confirms "post-campaign retention strategies" and CRM-ready exports.`
- [x] **Data Portability Guarantees?** (Yes/No): `Yes – Proposal confirms: "co-controller data framework that ensures full client access to user data" + "CRM-ready exports" + "post-campaign retention strategies"`

- **Observations:**
  > `💰 PRICING NOW CONFIRMED: $150,000 – $225,000 USD annual license fee. This is a fixed annual license, NOT a per-user or revenue-share model. The fixed model gives budget predictability – no surprise costs from traffic spikes. The $75k range likely maps to scope flexibility (full feature set vs. reduced). Compared to other suppliers, this is the premium option but includes fully managed end-to-end service (design, development, operations, support). Cost-per-registration could be very low if 15M target is hit (~$0.01-$0.015/user).`
- **Block Rating (1-5):** `3 [Premium pricing confirmed – $150k-$225k USD annual license. Budget predictability is positive but total cost is highest among evaluated suppliers]`

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

> **Updated: 2026-02-20** – Now includes data from the formal Genius Sports proposal document.

## Executive Summary
Genius Sports is a **premium, enterprise-grade gamification partner** with the strongest pedigree in this evaluation – they are the official technology partner behind **FIFA's PlayZone**, handling millions of users at World Cup scale. Unlike Fan Arena or Easypromos, Genius offers **fully custom builds** (not white-label), providing complete creative and technical control. They deliver an **end-to-end managed service** covering design, development, operations, and 24/7 Portuguese-speaking support.

The formal proposal confirms a **$150,000 – $225,000 USD annual license fee** for the World Cup Predictor. The proposal targets **up to 15 million registrations** and positions the platform as "Brazil's leading destination for tournament prediction, private leagues, and sponsor activation." The product is described as an "enterprise-scale engagement ecosystem" – not a template product or lightweight promotional game.

The product vision alignment is **near-perfect**: match score predictions, tournament predictions (winner, Golden Boot, Brazil progression), bracket challenges, private leagues (5 free / 100 premium), daily trivia with lucky numbers, weekly prize draws, sponsor-gated premium access via SSO, premium weekly missions (tied to broadcasts/influencers/sponsors), and social sharing incentives are all confirmed.

## Automated Risk Flags
| Category | Flag Condition | Risk Level | Alert |
| :--- | :--- | :--- | :--- |
| **Security** | `lgpd_compliant` == [Not Informed] | **⚠️ CRITICAL** | "LGPD compliance NOT confirmed – MUST be verified before proceeding." |
| **Security** | `has_penetration_test_report` == [Not Informed] | **HIGH** | "Security posture unverified – no pen test evidence." |
| **Scale** | `recent_load_test_evidence` == No | **HIGH** | "No recent proof of load capability – stress tests referenced but no report." |
| **Scale** | `has_auto_scaling` == [Not Informed] | **HIGH** | "Auto-scaling not explicitly confirmed – risk during peaks." |
| **UX** | `mobile_responsive_score` == [Not Assessed] | **MEDIUM** | "Mobile experience not evaluated." |
| **Product** | `real_time_updates` == [Not Informed] | **MEDIUM** | "Score update timing not specified." |

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| **Security / LGPD** | **⚠️ CRITICAL** | **Not Addressed.** LGPD compliance, data residency, certifications, age verification, and penetration testing NOT confirmed in either meeting or proposal. MUST be clarified before proceeding. |
| **Commercial / Cost** | **HIGH** | **Premium Pricing Confirmed.** $150,000 – $225,000 USD annual license. Highest cost option among evaluated suppliers. Fixed license model gives budget predictability. |
| **Timeline** | **HIGH** | **Mid-May Deadline is Tight.** Proposal: "If we confirm scope quickly and align on design decisions, we can achieve a mid-May go-live." Delay risks scope reduction. |
| **Data Ownership** | **MEDIUM** | **Co-Controller Model.** Proposal confirms: "co-controller data framework." Client has full access and CRM-ready exports, but NOT sole ownership. Contract must define boundaries. |
| **Notifications** | **LOW** | **Integration-Based.** CRM, analytics, and notification infrastructure integration confirmed, but no native notification engine described. |

## Key Strengths
| Strength Area | Rating | Description |
| :--- | :--- | :--- |
| **Experience & References** | ⭐⭐⭐⭐⭐ | FIFA PlayZone, MLB, publicly traded (NYSE: GENI). Unmatched pedigree. |
| **Product Feature Alignment** | ⭐⭐⭐⭐⭐ | Proposal confirms near-complete match: predictions, leagues, trivia, lucky draws, missions, sponsor activations. |
| **Data Pipeline** | ⭐⭐⭐⭐⭐ | Genius IS the sports data provider. No third-party dependency. |
| **Design & Development** | ⭐⭐⭐⭐⭐ | Full end-to-end managed service including design, dev, and operations. "Not a template product." |
| **Integration / SSO** | ⭐⭐⭐⭐⭐ | Multi-sponsor SSO proven with FIFA. Premium gating by subscription. CRM/analytics integration confirmed. |
| **Support** | ⭐⭐⭐⭐ | 24/7, Portuguese speaking, full lifecycle management, structured escalation. |
| **Budget Predictability** | ⭐⭐⭐⭐ | Fixed annual license ($150k-$225k) – no per-user or traffic-based cost surprises. |

## Block Ratings Summary
| Block | Rating | Status |
| :--- | :--- | :--- |
| 1. Robustness, Scale & Reliability | **4/5** | Promise reinforced by proposal |
| 2. Local Support & Operational Coverage | **4/5** | Strong indicators, SLA details needed |
| 3. User Support & Incident Management | **4/5** | Promise – credible due to FIFA ops |
| 4. Security, LGPD, Governance | **N/A** | ⚠️ Insufficient Data – CRITICAL gap |
| 5. Data Ownership, Access & Portability | **3/5** | Co-controller model, not sole ownership |
| 6. Core Product Features | **5/5** | Proven feature set, near-complete alignment |
| 7. League Management & Premium | **5/5** | Excellent alignment with league model |
| 8. Game Operation & Scoring | **5/5** | Genius IS the data provider |
| 9. Customization, UX & Front-End | **5/5** | Full creative ownership by Genius |
| 10. Integration Ecosystem | **5/5** | Proven with FIFA/MLB |
| 11. Notifications & Communication | **3/5** | CRM integration, no native engine |
| 12. Social Sharing & Virality | **4/5** | Sharing mechanic with incentive structure |
| 13. Geo-Restriction | **N/A** | Not assessed |
| 14. Roadmap & Evolution | **4/5** | Capable but May deadline is tight |
| 15. Commercial & Financial | **3/5** | Premium pricing ($150k-$225k USD) |
| 16. Team, Experience & References | **5/5** | FIFA, MLB, NYSE-listed |
| **Average (assessed blocks)** | **4.2/5** | |

## Final Recommendation
**✅ PROCEED WITH CAUTION – Best-in-Class Option, Pending Security Clarification**

Per system rules: 0 confirmed CRITICAL risks, but Security/LGPD is UNKNOWN (effectively a potential CRITICAL). >2 HIGH risks exist (cost, timeline, load test, pen test, auto-scaling). Average rating is 4.2 (>4.0). Recommendation: **PROCEED WITH CAUTION** until LGPD compliance is confirmed.

Genius Sports is the **clear technical and operational leader** in this evaluation. They have **proven World Cup-scale delivery** (FIFA PlayZone), the deepest feature set, and a fully managed service model that minimizes client-side resource requirements. The **$150k-$225k USD annual license** is the highest cost but includes everything (design, dev, ops, support).

**The decision hinges on three factors:**
1. **Security/LGPD:** Must confirm compliance before any contract. This is a blocking issue.
2. **Budget:** Can the project accommodate $150k-$225k USD? If within range + sponsor revenue potential, the ROI case is strong.
3. **Speed:** Contract must be signed rapidly to hit mid-May go-live without scope reduction.

**Immediate Next Steps:**
1. ~~**Review Proposal**~~ ✅ Done – Pricing confirmed at $150k-$225k USD annual license.
2. **Clarify Security & LGPD** – Request LGPD/GDPR compliance confirmation, data residency details, certifications (ISO, SOC), age verification capabilities, pen test reports.
3. **Clarify Data Ownership Contract Terms** – Ensure co-controller model has clear boundaries protecting client interests.
4. **Request Load Test Documentation** – Obtain concrete evidence of stress-tested infrastructure (concurrent users, architecture diagrams).
5. **Define Timeline Milestones** – Get detailed delivery schedule with checkpoints: design → build → UAT → go-live.
6. **Internal Budget Decision** – Present $150k-$225k USD to leadership and assess feasibility against project budget.
