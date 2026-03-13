# Questions for LiveLike – Data Architecture, Responsibilities, and Database Dependencies

This document outlines our technical questions for LiveLike. Each section begins with an explanation of our current context and primary concerns based on our internal alignment and the specific requirements of the CazéTV project.

---

### 1. Data Architecture and Database Ownership

**Context & Concern:** Our main concern is the governance and the boundary of responsibility regarding database management. We currently lack a robust internal infrastructure to manage millions of concurrent user sessions. While we prefer LiveLike's "API First" approach, we need to clearly define which data remains our responsibility to structure and maintain, and how this affects our internal operational load.

**Questions:**
- Which data is stored in LiveLike’s database and which data must be stored in CazéTV’s database?
- Can you confirm if only identity/authentication data (email, password, user ID) is stored in CazéTV’s database while all game-related data (predictions, leagues, rankings, scores, game events, etc.) is stored in LiveLike’s infrastructure?
- Are there any scenarios where game-related data needs to be stored or replicated in CazéTV’s database?
- Does LiveLike generate its own internal user ID that is mapped to the CazéTV SSO user?
- How does this mapping between the CazéTV user and the LiveLike user ID work technically?
- Is the mapping created only during the first login or verified every time the user logs in?

---

### 2. Frequency of Queries to the CazéTV Database

**Context & Concern:** Scalability is critical. During massive "calls-to-action" from CazéTV broadcasts, we expect millions of simultaneous users. We are worried about the potential for repeated queries to our authentication system becoming a bottleneck. We need to ensure that the integration doesn't create a dependency that could degrade performance for the user or crash our internal systems.

**Questions:**
- Does LiveLike query the CazéTV authentication database every time a user logs in, or only during the first login when the user is created?
- After authentication, does LiveLike operate using its own session/token, or does it continue querying the CazéTV database during gameplay?
- During peak moments (for example, millions of users joining after a CazéTV broadcast call-to-action), how many simultaneous queries could be triggered against the CazéTV authentication system?
- Is there any tokenization, caching, or session management mechanism implemented to avoid repeated calls to the authentication database?
- Is there a fallback mechanism if the CazéTV authentication system becomes slow or temporarily unavailable?

---

### 3. Operational Dependency on the CazéTV Infrastructure

**Context & Concern:** We want to establish a "single point of responsibility" for system availability. If there is a failure, it must be clear who is responsible for the fix. Our goal is to minimize the dependency of LiveLike's live operations on our relatively small internal infrastructure to avoid "cascading failures."

**Questions:**
- If the CazéTV database or authentication system goes offline, what happens to the LiveLike platform?
- Would new logins stop working, or would there be any fallback strategy?
- Would users who are already logged in still be able to continue playing normally?
- After login, does gameplay depend on any further calls to CazéTV infrastructure, or does everything run entirely within LiveLike systems?
- What level of availability and performance is required from the CazéTV authentication infrastructure to support this solution?

---

### 4. Infrastructure Ownership and Responsibilities

**Context & Concern:** Our internal team is not equipped to manage infrastructure for 10 million simultaneous users. We need to ensure that LiveLike, given its AWS auto-scale capabilities, carries the weight of the operational governance. We are looking for a partner who provides transparency and monitoring over all external dependencies.

**Questions:**
- In case of performance issues during traffic spikes, how are responsibilities divided between LiveLike and CazéTV?
- If there are authentication-related failures, is that considered a LiveLike issue or a CazéTV responsibility?
- Does LiveLike provide monitoring tools or alerts when external dependencies such as SSO begin degrading?
- Are there any recommended architecture patterns that minimize dependency on the client’s infrastructure?

---

### 5. SSO Integration

**Context & Concern:** We need a seamless integration with our modern stack, which may include integrations with third parties like iFood. Understanding the compliance with standard protocols is essential to ensure we can implement a secure and scalable SSO flow without "reinventing the wheel."

**Questions:**
- Which SSO standards are supported by LiveLike? (OAuth, OpenID Connect, SAML, etc.)
- What is the complete authentication flow expected for the integration?
- After authentication, does LiveLike issue its own session token to the user?
- What is the expiration policy for these tokens?

---

### 6. Data Access and Replication

**Context & Concern:** While LiveLike manages the games, the data generated is 100% CazéTV property. We need to understand how we can ingest this data into our own systems (e.g., for CRM purposes or real-time analytics) without impacting the live game performance.

**Questions:**
- Is it possible for LiveLike to send gameplay events (predictions, scores, rankings, etc.) to CazéTV systems through webhooks or streaming APIs?
- Are real-time event streams supported, or only batch exports?
- Can LiveLike provide periodic database exports or data replication so CazéTV can maintain a local copy of gameplay data?

---

### 7. Scalability and Peak Traffic

**Context & Concern:** This is our "north star." We were impressed by LiveLike's history of supporting 10M+ users. We need to understand the architectural safeguards you put in place specifically for SSO-heavy traffic to avoid bottle-necking at the client's identity provider.

**Questions:**
- What architecture is used to support very large spikes of simultaneous logins?
- Are there any recommended limits for external authentication requests (SSO) during peak events?
- How does LiveLike typically implement SSO in projects with 5–10+ million users?

---

### 8. Data Privacy and Compliance

**Context & Concern:** Compliance with LGPD (Brazil) and GDPR is non-negotiable. We need to ensure that the "encryption-only" processing mentioned in previous sessions is clearly documented and that user "right to be forgotten" requests can be fulfilled across both systems efficiently.

**Questions:**
- Which personal user data does LiveLike receive during the authentication process?
- Is this data stored permanently or only processed temporarily?
- Which user data is persisted in LiveLike systems?
- How does LiveLike handle user data deletion requests (LGPD / GDPR / Right to be Forgotten)?
