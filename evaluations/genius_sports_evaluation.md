# Supplier Evaluation Template

**Supplier Name:** `Genius Sports`
**Website:** `https://www.geniussports.com`
**Evaluator:** `Rodrigo`
**Date:** `2026-02-19`

**Source Materials:**
- Meeting Notes Summary (Gemini) – Feb 12, 2026 (4 pages)
- Full Meeting Transcript – Feb 12, 2026 (21 pages)
- **Genius Sports – World Cup Predictor Proposal** (Formal Proposal, 3 pages, received Feb 20, 2026)
- **Follow-Up Meeting Notes & Transcript** – Feb 23, 2026 (28 pages)
- Participants: Rodrigo Porto, Christian Abbonizio (Genius Sports), Patricia Souza

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic and proven load capacity.*

**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `Millions (FIFA PlayZone – millions of users playing their FIFA games)` `[Promise]`
- [x] **Strategy for 10M Concurrent Users (5 mins before game):**
  > `Genius confirmed they can accommodate stress tests for high concurrent user peaks, specifically mentioning 10 million concurrent users before a game starts (Meeting 1 – 00:19:46). Proposal confirms "stress-tested infrastructure and dedicated hosting environments" for peak matchday traffic. Targeting up to 15 million registrations.` `[Promise → Proposal Confirmed]`
- [x] **Maximum Simultaneous Users Tested:** `FIFA and IOC activations reached "many millions of users" (Follow-Up – 00:18:57). In terms of project scope, FIFA and IOC were "much much larger activations" with "similar user scale" (~15M).` `[Evidence – Follow-Up]`

**Infrastructure & Platforms:**
- [x] **Auto-scaling Infrastructure?** (Yes/No): `Implied Yes – Proposal confirms "dedicated hosting environments" and "stress-tested infrastructure." Follow-up confirms variable hosting costs are absorbed into the license fee, meaning Genius bears the scaling cost regardless of user count.`
- [ ] **Uptime SLA (%):** `Standard SLAs for uptime confirmed (Meeting 1 – 00:22:24), exact % not specified`
- [x] **Platforms Supported:**
    - [x] Web Desktop `(Proposal confirms: "responsive web" – primary platform)`
    - [x] Web Mobile `(Follow-Up confirms: web view solution recommended, accessible on mobile and desktop – 00:03:18)`
    - [x] App iOS `(Web view embed into existing app – confirmed. Follow-Up: native app development NOT an option for this timeline – 00:07:47)`
    - [x] App Android `(Web view embed into existing app – confirmed. Follow-Up: native app NOT recommended – 00:07:47)`

- **Observations:**
  > `Strong signal further reinforced by follow-up meeting: FIFA AND IOC (Olympics) activations confirmed at "many millions of users" scale (Follow-Up – 00:18:57). Christian stated these were "much much larger activations" in project scope. The platform approach is confirmed as responsive web view (not native app), which is the recommended and most feasible approach for the timeline. Hosting variable costs are absorbed into the annual license fee – Genius bears the infrastructure scaling risk.`
- **Block Rating (1-5):** `4 → 4.5 [Follow-up adds IOC reference and confirms Genius absorbs hosting/scaling costs. Still missing specific load test documentation.]`

---

## 2. Local Support & Operational Coverage
*Focus on the vendor's ability to provide reliable, real-time operational support during a high-stakes global event.*

**Local Presence & Timezone Alignment:**
- [x] **Local Support in Brazil?** (Yes/No): `Yes – Portuguese-speaking support is available (Meeting 1 – 00:21:05)`
- [x] **Portuguese-Speaking Support Team?** (Yes/No): `Yes (Meeting 1 – 00:21:05)`
- [ ] **Timezone Coverage Strategy for Brazil:**
  > `[Not Informed] – Not explicitly discussed, but Portuguese-speaking support availability implies coverage`
- [ ] **Dedicated Local Account Managers?** (Yes/No): `[Not Informed]`

**Support Availability:**
- [x] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `Yes – Genius provides 24/7 support (Meeting 1 – 00:22:24)`
- [ ] **SLA Response Times for Critical Incidents:** `Standard SLAs for uptime confirmed, specific response times not detailed`
- [ ] **Dedicated War-Room Structure During Major Events?** (Yes/No): `[Not Informed]`

**Operational Escalation Flow:**
- [x] **L1 Support (User Issues) – Handled by:** `✅ CONFIRMED (Follow-Up – 00:37:48): Genius manages ALL user support as first point of contact. They set up their own ZenDesk and support channels to inbound all user messages. Client does NOT need to build a support team.`
- [x] **L2 Technical Issues – Handled by:** `Full escalation pathways for bug triage confirmed (Meeting 1 – 00:22:24). Follow-Up (00:39:30): Genius escalates to client only for specific issues – purely informational ("hey just so you guys know this is happening, we're addressing this").`
- [ ] **L3 Infrastructure Failures – Handled by:** `[Not Informed explicitly – strongly implied Genius handles as full managed service]`

- **Observations:**
  > `✅ SIGNIFICANTLY CLARIFIED in follow-up: Genius runs a FULLY MANAGED support service. They set up their own ZenDesk, handle all inbound user messages, and only escalate to client for informational purposes. Client involvement in user support is "completely optional" – they can choose to have creative control over user interactions but it is NOT required (Follow-Up – 00:40:49). This eliminates the need for the client to hire or train a dedicated support team. Very strong support model.`
- **Block Rating (1-5):** `4 → 5 [Follow-up confirms fully managed ZenDesk-based support. Client does not need their own support team.]`

---

## 3. User Support & Incident Management
*Focus on operational ownership of user issues and incident resolution.*

**Support Ownership:**
- [x] **Who Handles User Complaints?** `Genius manages ALL user support as first point of contact via ZenDesk (Follow-Up – 00:37:48). Escalation to client is informational only and optional.`
- [x] **Who Handles Technical Bug Reports?** `Full escalation pathways for bug triage (Meeting 1 – 00:22:24). Genius handles and informs client as needed.`

**Escalation Process:**
- [x] **Defined Workflow for Critical Bugs?** (Yes/No): `Yes – Full escalation pathways for bug triage confirmed (Meeting 1 – 00:22:24). Follow-Up confirmed structured escalation with ZenDesk infrastructure.`
- [ ] **Defined Workflow for Mass User Incidents?** (Yes/No): `[Not Informed – implied by FIFA/IOC-scale operations]`

- **Observations:**
  > `Follow-up meeting clarified that support is a fully managed service. Client does NOT need a custom support team. Genius handles everything through their ZenDesk infrastructure. Escalations to client are informational and optional. Christian specifically stated: "unless the client wants to have a direct line of communication with the end user, you don't need to do that" (Follow-Up – 00:40:49).`
- **Block Rating (1-5):** `4 → 5 [Follow-up confirms fully managed support – no client-side support team required]`

---

## 4. Security, LGPD, Governance & Compliance
*Focus on legal compliance, data safety, and youth participation regulations.*

**Data Protection & Compliance:**
- [ ] **LGPD/GDPR Compliant?** (Yes/No): `[Not Informed – not addressed in either meeting or follow-up]`
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
  > `⚠️ STILL A MAJOR GAP after two meetings: Security, LGPD compliance, and age verification remain NOT discussed. This is CRITICAL for the Brazilian market and must be addressed before any contract. However, Genius's global operations with FIFA and IOC across multiple territories with "tons of different tax laws" (Follow-Up – 00:18:03) suggests compliance frameworks exist.`
- **Block Rating (1-5):** `[Not Assessed – Insufficient Data – STILL CRITICAL GAP]`

---

## 5. Data Ownership, Access & Portability
*Focus on guaranteeing full strategic control over user data and long-term usability.*

**Data Ownership:**
- [x] **All User Data Fully Owned by Client?** (Yes/No): `No – Co-controller status. Both the client and Genius share privileges and unrestricted access to user data (Meeting 1 – 00:23:39)`
- [ ] **Any Restrictions on Data Usage?** (Yes/No): `No restrictions – both parties have unrestricted access`
  > `Co-controller model: data lives in Genius's databases, both parties co-own and have full access`

**Data Access:**
- [x] **Access to Full User Database?** (Yes/No): `Yes – Full unobstructed access (Meeting 1 – 00:23:39)`
- [x] **Access to Behavioral Event Data?** (Yes/No): `Yes – Follow-Up (00:34:33): Genius collects user analytics on behavior, provides insights on how people use the product, and feeds data back to client.`
- [x] **Access to Prediction History?** (Yes/No): `[Implied Yes by full access model]`

**Data Collection Details (NEW – Follow-Up):**
- [x] **Registration Data:** `Email, first/last name, phone number – configurable in registration flow (Follow-Up – 00:34:33)`
- [x] **Behavioral Analytics:** `User engagement data, game behavior, usage patterns – collected and shared with client (Follow-Up – 00:34:33)`
- [x] **Lookalike Audiences:** `✅ BONUS: Genius can match collected user data with their broader global sports fan database to build lookalike audiences for targeted marketing campaigns (Follow-Up – 00:35:35)`
- [x] **Analytics Dashboard:** `Yes – comprehensive analytics dashboards to track specific user behaviors, understand which parts of the game work, and inform ongoing product improvement (Follow-Up – 00:36:39)`

**Data Extraction Methods:**
- [ ] **Direct Platform Exports?** (Yes/No): `[Not Informed]`
- [ ] **APIs for Real-Time Extraction?** (Yes/No): `[Not Informed]`
- [x] **Scheduled Automated Data Dumps?** (Yes/No): `Yes – File transfer protocols to share data into client's databases, CRM systems, email marketing systems (Meeting 1 – 00:24:55)`

**Exit Scenario (Critical):**
- [x] **If Partnership Ends – What Happens to User Accounts?**
  > `Data can be safely stored in the client's database at contract end (Meeting 1 – 00:24:55)`
- [x] **If Partnership Ends – What Happens to Historical Data?**
  > `Full data transfer confirmed – "in whatever way they prefer it to be transferred over" (Meeting 1 – 00:24:55)`
- [ ] **If Partnership Ends – What Happens to Behavioral Insights?**
  > `[Not Informed – implied covered by full data transfer]`
- [x] **Full Data Export Guaranteed on Exit?** (Yes/No): `Yes (Meeting 1 – 00:24:55)`
- [x] **⚠️ Code Ownership Post-Contract:** `NO – Genius retains ownership of the underlying code. Client does NOT get access to codebase after contract ends. Client owns the product's look, feel, and branding (which they can repurpose), but the technology belongs to Genius. This is why it's a LICENSE fee model. (Follow-Up – 00:25:41, 00:26:59)`

- **Observations:**
  > `Follow-up meeting significantly enriched the data picture: comprehensive analytics dashboards, behavioral data, lookalike audiences via Genius global fan graph, configurable registration fields. The MAJOR NEW FINDING is that Genius retains code ownership – client CANNOT maintain the product independently after contract ends. This is critical for long-term planning: if the client wants to continue, they MUST renew the license. Also, co-controller data model remains a point for legal review.`
- **Block Rating (1-5):** `3 [Co-controller model + proprietary code ownership means full platform dependency on Genius. Data access is excellent, but code lock-in is a strategic risk.]`

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

**Development Approach (NEW – Follow-Up):**
- [x] **New Development Required?** `Minimal. Follow-Up (00:08:42): Work is largely CONFIGURATION – "piecing together existing pieces of development work into a completely new bespoke structure." Back-end technology is leveraged from existing builds. It is a full custom build from the ground up BUT leveraging existing back-end technology. Christian confirmed "all things that we have done before" for "the vast majority" of features.`
- [x] **Only Truly New Feature:** `WhatsApp integration for in-app predictions – never been done before by Genius (Follow-Up – 00:22:47). Sending links via WhatsApp = "almost zero concerns." Making predictions WITHIN WhatsApp = needs investigation.`

**Prediction Types:**
- [x] Match Result (1x2) `(Proposal confirmed: "predict match scores across the group stage and knockout rounds")`
- [x] Exact Score `(Proposal confirmed: "predict match scores" – exact score input)`
- [x] Special Predictions `(Proposal confirmed: "tournament-level predictions, including overall winner, Golden Boot winner, and Brazil's progression")`
- [ ] Live Predictions `[Not Informed in proposal or follow-up]`
- [x] **Multiple Prediction Types Supported?** (Yes/No): `Yes – match predictions, tournament predictions, daily trivia`
- [x] **Configurable Scoring Logic?** (Yes/No): `Yes – Proposal: "Both tiers will use identical scoring mechanics to preserve fairness" implies configurable scoring system`

**Rankings:**
- [x] Global `(Implied by leaderboards)`
- [x] Public Leagues `(Free-to-play basic leaderboard – Meeting 1)`
- [x] Private Leagues `(Standard part of product builds – Meeting 1)`
- [ ] By Period (Day/Round/Tournament) `[Not Informed]`

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No) `Yes – Proposal: "identical scoring mechanics" between tiers, premium gets "enhanced rewards"`
- [ ] Multiple Rules Supported? (Yes/No) `[Not Informed – implied by custom builds]`
- [x] Missions / Challenges? (Yes/No) `Yes – Proposal confirms: "exclusive weekly missions" for premium users, daily trivia quiz`
- [x] Badges / Achievements? (Yes/No) `Yes – prototype included badges (Meeting 1 – 00:39:52)`
- [x] Prizes: `Proposal confirms: "standard prizing" (free), "enhanced rewards" (premium), weekly lucky number prize draws, experiential rewards for premium missions`

**Real-time API:**
- [ ] API for Live Data Display? (Yes/No) `[Not Informed]`

- **Observations:**
  > `Follow-up confirms development approach is primarily CONFIGURATION, not greenfield development. Christian: "it's piecing together existing pieces of development work into a completely new bespoke structure." Leveraging existing back-end technology. Only truly new feature exploration is WhatsApp in-app predictions. Feature set remains the strongest among evaluated suppliers. FIFA case studies confirmed as prediction-based games (fantasy, pick'ems, brackets – exact same product type).`
- **Block Rating (1-5):** `5 [Proven feature set via FIFA, confirmed configuration-based approach, near-complete alignment with prototype]`

---

## 7. League Management & Premium Infrastructure
*Focus on private and premium league scalability, creation, and administration.*

**Private Leagues:**
- [x] **Free Creation?** (Yes/No): `Yes – standard feature (Meeting 1 – 00:02:16)`
- [ ] **Invite via Link?** (Yes/No): `[Not Informed – implied by private league feature]`
- [x] **Participant Limit Config?** (Yes/No): `Yes – Proposal confirms: Free users join up to 5 private leagues, Premium users create and join up to 100`
- [x] **How Scalable Is Private League Creation?**
  > `Proposal: "The private league engine will serve as a core differentiator." Positioned as national hub for friend-based competition. "Brazil's strong culture of social prediction" referenced.`
- [ ] **Maximum Number of Private Leagues Supported:** `[Not Informed – but designed for national scale with 15M registrations target]`

**Sponsored Leagues (NEW – Follow-Up):**
- [x] **Sponsor-Branded Leagues?** (Yes/No): `Yes – Follow-Up (00:15:02): Sponsored leagues (e.g., "Coca-Cola League") are ALREADY IN SCOPE. No additional cost or scope change.`
- [x] **Data Segmentation per Sponsor?** (Yes/No): `Yes – Follow-Up (00:16:23): User data can be segmented by sponsored league (e.g., "these are the 100,000 people that played the Coca-Cola league and here's their data"). This does NOT increase project scope.`

**Premium League Logic:**
- [x] **League Access Restricted by Subscription Status?** (Yes/No): `Yes – users with existing paid subscriptions from sponsors can log in as premium users via SSO (Meeting 1 – 00:09:50, 00:27:33)`
- [x] **League Access Restricted by External Partner Eligibility?** (Yes/No): `Yes – sponsor-based gating via SSO (Meeting 1 – 00:09:50)`
- [x] **Support for Public Leagues?** (Yes/No): `Yes – free-to-play basic leaderboard (Meeting 1)`
- [x] **Support for Private Leagues?** (Yes/No): `Yes – standard part of builds (Meeting 1)`
- [x] **Support for Premium Leagues?** (Yes/No): `Yes – premium leaderboard with better prizes (Meeting 1)`
- [x] **Paid-Entry Premium Leagues?** (Yes/No): `Possible – Follow-Up (00:40:49): Discussed as contingency if no sponsors. Would require payment gateway integration (additional cost, NOT in base license).`

**Administration Controls:**
- [ ] **League Moderation Tools?** (Yes/No): `[Not Informed]`
- [ ] **Anti-Fraud Mechanisms?** (Yes/No): `[Not Informed]`

- **Observations:**
  > `Follow-up confirms sponsored leagues are already in scope at no extra cost. Multi-sponsor data segmentation already built in. The paid-entry premium league option is available as a contingency but adds complexity (payment gateway, legal considerations in Brazil). Very strong league infrastructure.`
- **Block Rating (1-5):** `5 [Excellent alignment with league model requirements. Sponsored leagues already in scope.]`

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
- [x] **Full CSS/Theme Customization:** (Yes/No): `Yes – fully custom builds, not white-label templates (Meeting 1 – 00:03:14)`
- [x] **Full UI Customization or Limited Branding?**
  > `Full custom UI – "Genius does not use white-label solutions, opting for custom builds to provide full flexibility over features and creative control" (Meeting 1 – 00:03:14). Follow-Up confirms: "full custom build from the ground up" with "design UX prototyping aspect of it all the way through the front-end build" (00:08:42).`
- [x] **Custom Domain (CNAME):** (Yes/No): `Yes – implied by custom builds (FIFA PlayZone sits as micro-site within FIFA.com)`
- [ ] **Mobile Responsive Score (1-10):** `[Not Assessed – mobile web view is recommended approach]`

**Design Ownership:**
- [x] **Vendor Provides UI/UX Designers?** (Yes/No): `Yes – end-to-end managed service includes design (Meeting 1 – 00:06:06). Follow-Up confirms full design-to-build pipeline.`
- [x] **Vendor Provides Front-End Development Support?** (Yes/No): `Yes – full development capability (React Native, native web – Meeting 1 – 00:08:37). Follow-Up confirms web view as recommended approach.`
- [ ] **Client Must Supply Design Resources?** (Yes/No): `No – Genius handles "the entire end-to-end experience of building it" including design; client provides branding guides`

**Live Demo (NEW – Follow-Up):**
- [x] **Demo / Testing Environment Available?** (Yes/No): `Yes – Christian committed to providing links to live or testing environments of prediction games. Some are live in market, others are testing environments (Follow-Up – 00:20:12). Final product will be fully customized – demos show functionality, not final look.`

- **Observations:**
  > `Premium offering reinforced by follow-up. Full end-to-end design and development confirmed. Development is "design UX prototyping all the way through the front-end build." Live demo links being provided for client to experience the product functionality. Client will see "how our products work" even though the final product will look and feel like their own brand.`
- **Block Rating (1-5):** `5 [Full creative and development ownership by Genius. Demo access being provided.]`

---

## 10. Integration Ecosystem & Partner Connectivity
*Focus on connecting with existing client tech, third-party data sources, and membership systems.*

**Documented APIs:**
- [x] Login/SSO `(Single sign-on with multiple third-party providers confirmed – Meeting 1 – 00:09:50, 00:10:59)`
- [ ] Partners `[Not Informed – specific API docs not discussed]`

**Partner Integration:**
- [x] Partner Benefits? (Yes/No) `Yes – sponsor activations layered into games (Meeting 1 – 00:12:03)`
- [x] Subscription Status? (Yes/No) `Yes – premium access via existing sponsor subscription (Meeting 1 – 00:09:50)`
- [ ] External Rewards? (Yes/No) `[Not Informed]`

**Third-Party Integration Scope (NEW – Follow-Up):**
- [x] **Multiple Sponsors Impact on Scope?** `NO IMPACT – Follow-Up (00:15:02, 00:16:23): Sponsored leagues and user data segmentation per sponsor are ALREADY IN SCOPE. Adding multiple sponsors does NOT change the development scope or cost.`
- [x] **Technical Integration Dependencies?** `Follow-Up (00:03:18): The $75k cost range gap partly depends on technical integrations. Once CazeTV documentation on subscription services is reviewed, the cost range can be narrowed.`

**External Database Integration:**
- [x] **Can Connect to Loyalty Programs (e.g., iFood Club)?** (Yes/No): `Yes – integrates with CRM systems, email marketing systems, various databases (Meeting 1 – 00:07:18, 00:24:55)`
- [x] **Can Connect to Subscription Databases?** (Yes/No): `Yes – SSO with sponsor subscription verification (Meeting 1 – 00:09:50)`

**WhatsApp Integration (NEW – Follow-Up):**
- [x] **WhatsApp as Communication Channel?** (Yes/No): `Yes – Follow-Up (00:25:41): Sending links via WhatsApp to redirect users to prediction page = "almost zero concerns, can almost certainly do this."`
- [ ] **WhatsApp In-App Predictions?** (Yes/No): `Under Investigation – Follow-Up (00:22:47): Making predictions directly within WhatsApp has NEVER been done by Genius before. They will investigate WhatsApp APIs. Not guaranteed.`
- [ ] **WhatsApp Business API Integration?** (Yes/No): `Under Investigation – Rodrigo emphasized WhatsApp's dominance in Brazil (99% penetration). Genius will explore official WhatsApp Business API integration (Follow-Up – 00:24:14).`

**Access Authorization:**
- [x] **Entry to Premium Leagues Gated by Partner Status?** (Yes/No): `Yes (Meeting 1 – 00:09:50)`
- [x] **Entry to Premium Leagues Gated by Subscription Verification?** (Yes/No): `Yes – user with active subscription logs in directly as premium (Meeting 1 – 00:27:33)`
- [ ] **Entry to Premium Leagues Gated by External APIs?** (Yes/No): `[Implied Yes via SSO]`

**Experience:**
- [x] Co-branding Support? (Yes/No) `Yes – offered to brand proposal to potential sponsor (Meeting 1 – 00:45:09)`
- [x] Exclusive Partner Areas? (Yes/No) `Yes – sponsor activations and premium leagues (Meeting 1 – 00:12:03)`
- [x] Track Record with Media/Sponsors? (Yes/No) `Yes – FIFA, IOC (Olympics), Major League Baseball, major sports organizations worldwide plus Brazilian sportsbooks (Follow-Up – 00:16:23, 00:18:57)`

- **Observations:**
  > `Follow-up significantly clarified the integration picture: multiple sponsors do NOT change scope. WhatsApp integration has two tiers: (1) link-sending – easy, near-certain; (2) in-app predictions – uncharted territory for Genius, needs investigation. Genius's Brazilian presence is through sportsbook data partnerships (NFL data rights in Brazil). The $75k cost range gap is partly driven by technical integration complexity.`
- **Block Rating (1-5):** `5 [Proven integration ecosystem. Multi-sponsor already in scope. WhatsApp link-sending feasible.]`

---

## 11. Channels, Notifications & User Communication
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [x] **Email Automation:** (Yes/No): `Yes – Follow-Up (00:05:34): Game reminder emails (score updates, "don't forget to make your picks this week") are INCLUDED in the base license cost.`
- [ ] **Web Push Notifications:** (Yes/No): `[Not Informed explicitly – proposal mentions "notification infrastructure" integration]`
- [ ] **WhatsApp Notifications:** (Yes/No): `Under Investigation – Follow-Up: WhatsApp as notification/engagement channel is being explored. Link-sending via WhatsApp is feasible.`

**Communication Ownership:**
- [ ] **Who Manages Messaging Templates?** `[Not Informed – implied shared via CRM integration]`
- [ ] **Who Manages Campaign Scheduling?** `[Not Informed – implied shared via CRM integration]`

**Additional Costs for Communication (NEW – Follow-Up):**
- [x] **Marketing Campaigns for User Acquisition:** `ADDITIONAL COST – Follow-Up (00:06:43): Running marketing campaigns to drive user acquisition and building associated creative assets (banners, social media assets) are NOT included in the base license. Genius can help but at additional cost. Cost efficiencies available since client is already committing to the bigger product build.`

- **Observations:**
  > `Follow-up clarified: game-related emails (reminders, score updates) are INCLUDED. Marketing/acquisition campaigns are EXTRA. Genius can build creative banners and assets for advertising the game (YouTube, socials, etc.) but these are additional costs with potential volume discounts. WhatsApp integration for notifications is being explored. Daily engagement mechanic (trivia → lucky numbers) still serves as a strong organic re-engagement driver.`
- **Block Rating (1-5):** `3 → 4 [Game emails confirmed included. Marketing campaigns at extra cost but with efficiencies. WhatsApp under investigation.]`

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
  > `Not discussed in either meeting. Should be clarified given the Brazil-specific nature of the project.`
- **Block Rating (1-5):** `[Not Assessed – Insufficient Data]`

---

## 14. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [x] **Can Close Dedicated Roadmap for Cup?** (Yes/No): `Yes – custom build dedicated to this project`
- [x] **Open to Partner-Specific Features?** (Yes/No): `Yes – custom development is their model. "Almost all features in the prototype have been built before" (Meeting 1 – 00:42:49). Also open to live triggers and influencer-driven missions.`
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Low] – custom builds, not shared platform` `[Promise]`
- **Timelines (UPDATE – Follow-Up):**
    - Design & Prototyping: `March 2026 – a couple weeks of design, kicking off back-end development simultaneously (Follow-Up – 00:10:56)`
    - Development: `March–May 2026 – development through April and May while finalizing front-end prototyping (Follow-Up – 00:10:56)`
    - Go-Live Target: `May 11–18, 2026 (Rodrigo's preferred window). Christian's target: end of May (2 weeks before World Cup kickoff in June). Prioritized feature rollout possible – get registration and initial predictions open first, then V2 sprints until World Cup (Follow-Up – 00:12:04).`
    - Contract/LOI Deadline: `Within 2 weeks from Feb 23, 2026 (i.e., by ~March 9, 2026). Letter of Intent acceptable to start work (Follow-Up – 00:13:54).`

**Multi-Year / Multi-Sport License (NEW – Follow-Up):**
- [x] **Product Reusable for Other Competitions?** (Yes/No): `Yes – Follow-Up (00:28:04): Women's World Cup 2027, domestic league (year-round), other sports. Multi-year license restructuring possible for cost efficiencies.`
- [x] **Adaptation Cost for New Competitions:** `Additional work required within an expanded multi-sport license. New match feeds, prediction structures, and fixtures would be covered within expanded license. Major deviations = change request / additional license fee (Follow-Up – 00:29:18, 00:30:53).`
- [x] **Post-World Cup Platform State:** `If client decides not to continue, platform can remain online for users to view results for an agreed period, then goes into "dormant state" (Follow-Up – 00:32:02).`

- **Observations:**
  > `Timeline is now much clearer: design in March, dev through April-May, go-live target May 11-18 (Rodrigo's preference) or end of May at latest. Contract or LOI needed by ~March 9. Feature prioritization strategy agreed – launch with core predictions/registration, then sprint remaining features. Multi-year license option opens up Women's World Cup 2027 and domestic league as cost-efficient extensions. Dormant state option provides graceful exit.`
- **Block Rating (1-5):** `4 [Timeline now detailed. May 11-18 launch feasible with rapid sign-off. Multi-year option adds strategic value.]`

---

## 15. Commercial, Contractual & Financial Risk
*Focus on cost structure, lock-in risks, and financial predictability.*

**Cost Structure (SIGNIFICANTLY CLARIFIED – Follow-Up):**
- [x] **Setup Fee Range:** `$150,000 – $225,000 USD (Annual License Fee) [Proposal Confirmed]`
- [x] **Pricing Model:** `Annual License Fee – fixed range. ALL-ENCOMPASSING. Follow-Up (00:03:18): license fee covers variable costs including hosting, user scaling impacts, and game-related email communications.`

**Cost Variability & Budget Risk (CLARIFIED – Follow-Up):**
- [x] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `NO – Follow-Up (00:03:18): "licensing fees are intended to be all-encompassing costs... covering variable costs for hosting and all of that kind of stuff for different user impacts." Whether 1M or 20M+ users, Genius absorbs hosting costs.`
- [x] **Can Costs Increase Due to API Usage?** (Yes/No): `NO – implied by all-encompassing license model`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `Yes – Follow-Up (00:03:18): The $75k gap between $150k and $225k depends on: (1) total scope/features, (2) technical integration complexity (especially CazeTV subscription integration documentation). Range narrows once integrations are scoped.`

**What's Included in the License (CLARIFIED – Follow-Up):**
- [x] Hosting & Infrastructure (variable costs absorbed)
- [x] Design, UX & Prototyping
- [x] Full Front-End Custom Build
- [x] Back-End Development (leveraging existing tech)
- [x] Game Reminder Emails (score updates, pick reminders)
- [x] User Support (fully managed via ZenDesk)
- [x] 24/7 Operations & Monitoring
- [x] Sports Data Feed

**What's NOT Included (CLARIFIED – Follow-Up):**
- [x] **Marketing Campaigns for User Acquisition** – additional cost (Follow-Up – 00:06:43)
- [x] **Creative Assets for Advertising** (banners, social media assets) – additional cost, but cost efficiencies if bundled (Follow-Up – 00:07:47)
- [x] **Native App Development** – not recommended for this timeline, would be additional cost if pursued (Follow-Up – 00:03:18)
- [x] **Payment Gateway Fees** – pass-on cost if premium paid leagues are implemented (Follow-Up – 00:44:34)
- [x] **Prize Fulfillment** – client responsibility
- [x] **Multi-Sport Adaptations** – additional license scope/change request (Follow-Up – 00:30:53)

**Payment Gateway Option (NEW – Follow-Up):**
- [x] **Payment Gateway Partners:** `Stripe (direct experience), Plucky (paid leagues partner). Plucky's jurisdiction in Brazil unclear. Other options to be explored (Follow-Up – 00:42:06).`
- [x] **Payment Collection Model:** `Payments collected on behalf of client. Could be structured as hybrid: license fee + revenue share. Gateway fees are pass-on costs (Follow-Up – 00:44:34).`
- [x] **Brazilian Payment Processing:** `⚠️ Under Investigation – Follow-Up (00:18:03): Genius is consulting finance team about tax implications of Brazil operations. They operate globally with "tons of different tax laws" and are confident a solution exists. Christian: "I'd be shocked if we can't find something that works for both." ~40% tax issue for cross-border payments being actively addressed.`

**Contract Terms:**
- [x] **License Model:** `Annual license – Genius retains code ownership. Client licenses the technology. (Follow-Up – 00:25:41)`
- [x] **Multi-Year Option:** `Available – restructure commercials for multi-year with Women's World Cup, domestic league, other sports. More cost-effective with longer commitment (Follow-Up – 00:28:04).`
- [ ] **Early Termination Penalties?** (Yes/No): `[Not Informed]`
- [x] **Post-Contract State:** `Platform can remain online in "dormant state" for users to view results after World Cup ends (Follow-Up – 00:32:02).`

**Platform Dependency & Exit Risks:**
- [x] **⚠️ CODE LOCK-IN (NEW – Follow-Up):** `Genius retains ownership of underlying code. Client CANNOT independently maintain, modify, or operate the product after contract ends. The license fee model means perpetual dependency on Genius for any platform operation. Client owns branding/look/feel only (Follow-Up – 00:25:41, 00:26:59).`
- [x] **Data Portability Guarantees?** (Yes/No): `Yes – co-controller data framework, CRM-ready exports, full data transfer at exit`

- **Observations:**
  > `💰 MAJOR CLARITY from follow-up: The license fee is ALL-ENCOMPASSING. Variable costs (hosting, scaling, email) are absorbed by Genius. The $75k range ($150k→$225k) maps to scope complexity (features + technical integrations). Additional costs are: marketing campaigns, creative assets, native app development, payment gateway fees, multi-sport adaptations. ⚠️ KEY RISK CONFIRMED: Code lock-in. Genius retains ALL code IP. Client cannot operate independently post-contract. This is the trade-off for the fully managed model. Payment processing in Brazil is under investigation but Genius is confident a solution exists. Multi-year licensing offers cost efficiencies.`
- **Block Rating (1-5):** `3 [All-encompassing license is positive for cost predictability. Code lock-in is a strategic risk. Premium pricing confirmed. Brazilian payment processing TBD.]`

---

## 16. Team, Experience & References
*Focus on supplier maturity.*

- [x] **Years in Market:** `[Established – Genius Sports is a publicly traded company (NYSE: GENI)]`
- [x] **Previous World Cup/Massive Event Cases:** `Yes – FIFA PlayZone (prediction games, fantasy, pick'ems, brackets). IOC (Olympics) activation. Both "many millions of users" scale (Follow-Up – 00:18:57). These are prediction-based games – "exactly what we're talking about here" (Follow-Up – 00:20:12).`
- [x] **Brazilian Market Presence:** `Yes, but NOT for free-to-play predictor games. Genius has major partnerships with Brazilian sportsbooks (official NFL data rights). No current Brazilian free-to-play predictor clients (Follow-Up – 00:16:23).`
- [ ] **Reference Contacts Provided?** (Yes/No): `Case studies deck previously shared. Live demo links being prepared for client experience (Follow-Up – 00:20:12).`

- **Observations:**
  > `Genius Sports remains the strongest reference: publicly traded (NYSE: GENI), FIFA partner, IOC partner, MLB partner, works with all major Brazilian sportsbooks. Follow-up confirmed FIFA and IOC activations were PREDICTION-BASED games at "many millions" scale. No current free-to-play predictor clients in Brazil specifically, but extensive Brazilian partnerships through their data business. Demo links being provided for client to experience live products.`
- **Block Rating (1-5):** `5 [FIFA + IOC + MLB partner, publicly traded, proven at prediction games at World Cup/Olympics scale]`

---

# Executive Summary & Recommendation

> **Updated: 2026-02-24** – Now includes data from the formal proposal AND follow-up meeting (Feb 23, 2026).

## Executive Summary
Genius Sports is a **premium, enterprise-grade gamification partner** with the strongest pedigree in this evaluation – they are the official technology partner behind **FIFA's PlayZone** and the **IOC's Olympic activations**, handling millions of users at World Cup and Olympic scale. Unlike Fan Arena or Easypromos, Genius offers **fully custom builds** (not white-label), providing complete creative and technical control. They deliver an **end-to-end managed service** covering design, development, operations, support (via ZenDesk), and game-related communications.

The follow-up meeting (Feb 23, 2026) significantly clarified the commercial model: the **$150,000 – $225,000 USD annual license** is **ALL-ENCOMPASSING** – it covers variable costs including hosting, infrastructure scaling, game emails, user support, and sports data feeds. The **$75,000 range** depends on total feature scope and technical integration complexity. Additional costs exist only for: marketing campaigns, creative assets for advertising, payment gateway fees, and multi-sport adaptations.

**Critical finding:** Genius **retains ownership of all underlying code**. The client owns branding/look/feel but CANNOT independently operate or maintain the product after contract ends. This is a license model – perpetual platform dependency on Genius.

Development is primarily **configuration-based** – "piecing together existing development work into a new custom build" leveraging proven back-end technology. Only WhatsApp in-app predictions would be truly new development.

## Automated Risk Flags
| Category | Flag Condition | Risk Level | Alert |
| :--- | :--- | :--- | :--- |
| **Security** | `lgpd_compliant` == [Not Informed] | **⚠️ CRITICAL** | "LGPD compliance NOT confirmed – MUST be verified before proceeding." |
| **Security** | `has_penetration_test_report` == [Not Informed] | **HIGH** | "Security posture unverified – no pen test evidence." |
| **Scale** | `recent_load_test_evidence` == No | **HIGH** | "No recent proof of load capability – stress tests referenced but no report." |
| **Commercial** | `code_ownership` == Genius (Not Client) | **HIGH** | "Client cannot operate product independently. Full platform lock-in." |
| **UX** | `mobile_responsive_score` == [Not Assessed] | **MEDIUM** | "Mobile experience not evaluated." |

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| **Security / LGPD** | **⚠️ CRITICAL** | **STILL Not Addressed after 2 meetings.** LGPD compliance, data residency, certifications, age verification, and penetration testing NOT confirmed. MUST be clarified before any contract. |
| **Code Lock-In** | **HIGH** | **NEW FINDING.** Genius retains ownership of all underlying code. Client CANNOT maintain or operate the product independently post-contract. Perpetual license dependency. |
| **Commercial / Cost** | **HIGH** | **Premium Pricing Confirmed.** $150k–$225k USD annual license (all-encompassing). Highest cost but includes everything. Additional costs for marketing, creative, payment gateway. |
| **Timeline** | **MEDIUM** | **Tighter than Before.** Contract/LOI needed by ~March 9 to hit May 11-18 go-live. Phased launch approach agreed (core first, then sprints). |
| **Brazilian Payments** | **MEDIUM** | **Under Investigation.** ~40% tax on cross-border payments is a concern. Genius consulting finance team. Confident a solution exists but unconfirmed. |
| **Data Ownership** | **MEDIUM** | **Co-Controller Model.** Client has full access and CRM-ready exports, but NOT sole data ownership. Contract must define boundaries. |
| **WhatsApp** | **LOW** | **In-App Predictions Not Guaranteed.** Genius has never done WhatsApp in-app predictions before. Link-sending via WhatsApp is feasible. |

## Key Strengths
| Strength Area | Rating | Description |
| :--- | :--- | :--- |
| **Experience & References** | ⭐⭐⭐⭐⭐ | FIFA PlayZone, IOC Olympics, MLB. Publicly traded (NYSE: GENI). Prediction games at millions-user scale. |
| **Product Feature Alignment** | ⭐⭐⭐⭐⭐ | Near-complete match. Configuration-based development leveraging proven tech. |
| **Data Pipeline** | ⭐⭐⭐⭐⭐ | Genius IS the sports data provider. No third-party dependency. |
| **Design & Development** | ⭐⭐⭐⭐⭐ | Full end-to-end managed service. Design, UX, prototyping, front-end, back-end. |
| **Integration / SSO** | ⭐⭐⭐⭐⭐ | Multi-sponsor SSO proven. Sponsored leagues already in scope at no extra cost. |
| **Support** | ⭐⭐⭐⭐⭐ | Fully managed via ZenDesk. Client does NOT need own support team. Portuguese-speaking. 24/7. |
| **Budget Predictability** | ⭐⭐⭐⭐ | All-encompassing license absorbs variable costs (hosting, scaling, emails). |
| **Data & Analytics** | ⭐⭐⭐⭐ | Comprehensive analytics dashboards, behavioral data, lookalike audiences via global fan graph. |

## Block Ratings Summary
| Block | Rating | Status |
| :--- | :--- | :--- |
| 1. Robustness, Scale & Reliability | **4.5/5** | IOC added. Genius absorbs hosting costs. |
| 2. Local Support & Operational Coverage | **5/5** | ✅ Fully managed ZenDesk support confirmed |
| 3. User Support & Incident Management | **5/5** | ✅ No client support team needed |
| 4. Security, LGPD, Governance | **N/A** | ⚠️ STILL NOT ADDRESSED – CRITICAL |
| 5. Data Ownership, Access & Portability | **3/5** | Co-controller + code lock-in |
| 6. Core Product Features | **5/5** | Configuration-based, proven feature set |
| 7. League Management & Premium | **5/5** | Sponsored leagues already in scope |
| 8. Game Operation & Scoring | **5/5** | Genius IS the data provider |
| 9. Customization, UX & Front-End | **5/5** | Full creative ownership + demo access |
| 10. Integration Ecosystem | **5/5** | Multi-sponsor no extra cost. WhatsApp explore. |
| 11. Notifications & Communication | **4/5** | Game emails included. Marketing extra. |
| 12. Social Sharing & Virality | **4/5** | Sharing mechanic with incentive structure |
| 13. Geo-Restriction | **N/A** | Not assessed |
| 14. Roadmap & Evolution | **4/5** | Timeline detailed. Multi-year option available. |
| 15. Commercial & Financial | **3/5** | All-encompassing but code lock-in risk |
| 16. Team, Experience & References | **5/5** | FIFA + IOC + MLB, NYSE-listed |
| **Average (assessed blocks)** | **4.5/5** | ⬆️ Up from 4.2 |

## Final Recommendation
**✅ PROCEED WITH CAUTION – Best-in-Class Option, Pending Security Clarification & Contract Review**

Per system rules: 0 confirmed CRITICAL risks, but Security/LGPD is UNKNOWN (effectively a potential CRITICAL). Code lock-in is a HIGH strategic risk. Average rating is 4.5 (>4.0). Recommendation: **PROCEED WITH CAUTION** until LGPD compliance and code ownership terms are contractually resolved.

Genius Sports is the **clear technical and operational leader** in this evaluation. The follow-up meeting reinforced their position: all-encompassing license, fully managed support, configuration-based development, IOC added to FIFA references, and sponsored leagues already in scope.

**The decision now hinges on five factors:**
1. **Security/LGPD:** Must confirm compliance before any contract. This is a blocking issue.
2. **Code Lock-In:** Client must accept perpetual Genius dependency or negotiate code escrow/exit terms.
3. **Budget:** Can the project accommodate $150k-$225k USD? All-encompassing nature reduces hidden cost risk.
4. **Brazilian Payments:** ~40% tax issue on cross-border payments must be resolved. Genius is investigating.
5. **Speed:** Contract/LOI must be signed by ~March 9 to hit May 11-18 go-live.

**Immediate Next Steps:**
1. ~~**Review Proposal**~~ ✅ Done – Pricing confirmed at $150k-$225k USD annual license.
2. ~~**Follow-Up Meeting**~~ ✅ Done – Feb 23, 2026. Key clarifications obtained.
3. **Clarify Security & LGPD** – Request LGPD/GDPR compliance confirmation, data residency details, certifications (ISO, SOC), age verification capabilities, pen test reports.
4. **Negotiate Code Lock-In Terms** – Explore code escrow, source code access on exit, or minimum viability guarantees.
5. **Resolve Brazilian Payment/Tax Issue** – Await Genius finance team response on Brazil tax structure.
6. **Request Live Demo Links** – Christian committed to providing these. Critical for client (CazeTV) presentation.
7. **Receive Statement of Work** – Christian to outline features in/out at various price points.
8. **Receive Multi-Year Commercial Option** – Women's World Cup + domestic league packaging.
9. **Await WhatsApp Integration Feasibility** – Christian to investigate.
10. **Internal Decision by End of Week** – Rodrigo to update Christian on path forward.
11. **Sign Contract/LOI by ~March 9** – Required for May launch window.
