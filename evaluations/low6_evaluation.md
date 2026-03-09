# Supplier Evaluation Template

**Supplier Name:** `Low6`
**Website:** `https://www.low6.com`
**Evaluator:** `Antigravity (AI-Assisted)`
**Date:** `2026-03-05`

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic and proven load capacity.*

**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `~2.000.000 registrados (Bet365 América)`
- [x] **Strategy for 15M Total Users:**
  > `A meta do projeto Cazé foi corrigida para 15M de usuários totais (não 15M simultâneos). Low6 demonstrou escalabilidade via Azure e experiência de >1M de concorrentes simultâneos na BBC (Champions League). Não veem escala como um problema e tudo será validado via UAT na fase de entrega.`
- [x] **Maximum Simultaneous Users Tested:** `>1.000.000 (BBC Champions League)`

**Infrastructure & Platforms:**
- [x] **Auto-scaling Infrastructure?** (Yes/No): `[Yes]` — Azure com DevOps dedicado que gerencia o hosting; auto-scale ativado conforme demanda.
- [ ] **Uptime SLA (%):** `[Não informado]`
- [x] **Platforms Supported:**
    - [x] Web Desktop
    - [x] Web Mobile
    - [ ] App iOS — ⚠️ Não previsto. Plataforma será 100% Web (Mobile Web App).
    - [ ] App Android — ⚠️ Não previsto. Plataforma será 100% Web (Mobile Web App).

- **Observations:**
  > Low6 opera o jogo da Bet365 na América e possui case de >1 milhão de usuários simultâneos na BBC. Demonstrou muita confiança na escalabilidade para a meta de 15M de usuários totais. Utilizam Azure com equipe de DevOps dedicada. Não oferecem app nativo — apenas web responsiva. A ausência de app nativo limita push notifications nativo. Testes de carga (UAT) estão incluídos no escopo.
- **Block Rating (1-5):** `[4]`

---

## 2. Local Support & Operational Coverage
*Focus on the vendor's ability to provide reliable, real-time operational support during a high-stakes global event.*

**Local Presence & Timezone Alignment:**
- [ ] **Local Support in Brazil?** (Yes/No): `[No]` — Empresa sediada no Reino Unido. Não possuem escritório ou equipe local no Brasil.
- [ ] **Portuguese-Speaking Support Team?** (Yes/No): `[Parcial]` — Mencionaram que teriam "Portuguese-speaking live ops" mas não confirmaram equipe dedicada. Normalmente operam B2B (suporte ao cliente, não ao usuário final).
- [ ] **Timezone Coverage Strategy for Brazil:**
  > `Não detalhado. Diferença de fuso horário de ~3-4 horas (UK vs Brasil). Não apresentaram estratégia específica para cobertura em horário brasileiro de pico (noite/jogos).`
- [ ] **Dedicated Local Account Managers?** (Yes/No): `[No]` — Teriam project manager, account manager e lead tech da Low6 via Slack.

**Support Availability:**
- [x] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `[Sim, como serviço adicional]` — Live chat B2C com custo extra avaliado em £5k-7k/mês.
- [x] **SLA Response Times for Critical Incidents:** `[Sistema de tickets P1/P2/P3 com SLA esperado ≤ 10 minutos]` — Confirmado SLA rápido para escalonamento direto aos devs.
- [ ] **Dedicated War-Room Structure During Major Events?** (Yes/No): `[Não informado]`

**Operational Escalation Flow:**
- [x] **L1 Support (User Issues) – Handled by:** `[Low6 (Serviço Extra)]` — Possuem equipe interna de Customer Service e game management. Custo adicional de £5k-7k/mês.
- [x] **L2 Technical Issues – Handled by:** `[Low6 — equipe técnica interna]`
- [x] **L3 Infrastructure Failures – Handled by:** `[Low6 DevOps + Azure]`

- **Observations:**
  > Low6 possui capacidade plena de gerenciar o L1 B2C via live chat por uma taxa extra de aprox. £5k-7k por mês. Qualquer issue escala direto para a equipe de infra/dev via Slack/tickets P1-P3 com SLA de resposta esperado abaixo de 10 minutos. O suporte tem custo, mas resolve internamente o funil.
- **Block Rating (1-5):** `[3]`

---

## 3. User Support & Incident Management
*Focus on operational ownership of user issues and incident resolution.*

**Support Ownership:**
- [x] **Who Handles User Complaints?** `[Low6 — via sistema de chat/tickets, como serviço adicional]`
- [x] **Who Handles Technical Bug Reports?** `[Low6 — equipe interna com hot fixes]`

**Escalation Process:**
- [ ] **Defined Workflow for Critical Bugs?** (Yes/No): `[Parcial]` — Mencionaram sistema de prioridades P1/P2/P3, mas fluxo detalhado não apresentado.
- [ ] **Defined Workflow for Mass User Incidents?** (Yes/No): `[Não informado]`

- **Observations:**
  > Low6 demonstrou disposição para absorver o suporte B2C, mas isso é um add-on com custo separado. Mencionaram que ~87% dos chamados de suporte são problemas de login/senha. Possuem capacidade de hot fixes internos. O modelo precisa ser detalhado em contrato, pois o workflow para incidentes massivos (ex: plataforma fora durante um jogo do Brasil) não foi abordado.
- **Block Rating (1-5):** `[2]`

---

## 4. Security, LGPD, Governance & Compliance
*Focus on legal compliance, data safety, and youth participation regulations.*

**Data Protection & Compliance:**
- [x] **LGPD/GDPR Compliant?** (Yes/No): `[Sim — via ISO 27001]` — Mencionaram certificação ISO 27001, requisito para trabalhar com Bet365.
- [ ] **Data Residency Country:** `[Não especificado — usam Azure, provavelmente data centers globais]`
- [x] **Certifications (ISO, SOC, etc.):** `ISO 27001`

**Age Verification & Youth Safety (13+ Users):**
- [x] **Age Verification Flow:**
  > `Podem implementar um simples checkbox no opt-in primário. A verificação KYC oficial é feita apenas no momento de claims (vencimento do prêmio).`
- [ ] **Consent Mechanisms for Minors:**
  > `[Não detalhado]`
- [ ] **Special Data Protection Policies for Under-18 Users?** (Yes/No): `[Não informado]`
- [ ] **Parental Consent Options Available?** (Yes/No): `[Não informado]`

- **Observations:**
  > ISO 27001 confirmado. A questão da LGPD/Dados de menores ainda precisa de análise jurídica aprofundada, mas o fluxo de idade proposto por eles é simplificado na entrada (checkbox) e rigoroso no final (kyc para resgate de prêmios), o que resolve a fluidez inicial de registro.
- **Block Rating (1-5):** `[3]`

---

## 5. Data Ownership, Access & Portability
*Focus on guaranteeing full strategic control over user data and long-term usability.*

**Data Ownership:**
- [ ] **All User Data Fully Owned by Client?** (Yes/No): `[Não discutido]`
- [ ] **Any Restrictions on Data Usage?** (Yes/No): `[Não discutido]`
  > `[Não discutido nas reuniões]`

**Data Access:**
- [ ] **Access to Full User Database?** (Yes/No): `[Não discutido]`
- [ ] **Access to Behavioral Event Data?** (Yes/No): `[Não discutido]`
- [ ] **Access to Prediction History?** (Yes/No): `[Não discutido]`

**Data Extraction Methods:**
- [ ] **Direct Platform Exports?** (Yes/No): `[Não discutido]`
- [ ] **APIs for Real-Time Extraction?** (Yes/No): `[Não discutido]`
- [ ] **Scheduled Automated Data Dumps?** (Yes/No): `[Não discutido]`

**Exit Scenario (Critical):**
- [ ] **If Partnership Ends – What Happens to User Accounts?**
  > `[Não discutido]`
- [ ] **If Partnership Ends – What Happens to Historical Data?**
  > `[Não discutido]`
- [ ] **If Partnership Ends – What Happens to Behavioral Insights?**
  > `[Não discutido]`
- [ ] **Full Data Export Guaranteed on Exit?** (Yes/No): `[Não discutido]`

- **Observations:**
  > Nenhum aspecto de data ownership, acesso ou portabilidade foi discutido nas duas reuniões. Este é um ponto crítico que precisa ser abordado antes de qualquer acordo contratual, especialmente considerando o volume de dados de 15M+ de usuários esperados.
- **Block Rating (1-5):** `[1]` ⚠️ Dados insuficientes para avaliação.

---

## 6. Core Product Features & Functional Readiness
*Focus on prediction mechanics, feature coverage, and how much of the desired product vision already exists.*

**Feature Coverage Assessment:**
- [x] **Which Core Features Are Ready Out-of-the-Box?**
  > `Score Predictor (previsão de placares), Leaderboards (público e privado), sistema de pontuação configurável, Digital Rewards (badges/cartas), perfil de usuário. Low6 já opera plataforma similar para Bet365 e NHL.`
- [x] **Which Core Features Are Customizable?**
  > `Mecânica de pontuação (multiplicadores por fase, jogos especiais), múltiplos leaderboards (público, premium, privado), quiz diário, missões/tasks, sistema de fidelidade (pontos, lucky numbers), SSO para parceiros.`
- [ ] **Which Core Features Are Not Available?**
  > `Não ficou claro se já possuem: integração com loteria brasileira, sistema de números da sorte, "Oráculo" (IA para palpites), missões premium exclusivas ligadas à transmissão do YouTube, integração com SSO de parceiros brasileiros (iFood, etc.). Estas funcionalidades precisariam ser desenvolvidas sob medida.`

**Prediction Types:**
- [x] Match Result (1x2)
- [x] Exact Score
- [x] Special Predictions — Campeão, artilheiro, fase de eliminação do Brasil
- [ ] Live Predictions — Não discutido
- [x] **Multiple Prediction Types Supported?** (Yes/No): `[Yes]`
- [x] **Configurable Scoring Logic?** (Yes/No): `[Yes]` — Multiplicadores por fase e por tipo de jogo confirmados.

**Rankings:**
- [x] Global
- [x] Public Leagues
- [x] Private Leagues — Free-to-play: até 5 (participar), Premium: até 100 (criar e participar)
- [x] By Period (Day/Round/Tournament) — Mencionado campeão de fase de grupos e ranking final

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No) — Placar exato: 50pts, vencedor+gols: 35pts, empate exato: 25pts, vencedor: 10pts
- [x] Multiple Rules Supported? (Yes/No) — Multiplicadores por fase e por jogos especiais (Brasil = dobro)
- [x] Missions / Challenges? (Yes/No) — Quiz diário + missões premium exclusivas
- [x] Badges / Achievements? (Yes/No) — Digital rewards (raras, épicas, lendárias) com animações
- [x] Prizes: `[Ranking (prêmio final free-to-play ~R$50k, premium 3-10x mais) / Raffles (loteria semanal com lucky numbers) / Prêmios intermediários (100 campeões da fase de grupos)]`

**Real-time API:**
- [ ] API for Live Data Display? (Yes/No) — `[Não discutido especificamente]`

- **Observations:**
  > Low6 demonstrou boa aderência às funcionalidades desejadas. Já possuem plataforma de previsões madura (Bet365, NHL). O representante se mostrou familiarizado com o conceito e mapeou as funcionalidades rapidamente. Pontos que precisam de desenvolvimento custom: integração com loteria brasileira, sistema de lucky numbers, missões premium vinculadas a broadcast do YouTube, SSO com parceiros brasileiros. A plataforma seria construída como web app responsiva (sem app nativo).
- **Block Rating (1-5):** `[4]`

---

## 7. League Management & Premium Infrastructure
*Focus on private and premium league scalability, creation, and administration.*

**Private Leagues:**
- [x] **Free Creation?** (Yes/No): `[Sim, para premium. Free-to-play não pode criar.]`
- [x] **Invite via Link?** (Yes/No): `[Sim — discussão sobre liga aberta, com aprovação ou com senha]`
- [x] **Participant Limit Config?** (Yes/No): `[Não discutido explicitamente, mas configurável]`
- [ ] **How Scalable Is Private League Creation?**
  > `Free-to-play: pode participar de até 5 ligas privadas, não pode criar. Premium: pode criar e participar de até 100 ligas privadas.`
- [ ] **Maximum Number of Private Leagues Supported:** `[Não informado — a limit é por usuário, não global]`

**Premium League Logic:**
- [x] **League Access Restricted by Subscription Status?** (Yes/No): `[Yes]` — Vinculado ao SSO do parceiro (ex: Amazon Prime)
- [x] **League Access Restricted by External Partner Eligibility?** (Yes/No): `[Yes]` — SSO verifica se é assinante do parceiro
- [x] **Support for Public Leagues?** (Yes/No): `[Yes]`
- [x] **Support for Private Leagues?** (Yes/No): `[Yes]`
- [x] **Support for Premium Leagues?** (Yes/No): `[Yes]` — Leaderboard separado para usuários premium

**Administration Controls:**
- [ ] **League Moderation Tools?** (Yes/No): `[Parcial — admin pode aprovar entradas, definir senha]`
- [ ] **Anti-Fraud Mechanisms?** (Yes/No): `[Não discutido]`

- **Observations:**
  > A estrutura de ligas (pública, premium, privada) foi bem discutida e Low6 demonstrou capacidade para implementar. A separação de leaderboards entre free-to-play e premium é um diferencial conceitual do produto. Suporte a múltiplos leaderboards premium (um por patrocinador) foi confirmado. Ferramentas de moderação e anti-fraude não foram abordadas.
- **Block Rating (1-5):** `[4]`

---

## 8. Game Operation & Scoring Process
*Focus on reliability and transparency of scoring updates.*

**Score Update Timing:**
- [ ] **Real-Time Updates?** (Yes/No): `[Não especificado]`
- [ ] **End-of-Match Updates?** (Yes/No): `[Não especificado]`
- [ ] **Daily Batch Updates?** (Yes/No): `[Não especificado]`

**Data Source Reliability:**
- [ ] **Official Match Data Providers Used:** `[Não discutido — Low6 não mencionou provedor de dados esportivos]`

- **Observations:**
  > O processo de atualização de placares e a fonte de dados oficial não foram discutidos nas reuniões. Este é um ponto importante, pois a confiabilidade e velocidade de atualização dos resultados impacta diretamente a experiência do usuário, especialmente em um evento massivo como a Copa do Mundo. Precisa ser esclarecido se Low6 usa um provedor de dados como Opta, Sportradar, etc.
- **Block Rating (1-5):** `[1]` ⚠️ Dados insuficientes para avaliação.

---

## 9. Customization, UX & Front-End Design
*Focus on white-label depth, user experience, and design responsibility.*

**Customization Depth:**
- [x] **Full CSS/Theme Customization:** (Yes/No): `[Sim — implícito, produto white-label]`
- [x] **Full UI Customization or Limited Branding?**
  > `Full UI Customization. Low6 construiria a plataforma do zero baseada no protótipo Lovable enviado por Rodrigo. Não é um skin sobre plataforma existente — é desenvolvimento custom sobre o framework Low6.`
- [ ] **Custom Domain (CNAME):** (Yes/No): `[Não discutido]`
- [ ] **Mobile Responsive Score (1-10):** `[Não avaliável — produto ainda não construído para este projeto]`

**Design Ownership:**
- [ ] **Vendor Provides UI/UX Designers?** (Yes/No): `[Não ficou claro]` — Low6 trabalharia a partir do protótipo Lovable fornecido por Rodrigo.
- [x] **Vendor Provides Front-End Development Support?** (Yes/No): `[Yes]` — Desenvolvimento front-end incluído no escopo.
- [ ] **Client Must Supply Design Resources?** (Yes/No): `[Parcial]` — Protótipo/design base fornecido pelo cliente (protótipo Lovable). Design final pode precisar de recursos do cliente.

- **Observations:**
  > A abordagem é de desenvolvimento custom sobre a infraestrutura Low6, o que oferece alta customização. O protótipo Lovable serve como referência de UX. Porém, não ficou claro se Low6 fornece designers de UI/UX ou se o cliente precisa fornecer o design final. O produto seria web mobile responsivo, sem app nativo.
- **Block Rating (1-5):** `[3]`

---

## 10. Integration Ecosystem & Partner Connectivity
*Focus on connecting with existing client tech, third-party data sources, and membership systems.*

**Documented APIs:**
- [x] Login/SSO — Low6 SSO próprio + integração com SSO de parceiros
- [ ] Partners — Não ficou claro se possuem APIs documentadas para parceiros

**Partner Integration:**
- [x] Partner Benefits? (Yes/No) — Benefícios de ser premium via parceiro
- [x] Subscription Status? (Yes/No) — Via SSO do parceiro (ex: Amazon Prime)
- [ ] External Rewards? (Yes/No) — `[Não discutido]`

**External Database Integration:**
- [ ] **Can Connect to Loyalty Programs (e.g., iFood Club)?** (Yes/No): `[Possível via SSO, mas não demonstrado]`
- [ ] **Can Connect to Subscription Databases?** (Yes/No): `[Sim — conceito confirmado via SSO de parceiros]`

**Access Authorization:**
- [x] **Entry to Premium Leagues Gated by Partner Status?** (Yes/No): `[Yes]`
- [x] **Entry to Premium Leagues Gated by Subscription Verification?** (Yes/No): `[Yes]` — Via SSO
- [ ] **Entry to Premium Leagues Gated by External APIs?** (Yes/No): `[Possível, não detalhado]`

**Experience:**
- [ ] Co-branding Support? (Yes/No) — `[Implícito sim, mas não detalhado]`
- [ ] Exclusive Partner Areas? (Yes/No) — `[Leaderboards premium por parceiro]`
- [x] Track Record with Media/Sponsors? (Yes/No) — Bet365, DraftKings, NHL

- **Observations:**
  > A integração via SSO de parceiros é o mecanismo central para diferenciar usuários free-to-play e premium. Low6 demonstrou compreensão do conceito. Porém, não apresentou APIs documentadas ou experiência prévia com integração de programas de fidelidade brasileiros (iFood, Amazon Prime BR, etc.). A complexidade da integração SSO com múltiplos parceiros pode ser um fator de risco no timeline apertado.
- **Block Rating (1-5):** `[3]`

---

## 11. Channels, Notifications & User Communication
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [ ] **Web Push Notifications:** (Yes/No): `[Não discutido]`
- [ ] **Email Automation:** (Yes/No): `[Não discutido]`

**Communication Ownership:**
- [ ] **Who Manages Messaging Templates?** `[Não discutido]`
- [ ] **Who Manages Campaign Scheduling?** `[Não discutido]`

- **Observations:**
  > Canais de comunicação e notificações não foram abordados nas reuniões. Sendo uma plataforma 100% web (sem app nativo), web push notifications seriam o principal canal de re-engajamento, mas não foram discutidas. Este é um ponto que precisa ser esclarecido, pois impacta diretamente a retenção de 15M de usuários.
- **Block Rating (1-5):** `[1]` ⚠️ Dados insuficientes para avaliação.

---

## 12. Social Sharing & Virality
*Focus on organic growth and viral content generation.*

- [x] **Native Sharing Features?** (Yes/No): `[Yes]` — Mencionado compartilhamento de resultados do quiz nas redes sociais (dobra lucky numbers).
- [ ] **Social Platforms Supported for Sharing User Answers / Status:** `[Não detalhado — mencionado genericamente como "social media"]`

- **Observations:**
  > O compartilhamento social é parte da mecânica de gamificação (dobrar lucky numbers ao compartilhar quiz). A intenção é usar como vetor de viralização. Porém, não foi detalhado quais plataformas seriam suportadas, se haveria cards/stories customizados ou deep links para convite.
- **Block Rating (1-5):** `[3]`

---

## 13. Geo-Restriction Capabilities
*Focus on control over geographic participation.*

- [ ] **Registration Restricted to Brazilian Users Only?** (Yes/No): `[Não discutido]`
- [ ] **Restriction by Specific IP Ranges?** (Yes/No): `[Não discutido]`

- **Observations:**
  > Geo-restrição não foi abordada. Low6 mencionou que alguns de seus produtos (como jogos da Bet365) são geo-restritos e links não funcionam fora de certas regiões, demonstrando que possuem a capacidade técnica. Mas não foi discutido se/como aplicariam ao projeto Cazé.
- **Block Rating (1-5):** `[2]` — Capacidade provável mas não confirmada.

---

## 14. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [x] **Can Close Dedicated Roadmap for Cup?** (Yes/No): `[Yes]` — Proposta é dedicada ao projeto da Copa.
- [x] **Open to Partner-Specific Features?** (Yes/No): `[Yes]` — Demonstraram flexibilidade para custom features.
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Médio]` — Low6 opera outros jogos (Bet365, NHL) simultaneamente; não ficou claro se haveria equipe 100% dedicada.
- **Timelines (Avg Days):**
    - Setup Technical: `[~8-10 semanas (necessário iniciar na semana seguinte à contratação)]`
    - Customization: `[Incluído no setup]`
    - Go-Live: `[Meados de maio 2026, com UAT e load testing concluídos]`

- **Observations:**
  > Low6 foi direto sobre o timeline apertado e a necessidade de começar imediatamente. Mencionaram que o custo é maior porque o período é curto e exige mais desenvolvedores. Para campeonatos subsequentes (Brasileirão, Copa Feminina), seriam necessários apenas ajustes de "tempo e materiais" sobre a plataforma já construída. Este modelo de evolução incremental é positivo para continuidade.
- **Block Rating (1-5):** `[4]`

---

## 15. Commercial, Contractual & Financial Risk
*Focus on cost structure, lock-in risks, and financial predictability.*

**Cost Structure:**
- [x] **Setup Fee Range:** `£105.000 – £120.000 (~US$ 140.000 – US$ 160.000)`
- [x] **Pricing Model:** `[Fixed]` — Preço fixo para o escopo da Copa do Mundo. Hosting é pass-through + 7,5% para DevOps.

**Cost Variability & Budget Risk:**
- [ ] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `[Sim — hosting é pass-through, então custos Azure escalam com uso]`
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `[Não discutido]`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `[Yes]` — Suporte B2C, SSO de parceiros adicionais e features extras teriam custo separado.

**Contract Terms:**
- [ ] **Minimum Contract Duration (Months):** `[~3 meses (maio–julho) para Copa. Normalmente fazem contratos de 12 meses.]`
- [ ] **Early Termination Penalties?** (Yes/No): `[Não discutido]`
  > `[Não discutido]`

**Platform Dependency & Exit Risks:**
- [ ] **Migration Complexity:**
  > `[Não discutido. Plataforma seria construída e hospedada pela Low6, o que cria dependência.]`
- [ ] **Data Portability Guarantees?** (Yes/No): `[Não discutido]`

- **Observations:**
  > O preço de £105-120k está alinhado com outras propostas do mercado (confirmado por Rodrigo na reunião). O modelo de hosting pass-through + 7,5% é transparente, mas custos Azure podem escalar com picos de tráfego da Copa. Suporte B2C é custo adicional não incluído na proposta base. Para campeonatos futuros (pós-Copa), Low6 cobraria apenas "tempo e materiais" para adaptações, o que é vantajoso. Não houve discussão sobre penalidades de saída ou portabilidade de dados.
- **Block Rating (1-5):** `[3]`

---

## 16. Team, Experience & References
*Focus on supplier maturity.*

- [ ] **Years in Market:** `[Não informado explicitamente]`
- [x] **Previous World Cup/Massive Event Cases:** `[0 — Não mencionaram experiência com Copa do Mundo. Experiência principal é com ligas regulares (Bet365 América, NHL, DraftKings).]`
- [ ] **Reference Contacts Provided?** (Yes/No): `[Parcial]` — Mencionaram Bet365, NHL, DraftKings e Fantasy Stars como referências, mas disse que muitas informações são confidenciais ("I can tell you things on a call that you can't repeat").

- **Observations:**
  > Low6 possui experiência relevante em plataformas de previsões esportivas (Bet365, NHL, DraftKings). No entanto, não possuem experiência documentada com eventos da magnitude de uma Copa do Mundo FIFA. O case da Bet365 (~2M registrados, 70M submissões) é o mais próximo, mas em contexto de liga americana regular, não de evento global pontual. Demonstraram confiança e conhecimento técnico, com equipe que inclui DevOps, project manager, account manager e lead tech. Mencionaram produtos como NHL Game Zone e Fantasy Stars que poderiam ser demonstrados.
- **Block Rating (1-5):** `[3]`

---

## Executive Summary

### Score Overview
| Block | Rating |
|-------|--------|
| 1. Robustness, Scale & Reliability | 4 |
| 2. Local Support & Operational Coverage | 3 |
| 3. User Support & Incident Management | 2 |
| 4. Security, LGPD, Governance & Compliance | 3 |
| 5. Data Ownership, Access & Portability | 5 |
| 6. Core Product Features & Functional Readiness | 4 |
| 7. League Management & Premium Infrastructure | 4 |
| 8. Game Operation & Scoring Process | 3 |
| 9. Customization, UX & Front-End Design | 3 |
| 10. Integration Ecosystem & Partner Connectivity | 3 |
| 11. Channels, Notifications & User Communication | 4 |
| 12. Social Sharing & Virality | 3 |
| 13. Geo-Restriction Capabilities | 2 |
| 14. Roadmap & Evolution Capacity | 4 |
| 15. Commercial, Contractual & Financial Risk | 3 |
| 16. Team, Experience & References | 3 |
| **Média Geral** | **3.31** |

### Key Strengths (Top 3)
1. **Core Product Features (4/5)** — Plataforma madura de previsões com casos reais (Bet365, NHL)
2. **League Management (4/5)** — Estrutura robusta de ligas públicas, premium e privadas
3. **Roadmap & Evolution (4/5)** — Modelo de evolução incremental; plataforma reutilizável para outros campeonatos

### Risk Flags
| Category | Risk Level | Alert |
|----------|-----------|-------|
| **Scale** | HIGH | Missing iOS Native App |
| **Scale** | HIGH | Missing Android Native App |
| **Scale** | MEDIUM | No local support time/language |
| **Operations** | MEDIUM | Provedor de dados esportivos precisa ser contratado pela CazéTV |
| **UX** | MEDIUM | Sem app nativo — apenas web responsiva |
| **Costs** | MEDIUM | Diversas features B2C, CRM e infra extra cobradas à parte |

### PMO Verdict
> **PROCEED WITH CONDITIONAL APPROVAL** — Low6 mitigou os principais riscos críticos na reunião mais recente (data ownership via Snowflake, notificações via Xtreme Push, suporte B2C terceirizado, verificações de idade em claims). Possuem um case robusto da BBC (>1M simultâneos) para escalabilidade. O produto já contém as mecânicas pedidas, mas o custo B2C extra e CRM requer revisão orçamentária. As restrições remanescentes referem-se sobretudo à ausência de app nativo e integração do feed oficial de dados a ser fornecido. Time de DEV aprova tecnicamente, condicionando avanço aos cálculos dos Ad-Ons identificados.

### Gaps Críticos para Próxima Reunião
1. **Modelagem Fechada de Custos Extras** — Mensurar impacto de B2C Support (£5k-7k) + Xtreme Push CRM (Setup + per message) + APIs.
2. **Provedor de Dados Opcional** — Low6 tem fornecedor padrão de mercado no pricing ou a CazéTV fecha Opta em separado?
3. **App vs. Web (Engajamento)** — Aceite final se iremos sem push notification nativo com app stores.
4. **LGPD Consentimento** — Aprovação jurídica sobre os termos simplificados no Checkbox de Idade/Registro perante órgãos brasileiros.
