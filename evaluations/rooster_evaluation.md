# Supplier Evaluation Template

**Supplier Name:** `Rooster`
**Website:** `[Não informado]`
**Evaluator:** `Rodrigo`
**Date:** `2026-02-20`

**Source Materials:**
- Proposta Rooster v1 (Apresentação, 10 slides, recebida 18/02/2026)
- **Proposta Rooster v2** (Apresentação atualizada, 13 páginas, recebida 20/02/2026)

---

## 1. Robustness, Scale & Reliability

**Peak Performance & Proven Scale:**
- [ ] **Highest Participants Record (Single Game):** `[Não informado – Nenhum case anterior mencionado]`
- [x] **Strategy for 10M Concurrent Users:**
  > `Proposta declara: "plataforma projetada para escalar elasticamente e suportar picos massivos de audiência, podendo atingir ordem de dezenas de milhões de usuários simultâneos, conforme dimensionamento de infraestrutura." Auto-scaling horizontal + balanceamento global. Testes de carga contínuos.`
- [ ] **Maximum Simultaneous Users Tested:** `[Não informado – claim de "dezenas de milhões" mas sem evidência]`

**Infrastructure & Platforms:**
- [x] **Auto-scaling Infrastructure?** Yes: `Arquitetura cloud distribuída com auto-scaling horizontal e balanceamento global.`
- [x] **Uptime SLA (%):** `~99.9% durante períodos críticos (target)`
- [x] **Platforms Supported:**
    - [x] Web Desktop `(Totalmente responsivo)`
    - [x] Web Mobile `(Totalmente responsivo)`
    - [x] App iOS `(Via WebView/SDK – integração em apps existentes. Nativo como evolução futura.)`
    - [x] App Android `(Via WebView/SDK – integração em apps existentes. Nativo como evolução futura.)`

- **Observations:**
  > Claims são ambiciosos ("dezenas de milhões") mas sem evidência. Provedor cloud não especificado. Testes de carga mencionados mas sem resultados. Boa estrutura declarada (auto-scaling, redundância, monitoring). Target 99.9% é sólido se formalizado em contrato. WebView/SDK para mobile é adequado.
- **Block Rating (1-5):** `3 [Boas declarações mas zero evidência. Sem provedor cloud identificado. Sem cases.]`

---

## 2. Local Support & Operational Coverage

- [x] **Local Support in Brazil?** Yes: `Empresa brasileira`
- [x] **Portuguese-Speaking Support Team?** Yes
- [x] **24/7 Support During Peak?** `Sim durante jogos – "regime de plantão técnico contínuo durante dias de jogos"`
- [x] **War-Room Structure?** Yes: `Confirmado – "estrutura de war-room operacional para monitoramento e resposta a incidentes"`
- [x] **Dedicated Team:** `~7 profissionais full-time exclusivos (4 tech + 3 ops/produto)`
- [x] **SLA Response Times:**
  - Critical: **≤ 15 minutos**
  - High Priority: **≤ 1 hora**
  - Escalonamento em 3 níveis: operacional, técnico, infraestrutura

- **Observations:**
  > ✅ Forte: equipe dedicada (7 FTE), war-room, SLAs definidos (15min/1h), plantão em jogos. Tudo em português, sem barreira de fuso. Um dos melhores perfis de suporte local entre os fornecedores.
- **Block Rating (1-5):** `4 [Equipe dedicada, war-room, SLAs definidos, presença 100% local]`

---

## 3. User Support & Incident Management

- [x] **Escalation Process:** `3 níveis – operacional, técnico, infraestrutura`
- [ ] **Who Handles User Complaints?** `[Não informado – provavelmente time de ops/produto (3 pessoas)]`
- [ ] **Feature Flags / Rollback?** `[Não informado]`

- **Block Rating (1-5):** `3 [Escalonamento definido mas falta detalhamento de processo e ferramentas]`

---

## 4. Security, LGPD, Governance & Compliance

- [ ] **LGPD/GDPR Compliant?** `Implícito – seção de "Segurança, Compliance & Governança" mas sem detalhamento LGPD específico`
- [ ] **Data Residency Country:** `[Não informado]`
- [ ] **Certifications (ISO, SOC, etc.):** `[Não informado]`
- [x] **Age Verification / Consent for Minors:** `Sim – "Mecanismos de consentimento aplicáveis a menores de idade" + "Controles adicionais de privacidade e governança"`

- **Observations:**
  > v2 adicionou seção de segurança com consentimento para menores – ponto positivo. Porém sem detalhamento de LGPD, certificações, pen tests, criptografia, WAF. Menção genérica a compliance sem substância técnica.
- **Block Rating (1-5):** `2 [Melhoria parcial com consentimento para menores. Sem LGPD detalhada, sem certificações.]`

---

## 5. Data Ownership, Access & Portability

- [x] **All User Data Fully Owned by Client?** Yes: `"100% dos dados gerados na plataforma pertencem à CazéTV"`
- [x] **Access to Full User Database?** Yes: `"Acesso integral à base de usuários e dados comportamentais"`
- [x] **Full Data Export Guaranteed?** Yes: `"Exportação completa garantida mediante solicitação"`
- [x] **APIs for Extraction?** Yes: `"APIs disponíveis para integração e extração de dados"`
- [x] **Full Portability on Exit?** Yes: `"Portabilidade integral dos dados e históricos garantida ao término da parceria"`

- **Observations:**
  > ✅ Excelente: v2 cobre todos os pontos de data ownership. 100% cliente, APIs, exportação, portabilidade.
- **Block Rating (1-5):** `5 [Propriedade total, APIs, export, portabilidade integral. Cobertura completa.]`

---

## 6. Core Product Features & Functional Readiness

- [x] **Match Result (1x2):** `Sim – "Palpites de resultado"`
- [x] **Exact Score:** `Sim – "placar exato" confirmado em v2`
- [x] **Special Predictions:** `Sim – "previsões especiais" confirmado em v2`
- [ ] **Live Predictions:** `[Não informado]`
- [x] **Rankings:** `Global + ligas públicas e privadas. Atualizações em "tempo próximo ao real"`
- [x] **Leagues:** `Públicas + Privadas. Criação ilimitada. Convites via link.`
- [x] **Gamification:** `"Gamificação, missões e benefícios" – declarado mas não detalhado`
- [x] **AI Features:** `"IA de sugestões e estatísticas" – declarado, sem detalhamento`
- [x] **Admin/Anti-fraud:** `Sim – "Gestão administrativa e controles antifraude" (v2)`
- [ ] **Quizzes / Lucky Numbers:** `[Não informado]`
- [ ] **Prizes / Sorteios:** `[Não informado]`

- **Observations:**
  > v2 melhorou com placar exato, previsões especiais, ligas ilimitadas e antifraude. Gamificação e missões mencionados mas sem detalhamento. IA declarada sem explicação. Quizzes, lucky numbers e sorteios continuam sem menção.
- **Block Rating (1-5):** `3 [Boa cobertura de features base. Falta detalhamento de gamificação/quiz/prizes.]`

---

## 7. League Management & Premium Infrastructure

- [x] **Free Creation?** Yes
- [x] **Unlimited Leagues?** Yes: `"Criação ilimitada de ligas"`
- [x] **Invite via Link?** Yes
- [ ] **Premium/Freemium Model:** `[Não detalhado]`
- [x] **Admin Controls:** `Sim – "Gestão administrativa" (v2)`
- [x] **Anti-fraud:** `Sim – "Controles antifraude" (v2)`

- **Block Rating (1-5):** `4 [Ligas ilimitadas, convite via link, gestão admin, antifraude. Modelo premium não detalhado.]`

---

## 8. Game Operation & Scoring Process

- [ ] **Scoring Logic:** `[Não detalhado – tipos de palpite confirmados mas regras/pontuação não]`
- [ ] **Data Provider:** `[Não especificado – provedor de dados esportivos não mencionado]`
- [x] **Real-time Updates:** `"Atualizações em tempo próximo ao real"`

- **Block Rating (1-5):** `2 [Sem provedor de dados esportivos definido. Sem regras de pontuação.]`

---

## 9. Customization, UX & Front-End Design

- [x] **Responsive:** Yes – `Web Desktop e Mobile totalmente responsivos`
- [x] **Mobile Integration:** `Via WebView/SDK em apps iOS/Android existentes`
- [ ] **Design Ownership:** `[Não informado – quem faz design/UX?]`

- **Block Rating (1-5):** `3 [Responsivo + WebView/SDK. Sem detalhes de customização ou design ownership.]`

---

## 10. Integration Ecosystem & Partner Connectivity

- [x] **SSO/Auth APIs:** `Sim – "APIs para autenticação e SSO" (v2)`
- [x] **Partner Integration:** `Sim – "Integração com sistemas de parceiros e bases externas" (v2)`
- [x] **Benefits Programs:** `Sim – "Compatibilidade com programas de benefícios e plataformas externas" (v2)`

- **Block Rating (1-5):** `3 [SSO, parceiros e benefícios confirmados. Sem detalhamento técnico de APIs.]`

---

## 11. Channels, Notifications & User Communication

- [ ] Push Notifications: `[Não informado]`
- [ ] Email: `[Não informado]`
- [ ] CRM: `[Não informado]`

- **Block Rating (1-5):** `1 [Zero informação sobre notificações ou comunicação com usuários]`

---

## 12. Social Sharing & Virality

- [ ] Native Sharing: `[Não informado]`

- **Block Rating (1-5):** `1 [Nenhuma funcionalidade de social sharing mencionada]`

---

## 13. Geo-Restriction Capabilities

- `[Não informado]`
- **Block Rating (1-5):** `N/A`

---

## 14. Roadmap & Evolution Capacity

- [x] **Cronograma:** Kickoff ~2w → Dev ~8-12w → Testes ~4w → Go-live antes da Copa
- [x] **Total:** ~14-18 semanas (3.5-4.5 meses)
- [ ] **Post-Cup:** `[Não informado – suporte pós-copa incluído na 3ª parcela (20%)]`

- **Block Rating (1-5):** `3 [Cronograma definido e viável. Apps nativos como evolução futura. Pós-copa indefinido.]`

---

## 15. Commercial, Contractual & Financial Risk

- [x] **Total Cost:** `R$ 1.154.000 (~$193k USD)`
- [x] **Cost Model:** `Investimento fixo all-inclusive (dev + infra + operação Copa)`
- [x] **Variable Costs:** `NÃO – "Custos não variam em função do volume de usuários"`
- [x] **Payment:** `50% assinatura + 30% antes da Copa + 20% pós-Copa`
- [x] **SLAs in Contract:** `Sim – "Níveis de serviço formalizados em contrato"`

- **Observations:**
  > ✅ Modelo muito favorável: custo fixo all-inclusive, sem variação por tráfego, inclui infra e operação. Preço competitivo (R$ 1.154k vs Quality R$ 1.2M+ ou Fan Arena R$ 2.2-3.4M). Risco: entrada de 50% é alta.
- **Block Rating (1-5):** `4 [Preço competitivo, custo fixo, inclui infra e operação. Entrada 50% é alta.]`

---

## 16. Team, Experience & References

- [ ] **Years in Market:** `[Não informado]`
- [ ] **Previous World Cup/Massive Event Cases:** `[Nenhum mencionado]`
- [ ] **Reference Contacts:** `[Não fornecidos]`

- **Block Rating (1-5):** `1 [Zero informação sobre experiência, cases ou referências]`

---

# Executive Summary & Recommendation

## Executive Summary
Rooster é uma empresa brasileira que propõe construir o Bolão CazéTV por R$ 1.154.000 (custo fixo all-inclusive que inclui desenvolvimento, infraestrutura e operação durante a Copa). A proposta v2 endereçou várias lacunas da v1, adicionando SLAs (15min/1h), war-room, dados 100% do cliente, SSO, cronograma (14-18 semanas) e consentimento para menores.

Porém, a proposta continua sendo uma **apresentação comercial** sem profundidade técnica. Não há cases de escala anteriores, provedor cloud não é especificado, LGPD não é detalhada, notificações estão ausentes, e features de gamificação (quiz, lucky numbers, sorteios) não são confirmadas.

## Automated Risk Flags
| Category | Flag Condition | Risk Level | Alert |
| :--- | :--- | :--- | :--- |
| **Scale** | `highest_participants_in_single_game` < 100k | **CRITICAL** | "No history of massive single-event scale." |
| **Scale** | `recent_load_test_evidence` == No | **HIGH** | "No recent proof of load capability." |
| **Security** | `lgpd_detailed` == No | **HIGH** | "LGPD compliance not detailed." |
| **Security** | `certifications` == None | **HIGH** | "No security certifications mentioned." |
| **Notifications** | `push_email_crm` == None | **HIGH** | "No re-engagement channels." |
| **References** | `previous_cases` == None | **HIGH** | "No track record or references provided." |

## Block Ratings Summary
| Block | Rating | Status |
| :--- | :--- | :--- |
| 1. Robustness, Scale & Reliability | **3/5** | Good claims, zero evidence |
| 2. Local Support & Operational Coverage | **4/5** | ✅ Strong: 7 FTE, war-room, SLAs |
| 3. User Support & Incident Management | **3/5** | Escalation defined |
| 4. Security, LGPD, Governance | **2/5** | Minor consent only |
| 5. Data Ownership, Access & Portability | **5/5** | ✅ 100% client, APIs, portability |
| 6. Core Product Features | **3/5** | Base features, gamification unclear |
| 7. League Management & Premium | **4/5** | ✅ Unlimited, admin, antifraude |
| 8. Game Operation & Scoring | **2/5** | No data provider, no scoring rules |
| 9. Customization, UX & Front-End | **3/5** | Responsive + WebView |
| 10. Integration Ecosystem | **3/5** | SSO + Partners confirmed |
| 11. Notifications & Communication | **1/5** | ❌ Zero |
| 12. Social Sharing & Virality | **1/5** | ❌ None |
| 13. Geo-Restriction | **N/A** | Not assessed |
| 14. Roadmap & Evolution | **3/5** | 14-18 week timeline |
| 15. Commercial & Financial | **4/5** | ✅ Fixed cost, competitive |
| 16. Team, Experience & References | **1/5** | ❌ Zero info |
| **Average (assessed blocks)** | **2.8/5** | |

## Final Recommendation
**⚠️ PROCEED WITH CAUTION**

Per system rules: CRITICAL risk (no proven scale history) + multiple HIGH risks (LGPD, certifications, no references). But strong commercial model (fixed cost, all-inclusive) and good support structure (7 FTE, war-room, SLAs).

**Before Decision, Rooster MUST provide:**
1. **Cloud provider identification** (AWS? GCP? Azure?) + region
2. **Load test evidence** – actual results, not just claims
3. **LGPD compliance details** – how data is protected, consent flows, data residency
4. **Cases/references** – any project at scale, even outside sports
5. **Data provider** – who supplies match results? Cost?
6. **Gamification details** – quizzes, missions, prizes – are they included?
7. **Notification stack** – push, email, CRM – what's the plan?
8. **Design/UX ownership** – who creates the design?
