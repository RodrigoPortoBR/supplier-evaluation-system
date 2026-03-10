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
- [x] **Local Support in Brazil?** (Yes/No): `[No]` — Mas possuem equipe na Europa e América do Norte.
- [x] **Portuguese-Speaking Support Team?** (Yes/No): `[Yes]`
- [x] **Timezone Coverage Strategy for Brazil:**
  > `Atendimento a partir da Europa e América do Norte, cobrindo o fuso brasileiro durante o torneio.`
- [x] **Dedicated Local Account Managers?** (Yes/No): `[No]` — Gestão liderada a partir da América do Norte; Dev na Índia.

**Support Availability:**
- [x] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `[Sim, como serviço adicional opcional]`
- [x] **SLA Response Times for Critical Incidents:** `[2 Horas no padrão (pode ser menor com aditivo 24/7)]`
- [x] **Dedicated War-Room Structure During Major Events?** (Yes/No): `[Monitoramento ativo via Slack dedicado]`

**Operational Escalation Flow:**
- [x] **L1 Support (User Issues) – Handled by:** `[CazéTV]` — LiveLike NÃO oferece suporte B2C, mas fornece **dashboard e CMS completo** para que a equipe Tier-1 da CazéTV investigue e resolva reclamações individuais (pontos faltantes, recompensas não creditadas, contas bloqueadas) sem necessidade de escalonar tickets para a LiveLike.
- [x] **L2 Technical Issues – Handled by:** `[LiveLike]`
- [x] **L3 Infrastructure Failures – Handled by:** `[LiveLike + AWS]`

- **Observations:**
  > O suporte B2B (para o cliente) é muito bem estruturado com SLA, tickets e canal Slack. A CazéTV deve internalizar ou terceirizar 100% do suporte B2C, **porém a LiveLike confirmou que fornece um dashboard administrativo e CMS completo** no qual a equipe de suporte da CazéTV será treinada. A equipe de Customer Support da LiveLike também pode auxiliar a equipe da CazéTV. Presença de falantes de português no suporte B2B foi confirmada. **Isso mitiga significativamente o risco operacional de L1.**
- **Block Rating (1-5):** `[3]` *(Atualizado: Dashboard/CMS para L1 confirmado)*

---

## 3. User Support & Incident Management
*Focus on operational ownership of user issues and incident resolution.*

**Support Ownership:**
- [x] **Who Handles User Complaints?** `[CazéTV / Cliente]` — Usando o dashboard/CMS completo fornecido pela LiveLike para investigar reclamações individuais.
- [x] **Who Handles Technical Bug Reports?** `[LiveLike (com patches rápidos)]`

**Escalation Process:**
- [x] **Defined Workflow for Critical Bugs?** (Yes/No): `[Yes]` — Ticket automatizado via E-mail/Telefone/Slack.
- [x] **Defined Workflow for Mass User Incidents?** (Yes/No): `[Yes]` — Detalhado no futuro SLA.

- **Observations:**
  > A resolução de bugs técnicos (L2/L3) é rápida e via patches. A CazéTV operará o L1 usando o **CMS/Dashboard administrativo da LiveLike**, onde poderá investigar problemas individuais de usuários (pontos, recompensas, contas) de forma autônoma. A equipe de Customer Support da LiveLike assiste no treinamento e can auxiliar conforme necessário.
- **Block Rating (1-5):** `[4]` *(Atualizado: ferramentas de suporte L1 confirmadas)*

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
- [ ] **Setup Fee Range:** `US$ 325.000` (Total Base para 10M de usuários)
- [x] **Pricing Model:** `[Hybrid (Setup + Tech License / Subscription + Volume Usage)]`

**Cost Variability & Budget Risk:**
- [x] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `[Yes - Usage-Based Allowance]`
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `[Possivelmente contemplado no Usage]`
- [ ] **Can Costs Increase Due to Extra Features?** (Yes/No): `[Yes (SLA 24/7 por exemplo)]`

**Contract Terms:**
- [x] **Minimum Contract Duration (Months):** `≈ 2 a 3 Meses para a Copa do Mundo (Implementação, Licença Gaming Hub, Professional Services e Usage baseados nesse período)`
- [ ] **Early Termination Penalties?** (Yes/No): `[N/A para modelo proof-of-concept]`

**Platform Dependency & Exit Risks:**
- [ ] **Migration Complexity:**
  > `Não há Lock-In pelo foco em IDs anônimos e dados de posse da CazéTV. Fácil migração se parar no POC.`
- [x] **Data Portability Guarantees?** (Yes/No): `[Yes]`

- **Observations:**
  > O modelo tem um custo base de **US$ 325.000**, o que é consideravelmente alto. Ele inclui: Implementação ($25k), Licença com 3 jogos ($50k), Créditos de Professional Services ($50k) e Usage garantido até 10 Milhões de Usuários ($200k). O tráfego extra custa **$20.000 a cada 1 milhão de usuários excedentes**. Para nossa meta de 15M, o custo final seria em torno de **US$ 425.000** (aprox R$ 2.5 Milhões), tornando-se uma das opções mais caras da mesa.
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
