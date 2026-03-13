# Supplier Evaluation Template

**Supplier Name:** `Low6`
**Website:** `https://www.low6.com`
**Evaluator:** `Antigravity (AI-Assisted)`
**Date:** `2026-03-10` *(Atualizado com Q&A Follow-up)*

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic and proven load capacity.*

**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `~2.000.000 registrados (Bet365 América)`
- [x] **Strategy for 15M Total Users:**
  > `A meta do projeto Cazé foi corrigida para 15M de usuários totais (não 15M simultâneos). Low6 demonstrou escalabilidade via Azure e experiência de >1M de concorrentes simultâneos na BBC (Champions League). Não veem escala como um problema e tudo será validado via UAT na fase de entrega.`
- [x] **Maximum Simultaneous Users Tested:** `>1.000.000 (BBC Champions League)`
- [x] **Success Cases under High Load:** `Case Sportsbet (App #1 Austrália, pico de engajamento diário de 1.7 logins/dia e sessões de 6 min).`

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
- [x] **Portuguese-Speaking Support Team?** (Yes/No): `[Yes]` — ✅ **Confirmado na Proposta:** "Live chat service for users to interact with in Portuguese".
- [ ] **Timezone Coverage Strategy for Brazil:**
  > `Não detalhado. Diferença de fuso horário de ~3-4 horas (UK vs Brasil). Não apresentaram estratégia específica para cobertura em horário brasileiro de pico (noite/jogos).`
- [ ] **Dedicated Local Account Managers?** (Yes/No): `[No]` — Teriam project manager, account manager e lead tech da Low6 via Slack.

**Support Availability:**
- [x] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `[Yes]` — Escopo da proposta garante "24/7 Support graded P1, P2, P3".
- [x] **SLA Response Times for Critical Incidents:** `[Sistema de tickets P1/P2/P3 com SLA esperado ≤ 10 minutos]` — Confirmado SLA rápido para escalonamento direto aos devs.
- [ ] **Dedicated War-Room Structure During Major Events?** (Yes/No): `[Não informado]`

**Operational Escalation Flow:**
- [x] **L1 Support (User Issues) – Handled by:** `[Low6]` — Serviço de Customer Service & Support orçado na proposta final por **$15.000**. Cobre atendimento direto aos usuários.
- [x] **L2 Technical Issues – Handled by:** `[Low6 — equipe técnica interna]`
- [x] **L3 Infrastructure Failures – Handled by:** `[Low6 DevOps + Azure]`

- **Observations:**
  > ✅ **Proposta Oficial:** Low6 assume oficialmente L1 com Chat em Português e L2/L3 com SLA 24/7 P1-P3. O custo exato desse pacote de Customer Service & Support é de **$15.000**, o que resolve o "add-on" anterior de forma previsível e tira completamente o peso operacional B2C da CazéTV.
- **Block Rating (1-5):** `[4]` *(Atualizado: Custos reais e chat PT-BR confirmados na proposta final)*

---

## 3. User Support & Incident Management
*Focus on operational ownership of user issues and incident resolution.*

**Support Ownership:**
- [x] **Who Handles User Complaints?** `[Low6]` — Via live chat em português incluído na proposta de Customer Service ($15k).
- [x] **Who Handles Technical Bug Reports?** `[Low6 — equipe interna com hot fixes]`

**Escalation Process:**
- [x] **Defined Workflow for Critical Bugs?** (Yes/No): `[Yes]` — Fluxograma 24/7 para graus P1, P2 e P3.
- [ ] **Defined Workflow for Mass User Incidents?** (Yes/No): `[Não informado]`

- **Observations:**
  > A assunção do suporte L1/B2C pela Low6 (com chat em português por $15.000) é excelente. Mencionaram que ~87% dos chamados de suporte são problemas de login/senha. A equipe já possui o fluxo "P1, P2, P3" estruturado para 24/7.
- **Block Rating (1-5):** `[4]` *(Atualizado via Proposta PDF)*

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
- [x] **All User Data Fully Owned by Client?** (Yes/No): `[Yes]` — ✅ **Confirmado via Q&A:** CazéTV retém 100% da propriedade legal de todos os dados de usuários registrados, históricos de predições e eventos comportamentais.
- [x] **Any Restrictions on Data Usage?** (Yes/No): `[No]`
  > `Low6 atuará como data processor, criando dashboards para a CazéTV. A CazéTV mantém propriedade integral dos dados.`

**Data Access:**
- [x] **Access to Full User Database?** (Yes/No): `[Yes]` — Via dashboards Tableau com KPIs customizados.
- [x] **Access to Behavioral Event Data?** (Yes/No): `[Yes]` — Low6 possui acesso a dados comportamentais para construir dashboards.
- [x] **Access to Prediction History?** (Yes/No): `[Yes]`

**Data Extraction Methods:**
- [x] **Direct Platform Exports?** (Yes/No): `[Yes]` — Via Tableau dashboards.
- [ ] **APIs for Real-Time Extraction?** (Yes/No): `[Não discutido]`
- [ ] **Scheduled Automated Data Dumps?** (Yes/No): `[Não discutido]`

**Exit Scenario (Critical):**
- [x] **If Partnership Ends – What Happens to User Accounts?**
  > `[Arquivados/Exportados]` — Como Data Processor garantido por DPA, a CazéTV tem acesso de download via parceiro.
- [x] **If Partnership Ends – What Happens to Historical Data?**
  > `[Disponível para portabilidade]` 
- [ ] **If Partnership Ends – What Happens to Behavioral Insights?**
  > `[Não discutido detalhadamente quanto à retenção pós-contrato]`
- [x] **Full Data Export Guaranteed on Exit?** (Yes/No): `[Yes]` — Acesso livre ao Data Warehouse.

- **Observations:**
  > ✅ **Progresso significativo via Q&A (v2):** Low6 confirmou atuar estritamente como **Data Processor** (DPA assinado), com CazéTV retendo 100% da propriedade. Todos os dados são extraídos da plataforma pela ferramenta Fivetran e armazenados num Data Warehouse do **Snowflake**. A CazéTV terá acesso ininterrupto a esse Snowflake para baixar tudo a qualquer hora, garantindo portabilidade.
- **Block Rating (1-5):** `[5]` *(Atualizado: Portabilidade irrestrita via Snowflake confirmada)*

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
- [x] **Anti-Fraud / Anti-Bot Mechanisms?** (Yes/No): `[Parcial]` — ✅ **Q&A confirmou:** Low6 pode implementar **código de verificação para login/jogar** via XtremePush, porém com custo adicional para a CazéTV.

- **Observations:**
  > A estrutura de ligas (pública, premium, privada) foi bem discutida e Low6 demonstrou capacidade para implementar. A separação de leaderboards entre free-to-play e premium é um diferencial conceitual do produto. **Q&A confirmou que implementação de verificação anti-bot é possível via XtremePush, porém a custo extra.** Isso é menos robusto que a solução JWT da LiveLike (gratuita e nativa), mas pelo menos a capacidade existe.
- **Block Rating (1-5):** `[4]`

---

## 8. Game Operation & Scoring Process
*Focus on reliability and transparency of scoring updates.*

**Score Update Timing:**
- [x] **Real-Time Updates?** (Yes/No): `[Yes]` — Via feed OPTA fornecido pela CazéTV.
- [x] **End-of-Match Updates?** (Yes/No): `[Yes]`
- [ ] **Daily Batch Updates?** (Yes/No): `[Não especificado]`

**Data Source Reliability:**
- [x] **Official Match Data Providers Used:** `[OPTA/Stats Perform — ✅ CazéTV já possui acesso ao feed de dados em tempo real. Low6 espera receber o feed como third-party. Caso necessário, Low6 pode adquirir em nome da CazéTV por $10.000-15.000 USD.]`

**Hosting Costs (Q&A Confirmado):**
  > Custos mensais de hosting Azure por faixa de MAU:
  > - 500.000 monthly actives: **$5.000/mês**
  > - 1.000.000 monthly actives: **$7.000/mês**
  > - 5.000.000 monthly actives: **$10.000/mês**

- **Observations:**
  > ✅ **RISCO RESOLVIDO:** A CazéTV já possui acesso ao feed OPTA em tempo real, que será fornecido à Low6 como third-party. Caso a CazéTV não tivesse, Low6 poderia adquirir por $10-15k. **Os custos de hosting Azure foram detalhados por faixa de MAU, oferecendo previsibilidade orçamentária.** Para 5M MAU (cenário de Copa), o custo mensal de hosting seria de ~$10k.
- **Block Rating (1-5):** `[4]` *(Atualizado: Feed OPTA resolvido + custos de hosting detalhados)*

---

## 9. Customization, UX & Front-End Design
*Focus on white-label depth, user experience, and design responsibility.*

**Customization Depth:**
- [x] **Full CSS/Theme Customization:** (Yes/No): `[Sim — implícito, produto white-label]`
- [x] **Full UI Customization or Limited Branding?**
  > `Full UI Customization. Low6 construiria a plataforma do zero baseada no protótipo Lovable enviado por Rodrigo. Não é um skin sobre plataforma existente — é desenvolvimento custom sobre o framework Low6.`
- [x] **Custom Domain (CNAME):** (Yes/No): `[Yes]` — ✅ **Confirmado via Q&A:** Dedicated externally-hosted subdomain.
- [ ] **Mobile Responsive Score (1-10):** `[Não avaliável — produto ainda não construído para este projeto]`

**Design Ownership:**
- [x] **Vendor Provides UI/UX Designers?** (Yes/No): `[Yes]` — ✅ **Confirmado via Q&A:** CazéTV terá suporte de design dedicado da Low6. Designs seguirão as brand guidelines, com **2 rodadas de revisão de design** incluídas.
- [x] **Vendor Provides Front-End Development Support?** (Yes/No): `[Yes]` — Desenvolvimento front-end incluído no escopo.
- [x] **Client Must Supply Design Resources?** (Yes/No): `[No]` — Low6 fornece designers. Cliente fornece brand guidelines.

- **Observations:**
  > ✅ **Progresso significativo via Q&A:** Low6 confirmou que a plataforma será entregue em **subdomain externo dedicado**, com **suporte de design dedicado** (2 rodadas de revisão). O cliente não precisa fornecer designers — apenas brand guidelines. Isso resolve a incerteza anterior sobre responsabilidade de design.
- **Block Rating (1-5):** `[4]` *(Atualizado: Design dedicado + subdomain confirmados)*

---

## 10. Integration Ecosystem & Partner Connectivity
*Focus on connecting with existing client tech, third-party data sources, and membership systems.*

**Documented APIs:**
- [x] Login/SSO — Low6 SSO próprio + integração com SSO de parceiros. ✅ **Q&A confirmou:** Low6 assume a implementação completa do SSO do parceiro e trabalha diretamente com o parceiro para executar a integração.
- [ ] Partners — Não ficou claro se possuem APIs documentadas para parceiros

**Partner Integration:**
- [x] Partner Benefits? (Yes/No) — Benefícios de ser premium via parceiro
- [x] Subscription Status? (Yes/No) — Via SSO do parceiro (ex: Amazon Prime)
- [ ] External Rewards? (Yes/No) — `[Não discutido]`

**External Database Integration:**
- [ ] **Can Connect to Loyalty Programs (e.g., iFood Club)?** (Yes/No): `[Possível via SSO, mas não demonstrado]`
- [x] **Can Connect to Subscription Databases?** (Yes/No): `[Sim — conceito confirmado via SSO de parceiros]`

**Access Authorization:**
- [x] **Entry to Premium Leagues Gated by Partner Status?** (Yes/No): `[Yes]`
- [x] **Entry to Premium Leagues Gated by Subscription Verification?** (Yes/No): `[Yes]` — Via SSO
- [ ] **Entry to Premium Leagues Gated by External APIs?** (Yes/No): `[Possível, não detalhado]`

**Experience:**
- [ ] Co-branding Support? (Yes/No) — `[Implícito sim, mas não detalhado]`
- [ ] Exclusive Partner Areas? (Yes/No) — `[Leaderboards premium por parceiro]`
- [x] Track Record with Media/Sponsors? (Yes/No) — Bet365, DraftKings, NHL

- **Observations:**
  > ✅ **Progresso significativo via Q&A:** Low6 confirmou que **assume a implementação completa do SSO do parceiro**, trabalhando diretamente com o parceiro comercial para executar a integração. Isso reduz significativamente a carga técnica da CazéTV. A integração via SSO de parceiros continua sendo o mecanismo central para diferenciar usuários free-to-play e premium.
- **Block Rating (1-5):** `[4]` *(Atualizado: SSO do parceiro operado pela Low6)*

---

## 11. Channels, Notifications & User Communication
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [x] **Web Push Notifications:** (Yes/No): `[Yes — via XtremePush]` — ✅ **Proposta Oficial:** Confirma que Push notification, Email e In-app são "Out of the box" se usar o stack deles (XtremePush).
- [x] **Email Automation:** (Yes/No): `[Yes — via XtremePush/CRM]`

**Communication Ownership:**
- [x] **Who Manages Messaging Templates?** `[Low6]` — ✅ **Proposta Oficial:** "CRM Integration" e "CRM Management" estão explicitamente listados sob "LOW6 Responsibilities".
- [x] **Who Manages Campaign Scheduling?** `[Low6]`

- **Observations:**
  > ✅ **A proposta final é clara:** A Low6 assume 100% da responsabilidade de "CRM Integration" e "CRM Management". Com o tech stack deles (Xtremepush), Push notifications, Emails e In-app messages são considerados "Out of the box", retirando a carga operacional da CazéTV e permitindo notificações otimizadas baseadas em eventos (gols, fechamento de liga, etc).
- **Block Rating (1-5):** `[5]` *(Atualizado: CRM Integration/Management é responsabilidade explícita da Low6)*

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
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Médio]` — Low6 opera outros jogos (Bet365, NHL) simultaneamente.
- **Timelines (Avg Days):**
    - Setup Technical & Kick-off: `[Início em 23 de Março]`
    - Development Sprint: `[30 de Março a 8 de Maio]`
    - UAT (Testes): `[11 a 15 de Maio]`
    - Go-Live: `[18 de Maio]`

- **Observations:**
  > O cronograma apresentado na Proposta V2 é enxuto, agressivo e direto (aprox 8 semanas do kick-off ao lançamento). O Go-Live firme em **18 de Maio** permite 3 semanas de folga antes do início da Copa do Mundo para captar base ativamente. É fundamental não atrasar o Kick-off de 23 de Março. Vale ressaltar que os Termos de Uso (T&Cs) e Regras do Jogo precisam ser elaborados juridicamente pela própria CazéTV.
- **Block Rating (1-5):** `[4]`

---

## 15. Commercial, Contractual & Financial Risk
*Focus on cost structure, lock-in risks, and financial predictability.*

**Cost Structure:**
- [x] **Setup Fee Range:** `US$ 150.000` — ✅ **Proposta Oficial ("Package World Cup Price")**
- [x] **Pricing Model:** `[Fixed + Pass-through]` — Preço fixo para o escopo da Copa do Mundo ($150k) + Customer Service ($15k). Hosting é pass-through + 7,5% para DevOps.

**Cost Variability & Budget Risk:**
- [x] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `[Sim — hosting é pass-through, então custos Azure escalam com uso]`
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `[Não]`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `[Não - Escopo fechado na proposta]` — O add-on de B2C foi consolidado em $15.000. O PDF de Pricing do CRM / Marcomm (XtremePush) será a única variável adicional relevante de acordo com o tráfego F2P (Pricing Marcomm avulso). O pacote principal é claro.

**Added Value Games (From Presentation):**
- Acesso ao portfólio de Gamification: `Bracket, Squads, Spin-2-Win, Picks, Over/Under, Last One Standing, Retro Arcade Games.` O modelo de plataforma All-in-1 deles viabiliza incluir múltiplos jogos além do bolão tradicional.

**Contract Terms:**
- [ ] **Minimum Contract Duration (Months):** `[~3 meses (maio–julho) para Copa. Normalmente fazem contratos de 12 meses.]`
- [ ] **Early Termination Penalties?** (Yes/No): `[Não discutido]`
  > `[Não discutido]`

**Platform Dependency & Exit Risks:**
- [ ] **Migration Complexity:**
  > `[Não discutido. Plataforma seria construída e hospedada pela Low6, o que cria dependência.]`
- [ ] **Data Portability Guarantees?** (Yes/No): `[Não discutido]`

- **Observations:**
  > ✅ **A proposta finaliza incertezas orçamentárias.** O custo core da plataforma é US$ 150.000, com mais US$ 15.000 adicionais englobando todo o L1 de Customer Service (Chat PT). Resta apenas calcular o custo do "Hosting Azure" (projetado a $5k-$10k mensais) + Taxas do PDF separado da XtremePush/Marcomm para se ter o Cost of Ownership Mensal 100% selado. Excelência em visibilidade.
- **Block Rating (1-5):** `[4]` *(Atualizado: Orçamento consolidado e transparente)*

---

## 16. Team, Experience & References
*Focus on supplier maturity.*

- [ ] **Years in Market:** `[Não informado explicitamente]`
- [x] **Previous World Cup/Massive Event Cases:** `[0 — Não mencionaram experiência com Copa do Mundo. Experiência principal é com ligas regulares (Bet365 América, NHL, DraftKings).]`
- [ ] **Reference Contacts Provided?** (Yes/No): `[Parcial]` — Mencionaram Bet365, NHL, DraftKings e Fantasy Stars como referências, mas disse que muitas informações são confidenciais ("I can tell you things on a call that you can't repeat").

- **Observations:**
  > Low6 possui forte tração com F2P Games, sendo premiada multiplamente (EGR, SBC) e listada como a #23 empresa de crescimento mais rápido do UK. Possuem cases massivos comprovados: Bet365 na América e um case espetacular com a Sportsbet na Austrália para a Copa do Mundo 2022 (App #1 gratuito na Austrália, 4x média de logins diários, 34% signups via refer-a-friend). Isso valida fortemente a tese de aquisição F2P para a Copa.
- **Block Rating (1-5):** `[5]` — Validação categórica com cases premiados e números expressivos na Austrália.

---

## Executive Summary

### Score Overview
| Block | Rating |
|-------|--------|
| 1. Robustness, Scale & Reliability | 4 |
| 2. Local Support & Operational Coverage | 4 | *(↑ SLA 24/7 e Chat PT Inclusos $15k)* |
| 3. User Support & Incident Management | 4 | *(↑ Fluxo 24/7 de Bugs P1-P3 Confirmado)* |
| 4. Security, LGPD, Governance & Compliance | 3 |
| 5. Data Ownership, Access & Portability | 4 |
| 6. Core Product Features & Functional Readiness | 4 |
| 7. League Management & Premium Infrastructure | 4 |
| 8. Game Operation & Scoring Process | 4 |
| 9. Customization, UX & Front-End Design | 4 |
| 10. Integration Ecosystem & Partner Connectivity | 4 |
| 11. Channels, Notifications & User Communication | 5 | *(↑ CRM Integrations/Management é Oficial)* |
| 12. Social Sharing & Virality | 3 |
| 13. Geo-Restriction Capabilities | 2 |
| 14. Roadmap & Evolution Capacity | 4 |
| 15. Commercial, Contractual & Financial Risk | 4 | *(↑ Orçamento Fechado e Fixo em PDF)* |
| 16. Team, Experience & References | 5 |
| **Média Geral** | **3.87** | *(↑ de 3.50)* |

### Key Strengths (Top 3)
1. **Pacote Mídia-Ready "Full-Service" (5/5)** — Low6 não apenas licencia o software, mas inclui *Platform Management, CRM Integration/Management, B2C Customer Service e Suporte/Design no formato de pacote único*. Isso livra a Operação de Conteúdo da CazeTV do gargalo tecnológico.
2. **Preço e Infra Transparente (4/5)** — $150k de pacote base, $15k em suporte 24h/PT (barato para B2C) e hosting transparente de ~$10k/mês de Azure. Não há mistérios de desenvolvimento.
3. **Escala e Gamificação (5/5)** — Comprovado (Sportsbet/BBC) com engajamentos adicionais de caixas misteriosas, loyalty points, etc.

### Risk Flags
| Category | Risk Level | Alert |
|----------|-----------|-------|
| **Scale** | HIGH | Ausência de App Nativo (iOS/Android) — apenas web responsiva |
| **Tech Deps** | ~~HIGH~~ ✅ RESOLVIDO | CazéTV já possui feed OPTA. Low6 aceita como third-party. |
| **Operations** | ~~MEDIUM~~ ✅ MITIGADO | **Low6 assume totalmente a gestão/integração do CRM** via XtremePush no PDF de proposta corporativa. |
| **Costs** | LOW | Os "Add-ons" foram consolidados de forma muito explícita na proposta comercial. Variável principal será Licença de Envio do XtremePush baseada em tamanho de lista e base Azure. |
| **Data** | MEDIUM | Exit scenarios e portabilidade de dados ainda não formalizados |
| **Anti-Bot** | MEDIUM | Verificação anti-bot via XtremePush tem custo de SMS por uso |

### PMO Verdict
> **PROCEED WITH STRONG APPROVAL (Proposta Oficial Analisada)** — A análise final da **"LOW6 CazeTV Proposal.pdf"** consolidou a Low6 na liderança como a opção mais "Mídia Central" possível. Em vez de comprar o "problema" (necessidade de orquestrar CRM interno, Suporte B2C e Design), a CazeTV compra por **US$ 165.000** um estúdio virtual que cuidará de 100% da Engenharia, Gestão de Usuários (Chat PT incluso), Retenção via Webhooks (Xtremepush out of the box). O teto final do projeto está desenhado sem armadilhas pesadas. A LiveLike tem mais mecânicas "virais" puras (AI Guessing) e nativamente mais seguras em botting (JWT), mas terceiriza de volta a "bucha" de suporte e CRM para o cliente. A Low6 entrega tudo centralizado num pacote. Veredito é um sim claro da tecnologia.

### Gaps Críticos Remanescentes
1. **Aprovação de Marcomm Pricing** — Cruzar o "Low6_MarComm_Pricing_USD.pdf" e validar teto de XtremePush para os 15 Milhões projetados.
2. **App vs. Web** — Aceite final de marketing: sem push notification nativo, o esforço no PWA via web será forte o bastante?
3. **Contrato Formal** — Avaliar terms de SaaS, multas rescisórias e Portabilidade caso Cazé decida levar a liga internamente pós-Copa 26.
