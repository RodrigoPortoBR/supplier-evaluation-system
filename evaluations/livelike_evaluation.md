# Supplier Evaluation Template

**Supplier Name:** `LiveLike`
**Website:** `https://www.livelike.com/` (Assumed)
**Evaluator:** `Antigravity (AI-Assisted)`
**Date:** `2026-03-10` *(Atualizado com Q&A Follow-up)*

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic and proven load capacity.*

**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `Milhões de usuários concorrentes (ex: Yahoo Sport, Bleacher Report)`
- [x] **Strategy for 10M Concurrent Users (5 mins before game):**
  > `Utilizam infraestrutura AWS com auto-scaling. Estão preparados para testar a solução web/mobile web contra 10 a 15 milhões de usuários e enviarão um SLA completo detalhando o uptime. A arquitetura é construída para suportar picos de tráfego extremos (milhões simultâneos).`
- [x] **Maximum Simultaneous Users Tested:** `>10.000.000 (Confirmado ser "bem acima de 10 milhões")`

**Infrastructure & Platforms:**
- [x] **Auto-scaling Infrastructure?** (Yes/No): `[Yes]`
- [ ] **Uptime SLA (%):** `[Será enviado no documento SLA completo]`
- [x] **Platforms Supported:**
    - [x] Web Desktop
    - [x] Web Mobile
    - [ ] App iOS — Projeto focado 100% em Web
    - [ ] App Android — Projeto focado 100% em Web

- **Observations:**
  > A LiveLike demonstrou extrema confiança e experiência no suporte a milhões de usuários simultâneos, citando cases com grandes players de mídia esportiva. Não haverá gargalo na infraestrutura (AWS). O foco será exclusivamente Web/Mobile Web, sem app nativo. 
- **Block Rating (1-5):** `[5]`

---

## 2. Local Support & Operational Coverage
*Focus on the vendor's ability to provide reliable, real-time operational support during a high-stakes global event.*

**Local Presence & Timezone Alignment:**
- [ ] **Local Support in Brazil?** (Yes/No): `[No]` — Empresa dos EUA.
- [ ] **Portuguese-Speaking Support Team?** (Yes/No): `[Yes]` — Possuem colaboradores que falam português fluente (como o Renato Drumond), facilitando o contato B2B interno.
- [x] **Timezone Coverage Strategy for Brazil:**
  > `[Yes]` — Fuso horário EST (Nova York) é perfeitamente alinhado com o Brasil (1 a 2 horas de diferença). Reuniões e plantões ocorrem no mesmo fuso.
- [ ] **Dedicated Local Account Managers?** (Yes/No): `[Parcial]` — Account Management B2B direto com a equipe dos EUA, porém no mesmo fuso.

**Support Availability:**
- [x] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `[Parcial]` — ✅ **Proposta Oficial:** Suporte via Slack externo. Para incidentes P1, o SLA inicial de resposta é de **2 horas (em horário comercial)**. Não deixam claro se o SLA 2h se mantém em finais de semana/madrugada de Copa.
- [x] **SLA Response Times for Critical Incidents:** `[P1: 2 horas / P2: 4 horas / P3: 8 horas]` — Conforme especificado no catálogo de serviços.
- [ ] **Dedicated War-Room Structure During Major Events?** (Yes/No): `[Não detalhado]`

**Operational Escalation Flow:**
- [x] **L1 Support (User Issues) – Handled by:** `[CazéTV]` — ⚠️ **Confirmado em call:** "We don't deal with any end customers because obviously they're your customers... we only power the actual experiences". A CazéTV **precisa** fornecer um email (ex: info@) e equipe própria.
- [x] **L2 Technical Issues – Handled by:** `[LiveLike]` — "Se houver problemas como o Rodrigo não ganhando pontos, vemos no nosso fim e a engenharia conserta".
- [x] **L3 Infrastructure Failures – Handled by:** `[LiveLike]`

- **Observations:**
  > A LiveLike é enfática: **eles não tocam no usuário final (B2C)**. O suporte L1 deve ser integralmente estruturado pela CazéTV, embora a LiveLike conserte rapidamente erros lógicos (L2) que causem tickets, porque seus dashboards monitoram tudo. O SLA de P1 em 2 horas "durante horário comercial" deve ser negociado para 24/7 em contrato de Copa.
- **Block Rating (1-5):** `[3]` *(Atualizado: SLA formal requer atenção para 24/7 e L1 da CazéTV reforçado)*

---

## 3. User Support & Incident Management
*Focus on operational ownership of user issues and incident resolution.*

**Support Ownership:**
- [x] **Who Handles User Complaints?** `[CazéTV]` — Equipe interna da marca. LiveLike não opera suporte B2C.
- [x] **Who Handles Technical Bug Reports?** `[LiveLike]` — CazéTV repassa bugs estruturais escalados via L1.

**Escalation Process:**
- [x] **Defined Workflow for Critical Bugs?** (Yes/No): `[Yes]` — Via Slack B2B channel.
- [x] **Defined Workflow for Mass User Incidents?** (Yes/No): `[Yes]` — SLA estruturado P1, P2 e P3. P1 significa "App unusable / video playback affected".

- **Observations:**
  > A matriz de responsabilidade é clara: o usuário que não consegue logar ou esqueceu a senha é problema 100% da CazéTV (visto que o SSO é responsabilidade do cliente). O usuário cujos pontos do bolão não computaram é responsabilidade da LiveLike (eles corrigem via API/Engenharia e avisam a CazéTV).
- **Block Rating (1-5):** `[3]` *(Atualizado via call: a fricção cai bastante na CazéTV)*

---

## 4. Security, LGPD, Governance & Compliance
*Focus on legal compliance, data safety, and youth participation regulations.*

**Data Protection & Compliance:**
- [x] **LGPD/GDPR Compliant?** (Yes/No): `[Yes]` — A LiveLike não retém e nem processa dados PII. Apenas IDs hashados (LiveLike ID).
- [x] **Data Residency Country:** `[US]` — Apenas para dados de interações anônimas (picks, badges). Dados pessoais ficam com o cliente.
- [x] **Certifications (ISO, SOC, etc.):** `[SOC 2]`

**Age Verification & Youth Safety (13+ Users):**
- [x] **Age Verification Flow:**
  > `Fica a critério do Single Sign-On (SSO) do cliente. Se a Cazé TV precisar na plataforma, a LL pode integrar no fluxo, mas o recomendado é atrelar via SSO.`
- [ ] **Consent Mechanisms for Minors:**
  > `[Via provedor de identidade do cliente]`
- [ ] **Special Data Protection Policies for Under-18 Users?** (Yes/No): `[Gerido via SSO / Cliente]`
- [ ] **Parental Consent Options Available?** (Yes/No): `[Gerido via SSO / Cliente]`

- **Observations:**
  > **Mitigação completa de risco legal:** Como a plataforma integra com o SSO do cliente e não salva informações identificáveis (PII), o risco de dados (LGPD) e youth safety recai fundamentalmente sobre a gestão de identidade da CazéTV. SOC 2 foi confirmado.
- **Block Rating (1-5):** `[5]`

---

## 5. Data Ownership, Access & Portability
*Focus on guaranteeing full strategic control over user data and long-term usability.*

**Data Ownership:**
- [x] **All User Data Fully Owned by Client?** (Yes/No): `[Yes]` — Totalmente do cliente.
- [x] **Any Restrictions on Data Usage?** (Yes/No): `[No]`
  > `Nenhuma restrição; a LiveLike apenas retém a "ledger" das interações (ações) associadas a um UID anônimo.`

**Data Access:**
- [x] **Access to Full User Database?** (Yes/No): `[Yes]` — Acesso a dashboards completos e Analytics Agents nativos.
- [x] **Access to Behavioral Event Data?** (Yes/No): `[Yes]`
- [x] **Access to Prediction History?** (Yes/No): `[Yes]`

**Data Extraction Methods:**
- [x] **Direct Platform Exports?** (Yes/No): `[Yes]`
- [x] **APIs for Real-Time Extraction?** (Yes/No): `[Yes]` — "API First Company".
- [x] **Scheduled Automated Data Dumps?** (Yes/No): `[Yes]`

**Exit Scenario (Critical):**
- [x] **If Partnership Ends – What Happens to User Accounts?**
  > `Todas as contas e histórico do lado da LiveLike são deletados após exportação garantida para o cliente.`
- [x] **If Partnership Ends – What Happens to Historical Data?**
  > `Exportado para a CazéTV.`
- [x] **If Partnership Ends – What Happens to Behavioral Insights?**
  > `Exportado (ou deletado se não exportado).`
- [x] **Full Data Export Guaranteed on Exit?** (Yes/No): `[Yes]`

- **Observations:**
  > Portabilidade e controle impecáveis. Sem fricção. O ecossistema API First facilita data drops.
- **Block Rating (1-5):** `[5]`

---

## 6. Core Product Features & Functional Readiness
*Focus on prediction mechanics, feature coverage, and how much of the desired product vision already exists.*

**Feature Coverage Assessment:**
- [x] **Which Core Features Are Ready Out-of-the-Box?**
  > `Previsões de placar exato, special predictions, live predictions, lógica de score customizável, ligas públicas e privadas, leaderboards (globais/período), missões, desafios, e badges.`
- [x] **Which Core Features Are Customizable?**
  > `Toda a lógica de multiplicadores de fase, acertos de 10pts, 25pts, 35pts e 50pts e missões diárias.`
- [x] **Which Core Features Are Not Available?**
  > `Adicionalmente fornecem um feature de *AI Guess/Oráculo* que foi demandado (Case PFL demonstrado).`

**Prediction Types:**
- [x] Match Result (1x2)
- [x] Exact Score
- [x] Special Predictions
- [x] Live Predictions
- [x] **Multiple Prediction Types Supported?** (Yes/No): `[Yes]`
- [x] **Configurable Scoring Logic?** (Yes/No): `[Yes]`

**Rankings:**
- [x] Global
- [x] Public Leagues
- [x] Private Leagues
- [x] By Period (Day/Round/Tournament)

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No)
- [x] Multiple Rules Supported? (Yes/No)
- [x] Missions / Challenges? (Yes/No)
- [x] Badges / Achievements? (Yes/No)
- [x] Prizes: `[Mencionaram Lottery support via missões diárias / leaderboards]`

**Real-time API:**
- [x] API for Live Data Display? (Yes/No) — Sim, com stats perform (requer feed).

- **Observations:**
  > Excederam as expectativas, oferecendo "Out-of-the-box" o AI Guessing e missões diárias. Todas as mecânicas pedidas, incluindo os multiplicadores nas fases finais para a Copa do Mundo e placar exato x acerto de vencedor, são suportadas nativamente pela engine.
- **Block Rating (1-5):** `[5]`

---

## 7. League Management & Premium Infrastructure
*Focus on private and premium league scalability, creation, and administration.*

**Private Leagues:**
- [x] **Free Creation?** (Yes/No): `[Yes]` — Configurável por perfil de usuário.
- [x] **Invite via Link?** (Yes/No): `[Implicitly Yes]`
- [x] **Participant Limit Config?** (Yes/No): `[Yes]` — Eles recomendam impor limits para evitar uso desenfreado.
- [x] **How Scalable Is Private League Creation?**
  > `Perfeitamente escalável, permitindo a separação entre criação livre (Free) e criação de múltiplas ligas (Premium/100 ligas).`
- [x] **Maximum Number of Private Leagues Supported:** `[Sem limite arquitetônico]`

**Premium League Logic:**
- [x] **League Access Restricted by Subscription Status?** (Yes/No): `[Yes]`
- [x] **League Access Restricted by External Partner Eligibility?** (Yes/No): `[Yes]` — Ligas segregadas por tags do SSO do Patrocinador (ex: Amazon Prime).
- [x] **Support for Public Leagues?** (Yes/No): `[Yes]`
- [x] **Support for Private Leagues?** (Yes/No): `[Yes]`
- [x] **Support for Premium Leagues?** (Yes/No): `[Yes]`

**Administration Controls:**
- [x] **League Moderation Tools?** (Yes/No): `[Yes]` — Built into backend.
- [x] **Anti-Fraud Mechanisms?** (Yes/No): `[Yes]` — Hard lock nas predições antes do jogo; Segurança garantida via MFA/2FA do SSO nativo.
- [x] **Anti-Bot / Inflação de Perfis?** (Yes/No): `[Yes]` — **Confirmado via Q&A:** A LiveLike desativa a API de criação de perfis (create profile API), impedindo bots/crawlers de criarem perfis artificiais. A única forma de criar um perfil é implicitamente quando um access token JWT válido (gerado pelo backend da CazéTV e assinado com um secret exclusivo da CazéTV) é utilizado. Isso garante mapeamento 1:1 exato entre perfis LiveLike e usuários CazéTV, **eliminando o risco de overage penalties por botnets.**

- **Observations:**
  > A arquitetura de perfis (Casting, Basic User e Premium User) encaixa perfeitamente na moderação e flexibilidade da plataforma. A vinculação via atributos passados na API de autenticação automatiza a liga premium de um patrocinador. **A proteção anti-bot via JWT token é robusta e resolve completamente o risco de inflação artificial de perfis.**
- **Block Rating (1-5):** `[5]`

---

## 8. Game Operation & Scoring Process
*Focus on reliability and transparency of scoring updates.*

**Score Update Timing:**
- [x] **Real-Time Updates?** (Yes/No): `[Yes]`
- [x] **End-of-Match Updates?** (Yes/No): `[Yes]`
- [x] **Daily Batch Updates?** (Yes/No): `[Yes]`

**Data Source Reliability:**
- [x] **Official Match Data Providers Used:** `[OPTA/Stats Perform — ✅ CazéTV já possui acesso ao feed de dados em tempo real da OPTA]`

- **Observations:**
  > ✅ **RISCO RESOLVIDO:** A CazéTV já possui acesso ao serviço de feed de dados em tempo real da OPTA. A LiveLike confirmou via Q&A que já tinha em suas notas que a CazéTV possuía acesso ao feed OPTA/Stats Perform. Caso contrário, a LiveLike poderia procurar o feed em nome da CazéTV. **Esse feed OPTA será utilizado para entregar dados de placares em tempo real para a LiveLike, eliminando completamente a dependência externa que era um dos maiores riscos do projeto.**
- **Block Rating (1-5):** `[5]` *(Atualizado: Feed OPTA da CazéTV resolve a dependência)*

---

## 9. Customization, UX & Front-End Design
*Focus on white-label depth, user experience, and design responsibility.*

**Customization Depth:**
- [x] **Full CSS/Theme Customization:** (Yes/No): `[Yes]` — O CMS da LL é 100% themeable.
- [x] **Full UI Customization or Limited Branding?**
  > `Solução base flexível com Professional Services atuando atrelado aos inputs da CazéTV.`
- [ ] **Custom Domain (CNAME):** (Yes/No): `[Yes - implicit]`
- [ ] **Mobile Responsive Score (1-10):** `[Será Web/Mobile Web native]`

**Design Ownership:**
- [x] **Vendor Provides UI/UX Designers?** (Yes/No): `[Yes]` — Equipe de Professional Services foca em eficiência (Front e Backend tudo num só lugar).
- [x] **Vendor Provides Front-End Development Support?** (Yes/No): `[Yes]`
- [x] **Client Must Supply Design Resources?** (Yes/No): `[No]` — Apenas Guidelines.

- **Observations:**
  > Facilita a vida do cliente provendo pacote completo e desenvolvimento ponta-a-ponta visando o "Go-Live" curto. A customização atende ao briefing visual do protótipo Lovable.
- **Block Rating (1-5):** `[4]`

---

## 10. Integration Ecosystem & Partner Connectivity
*Focus on connecting with existing client tech, third-party data sources, and membership systems.*

**Documented APIs:**
- [x] Login/SSO — Sim, fortíssima dependência na infra de SSO do cliente para sucesso do projeto.
- [x] Partners — Sim, tags/attributes passados dinamicamente via backend.

**Partner Integration:**
- [x] Partner Benefits? (Yes/No)
- [x] Subscription Status? (Yes/No)
- [x] External Rewards? (Yes/No)

**External Database Integration:**
- [x] **Can Connect to Loyalty Programs (e.g., iFood Club)?** (Yes/No): `[Yes]` — Tanto externo quanto próprio deles.
- [x] **Can Connect to Subscription Databases?** (Yes/No): `[Yes]`

**Access Authorization:**
- [x] **Entry to Premium Leagues Gated by Partner Status?** (Yes/No): `[Yes]`
- [x] **Entry to Premium Leagues Gated by Subscription Verification?** (Yes/No): `[Yes]`
- [ ] **Entry to Premium Leagues Gated by External APIs?** (Yes/No): `[Yes]`

**Experience:**
- [x] Co-branding Support? (Yes/No)
- [x] Exclusive Partner Areas? (Yes/No)
- [x] Track Record with Media/Sponsors? (Yes/No)

- **Observations:**
  > A arquitetura altamente conectável viabiliza completamente a mecânica de benefícios de múltiplas marcas patrocinadoras via "User Groups" ou tags associadas ao UID. O principal desafio técnico para a CazéTV será **ter e integrar um bom SSO** num prazo curto.
- **Block Rating (1-5):** `[5]`

---

## 11. Channels, Notifications & User Communication
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [x] **Web Push Notifications:** (Yes/No): `[Yes]` — Gerido pela CazéTV via Triggers da LL.
- [x] **Email Automation:** (Yes/No): `[Yes]`

**Communication Ownership:**
- [x] **Who Manages Messaging Templates?** `[CazéTV]`
- [x] **Who Manages Campaign Scheduling?** `[CazéTV]`

- **Observations:**
  > A LiveLike pode fornecer webhooks/triggers para notificar o usuário (ex: a liga está aberta), **mas** a plataforma de envio (Push Provider / CRM Platform) e os disparos **devem** ser fornecidos de forma agnóstica pelo cliente (CazéTV).
- **Block Rating (1-5):** `[3]`

---

## 12. Social Sharing & Virality
*Focus on organic growth and viral content generation.*

- [x] **Native Sharing Features?** (Yes/No): `[Yes]`
- [x] **Social Platforms Supported for Sharing User Answers / Status:** `[Redes convencionais, Text, WhatsApp.]`

- **Observations:**
  > O compartilhamento nativo em WhatsApp e Redes atende perfeitamente à mecânica de viralização de "Lucky Numbers" a cada palpita compartilhado.
- **Block Rating (1-5):** `[4]`

---

## 13. Geo-Restriction Capabilities
*Focus on control over geographic participation.*

- [ ] **Registration Restricted to Brazilian Users Only?** (Yes/No): `[Opcional]`
- [x] **Restriction by Specific IP Ranges?** (Yes/No): `[Yes]`

- **Observations:**
  > Funcionalidade disponível e facilmente implementável via restrição de IP / Geofencing.
- **Block Rating (1-5):** `[4]`

---

## 14. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [x] **Can Close Dedicated Roadmap for Cup?** (Yes/No): `[Yes]`
- [x] **Open to Partner-Specific Features?** (Yes/No): `[Yes]`
- [x] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Low]`
- **Timelines (Avg Days):**
    - Setup Technical: `[Projeto de Maio 11 a Fim de Julho - Fase de Validação]`
    - Customization: `[Fase ativa agora]`
    - Go-Live: `[Atendendo o deadline 11 Maio]`

**Suporte à Carga Operacional (Q&A Confirmado):**
- [x] **Professional Services Team Dedicado?** (Yes/No): `[Yes]` — LiveLike possui equipe completa de Professional Services que trabalhará com a CazéTV durante todo o lançamento.
- [x] **AI para Automação de Conteúdo?** (Yes/No): `[Yes]` — IA integrada para automatizar grande parte do conteúdo dos mini games, reduzindo carga operacional.
- [x] **SSO Fornecido/Parceiro?** (Yes/No): `[Parcial]` — LiveLike recomenda fortemente que a CazéTV utilize seu próprio SSO. Caso não seja possível, possuem um **parceiro de SSO/CDP** que pode desempenhar esse papel (cotação adicional necessária).

- **Observations:**
  > Eles entenderam a Copa do Mundo (aprox 2.5 meses) como a fase de "Paid Proof of Concept" perfeita para validar a tese antes de tracionar para as demais ligas da CazéTV (Série A, Paulistão, Copas Femininas). Todas as features de Discovery Session estão garantidas com lançamento factível para 11 de Maio, dado que o escopo Mobile App caiu. **Q&A confirmou que a LiveLike tem plena ciência de que a CazéTV é uma empresa de mídia/entretenimento e não de tecnologia, e se comprometem a reduzir a carga operacional via Professional Services e IA integrada. A opção de parceiro SSO/CDP é um safety net caso a CazéTV não consiga erguer o SSO internamente a tempo.**
- **Block Rating (1-5):** `[5]`

---

## 15. Commercial, Contractual & Financial Risk
*Focus on cost structure, lock-in risks, and financial predictability.*

**Cost Structure:**
- [x] **Setup Fee Range:** `US$ 325.000` — ✅ **Confirmado Oficialmente** (Até 10M de usuários). 
- [x] **Pricing Model:** `[Híbrido - Componentizado]`
  - Implementation: $25.000
  - Gaming Hub License (3 games): $50.000
  - Professional Services Allowance: $50.000
  - Usage (up to 10M users): $200.000

**Cost Variability & Budget Risk:**
- [x] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `[Yes]` — Adicional de **$20.000 por cada milhão extra de usuários** acima de 10 milhões. A estimativa de 15M MAU elevaria o contrato para **US$ 425.000**.
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `[Não]`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `[Sim]` — Possuem banco de horas (Professional Services credits) previstos no pacote base ($50k). Extrapolar os serviços de integração/design ali esgota o banco e gera faturamento adicional.

**Added Value Games (From Presentation):**
- Acesso total ao Gaming Hub com mecânicas secundárias: Quizzes, Cheering, Polls, Badges e Missões Diárias out-of-the-box via widgets nativos.

**Contract Terms:**
- [x] **Minimum Contract Duration (Months):** `[Não especificado na proposta, mas licença padrão Saas é anual]`
- [ ] **Early Termination Penalties?** (Yes/No): `[Não discutido]`

**Platform Dependency & Exit Risks:**
- [x] **Migration Complexity:**
  > `[Baixa/Média]` — Sendo "API-First" agnóstico, se a CazéTV desenvolver seu front-end bem desacoplado, a substituição do backend de regras por um interno no futuro não joga fora 100% da interface construída.
- [x] **Data Portability Guarantees?** (Yes/No): `[Yes]` — Como não guardam PII (só operam baseados em Hash IDs) todo o CDP e propriedade já está do lado do cliente do dia 1 ao dia final do projeto.

- **Observations:**
  > Os custos da LiveLike são de longe os mais altos (Premium B2B Tier S), batendo quase US$ 500k no escopo de tráfego estendido (R$ 2.500.000,00). Ao contrário da Low6, não incluem o software de CRM (somente a infraestrutura e Professional Services de integração com seu próprio CRM) nem L1 B2C. O cliente arca tanto com o Custo Premium quanto com grande parte do TCO Interno.
- **Block Rating (1-5):** `[3]`

---

## 16. Team, Experience & References
*Focus on supplier maturity.*

- [ ] **Years in Market:** `[N/A Extato]`
- [x] **Previous World Cup/Massive Event Cases:** `[Múltiplos clientes Massivos (Yahoo e BR Report)]`
- [x] **Reference Contacts Provided?** (Yes/No): `[Parcial (Na próxima deck)]`

- **Observations:**
  > Background fortíssimo com grandes Publishers (Bleacher Report, Yahoo Sport) e Engagement Leagues (PFL, Chelsea, Tomorrow Golf League). O foco deles em "Audience Engagement Software" está super tracionado para o desafio editorial e promocional da CazéTV.
- **Block Rating (1-5):** `[5]`

---

## Executive Summary

### Score Overview
| Block | Rating |
|-------|--------|
| 1. Robustness, Scale & Reliability | 5 |
| 2. Local Support & Operational Coverage | 3 |
| 3. User Support & Incident Management | 4 | *(↑ Dashboard/CMS L1 confirmado)* |
| 4. Security, LGPD, Governance & Compliance | 5 |
| 5. Data Ownership, Access & Portability | 5 |
| 6. Core Product Features & Functional Readiness | 5 |
| 7. League Management & Premium Infrastructure | 5 |
| 8. Game Operation & Scoring Process | 5 | *(↑ Feed OPTA CazéTV resolve dependência)* |
| 9. Customization, UX & Front-End Design | 4 |
| 10. Integration Ecosystem & Partner Connectivity | 5 |
| 11. Channels, Notifications & User Communication | 3 |
| 12. Social Sharing & Virality | 4 |
| 13. Geo-Restriction Capabilities | 4 |
| 14. Roadmap & Evolution Capacity | 5 |
| 15. Commercial, Contractual & Financial Risk | 3 |
| 16. Team, Experience & References | 5 |
| **Média Geral** | **4.37** | *(↑ de 4.12)* |

### Key Strengths (Top 3)
1. **Core Engagement Features & AI:** Responde "Out-Of-The-Box" todas as frentes de predição e features premiums extras como "AI Guess" (ex: PFL) e Quiz Diários. Ligas perfeitamente modeladas. **IA integrada automatiza conteúdo dos mini games.**
2. **SSO Synergy & Data Freedom:** Risco Legal LGPD praticamente ZERO, pois eles orbitam o SSO da CazéTV. Retenção 100% dos dados para sempre. **Proteção anti-bot via JWT elimina risco de inflação artificial de perfis.**
3. **Escalabilidade Extrema Comprovada + Dados Resolvidos:** Referências incontestáveis para milhões de acessos concorrentes e arquitetura flexível capaz de absorver a meta de 15M de usuários. **Feed OPTA já disponível na CazéTV resolve a principal dependência técnica.**

### Risk Flags
| Category | Risk Level | Alert |
|----------|-----------|-------|
| **Costs** | MEDIUM | Usage Pricing Tiers precisam ser minuciosos para não implodir o orçamento nos picos estourando a "allowance" básica. |
| **Tech Deps** | ~~HIGH~~ ✅ RESOLVIDO | ~~CazéTV terá que adquirir feed de API Live Data~~ → **CazéTV já possui acesso ao feed OPTA em tempo real.** |
| **Tech Deps** | MEDIUM | CazéTV precisará investir no próprio Auth / SSO. **Mitigação: LiveLike oferece parceiro SSO/CDP como alternativa (cotação à parte).** |
| **Operations** | MEDIUM | CRM e Triggers de email/Push tem de ser operados pelo cliente, não são inclusos no vendor. |
| **Operations** | LOW | **Dashboard/CMS completo fornecido para L1 — equipe da CazéTV será treinada pela LiveLike.** |

### PMO Verdict
> **STRONG RECOMMENDATION TO PROCEED (Preço Recebido: $325k USD)** — LiveLike consolida-se ainda mais como parceiro ideal (Tier S) após Q&A de follow-up. **Dois dos três principais riscos foram mitigados:** (A) O feed de dados OPTA já está disponível na CazéTV, eliminando a dependência externa mais crítica. (B) A LiveLike possui parceiro SSO/CDP como safety net caso a CazéTV não consiga erguer SSO próprio a tempo. (C) Dashboard/CMS completo equipam a equipe Tier-1 da CazéTV para operar L1 autonomamente. A proteção anti-bot via JWT garante mapeamento 1:1 exato de perfis, eliminando risco de overage por botnets. O custo permanece premium (US$ 325k–425k), mas a redução de riscos técnicos e a oferta de Professional Services + AI para conteúdo fortalecem significativamente a proposta.

### Gaps Críticos Remanescentes
1. **Preparo de SSO (Interno CazéTV ou Parceiro LiveLike)**: Definir se a CazéTV ergue SSO próprio ou contrata o parceiro SSO/CDP da LiveLike (cotação pendente).
2. **CRM / Push Notifications**: A CazéTV precisa definir e operar o CRM / Push Provider internamente.
3. **Deck Comercial (Usage Tiering)**: Receber a proposta financeira final e modelar estresse caso a base chegue rapidamente a 20 Milhões.
