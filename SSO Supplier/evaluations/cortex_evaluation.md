# SSO Supplier Evaluation Template

**Supplier Name:** `Cortex`
**Website:** `[Not Provided — UK-based sports tech company]`
**Evaluator:** `Rodrigo / Antigravity (Agent)`
**Date:** `2026-04-09`

**Source Materials:**
- Cortex Intro Meeting — 2026-04-08 (34 min transcription, Google Meet / Gemini Notes)
- Participants: Rodrigo Porto, Patricia Souza (CazéTV); Jack Carter, Sharon Tuff, Ben Hayward, Ciaran Fisher (Cortex)

> ⚠️ **IMPORTANT:** This evaluation is based exclusively on a **first introductory call**. No formal proposal, architecture document, or commercial terms have been received yet. Many fields remain `[Awaiting Proposal]`. Cortex committed to delivering a proposal by **end of week (April 11, 2026)** with a follow-up meeting scheduled for **Monday April 14** at 1 PM BRT / 5 PM BST.

---

## 1. Architecture & Technical Solution
*Focus on the proposed identity system design and technology choices.*

**Proposed Stack:**
- [ ] **Identity Platform/Framework Used:** `Cortex proprietary SaaS platform — sports-specific SSO`
- [ ] **Cloud Provider & Region:** `[Awaiting Proposal — not specified in call. SaaS managed by Cortex.]`
- [ ] **Database for User Identity & PII:** `[Awaiting Proposal — not specified in call]`
- [ ] **Architecture Diagram Provided?** (Yes/No): `Não — prometido na proposta`

**Protocol & Standards Compliance:**
- [x] **OIDC (OpenID Connect) Support?** (Yes/No): `Sim — Ciaran Fisher confirmou: "it's a standard OIDC — Open ID Connect flow" (00:10:05)`
- [x] **OAuth 2.0 Support?** (Yes/No): `Sim — implícito no suporte a OIDC`
- [x] **JWT Token Issuance?** (Yes/No): `Sim — Ciaran descreveu fluxo de token: "the web browser pushes you back into the app and says 'hey, Rodrigo's logged in. Here's his token'" (00:13:26)`
- [ ] **Token Format & Claims Configurable?** (Yes/No): `[Awaiting Proposal]`

**Authentication Methods:**
- [ ] Email + Password `[Awaiting Proposal — não especificado no call]`
- [ ] Google Social Login `[Awaiting Proposal]`
- [ ] Apple Social Login `[Awaiting Proposal]`
- [ ] Facebook Social Login `[Awaiting Proposal]`
- [ ] Other: `[Awaiting Proposal]`

> **Nota:** O call não detalhou métodos específicos de autenticação. O brief de seleção exige email/senha + social login (Google, Apple, Facebook).

- **Observations:**
  > `✅ Confirmação forte de OIDC/JWT como protocolo padrão. Cortex posiciona-se como plataforma SaaS esportiva ("sports-specific SSO"), não um framework genérico. Dois modelos de deployment mencionados: (1) micro-site rápido (recomendado para o prazo da Copa) e (2) API-based com front-end custom (para evolução futura). O micro-site é hospedado/gerenciado pela Cortex, com customização de marca. Upgrade futuro para front-end bespoke possível SEM refatoração do sistema inteiro — boa extensibilidade.`
- **Block Rating (1-5):** `3 [OIDC confirmado, mas sem detalhes de stack/infra. Modelo SaaS claro. Aguardando proposta técnica.]`

---

## 2. LiveLike Integration & Handshake
*Focus on compatibility and readiness to integrate with the LiveLike platform.*

**Integration Readiness:**
- [x] **SSO Endpoint Available for LiveLike?** (Yes/No): `Sim — Ciaran: "it's a standard OIDC flow, so it's relatively easy for other parties to integrate with" (00:10:05)`
- [x] **Token Format Compatible with LiveLike Spec?** (Yes/No): `Sim — OIDC + JWT é o padrão exigido pela LiveLike`
- [ ] **CazéTV Auth → LiveLike ID Mapping Flow Described?** (Yes/No): `Não detalhado — mencionado fluxo genérico de token handoff`
- [ ] **Handshake Certification Plan?** (Yes/No): `[Awaiting Proposal]`

**Integration Experience:**
- [x] **Previous Experience with Federated Identity Handshakes?** (Yes/No): `Sim`
  > `Ciaran Fisher mencionou que estava em OUTRA call com LiveLike para outro cliente DURANTE a mesma semana: "I just reason I was late to this call actually was I was on another call with LiveLike for a different customer" (00:08:59). Cortex já tem relação com LiveLike e experiência de integração.`
- [ ] **Estimated Integration Time with LiveLike:** `[Awaiting Proposal — Ciaran disse "relatively quick to spin up"]`

- **Observations:**
  > `🔥 PONTO FORTÍSSIMO: Cortex já tem relação ativa com LiveLike e estava literalmente em outra call com LiveLike no mesmo dia para outro cliente. Isso REDUZ DRASTICAMENTE o risco de integração. O OIDC flow é padrão e compatível. Documentação de integração prometida ("we can point some documentation around that as well for those third parties"). Integração descrita como "relatively straightforward".`
- **Block Rating (1-5):** `5 [Relação direta com LiveLike, experiência comprovada de integração, OIDC padrão compatível. Enorme mitigador de risco.]`

---

## 3. Scalability & Peak Performance
*Focus on ability to handle World Cup registration and authentication spikes.*

**Peak Capacity:**
- [ ] **Stated Peak Capacity (req/sec or req/min):** `[Awaiting Proposal — solicitado por Rodrigo: "if you can also send examples of those peaks that you're used to work with in numbers" (00:29:39)]`
- [ ] **Evidence / Load Test Results Provided?** (Yes/No): `Não — prometido na proposta`
- [ ] **Can Handle 100k+ req/min for Auth?** (Yes/No): `[Awaiting Proposal]`
- [x] **Strategy for Millions of Account Creations in Minutes:**
  > `Ben Hayward: "autoscaling is a fundamental feature of the sports-specific SSO piece, designed for automatic scalability during match peak periods" (00:28:43). Ciaran Fisher referenciou Six Nations como exemplo de picos extremos ("the traffic graph looks like a cliff") (00:29:39).`

**Infrastructure Resilience:**
- [x] **Auto-Scaling Configured?** (Yes/No): `Sim — "automatic scalability for peak periods around matches is absolutely fundamental to the product" (Ben Hayward, 00:28:43)`
- [ ] **Warm-Up / Pre-Scaling Plan for Launch Day?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Multi-AZ / Multi-Region Redundancy?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Rate Limiting & Abuse Protection?** (Yes/No): `Sim parcial — bot detection mencionado (Jack Carter, 00:26:34)`

**Reference Evidence:**
- [ ] **Largest B2C Auth Deployment (Users):** `[Awaiting Proposal — clientes mencionados: Arsenal, Liverpool "multiple millions and billions some would say" (Sharon, 00:25:23)]`
- [ ] **Highest Concurrent Auth Events Handled:** `[Awaiting Proposal — Six Nations referenciado como caso de pico extremo]`

- **Observations:**
  > `Auto-scaling apresentado como core do produto, não add-on. Clientes de Premier League (Arsenal, Liverpool) sugerem experiência com audiências globais massivas. Referência específica ao Six Nations (rugby) com padrão de pico tipo "cliff" similar à Copa. PORÉM: zero dados numéricos concretos até agora. Rodrigo solicitou métricas de peak nos clientes — Cortex confirmou que enviará. Fundamental avaliar os números na proposta.`
- **Block Rating (1-5):** `3 [Auto-scaling como core, referências fortes (Premier League, Six Nations), mas ZERO números concretos. Aguardando evidências.]`

---

## 4. Security, LGPD & Compliance
*Focus on data protection, PII handling, and Brazilian regulatory compliance.*

**Data Protection:**
- [ ] **LGPD Compliant?** (Yes/No): `[Awaiting Proposal — não discutido no call]`
- [ ] **PII Stored in Brazil?** (Yes/No): `[Awaiting Proposal — ⚠️ Cortex é empresa UK. Questão crítica para LGPD]`
- [ ] **Data Processing Agreement (DPA) Provided?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Encryption at Rest?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Encryption in Transit (TLS)?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Credential Hashing Algorithm:** `[Awaiting Proposal]`

**Security Posture:**
- [ ] **Certifications (ISO 27001, SOC 2, etc.):** `[Awaiting Proposal]`
- [ ] **Penetration Test Reports Available?** (Yes/No): `[Awaiting Proposal]`
- [ ] **WAF / DDoS Protection?** (Yes/No): `[Awaiting Proposal]`
- [x] **MFA Support Available?** (Yes/No): `Sim — "we invest really heavily in security... largely around multifactor authentication. It comes at no extra cost... rolled out to all our customers" (Jack Carter, 00:26:34)`
- [x] **Brute-Force / Account Takeover Protection?** (Yes/No): `Sim — bot detection + password security recommendations mencionados (Jack Carter, 00:27:28)`

**Age Verification & Consent:**
- [x] **Age Verification Mechanism?** (Yes/No): `Sim — separação de junior accounts (13-18) com relação a guardian: "we handle junior accounts separate from adults accounts... those aged between 13 to 18 have a relationship with the guardian" (Jack Carter, 00:26:34)`
- [x] **Parental Consent Flow for Minors (13+)?** (Yes/No): `Sim — "separate profiles" com vínculo a responsável`
- [ ] **LGPD-Specific Consent Audit Trail?** (Yes/No): `[Awaiting Proposal]`

- **Observations:**
  > `✅ MFA incluso sem custo extra para TODOS os clientes — posição forte de segurança. Bot detection e recomendações de senha segura como features nativas. Junior accounts com vínculo a guardian é feature diferenciada e alinhada com a necessidade legal (13+). ⚠️ PORÉM: LGPD não foi discutida. Como empresa UK operando SaaS, a residência dos dados é questão CRÍTICA. Precisa confirmar se PII pode ser armazenado no Brasil ou se existe DPA adequado. Certificações de segurança não mencionadas.`
- **Block Rating (1-5):** `3 [MFA, bot detection e junior accounts são pontos fortes. LGPD e residência de dados são lacunas CRÍTICAS a serem validadas na proposta.]`

---

## 5. Data Ownership, Access & Portability
*Focus on ensuring CazéTV retains full ownership and control of user identity data.*

**Ownership:**
- [ ] **All User Data 100% Owned by CazéTV?** (Yes/No): `[Awaiting Proposal — não houve declaração explícita de ownership]`
- [ ] **Any Restrictions on Data Usage?** (Yes/No): `[Awaiting Proposal]`

**Access:**
- [ ] **Direct Database Access Provided?** (Yes/No): `Provavelmente NÃO — modelo SaaS gerenciado pela Cortex`
- [x] **Admin Dashboard for User Management?** (Yes/No): `Sim — Ben: "we can show you the login dashboard. You can see all the different tools that you get access to. You have full control to change things whenever you want to" (00:23:18)`
- [ ] **APIs for Data Extraction?** (Yes/No): `[Awaiting Proposal]`

**Exit Scenario:**
- [x] **Full Data Export Guaranteed on Contract End?** (Yes/No): `Sim — Ciaran: "at the end of the tournament, you've got options. We can turn it off and export the data all to you or we can continue based on the license fee" (00:22:20)`
- [ ] **Migration Assistance Included?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Lock-In Risk Assessment:**
  > `⚠️ Modelo SaaS = sistema gerenciado e hospedado pela Cortex. Dados exportáveis no término, mas o sistema em si NÃO é transferido. Não há código-fonte entregue — é licenciamento. Se o contrato acabar, perde-se a plataforma mas mantém-se os dados. Lock-in de plataforma existe por natureza do modelo SaaS.`

- **Observations:**
  > `Dashboard de admin com controle total confirmado. Export de dados no término confirmado. Porém, por ser SaaS, não há entrega de código-fonte ou infraestrutura — o lock-in é de plataforma, não de dados. Aceitável se os dados forem portáveis e houver APIs para extração.`
- **Block Rating (1-5):** `3 [Export confirmado e admin dashboard. Lock-in de plataforma SaaS é trade-off aceitável mas precisa de APIs e garantias formais.]`

---

## 6. Extensibility & Identity Federation
*Focus on future-proofing the architecture for sponsor integration.*

- [x] **Supports Multiple Identity Providers (IdPs)?** (Yes/No): `Sim — account linking feature`
- [x] **Can Add Sponsor as Secondary IdP Without Refactoring?** (Yes/No): `Sim — Ben Hayward descreveu account linking: "we have that functionality... commonly used in sports for linking retail, ticketing accounts... you can link a DoorDash account ID to somebody's SSO profile" (00:05:40)`
- [x] **Identity Federation Strategy Described?** (Yes/No): `Sim`
  > `Cortex propõe SSO independente com "account linking": cada sponsor recebe um link de ID único ao perfil SSO do usuário. Permite acumular dados de múltiplos sponsors e eventos ao longo do tempo. Sharon Tuff enfatizou reuso do SSO: "you can roll from Football World Cup to Women's Football World Cup to Olympics to European sport" (00:04:48). Ben: "over time you build up an incredibly rich profile with all of their different linked accounts across your different sponsors" (00:05:40).`
- [x] **Account Linking (Social → Sponsor) Supported?** (Yes/No): `Sim — core feature da plataforma`
- [ ] **Custom Claims / Attributes Extensible?** (Yes/No): `[Awaiting Proposal]`

**Additional Feature — Entitlements:**
- [x] **Entitlements / Tier-Based Access Gating?** (Yes/No): `Sim — Sharon: "we have something called entitlements which enables you to gate certain privileges, certain access rights to certain spaces and content based on the rights that they're granted" (00:27:28). Pode ser usado para tiers premium vs base.`

- **Observations:**
  > `🔥 PONTO FORTÍSSIMO: Account linking é um diferencial competitivo claro de Cortex. Permite: (1) SSO independente sem depender do sponsor, (2) linking de IDs de sponsors ao perfil CazéTV, (3) construção progressiva de perfis ricos, (4) reuso do SSO em múltiplos eventos. Exatamente o que o brief pede em "extensible architecture for future identity federation." O sistema de entitlements pode servir para gating de ligas premium, embora isso possa sobrepor com funcionalidades da LiveLike.`
- **Block Rating (1-5):** `5 [Account linking é exatamente o que o brief exige. Feature nativa, comprovada em esportes, com extensibilidade cross-evento.]`

---

## 7. Operational Support & SLA
*Focus on ongoing reliability during World Cup operations.*

**SLA Commitments:**
- [ ] **Uptime SLA (%):** `[Awaiting Proposal]`
- [ ] **P1 Incident Response Time:** `[Awaiting Proposal — Rodrigo pediu "really fast SLAs" para dias de jogo (00:25:23)]`
- [ ] **P2 Incident Response Time:** `[Awaiting Proposal]`
- [ ] **24/7 Monitoring Included?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Proactive Alerting?** (Yes/No): `[Awaiting Proposal]`

**Support Structure:**
- [ ] **Dedicated Support Team?** (Yes/No): `[Awaiting Proposal]`
- [ ] **War-Room During Match Days?** (Yes/No): `[Awaiting Proposal — Rodrigo enfatizou necessidade de suporte nos "key points" dos jogos]`
- [ ] **Portuguese-Speaking Support?** (Yes/No): `[Awaiting Proposal — Cortex é UK-based, equipe do call é anglófona]`
- [ ] **Local Presence in Brazil?** (Yes/No): `Provavelmente NÃO — empresa UK`

**Maintenance:**
- [ ] **Security Patches Included in Contract?** (Yes/No): `[Awaiting Proposal — SaaS model sugere que sim]`
- [ ] **Scheduled Maintenance Windows Defined?** (Yes/No): `[Awaiting Proposal]`

- **Observations:**
  > `⚠️ LACUNA GRANDE: Nenhum SLA concreto foi discutido no call. Rodrigo pediu SLAs rápidos para dias de jogo, mas Cortex apenas disse "we can look into that as part of the proposal" (Jack, 00:25:23). Modelo SaaS sugere manutenção incluída, mas nada confirmado. ⚠️ Sem presença local no Brasil e sem suporte em português — diferença de fuso (4h) pode ser mitigação parcial, mas precisa solução para games noturnos/madrugada.`
- **Block Rating (1-5):** `2 [Zero SLAs definidos. Sem presença local ou suporte em português. Totalmente pendente da proposta.]`

---

## 8. Registration & User Experience
*Focus on the end-user registration and login flow.*

**Registration Flow:**
- [ ] **Frictionless Registration? (Minimal Fields)**  (Yes/No): `[Awaiting Proposal — micro-site mencionado mas UX não detalhada]`
- [ ] **Email Verification Flow?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Password Recovery / Reset Flow?** (Yes/No): `Parcial — Jack mencionou "password changes" e "recommend stronger passwords" (00:27:28)`
- [ ] **Account Deduplication Strategy?** (Yes/No): `[Awaiting Proposal]`

**User Management:**
- [ ] **Self-Service Profile Edit?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Account Deletion (LGPD Right)?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Session Management (Multi-Device)?** (Yes/No): `[Awaiting Proposal]`

**Deployment Model:**
- [x] **Micro-Site (Quick Deploy)?** (Yes/No): `Sim — solução recomendada para o prazo: "quick to deploy micro-site... can be branded, customized from our end" (Ciaran, 00:10:05)`
- [x] **Upgrade Path to Custom Front-End?** (Yes/No): `Sim — "it does allow you to upgrade to a fully-fledged bespoke front end at some point in the future... you don't have to refactor everything" (Ben, 00:11:13)`

**User Flow (Embedded in App):**
> Ciaran descreveu: User abre seção de predictor no app → "Hey, you need to log in" → direcionado ao browser para login → browser retorna ao app com token de autenticação (00:13:26). Arsenal app referenciado como exemplo.

- **Observations:**
  > `Micro-site como MVP é pragmático para o prazo. Upgrade path sem refatoração é bom sinal de arquitetura. UX de login via browser redirect é padrão OIDC mas pode criar fricção — precisa avaliar experiência real. Customização de opt-ins por marca/sponsor confirmada. Arsenal app prometido como exemplo de referência. Preferências e opt-ins customizáveis.`
- **Block Rating (1-5):** `3 [Micro-site pragmático. Upgrade path confirmado. UX detalhada pendente. Arsenal como referência a avaliar.]`

---

## 9. Documentation & Knowledge Transfer
*Focus on ensuring no vendor lock-in through complete documentation.*

- [ ] **Full Architecture Documentation Provided?** (Yes/No): `Não — Rodrigo pediu no brief. Sharon questionou o que exatamente era desejado. Ciaran esclareceu que por ser SaaS, a "arquitetura" é gerenciada pela Cortex (00:21:10).`
- [ ] **API Documentation Provided?** (Yes/No): `[Awaiting Proposal — Ciaran: "we can point some documentation around that as well for those third parties" (00:10:05)]`
- [ ] **Runbook / Ops Documentation?** (Yes/No): `[Awaiting Proposal — N/A se SaaS gerenciado]`
- [ ] **Knowledge Transfer Sessions Included?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Source Code Delivered (if custom)?** (Yes/No): `NÃO — modelo SaaS, código é propriedade da Cortex`

- **Observations:**
  > `Como SaaS, não há entrega de código-fonte ou arquitetura interna — o que muda a expectativa do brief. A documentação relevante é a documentação de APIs de integração (para LiveLike e futuras integrações), não a arquitetura interna. Cortex prometeu documentação de OIDC para third-party integration.`
- **Block Rating (1-5):** `3 [Modelo SaaS redefine a expectativa de documentação. API docs prometida. Source code N/A.]`

---

## 10. Timeline & Delivery
*Focus on ability to meet the aggressive delivery window.*

- [ ] **Proposed Kick-Off Date:** `[Awaiting Proposal — "as soon as possible"]`
- [ ] **Proposed Go-Live Date:** `[Awaiting Proposal — target May 11, 2026]`
- [ ] **LiveLike Integration Complete By:** `[Awaiting Proposal]`
- [ ] **Timeline Breakdown Provided?** (Yes/No): `Não — prometido na proposta: "we'll hone in on project timelines" (Jack, 00:30:39)`

**Milestone Plan:**
| Phase | Description | Duration | Date |
|---|---|---|---|
| Kick-Off | `[Awaiting Proposal]` | `[ ]` | `[ ]` |
| Development | Micro-site deploy + branding | `Ciaran: "relatively quick to spin up"` | `[ ]` |
| Integration & Testing | LiveLike OIDC handshake | `[ ]` | `[ ]` |
| Go-Live | `Target` | `[ ]` | `May 11, 2026` |

**Key Dependencies Identified:**
1. Domínio onde o SSO será hospedado (Ciaran, 00:10:05)
2. Decisão sobre sponsor (impacta account linking)
3. Integração com LiveLike

- **Observations:**
  > `Ciaran indicou que o micro-site é rápido de deployar e a integração OIDC é "relatively quick to spin up" para terceiros como LiveLike. A principal dependência do lado CazéTV é a definição do domínio. O fato de Cortex já ter relação com LiveLike acelera a integração. Timeline detalhado prometido na proposta — CRÍTICO avaliar se May 11 é viável.`
- **Block Rating (1-5):** `3 [Indicações positivas de velocidade, mas zero números concretos. Timeline prometido na proposta. May 11 target.]`

---

## 11. Commercial, Contractual & Financial
*Focus on cost structure, payment terms, and financial predictability.*

**Cost Structure:**
- [ ] **Implementation Cost (Phase 1):** `[Awaiting Proposal]`
- [ ] **Monthly Operations Cost (Phase 2):** `[Awaiting Proposal]`
- [ ] **Pricing Model:** `Annualized license fee — Sharon: "it's an annualized license fee... we typically trade in increments: three years, five years. We can look at year-long terms" (00:22:20)`

**Cost Variability:**
- [ ] **Costs Increase with User Volume?** (Yes/No): `Possível — Jack pediu confirmação de 15M profiles para definir tiers: "we'll put some tiers in so you can know how it would scale" (00:30:39)`
- [ ] **Costs Increase with Auth Request Volume?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Hidden Costs Identified:** `MFA incluso sem custo extra. Demais custos [Awaiting Proposal].`

**Contract Terms:**
- [ ] **Minimum Contract Duration (Months):** `[Awaiting Proposal — modelo preferencial é multi-year (3-5 anos), mas year-long é possível]`
- [ ] **Early Termination Penalties?** (Yes/No): `[Awaiting Proposal]`
- [ ] **Payment Terms:** `[Awaiting Proposal]`

- **Observations:**
  > `Modelo de licença anualizada com preferência para multi-year (3-5 anos). Sharon enfatizou a construção de business case para manter o SSO cross-events. Jack mencionará tiers de pricing baseados no volume de profiles (15M+). MFA sem custo extra é diferencial. Custos de implementação (Phase 1) vs operação (Phase 2) prometidos separados na proposta — alinhado com o que o brief pede.`
- **Block Rating (1-5):** `2 [Zero números. Modelo de licença claro mas sem valores. Totalmente pendente da proposta.]`

---

## 12. Team, Experience & References
*Focus on supplier maturity in identity/auth at scale.*

- [ ] **Years in Market:** `[Awaiting Proposal]`
- [x] **B2C Identity System Cases at Scale:** `Sim — Premier League clubs (Arsenal, Liverpool mencionados diretamente). Six Nations (rugby). "Top tier Premier League club kind of data with their global audiences" (Sharon, 00:25:23)`
- [ ] **Largest Auth Deployment (Users):** `[Awaiting Proposal — prometido: "examples of live work" + escalas numéricas]`
- [x] **Sports / Entertainment / Media Cases?** (Yes/No): `Sim`
  > `Posicionamento 100% esportivo. Arsenal app referenciado como exemplo concreto de SSO integration. Liverpool mencionado. Six Nations (rugby) como caso de pico de tráfego. "We are sports-specific. Ultimately everything we build is sport-specific" (Ben, 00:28:43). Jack Carter mencionou ter vivido no Brasil — conhecimento cultural do mercado.`
- [ ] **Reference Contacts Provided?** (Yes/No): `Não — Jack prometeu "apps that you can use to see the experience itself" + "examples of live work" (00:30:39)`
- [ ] **Team Size Dedicated to This Project:** `[Awaiting Proposal]`

**Team on Call:**
| Name | Role (Inferred) |
|---|---|
| Jack Carter | Commercial / Account Lead |
| Sharon Tuff | Business Development / Strategic Sales |
| Ben Hayward | Product / Solution Specialist |
| Ciaran Fisher | Technical Lead / CTO |

- **Observations:**
  > `✅ PONTO FORTE: Cortex é 100% sports-specific. Não é um fornecedor genérico de IAM tentando adaptar ao contexto esportivo — o produto foi construído para esporte. Referências Premier League (Arsenal, Liverpool) e Six Nations demonstram experiência com audiências massivas em contexto esportivo. Equipe de 4 pessoas no call com roles complementares. Jack mencionou experiência pessoal no Brasil. Arsenal app + exemplos de trabalho ao vivo prometidos como evidência concreta.`
- **Block Rating (1-5):** `4 [100% sports-specific, Premier League clients, experiência com picos esportivos. Dados numéricos pendentes. Melhor fit setorial entre os candidatos.]`

---

# Executive Summary & Recommendation

## Block Ratings Summary
| Block | Rating | Status |
| :--- | :--- | :--- |
| 1. Architecture & Technical Solution | **3/5** | OIDC confirmado, stack details pending |
| 2. LiveLike Integration & Handshake | **5/5** | ✅ Relação direta com LiveLike, integração comprovada |
| 3. Scalability & Peak Performance | **3/5** | Auto-scaling core, zero data points yet |
| 4. Security, LGPD & Compliance | **3/5** | MFA + junior accounts. LGPD/residency critical gap |
| 5. Data Ownership, Access & Portability | **3/5** | Export + dashboard confirmed. SaaS lock-in trade-off |
| 6. Extensibility & Identity Federation | **5/5** | ✅ Account linking = exactly what the brief requires |
| 7. Operational Support & SLA | **2/5** | ⚠️ Zero SLAs, no local presence, no PT support |
| 8. Registration & User Experience | **3/5** | Micro-site pragmatic, UX details pending |
| 9. Documentation & Knowledge Transfer | **3/5** | SaaS reframes expectations. API docs promised |
| 10. Timeline & Delivery | **3/5** | Positive signals, zero concrete dates |
| 11. Commercial, Contractual & Financial | **2/5** | ⚠️ Zero numbers, license model only |
| 12. Team, Experience & References | **4/5** | ✅ 100% sports-specific, Premier League clients |
| **Average (all blocks)** | **3.25/5** | **Based on intro call only — proposal pending** |

## Automated Risk Flags
| Category | Flag Condition | Risk Level | Alert |
| :--- | :--- | :--- | :--- |
| **LGPD** | `pii_stored_in_brazil` == [Unknown] | **CRITICAL** | "UK-based SaaS — PII residency not confirmed for Brazil." |
| **SLA** | `sla_defined` == No | **HIGH** | "Zero SLAs defined. P1 response time unknown." |
| **Local Support** | `local_presence_brazil` == No | **HIGH** | "No Portuguese support. No local team. 4h timezone gap." |
| **Numbers** | `peak_capacity_evidence` == None | **HIGH** | "Auto-scaling claimed but zero numerical evidence." |
| **Commercial** | `pricing_provided` == No | **MEDIUM** | "No costs shared yet. License model only." |

## Key Strengths
| Strength Area | Rating | Description |
| :--- | :--- | :--- |
| **LiveLike Integration** | ⭐⭐⭐⭐⭐ | Already working with LiveLike on another project. Lowest integration risk possible. |
| **Account Linking / Federation** | ⭐⭐⭐⭐⭐ | Exact match with brief requirement for sponsor IdP without refactoring. |
| **Sports-Specific DNA** | ⭐⭐⭐⭐ | 100% built for sport. Premier League, Six Nations. Understands match-day peaks. |
| **Junior Accounts** | ⭐⭐⭐⭐ | Built-in 13+ flow with guardian linking. Unique differentiator. |
| **MFA at No Extra Cost** | ⭐⭐⭐ | Security baseline included for all customers. |

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| **LGPD / Data Residency** | **⚠️ CRITICAL** | UK-based SaaS. PII storage location unknown. LGPD compliance not discussed. Must clarify in proposal. |
| **SLA / Operational Support** | **HIGH** | Zero SLAs, no local presence, no Portuguese. For Copa, need support during BR match times. |
| **No Numbers Yet** | **HIGH** | All performance claims are qualitative. Zero load test results, zero peak req/sec data. |
| **No Commercial Terms** | **HIGH** | No pricing shared. License model could be expensive for 15M+ profiles. |
| **SaaS Lock-In** | **MEDIUM** | Platform dependency inherent to SaaS. Data exportable but system not transferable. |

## What Must Be in the Proposal (Critical Items)
1. ☐ **LGPD compliance** — PII storage location, DPA, data residency guarantees
2. ☐ **Peak capacity numbers** — actual req/sec from Premier League and Six Nations deployments
3. ☐ **SLA model** — uptime %, P1/P2 response times, match-day coverage plan
4. ☐ **Pricing** — implementation + annual license, tiered by user volume
5. ☐ **Timeline** — kick-off to May 11 go-live with milestones
6. ☐ **LiveLike handshake plan** — specific integration steps and duration
7. ☐ **Data export format** — what exactly is exported on exit

## Final Recommendation
**⏳ HOLD — Awaiting Proposal (Strong Initial Impression)**

Cortex presents the **best strategic fit** of any SSO supplier evaluated so far:
- **Existing LiveLike relationship** (was on a call with LiveLike for another client the same day) → dramatically reduces integration risk
- **Account linking** = exactly what the brief requires for sponsor federation
- **100% sports-specific** → understands match-day peaks, junior accounts, entitlements

However, the intro call was qualitative only. **Critical gaps remain** in LGPD compliance (UK company + Brazilian PII), SLA commitments, performance data, and pricing. These **must** be addressed in the proposal expected by **April 11** before any recommendation can be made.

**Next Steps:**
- Receive proposal by Friday April 11
- Follow-up call: Monday April 14, 1 PM BRT / 5 PM BST
- Re-evaluate with complete data
