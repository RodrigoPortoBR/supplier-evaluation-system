import re

file_path = "G:\\My Drive\\Rodrigo\\Antigravity\\supplier-evaluation-system\\evaluations\\low6_evaluation.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace block 1
content = re.sub(
    r'\*\*Peak Performance & Proven Scale:\*\*.*?Maximum Simultaneous Users Tested:\*\* `100\.000 \(teste com DraftKings\)`',
    '''**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `~2.000.000 registrados (Bet365 América)`
- [x] **Strategy for 15M Total Users:**
  > `A meta do projeto Cazé foi corrigida para 15M de usuários totais (não 15M simultâneos). Low6 demonstrou escalabilidade via Azure e experiência de >1M de concorrentes simultâneos na BBC (Champions League). Não veem escala como um problema e tudo será validado via UAT na fase de entrega.`
- [x] **Maximum Simultaneous Users Tested:** `>1.000.000 (BBC Champions League)`''',
    content, flags=re.DOTALL
)

# Replace block 1 obs
content = re.sub(
    r'- \*\*Observations:\*\*\s+> Low6 opera o jogo da Bet365 na América com ~2M de usuários registrados, 10M de entradas e 70M de submissões\. Demonstrou confiança na escalabilidade\. Utilizam Azure com equipe de DevOps dedicada\. Realizaram teste de 100k concorrentes com DraftKings\. Não oferecem app nativo — apenas web responsiva\. A ausência de app nativo pode ser uma limitação para engajamento via push notifications, mas simplifica o deploy e a manutenção\. Testes de carga \(UAT \+ load testing\) estão incluídos no escopo como parte do processo de entrega\.\s+- \*\*Block Rating \(1-5\):\*\* `\[3\]`',
    '''- **Observations:**
  > Low6 opera o jogo da Bet365 na América e possui case de >1 milhão de usuários simultâneos na BBC. Demonstrou muita confiança na escalabilidade para a meta de 15M de usuários totais. Utilizam Azure com equipe de DevOps dedicada. Não oferecem app nativo — apenas web responsiva. A ausência de app nativo limita push notifications nativo. Testes de carga (UAT) estão incluídos no escopo.
- **Block Rating (1-5):** `[4]`''',
    content, flags=re.DOTALL
)

# Replace Block 2 and 3
content = re.sub(
    r'\*\*Support Availability:\*\*.*?Block Rating \(1-5\):\*\* `\[2\]`',
    '''**Support Availability:**
- [x] **24/7 Support Guaranteed During Peak Periods?** (Yes/No): `[Sim, como serviço adicional]` — Live chat B2C com custo extra avaliado em £5k-7k/mês.
- [x] **SLA Response Times for Critical Incidents:** `[Sistema de tickets P1/P2/P3 com SLA esperado ≤ 10 minutos]` — Confirmado SLA rápido para escalonamento direto aos devs.
- [ ] **Dedicated War-Room Structure During Major Events?** (Yes/No): `[Não informado]`

**Operational Escalation Flow:**
- [x] **L1 Support (User Issues) – Handled by:** `[Low6 (Serviço Extra)]` — Possuem equipe interna de Customer Service e game management. Custo adicional de £5k-7k/mês.
- [x] **L2 Technical Issues – Handled by:** `[Low6 — equipe técnica interna]`
- [x] **L3 Infrastructure Failures – Handled by:** `[Low6 DevOps + Azure]`

- **Observations:**
  > Low6 possui capacidade plena de gerenciar o L1 B2C via live chat por uma taxa extra de aprox. £5k-7k por mês. Qualquer issue escala direto para a equipe de infra/dev via Slack/tickets P1-P3 com SLA de resposta esperado abaixo de 10 minutos. O suporte tem custo, mas resolve internamente o funil.
- **Block Rating (1-5):** `[3]`''',
    content, count=1, flags=re.DOTALL
)

# Replace block 4 Age Verification
content = re.sub(
    r'\*\*Age Verification & Youth Safety \(13\+ Users\):\*\*.*?\*\*Block Rating \(1-5\):\*\* `\[3\]`',
    '''**Age Verification & Youth Safety (13+ Users):**
- [x] **Age Verification Flow:**
  > `Podem implementar um simples checkbox no opt-in primário. A verificação KYC oficial é feita apenas no momento de claims (vencimento do prêmio).`
- [ ] **Consent Mechanisms for Minors:**
  > `[Não detalhado]`
- [ ] **Special Data Protection Policies for Under-18 Users?** (Yes/No): `[Não informado]`
- [ ] **Parental Consent Options Available?** (Yes/No): `[Não informado]`

- **Observations:**
  > ISO 27001 confirmado. A questão da LGPD/Dados de menores ainda precisa de análise jurídica aprofundada, mas o fluxo de idade proposto por eles é simplificado na entrada (checkbox) e rigoroso no final (kyc para resgate de prêmios), o que resolve a fluidez inicial de registro.
- **Block Rating (1-5):** `[3]`''',
    content, flags=re.DOTALL
)


# Replace Block 5
content = re.sub(
    r'\*\*Data Ownership, Access & Portability\*\*.*?\*\*Block Rating \(1-5\):\*\* `\[1\]` ⚠️ Dados insuficientes para avaliação\.',
    '''**Data Ownership, Access & Portability**
*Focus on guaranteeing full strategic control over user data and long-term usability.*

**Data Ownership:**
- [x] **All User Data Fully Owned by Client?** (Yes/No): `[Sim]` — Confirmado expressamente. Low6 não retém nenhum direito. CazéTV é total dona.
- [x] **Any Restrictions on Data Usage?** (Yes/No): `[No]`
  > `A Low6 atua estritamente como processadora de dados.`

**Data Access:**
- [x] **Access to Full User Database?** (Yes/No): `[Sim]`
- [x] **Access to Behavioral Event Data?** (Yes/No): `[Sim]`
- [x] **Access to Prediction History?** (Yes/No): `[Sim]`

**Data Extraction Methods:**
- [x] **Direct Platform Exports?** (Yes/No): `[Sim]` — Planilhas protegidas ou acesso ao Snowflake.
- [x] **APIs for Real-Time Extraction?** (Yes/No): `[Sim]` — Low6 utiliza Fivetran transferindo para um Snowflake onde o cliente terá acesso total.
- [x] **Scheduled Automated Data Dumps?** (Yes/No): `[Não documentado, mas inerente ao Snowflake]`

**Exit Scenario (Critical):**
- [x] **If Partnership Ends – What Happens to User Accounts?**
  > `Exportadas para a CazéTV sem retenção pela Low6.`
- [x] **If Partnership Ends – What Happens to Historical Data?**
  > `CazéTV leva consigo todo o banco de dados e todos os dashboards gerados.`
- [x] **If Partnership Ends – What Happens to Behavioral Insights?**
  > `Dashboards inclusos na transição/fim do contrato.`
- [x] **Full Data Export Guaranteed on Exit?** (Yes/No): `[Sim]`

- **Observations:**
  > **Risco mitigado com sucesso.** Nas reuniões de follow-up a Low6 esclareceu que todo o dado e metadado gerado (incluindo painéis de analytics) é de posse total do cliente, atuando a Low6 puramente como processadora via Snowflake. Sem atrito no cenário de saída.
- **Block Rating (1-5):** `[5]`''',
    content, flags=re.DOTALL
)

# Replace Block 8 Data Source
content = re.sub(
    r'\*\*Game Operation & Scoring Process\*\*.*?- \*\*Block Rating \(1-5\):\*\* `\[1\]` ⚠️ Dados insuficientes para avaliação\.',
    '''**Game Operation & Scoring Process**
*Focus on reliability and transparency of scoring updates.*

**Score Update Timing:**
- [x] **Real-Time Updates?** (Yes/No): `[Sim]` — Possuem capacidade via script automatizado integrado a APIs.
- [x] **End-of-Match Updates?** (Yes/No): `[Sim]`
- [ ] **Daily Batch Updates?** (Yes/No): `[Não avaliado]`

**Data Source Reliability:**
- [x] **Official Match Data Providers Used:** `[Confirmado uso de feeds via API para automatização, requer API do lado ou comprada pela Low6]`

- **Observations:**
  > Atualizações de placares automáticas via integração de API, evitando intervenção manual. Cliente (CazéTV) precisará garantir a conexão de dados (sinal ou feed parceiro), ou caso não tenha, solicitar à Low6.
- **Block Rating (1-5):** `[3]`''',
    content, flags=re.DOTALL
)

# Replace Block 11 Channels
content = re.sub(
    r'\*\*Channels, Notifications & User Communication\*\*.*?- \*\*Block Rating \(1-5\):\*\* `\[1\]` ⚠️ Dados insuficientes para avaliação\.',
    '''**Channels, Notifications & User Communication**
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [x] **Web Push Notifications:** (Yes/No): `[Sim, via parceiro CRM]`
- [x] **Email & SMS Automation:** (Yes/No): `[Sim, via parceiro CRM]`

**Communication Ownership:**
- [x] **Who Manages Messaging Templates?** `[Cliente gerencia, plataforma via Xtreme Push (CRM parceiro)]`
- [x] **Who Manages Campaign Scheduling?** `[Cliente no portal CRM]`

- **Observations:**
  > A Low6 possui integração com a "Xtreme Push" para CRM e réguas de relacionamento (Push, e-mail, etc.). É um aditivo cobrado separadamente (setup fee + por mensagem), ou podem integrar o CRM proprietário do cliente.
- **Block Rating (1-5):** `[4]`''',
    content, flags=re.DOTALL
)

# Update the Score Table!
content = re.sub(
    r'\| 1\. Robustness, Scale & Reliability \| 3 \|\n\| 2\. Local Support & Operational Coverage \| 2 \|\n\| 3\. User Support & Incident Management \| 2 \|\n\| 4\. Security, LGPD, Governance & Compliance \| 3 \|\n\| 5\. Data Ownership, Access & Portability \| 1 ⚠️ \|\n\| 6\. Core Product Features & Functional Readiness \| 4 \|\n\| 7\. League Management & Premium Infrastructure \| 4 \|\n\| 8\. Game Operation & Scoring Process \| 1 ⚠️ \|\n\| 9\. Customization, UX & Front-End Design \| 3 \|\n\| 10\. Integration Ecosystem & Partner Connectivity \| 3 \|\n\| 11\. Channels, Notifications & User Communication \| 1 ⚠️ \|',
    '''| 1. Robustness, Scale & Reliability | 4 |
| 2. Local Support & Operational Coverage | 3 |
| 3. User Support & Incident Management | 2 |
| 4. Security, LGPD, Governance & Compliance | 3 |
| 5. Data Ownership, Access & Portability | 5 |
| 6. Core Product Features & Functional Readiness | 4 |
| 7. League Management & Premium Infrastructure | 4 |
| 8. Game Operation & Scoring Process | 3 |
| 9. Customization, UX & Front-End Design | 3 |
| 10. Integration Ecosystem & Partner Connectivity | 3 |
| 11. Channels, Notifications & User Communication | 4 |''',
    content
)

content = content.replace('| **Média Geral** | **2.63** |', '| **Média Geral** | **3.31** |')

content = content.replace(
    '''### Risk Flags
| Category | Risk Level | Alert |
|----------|-----------|-------|
| **Scale** | HIGH | Missing iOS Native App |
| **Scale** | HIGH | Missing Android Native App |
| **Scale** | MEDIUM | No local support time/language |
| **Data** | ⚠️ CRITICAL | Nenhuma discussão sobre data ownership, portability ou exit scenario |
| **Operations** | ⚠️ CRITICAL | Provedor de dados esportivos oficiais não identificado |
| **Engagement** | HIGH | Canais de notificação/re-engajamento não discutidos |
| **UX** | MEDIUM | Sem app nativo — apenas web responsiva |''',
    '''### Risk Flags
| Category | Risk Level | Alert |
|----------|-----------|-------|
| **Scale** | HIGH | Missing iOS Native App |
| **Scale** | HIGH | Missing Android Native App |
| **Scale** | MEDIUM | No local support time/language |
| **Operations** | MEDIUM | Provedor de dados esportivos precisa ser contratado pela CazéTV |
| **UX** | MEDIUM | Sem app nativo — apenas web responsiva |
| **Costs** | MEDIUM | Diversas features B2C, CRM e infra extra cobradas à parte |'''
)

content = content.replace(
    '''### PMO Verdict
> **PROCEED WITH CAUTION (PoC recomendado)** — Low6 demonstra forte capacidade técnica em plataformas de previsões esportivas, com cases relevantes (Bet365, NHL). Preço competitivo e modelo de evolução incremental são atrativos. Porém, múltiplos pontos críticos não foram abordados nas reuniões (data ownership, provedor de dados, notificações, LGPD detalhada, suporte local), e a ausência de app nativo pode ser limitante para uma audiência de 15M. Recomenda-se uma terceira reunião focada exclusivamente nos gaps identificados antes de decidir.

### Gaps Críticos para Próxima Reunião
1. **Data Ownership & Portability** — Quem é dono dos dados? Export garantido na saída?
2. **Provedor de Dados Esportivos** — Qual fonte oficial de resultados? (Opta, Sportradar, outro?)
3. **Estratégia de Notificações** — Push, email, SMS? Sem app nativo, como re-engajar?
4. **LGPD Específica** — Residência dos dados, verificação de idade, consentimento parental
5. **Suporte B2C Detalhado** — Custo, SLA, idioma, horário de cobertura
6. **Testes de Carga** — Pode testar acima de 1M concorrentes? Relatórios de Bet365?
7. **Geo-restrição** — Limitação por país/IP necessária?
8. **App vs. Web** — Impacto na experiência sem push notifications nativas''',
    '''### PMO Verdict
> **PROCEED WITH CONDITIONAL APPROVAL** — Low6 mitigou os principais riscos críticos na reunião mais recente (data ownership via Snowflake, notificações via Xtreme Push, suporte B2C terceirizado, verificações de idade em claims). Possuem um case robusto da BBC (>1M simultâneos) para escalabilidade. O produto já contém as mecânicas pedidas, mas o custo B2C extra e CRM requer revisão orçamentária. As restrições remanescentes referem-se sobretudo à ausência de app nativo e integração do feed oficial de dados a ser fornecido. Time de DEV aprova tecnicamente, condicionando avanço aos cálculos dos Ad-Ons identificados.

### Gaps Críticos para Próxima Reunião
1. **Modelagem Fechada de Custos Extras** — Mensurar impacto de B2C Support (£5k-7k) + Xtreme Push CRM (Setup + per message) + APIs.
2. **Provedor de Dados Opcional** — Low6 tem fornecedor padrão de mercado no pricing ou a CazéTV fecha Opta em separado?
3. **App vs. Web (Engajamento)** — Aceite final se iremos sem push notification nativo com app stores.
4. **LGPD Consentimento** — Aprovação jurídica sobre os termos simplificados no Checkbox de Idade/Registro perante órgãos brasileiros.'''
)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated low6_evaluation file successfully.")
