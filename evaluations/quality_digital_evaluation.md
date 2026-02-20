# Supplier Evaluation Template

**Supplier Name:** `Quality Digital (Quality Software S.A.)`
**Website:** `https://ri.quality.com.br`
**Evaluator:** `Rodrigo`
**Date:** `2026-02-20`

**Source Materials:**
- Proposta Quality Digital - Omni55 (Proposta Nº 101876, 35 pages, received Feb 20, 2026)
- Responsável: Antonio Filgueiras
- Emissão: Rio de Janeiro, 20/02/2026

> ⚠️ **IMPORTANTE:** Quality Digital é uma **software house** (outsourcing de desenvolvimento), NÃO um fornecedor de produto/plataforma SaaS. O modelo é fundamentalmente diferente dos demais fornecedores avaliados (Fan Arena, Genius Sports, Easypromos). Quality entrega **mão de obra especializada + código-fonte proprietário do cliente**, não uma plataforma pronta.

---

## 1. Robustness, Scale & Reliability
*Focus on the ability to handle World Cup peak traffic and proven load capacity.*

**Peak Performance & Proven Scale:**
- [ ] **Highest Participants Record (Single Game):** `[Não informado – Quality não é dona de produto, é software house. Não possui cases de plataforma própria em escala Copa]`
- [ ] **Strategy for 10M Concurrent Users (5 mins before game):**
  > `Proposta reconhece o risco de alta volumetria mas NÃO define estratégia específica. Recomenda "análise antecipada" e "testes de stress e carga antes do Go Live." Planejamento de capacidade depende de validação conjunta com o cliente.` `[Não Definido – Risco Reconhecido]`
- [ ] **Maximum Simultaneous Users Tested:** `[Não informado]`

**Infrastructure & Platforms:**
- [x] **Auto-scaling Infrastructure?** (Yes/No): `Sim – AWS ECS Fargate com auto-scaling. Proposta confirma "elasticidade frente a picos de acesso."`
- [ ] **Uptime SLA (%):** `[Não informado – SLAs serão definidos no contrato MSA]`
- [x] **Platforms Supported:**
    - [x] Web Desktop `(Next.js React – web responsiva)`
    - [x] Web Mobile `(Mobile-first responsive web)`
    - [ ] App iOS `❌ Explicitamente FORA do escopo: "Não haverá desenvolvimento de aplicativo nativo (iOS/Android) no MVP"`
    - [ ] App Android `❌ Explicitamente FORA do escopo`

- **Observations:**
  > `⚠️ PREOCUPAÇÃO CRÍTICA: Quality é uma software house, NÃO um fornecedor de produto. Não possui experiência comprovada operando plataforma própria em escala Copa. A arquitetura proposta (AWS Fargate + Aurora + Redis + SQS) é tecnicamente sólida e moderna, mas NUNCA FOI TESTADA para este cenário. Sem apps nativos. O dimensionamento de infraestrutura depende de validação futura – a proposta não define capacidade. Todos os custos de infra são do CLIENTE. O risco é significativo pois todos os riscos de escala ficam com o cliente.`
- **Block Rating (1-5):** `2 [Arquitetura moderna mas zero experiência comprovada em escala massiva. Sem apps nativos. Infra é responsabilidade do cliente.]`

---

## 2. Local Support & Operational Coverage
*Focus on the vendor's ability to provide reliable, real-time operational support during a high-stakes global event.*

**Local Presence & Timezone Alignment:**
- [x] **Local Support in Brazil?** (Yes/No): `Sim – Empresa brasileira, matriz RJ, filiais SP e PR`
- [x] **Portuguese-Speaking Support Team?** (Yes/No): `Sim – Equipe 100% brasileira`
- [x] **Timezone Coverage Strategy for Brazil:**
  > `Empresa nacional, horário comercial BR. Proposta menciona "estrutura de plantão dedicada em dias de jogos críticos" e "war room operacional" como recomendação.`
- [ ] **Dedicated Local Account Managers?** (Yes/No): `[Não informado diretamente – modelo de squad com gerente de conta]`

**Support Availability:**
- [ ] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `Não – Proposta recomenda "estrutura de plantão dedicada" mas não garante 24/7. Horas extras cobradas a 100%.`
- [ ] **SLA Response Times for Critical Incidents:** `[Não informado – SLAs serão parte do MSA]`
- [ ] **Dedicated War-Room Structure During Major Events?** (Yes/No): `Recomendado na proposta como "mitigação de risco reputacional", não confirmado como incluso.`

**Operational Escalation Flow:**
- [ ] **L1 Support (User Issues) – Handled by:** `[Não informado – modelo body shop, provavelmente responsabilidade do cliente]`
- [ ] **L2 Technical Issues – Handled by:** `[Sustentação coberta por 45 dias pós-launch (R$ 182k)]`
- [ ] **L3 Infrastructure Failures – Handled by:** `[Cliente – "custos de cloud ou serviços em nuvem" são responsabilidade do cliente]`

- **Observations:**
  > `Vantagem: empresa 100% brasileira com presença local. Desvantagem: modelo body shop não inclui operação contínua como serviço. Sustentação é limitada a 45 dias na Copa (R$ 182k extra). Após os 45 dias, não há cobertura. War room é "recomendação", não garantia. Horas extras = +100%. O suporte ao usuário NÃO está no escopo – é responsabilidade do cliente.`
- **Block Rating (1-5):** `3 [Presença local forte, mas modelo body shop e sustentação limitada]`

---

## 3. User Support & Incident Management
*Focus on operational ownership of user issues and incident resolution.*

**Support Ownership:**
- [ ] **Who Handles User Complaints?** `[Responsabilidade do CLIENTE – Quality faz desenvolvimento, não operação]`
- [ ] **Who Handles Technical Bug Reports?** `Quality durante período de sustentação (45 dias). Após, responsabilidade do cliente ou nova contratação.`

**Escalation Process:**
- [ ] **Defined Workflow for Critical Bugs?** (Yes/No): `[Não informado – proposta menciona change request formal]`
- [ ] **Defined Workflow for Mass User Incidents?** (Yes/No): `[Não informado]`

- **Observations:**
  > `Quality é uma software house – entrega código, não opera plataforma. Suporte ao usuário, gestão de incidentes em massa e operação contínua são responsabilidades do CLIENTE. Sustentação de 45 dias cobre bugs técnicos durante a Copa, mas não é um serviço de operação.`
- **Block Rating (1-5):** `2 [Modelo não inclui operação – cliente assume todo o gerenciamento pós-entrega]`

---

## 4. Security, LGPD, Governance & Compliance
*Focus on legal compliance, data safety, and youth participation regulations.*

**Data Protection & Compliance:**
- [x] **LGPD/GDPR Compliant?** (Yes/No): `Sim – Proposta detalha consentimentos LGPD no cadastro com auditoria (user_id, timestamp, IP, versão do termo). Masking de dados sensíveis nos logs.`
- [ ] **Data Residency Country:** `Brasil – AWS São Paulo (implícito pela arquitetura AWS)`
- [ ] **Certifications (ISO, SOC, etc.):** `[Não informado – Empresa listada na B3, BNDES acionista]`

**Age Verification & Youth Safety (13+ Users):**
- [ ] **Age Verification Flow:**
  > `[Não informado]`
- [ ] **Consent Mechanisms for Minors:**
  > `[Não informado]`
- [ ] **Special Data Protection Policies for Under-18 Users?** (Yes/No): `[Não informado]`
- [ ] **Parental Consent Options Available?** (Yes/No): `[Não informado]`

- **Observations:**
  > `✅ PONTO POSITIVO: Quality é o ÚNICO fornecedor que detalhou implementação LGPD na proposta – consentimentos com auditoria, masking de dados sensíveis (CPF, email, telefone), criptografia at-rest, WAF + rate limit, TLS end-to-end, Secrets Manager. Porém, verificação de idade e proteção de menores não foram abordados. Empresa listada na B3 com BNDES como acionista sugere governança corporativa sólida.`
- **Block Rating (1-5):** `4 [Melhor detalhamento de LGPD entre todos os fornecedores. Verificação de idade pendente.]`

---

## 5. Data Ownership, Access & Portability
*Focus on guaranteeing full strategic control over user data and long-term usability.*

**Data Ownership:**
- [x] **All User Data Fully Owned by Client?** (Yes/No): `SIM – 100% proprietário do cliente. Código-fonte entregue ao repositório do cliente. "Propriedade total da empresa contratante no final de cada entrega e/ou sprint."`
- [x] **Any Restrictions on Data Usage?** (Yes/No): `Não – Dados, código e infraestrutura são todos do cliente.`
  > `Zero restrição. Modelo de desenvolvimento sob encomenda = tudo pertence ao cliente.`

**Data Access:**
- [x] **Access to Full User Database?** (Yes/No): `Sim – Banco de dados do cliente (Aurora PostgreSQL na conta AWS do cliente)`
- [x] **Access to Behavioral Event Data?** (Yes/No): `Sim – Toda a observabilidade (CloudWatch, logs) na conta do cliente`
- [x] **Access to Prediction History?** (Yes/No): `Sim – Persistência com histórico por usuário e por partida`

**Data Extraction Methods:**
- [x] **Direct Platform Exports?** (Yes/No): `Sim – Acesso direto ao banco de dados e repositório de código`
- [ ] **APIs for Real-Time Extraction?** (Yes/No): `[Backend API disponível – construído sob medida]`
- [ ] **Scheduled Automated Data Dumps?** (Yes/No): `[Não informado – mas cliente tem controle total]`

**Exit Scenario (Critical):**
- [x] **If Partnership Ends – What Happens to User Accounts?**
  > `Tudo pertence ao cliente. Código-fonte, dados e infraestrutura são propriedade total do cliente.`
- [x] **If Partnership Ends – What Happens to Historical Data?**
  > `Dados permanecem em infraestrutura do cliente (AWS do cliente).`
- [x] **If Partnership Ends – What Happens to Behavioral Insights?**
  > `Logs e analytics ficam na conta AWS do cliente (CloudWatch).`
- [x] **Full Data Export Guaranteed on Exit?** (Yes/No): `Sim – Desnecessário, pois tudo já está no cliente.`

- **Observations:**
  > `✅ MÁXIMA NOTA: modelo de software house = ZERO lock-in. Código-fonte, dados, infra – tudo é 100% proprietário do cliente. Este é o cenário ideal de data ownership. Nenhum outro fornecedor oferece este nível de controle. O trade-off é que o cliente precisa operar e manter tudo sozinho após o contrato.`
- **Block Rating (1-5):** `5 [Propriedade total do cliente – zero lock-in, zero restrição]`

---

## 6. Core Product Features & Functional Readiness
*Focus on prediction mechanics, feature coverage, and how much of the desired product vision already exists.*

**Feature Coverage Assessment:**
- [x] **Which Core Features Are Ready Out-of-the-Box?**
  > `NENHUMA – Quality constrói do zero. Mas o MVP inclui: cadastro/login, palpites (placar exato), ligas públicas (Base/Premium), ligas privadas, ranking global e por liga, integração OPTA, CMS (Strapi).`
- [x] **Which Core Features Are Customizable?**
  > `Tudo – software sob medida. Porém, tempo e custo são altos.`
- [x] **Which Core Features Are Not Available?**
  > `❌ MUITAS features fora do MVP:
  > - Missões/Quiz funcionais (apenas placeholder visual)
  > - Lucky Numbers / Sorteios
  > - Premiações regulamentadas
  > - IA/LLM (oráculo, recomendações)
  > - Estatísticas avançadas
  > - Busca na plataforma
  > - Gamificação avançada (badges, níveis)
  > - Apps nativos (iOS/Android)
  > - Integração CRM/CDP
  > - Marketing automation
  > - Pagamentos`

**Prediction Types:**
- [ ] Match Result (1x2) `[Não explícito – proposta foca em "placar exato"]`
- [x] Exact Score `(Confirmado: "Registro de palpite por partida (placar A x B)")`
- [ ] Special Predictions `[Não informado – fora do MVP]`
- [ ] Live Predictions `[Não informado – fora do MVP]`
- [ ] **Multiple Prediction Types Supported?** (Yes/No): `Não no MVP – apenas placar`
- [x] **Configurable Scoring Logic?** (Yes/No): `Sim – "motor de regras de pontuação (server-side)" com acerto exato, acerto vencedor, empate`

**Rankings:**
- [x] Global `(Ranking geral por liga pública)`
- [x] Public Leagues `(Liga CazéTV Base + Liga Premium Sponsor)`
- [x] Private Leagues `(Criação e ranking de ligas privadas)`
- [ ] By Period (Day/Round/Tournament) `[Não informado]`

**Scoring & Engagement:**
- [x] Configurable Scoring System? (Yes/No) `Sim – motor de regras customizável`
- [ ] Multiple Rules Supported? (Yes/No) `[Não informado – motor único no MVP]`
- [ ] Missions / Challenges? (Yes/No) `❌ NÃO no MVP – apenas placeholder: "card Quiz diário — em breve"`
- [ ] Badges / Achievements? (Yes/No) `❌ NÃO – "Gamificação avançada (insígnias, níveis, badges evolutivos)" fora do escopo`
- [ ] Prizes: `❌ NÃO no MVP – "Sistema completo de premiações regulamentadas, sorteios, distribuição automática de prêmios ou números da sorte" FORA do escopo`

**Real-time API:**
- [x] API for Live Data Display? (Yes/No) `Sim – "Ranking em tempo real" via Redis + "Acompanha ranking em tempo real"`

- **Observations:**
  > `⚠️ MVP MUITO LIMITADO: O core do produto (palpites + ranking + ligas) existe, mas TODAS as features de gamificação (quiz, missões, lucky numbers, badges, sorteios) estão FORA do MVP. São "Fase 2" sem prazo ou orçamento definidos. Comparado aos demais fornecedores, Quality entrega ~40% das features por um custo similar. A vantagem é que o código é proprietário e customizável sem limites – mas precisa de mais tempo e dinheiro.`
- **Block Rating (1-5):** `2 [MVP cobre apenas o core básico. Gamificação, missões, sorteios – tudo fora do escopo]`

---

## 7. League Management & Premium Infrastructure
*Focus on private and premium league scalability, creation, and administration.*

**Private Leagues:**
- [x] **Free Creation?** (Yes/No): `Sim – criação de ligas privadas`
- [x] **Invite via Link?** (Yes/No): `Sim – "Link direto" + "Inserção manual de código"`
- [ ] **Participant Limit Config?** (Yes/No): `[Não informado no MVP]`
- [ ] **How Scalable Is Private League Creation?**
  > `Não definido. Dimensionamento depende de discovery.`
- [ ] **Maximum Number of Private Leagues Supported:** `[Não informado]`

**Premium League Logic:**
- [x] **League Access Restricted by Subscription Status?** (Yes/No): `Sim – "classificação de usuário Base vs Premium" com sponsor_id`
- [x] **League Access Restricted by External Partner Eligibility?** (Yes/No): `Sim – Integração sponsor (iFood Clube) para validação de elegibilidade`
- [x] **Support for Public Leagues?** (Yes/No): `Sim – Liga CazéTV Base`
- [x] **Support for Private Leagues?** (Yes/No): `Sim`
- [x] **Support for Premium Leagues?** (Yes/No): `Sim – Liga Premium sponsor-driven. Na ausência de sponsor integrado, opera como "Base" com fallback.`

**Administration Controls:**
- [ ] **League Moderation Tools?** (Yes/No): `❌ NÃO – "Não haverá: Gestão e aprovação de usuários (aprovação manual)"`
- [ ] **Anti-Fraud Mechanisms?** (Yes/No): `[Não informado – WAF e rate limit cobrem segurança básica]`

- **Observations:**
  > `Modelo de ligas Base/Premium/Privadas existe, mas é MVP simplificado. A estrutura de sponsor-gating é bem pensada (sponsor-ready com feature flag), porém não há ferramentas de moderação ou anti-fraude. A integração com iFood está condicionada à disponibilização de API pelo sponsor.`
- **Block Rating (1-5):** `3 [Estrutura de ligas funcional mas simplificada. Sem moderação. Sponsor-ready mas condicionado.]`

---

## 8. Game Operation & Scoring Process
*Focus on reliability and transparency of scoring updates.*

**Score Update Timing:**
- [x] **Real-Time Updates?** (Yes/No): `Sim – Processamento assíncrono via SQS após resultado oficial. Ranking materializado em Redis para leitura em tempo real.`
- [x] **End-of-Match Updates?** (Yes/No): `Sim – "Após ingestão do resultado oficial, executar o reprocessamento automático da pontuação"`
- [ ] **Daily Batch Updates?** (Yes/No): `Não – processamento é por partida, não batch`

**Data Source Reliability:**
- [ ] **Official Match Data Providers Used:** `OPTA (mediante contratação e licenciamento PELO CLIENTE). Custo OPTA é EXTRA e fora do escopo Quality. Fallback manual se OPTA não disponível.`

- **Observations:**
  > `Arquitetura de scoring é bem desenhada: OPTA → SQS → Worker Fargate → PostgreSQL → Redis. Idempotente e assíncrono. Porém, OPTA precisa ser contratada e paga pelo CLIENTE separadamente. Se OPTA não estiver disponível, fallback é CARGA MANUAL do resultado – risco alto de erro humano durante Copa.`
- **Block Rating (1-5):** `3 [Boa arquitetura de scoring, mas dados OPTA são responsabilidade/custo do cliente. Fallback manual é arriscado.]`

---

## 9. Customization, UX & Front-End Design
*Focus on white-label depth, user experience, and design responsibility.*

**Customization Depth:**
- [x] **Full CSS/Theme Customization:** (Yes/No): `Sim – Código-fonte 100% proprietário, customização total`
- [x] **Full UI Customization or Limited Branding?**
  > `Software sob medida – liberdade total de design e UX. Next.js frontend (React).`
- [x] **Custom Domain (CNAME):** (Yes/No): `Sim – Cliente controla domínio e infraestrutura`
- [ ] **Mobile Responsive Score (1-10):** `[Não avaliado – proposta descreve "mobile-first"]`

**Design Ownership:**
- [ ] **Vendor Provides UI/UX Designers?** (Yes/No): `[Não explícito – proposta não lista designer no squad. Quality é primariamente dev.]`
- [x] **Vendor Provides Front-End Development Support?** (Yes/No): `Sim – Squad inclui dev front-end (Next.js/React)`
- [x] **Client Must Supply Design Resources?** (Yes/No): `Sim – Cliente deve fornecer PO e provavelmente designer`

- **Observations:**
  > `Liberdade total de customização (código proprietário), mas o CLIENTE precisa fornecer design/UX. Quality NÃO mencionou designers no squad – foco é em engenharia. Isso significa que o cliente precisa ter time de design próprio ou contratar separadamente.`
- **Block Rating (1-5):** `3 [Liberdade total mas sem design incluso. Cliente precisa fornecer UX/UI.]`

---

## 10. Integration Ecosystem & Partner Connectivity
*Focus on connecting with existing client tech, third-party data sources, and membership systems.*

**Documented APIs:**
- [x] Login/SSO `(E-mail + senha. OAuth/SSO não mencionado explicitamente no MVP. Sponsor validation via API de elegibilidade.)`
- [ ] Partners `[Não informado – integração com sponsors condicionada à disponibilização de docs]`

**Partner Integration:**
- [x] Partner Benefits? (Yes/No) `Sim – "Visualização de benefícios por liga" sponsor-driven`
- [x] Subscription Status? (Yes/No) `Sim – Validação de premium true/false via API sponsor`
- [ ] External Rewards? (Yes/No) `[Não no MVP]`

**External Database Integration:**
- [ ] **Can Connect to Loyalty Programs (e.g., iFood Club)?** (Yes/No): `Condicionado – "a ativação da integração com sponsor ficará condicionada à formalização da parceria e à disponibilização de insumos técnicos"`
- [ ] **Can Connect to Subscription Databases?** (Yes/No): `[Condicionado – não garantido]`

**Access Authorization:**
- [x] **Entry to Premium Leagues Gated by Partner Status?** (Yes/No): `Sim – sponsor_id + feature flag`
- [x] **Entry to Premium Leagues Gated by Subscription Verification?** (Yes/No): `Sim (quando integração ativa)`
- [ ] **Entry to Premium Leagues Gated by External APIs?** (Yes/No): `Condicionado`

**Experience:**
- [ ] Co-branding Support? (Yes/No) `[Não informado]`
- [ ] Exclusive Partner Areas? (Yes/No) `[Não informado]`
- [ ] Track Record with Media/Sponsors? (Yes/No) `Proposta menciona clientes como iFood, mas sem cases específicos de gamificação/esporte`

- **Observations:**
  > `⚠️ Integrações são CONDICIONAIS e representam RISCO. Quality explicitamente lista como dependência: API docs, sandbox, credenciais, SLA – tudo do sponsor. Se o sponsor não entregar a tempo, o MVP fica sem liga premium funcional. Integração CRM/CDP é explicitamente FORA do escopo. Marketing automation FORA do escopo.`
- **Block Rating (1-5):** `2 [Integrações condicionais. CRM/marketing automation fora do escopo. Track record sem cases de esporte/gaming.]`

---

## 11. Channels, Notifications & User Communication
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [ ] **Web Push Notifications:** (Yes/No): `❌ Fora do escopo`
- [ ] **Email Automation:** (Yes/No): `❌ Fora do escopo – "Integração com ferramentas de marketing automation" listada como FORA DO ESCOPO`

**Communication Ownership:**
- [ ] **Who Manages Messaging Templates?** `[Fora do escopo]`
- [ ] **Who Manages Campaign Scheduling?** `[Fora do escopo]`

- **Observations:**
  > `⚠️ ZERO notificações. Quality explicitamente exclui integração com CRM/CDP e marketing automation. Não há push notifications, email automation, ou qualquer canal de re-engajamento. Isso é CRÍTICO para uma plataforma de Copa que depende de engajamento diário.`
- **Block Rating (1-5):** `1 [Nenhum canal de notificação ou re-engajamento. FORA do escopo.]`

---

## 12. Social Sharing & Virality
*Focus on organic growth and viral content generation.*

- [ ] **Native Sharing Features?** (Yes/No): `[Não informado no MVP]`
- [ ] **Social Platforms Supported for Sharing User Answers / Status:** `[Não informado]`

- **Observations:**
  > `Nenhuma funcionalidade de compartilhamento social mencionada na proposta. Convite para ligas privadas usa link/código, mas não há sharing de resultados, palpites ou ranking em redes sociais.`
- **Block Rating (1-5):** `1 [Nenhuma funcionalidade de social sharing]`

---

## 13. Geo-Restriction Capabilities
*Focus on control over geographic participation.*

- [ ] **Registration Restricted to Brazilian Users Only?** (Yes/No): `[Não informado]`
- [ ] **Restriction by Specific IP Ranges?** (Yes/No): `[Não informado – WAF existe mas geo-restriction não mencionado]`

- **Observations:**
  > `Não discutido. Como é software sob medida, pode ser implementado, mas não está no escopo atual.`
- **Block Rating (1-5):** `[Not Assessed – Insufficient Data]`

---

## 14. Roadmap & Evolution Capacity
*Focus on agility and future updates.*

- [x] **Can Close Dedicated Roadmap for Cup?** (Yes/No): `Sim – Squad dedicado ao projeto`
- [x] **Open to Partner-Specific Features?** (Yes/No): `Sim – software sob medida, mas via change request formal`
- [ ] **Risk of Conflict with Other Clients at Peak?** (Low/Med/High): `[Médio] – Profissionais alocados "mediante disponibilidade e aprovação da Quality". Risco de disputar recursos com outros clientes.`
- **Timelines (Avg Days):**
    - Setup Technical: `Kick-off: 30-45 dias após assinatura de contrato`
    - Customization: `2 meses de desenvolvimento`
    - Go-Live: `04 de Maio de 2026. ⚠️ Com kick-off de 30-45 dias + 2 meses dev = contrato precisa ser assinado AGORA (fev 2026) para viabilizar.`

- **Observations:**
  > `⚠️ TIMELINE CRÍTICA: Kick-off leva 30-45 dias da assinatura. + 2 meses de dev. Para go-live em 04/maio, contrato precisaria ser assinado no máximo início de fevereiro. Em 20/02, já está no limite. Além disso, Fase 2 (quiz, missões, sorteios) NÃO tem cronograma nem orçamento. A proposta entrega apenas o MVP core. Profissionais alocados "mediante disponibilidade" = risco de não conseguir montar squad a tempo.`
- **Block Rating (1-5):** `2 [Timeline muito apertada. MVP only. Fase 2 sem cronograma. Risco de disponibilidade de profissionais.]`

---

## 15. Commercial, Contractual & Financial Risk
*Focus on cost structure, lock-in risks, and financial predictability.*

**Cost Structure:**
- [x] **Setup Fee Range:** `Desenvolvimento MVP: R$ 444.205,98 (2 meses) + Sustentação Copa: R$ 182.571,52 (45 dias) = TOTAL: R$ 626.777,50`
- [x] **Pricing Model:** `Projeto fechado (squad dedicado) + Sustentação por período. Entrada de 15% + mensalidades.`

**Cost Variability & Budget Risk:**
- [x] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `SIM – ⚠️ Custos de infraestrutura AWS são 100% do CLIENTE e variam com tráfego. Quality não assume nenhum custo de cloud.`
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `SIM – OPTA é contratada e paga pelo cliente separadamente.`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `SIM – "Qualquer mudança relevante de escopo será formalmente analisada e refletida em revisão de estimativa." Change request formal.`

**Contract Terms:**
- [ ] **Minimum Contract Duration (Months):** `Projeto: ~3.5 meses (dev + sustentação). Aviso de 30 dias para mudanças no squad.`
- [ ] **Early Termination Penalties?** (Yes/No): `Sim – Entrada de 15% não reembolsável: "em caso de rescisão antes do abatimento, os valores não serão devolvidos"`
  > `15% do projeto = ~R$ 66.6k não reembolsável em caso de rescisão`

**Platform Dependency & Exit Risks:**
- [ ] **Migration Complexity:**
  > `ZERO dependência de plataforma. Código-fonte e infraestrutura são 100% do cliente. Migração não aplicável.`
- [x] **Data Portability Guarantees?** (Yes/No): `Sim – Tudo pertence ao cliente por design.`

- **Observations:**
  > `💰 CUSTOS TOTAIS ESTIMADOS:
  > - Desenvolvimento MVP: R$ 444.205,98
  > - Sustentação Copa (45 dias): R$ 182.571,52
  > - OPTA (licenciamento): ❓ Custo do cliente
  > - Infraestrutura AWS: ❓ Custo do cliente (variável com tráfego)
  > - Designer/UX: ❓ Não incluso
  > - Notificações/CRM: ❓ Não incluso
  > - Fase 2 (quiz, missões, sorteios): ❓ Sem orçamento
  > 
  > TOTAL VISÍVEL: R$ 626.777,50 (~$105k USD)
  > TOTAL REAL ESTIMADO (com infra + OPTA + design + Fase 2): Provavelmente R$ 1.2M+ (~$200k+ USD)
  > 
  > O preço visível é competitivo, mas os custos ocultos são significativos. O modelo transfere todo o risco financeiro de infra/escala para o cliente.`
- **Block Rating (1-5):** `2 [Preço visível baixo mas custos ocultos altos. Todo risco financeiro de infra transferido ao cliente. MVP não inclui features essenciais.]`

---

## 16. Team, Experience & References
*Focus on supplier maturity.*

- [x] **Years in Market:** `37 anos (fundada em 1989)`
- [ ] **Previous World Cup/Massive Event Cases:** `❌ ZERO cases de gaming/predictor/gamificação em eventos esportivos massivos. Quality é software house de TI/e-commerce.`
- [ ] **Reference Contacts Provided?** (Yes/No): `Não – Proposta lista clientes corporativos (Digital Business, Digital Commerce) mas sem cases específicos relevantes.`

- **Observations:**
  > `Quality é uma empresa sólida e madura (37 anos, listada na B3, BNDES acionista, operações em 5 países). Porém, seu DNA é TI corporativa, outsourcing e e-commerce – NÃO gaming, gamificação ou eventos esportivos. Não possui nenhum case de plataforma de predição ou engagement em escala Copa. A competência técnica existe, mas a experiência no domínio é ZERO.`
- **Block Rating (1-5):** `2 [Empresa madura mas zero experiência no domínio de gaming/esporte/engagement massivo]`

---

# Executive Summary & Recommendation

> **Data: 2026-02-20** – Baseado exclusivamente na proposta formal (Nº 101876).

## Executive Summary
Quality Digital é uma **software house brasileira** (listada na B3, fundada em 1989, BNDES acionista) que propõe construir o Bolão Digital do zero como **software proprietário** para a Cazé TV/Omni55. O modelo é fundamentalmente diferente dos demais fornecedores: Quality entrega **mão de obra de desenvolvimento + código-fonte**, não uma plataforma pronta.

A proposta cobre um **MVP limitado** por R$ 444k (dev) + R$ 182k (sustentação 45 dias) = **R$ 626.777,50 (~$105k USD)** – porém com custos ocultos significativos (infra AWS, OPTA, design, notificações, Fase 2). O MVP inclui apenas: cadastro, palpites (placar exato), ligas (base/premium/privadas), ranking, e integração OPTA. **Todas as features de gamificação** (quiz, missões, lucky numbers, sorteios, badges) estão **FORA do MVP** como "Fase 2" sem orçamento.

A arquitetura técnica é moderna e bem desenhada (Next.js, NestJS, AWS Fargate, Aurora PostgreSQL, Redis, SQS), mas nunca foi testada para escala Copa. A empresa não possui nenhuma experiência prévia em gaming, gamificação ou eventos esportivos massivos.

## Automated Risk Flags
| Category | Flag Condition | Risk Level | Alert |
| :--- | :--- | :--- | :--- |
| **Scale** | `highest_participants_in_single_game` < 100k | **CRITICAL** | "No history of massive single-event scale." |
| **Scale** | `platforms_supported.app_ios` == No | **HIGH** | "Missing iOS Native App." |
| **Scale** | `platforms_supported.app_android` == No | **HIGH** | "Missing Android Native App." |
| **Scale** | `recent_load_test_evidence` == No | **HIGH** | "No recent proof of load capability." |
| **Integrations** | `apis_documented.partners` == No | **HIGH** | "Partner ecosystem integration blocked by lack of API." |
| **Product** | `missions_challenges` == No | **HIGH** | "Quiz/Missions are placeholder only – zero engagement features in MVP." |
| **UX** | `mobile_responsive_score` == [Not Assessed] | **MEDIUM** | "Mobile experience not evaluated." |

## Key Risks
| Risk Area | Severity | Description |
| :--- | :--- | :--- |
| **Scale / Experience** | **⚠️ CRITICAL** | **Zero massive-event experience.** Quality has NEVER operated a gaming platform at World Cup scale. DNA is corporate IT/e-commerce outsourcing. |
| **MVP Scope** | **⚠️ CRITICAL** | **MVP is minimal.** Quiz, missions, lucky numbers, sorteios, badges, social sharing – ALL out of scope. Only delivers basic predictor + leagues + ranking. |
| **Native Apps** | **HIGH** | **No iOS/Android apps.** Explicitly excluded from scope. Web responsive only. |
| **Notifications** | **HIGH** | **Zero re-engagement.** No push notifications, no email automation, no CRM integration. All explicitly out of scope. |
| **Hidden Costs** | **HIGH** | **Real cost >> R$ 626k.** AWS infra (variable), OPTA licensing, designer/UX (not included), Fase 2 features – all are extra. Real total likely R$ 1.2M+. |
| **Timeline** | **HIGH** | **Go-live May 4 is at extreme risk.** Kickoff takes 30-45 days + 2 months dev. Contract needed by early Feb. Already past deadline. |
| **Operational Risk** | **HIGH** | **Client operates everything.** Quality builds and exits. Client manages infra, support, user issues, scaling, war room. |
| **Sponsor Integration** | **MEDIUM** | **Conditional.** iFood integration depends on sponsor providing API docs, sandbox, credentials. If unavailable, falls back to Base only. |

## Key Strengths
| Strength Area | Rating | Description |
| :--- | :--- | :--- |
| **Data Ownership** | ⭐⭐⭐⭐⭐ | 100% client-owned: code, data, infrastructure. Zero lock-in. Best data ownership model. |
| **LGPD / Security** | ⭐⭐⭐⭐ | Best LGPD implementation detail among all suppliers. Consent audit, data masking, WAF, TLS, encryption. |
| **Architecture** | ⭐⭐⭐⭐ | Modern, well-designed stack (Next.js, NestJS, AWS Fargate, Aurora, Redis, SQS). Cloud-native. |
| **Local Presence** | ⭐⭐⭐ | Brazilian company, RJ/SP offices, Portuguese native. |
| **Corporate Maturity** | ⭐⭐⭐ | 37 years, B3-listed, BNDES-backed. Solid corporate governance. |

## Block Ratings Summary
| Block | Rating | Status |
| :--- | :--- | :--- |
| 1. Robustness, Scale & Reliability | **2/5** | Zero proven scale. No apps. |
| 2. Local Support & Operational Coverage | **3/5** | Local but body-shop model. Sustentação 45d. |
| 3. User Support & Incident Management | **2/5** | Client responsibility |
| 4. Security, LGPD, Governance | **4/5** | Best LGPD detail. Age verification missing. |
| 5. Data Ownership, Access & Portability | **5/5** | 100% client-owned |
| 6. Core Product Features | **2/5** | MVP only – gamification all Fase 2 |
| 7. League Management & Premium | **3/5** | Functional but simplified |
| 8. Game Operation & Scoring | **3/5** | Good architecture. OPTA cost on client. |
| 9. Customization, UX & Front-End | **3/5** | Total freedom but no designer included |
| 10. Integration Ecosystem | **2/5** | Conditional. CRM/marketing excluded. |
| 11. Notifications & Communication | **1/5** | Zero. All out of scope. |
| 12. Social Sharing & Virality | **1/5** | None |
| 13. Geo-Restriction | **N/A** | Not assessed |
| 14. Roadmap & Evolution | **2/5** | Tight timeline. Fase 2 unbudgeted. |
| 15. Commercial & Financial | **2/5** | Low visible cost, high hidden costs |
| 16. Team, Experience & References | **2/5** | Mature company, zero domain experience |
| **Average (assessed blocks)** | **2.5/5** | |

## Final Recommendation
**❌ DISCARD – Fundamental Misalignment with Project Needs**

Per system rules: **CRITICAL risk triggered** (no history of massive scale + MVP scope too limited). Robustness rating < 3. Multiple HIGH risks.

Quality Digital is a **competent software house** but is **fundamentally the wrong type of supplier** for this project. The project needs a **turnkey gamification platform** with proven massive-event experience, not a body-shop building from scratch.

**Why DISCARD:**
1. **Wrong model:** Body shop / outsourcing ≠ managed product platform. Client assumes ALL operational risk.
2. **MVP too limited:** Delivers ~40% of required features. All gamification (quiz, missions, prizes, badges) excluded.
3. **Zero domain experience:** 37 years in IT, zero in gaming/sports/gamification at scale.
4. **Hidden costs:** Visible R$ 626k but real cost likely R$ 1.2M+ once infra, OPTA, design, Fase 2 are added.
5. **Timeline impossible:** Kick-off 30-45 days + 2 months. Contract needed in early Feb – already past.
6. **No engagement stack:** Zero notifications, zero CRM, zero social sharing. Platform has no way to re-engage users.

**Where Quality COULD fit:**
Quality could be a **strong complementary partner** for building custom integrations, additional features, or a dedicated mobile app – working alongside a primary SaaS platform provider (like Genius Sports or Fan Arena).
