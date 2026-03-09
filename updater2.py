import re

file_path = "G:\\My Drive\\Rodrigo\\Antigravity\\supplier-evaluation-system\\evaluations\\low6_evaluation.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Block 1: Intro / 1. Robustness, Scale & Reliability 
# Add the Sportsbet case study to robustness and references
content = re.sub(
    r'\*\*Peak Performance & Proven Scale:\*\*.*?Maximum Simultaneous Users Tested:\*\* `>1\.000\.000 \(BBC Champions League\)`',
    '''**Peak Performance & Proven Scale:**
- [x] **Highest Participants Record (Single Game):** `~2.000.000 registrados (Bet365 América)`
- [x] **Strategy for 15M Total Users:**
  > `A meta do projeto Cazé foi corrigida para 15M de usuários totais (não 15M simultâneos). Low6 demonstrou escalabilidade via Azure e experiência de >1M de concorrentes simultâneos na BBC (Champions League). Não veem escala como um problema e tudo será validado via UAT na fase de entrega.`
- [x] **Maximum Simultaneous Users Tested:** `>1.000.000 (BBC Champions League)`
- [x] **Success Cases under High Load:** `Case Sportsbet (App #1 Austrália, pico de engajamento diário de 1.7 logins/dia e sessões de 6 min).`''',
    content, flags=re.DOTALL
)

# Update Block 11 Channels
content = re.sub(
    r'\*\*Channels, Notifications & User Communication\*\*.*?- \*\*Block Rating \(1-5\):\*\* `\[4\]`',
    '''**Channels, Notifications & User Communication**
*Focus on user re-engagement and communication ownership.*

**Notification Channels:**
- [x] **Web Push Notifications:** (Yes/No): `[Sim, via parceiro CRM XtremePush]`
- [x] **Email & SMS Automation:** (Yes/No): `[Sim, via parceiro CRM XtremePush]`

**Communication Ownership:**
- [x] **Who Manages Messaging Templates?** `[Cliente gerencia, plataforma via Xtreme Push (CRM parceiro)]`
- [x] **Who Manages Campaign Scheduling?** `[Cliente no portal CRM]`

**CRM Pricing Details (XtremePush Add-On):**
- **MarComm Project Set-Up:** `$7,500 (Inclui setup de campanhas automatizadas, emails HTML, templates de Win Back, resumos de jogo, etc. Total de 11 dias de trabalho).`
- **MarComm Project Delivery (Resource):** `Recurso de marketing por 3 dias/mês (primeiros 3 meses) e 1 dia/mês nos seguintes. (Day rate: $650).`
- **MAU Passthrough Cost (Monthly):** `Escalona por MAU (ex: $925 para 0-50k; $1650 para 50-100k MAU).`
- **Volume Passthrough Cost:** `Escalona por volume de envios (ex: $600 até 250k; $1850 até 1M). *Obs: Para 15M de usuários, este custo mensal pode ser bastante elevado e precisa ser projetado na curva de tráfego.*`

- **Observations:**
  > A Low6 possui integração robusta desenhada com a "Xtreme Push" para CRM e réguas de relacionamento prontas (Welcome, Password, Contest Open, Win Back). O setup fee de $7.500 é razoável, mas os custos variáveis baseados em MAUs e Volume de Disparos precisarão ser muito bem dimensionados para uma base de 15 Milhões (os tiers mostrados no pricing param em 1M de envios).
- **Block Rating (1-5):** `[3]` — *Nota ajustada devido ao risco de custo variável alto para a régua de 15M.*''',
    content, flags=re.DOTALL
)

# Update Block 15 Models
content = re.sub(
    r'\*\*Cost Variability & Budget Risk:\*\*.*?Can Costs Increase Due to Extra Features\?\*\* \(Yes/No\): `\[Yes\]` — Suporte B2C, SSO de parceiros adicionais e features extras teriam custo separado\.',
    '''**Cost Variability & Budget Risk:**
- [x] **Can Costs Increase Due to Traffic Spikes?** (Yes/No): `[Sim — hosting é pass-through, então custos Azure escalam com uso]`
- [ ] **Can Costs Increase Due to API Usage?** (Yes/No): `[Não discutido]`
- [x] **Can Costs Increase Due to Extra Features?** (Yes/No): `[Yes]` — Suporte B2C (£5k-7k/mês), integrações adicionais de SSO e a régua de CRM (XtremePush) que possui precificação variável por MAU e volume.

**Added Value Games (From Presentation):**
- Acesso ao portfólio de Gamification: `Bracket, Squads, Spin-2-Win, Picks, Over/Under, Last One Standing, Retro Arcade Games.` O modelo de plataforma All-in-1 deles viabiliza incluir múltiplos jogos além do bolão tradicional.''',
    content, flags=re.DOTALL
)


# Update Block 16 References
content = re.sub(
    r'- \*\*Observations:\*\*\s+> Low6 possui experiência relevante em plataformas de previsões esportivas \(Bet365, NHL, DraftKings\)\. No entanto, não possuem experiência documentada com eventos da magnitude de uma Copa do Mundo FIFA\..*?- \*\*Block Rating \(1-5\):\*\* `\[3\]`',
    '''- **Observations:**
  > Low6 possui forte tração com F2P Games, sendo premiada multiplamente (EGR, SBC) e listada como a #23 empresa de crescimento mais rápido do UK. Possuem cases massivos comprovados: Bet365 na América e um case espetacular com a Sportsbet na Austrália para a Copa do Mundo 2022 (App #1 gratuito na Austrália, 4x média de logins diários, 34% signups via refer-a-friend). Isso valida fortemente a tese de aquisição F2P para a Copa.
- **Block Rating (1-5):** `[5]` — Validação categórica com cases premiados e números expressivos na Austrália.''',
    content, flags=re.DOTALL
)



# Update the Score Table!
content = re.sub(
    r'\| 1\. Robustness, Scale & Reliability \| 4 \|\n\| 2\. Local Support & Operational Coverage \| 3 \|\n\| 3\. User Support & Incident Management \| 2 \|\n\| 4\. Security, LGPD, Governance & Compliance \| 3 \|\n\| 5\. Data Ownership, Access & Portability \| 5 \|\n\| 6\. Core Product Features & Functional Readiness \| 4 \|\n\| 7\. League Management & Premium Infrastructure \| 4 \|\n\| 8\. Game Operation & Scoring Process \| 3 \|\n\| 9\. Customization, UX & Front-End Design \| 3 \|\n\| 10\. Integration Ecosystem & Partner Connectivity \| 3 \|\n\| 11\. Channels, Notifications & User Communication \| 4 \|\n\| 12\. Social Sharing & Virality \| 3 \|\n\| 13\. Geo-Restriction Capabilities \| 2 \|\n\| 14\. Roadmap & Evolution Capacity \| 4 \|\n\| 15\. Commercial, Contractual & Financial Risk \| 3 \|\n\| 16\. Team, Experience & References \| 3 \|',
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
| 11. Channels, Notifications & User Communication | 3 |
| 12. Social Sharing & Virality | 3 |
| 13. Geo-Restriction Capabilities | 2 |
| 14. Roadmap & Evolution Capacity | 4 |
| 15. Commercial, Contractual & Financial Risk | 3 |
| 16. Team, Experience & References | 5 |''',
    content
)

content = content.replace('| **Média Geral** | **3.31** |', '| **Média Geral** | **3.37** |')

content = content.replace(
    '''3. **Roadmap & Evolution (4/5)** — Modelo de evolução incremental; plataforma reutilizável para outros campeonatos''',
    '''3. **Team, Experience & References (5/5)** — Cases absurdos de crescimento F2P (Sportsbet na Austrália) e premiações em série como Supplier of the Year. Muito focado em aquisição e retenção gamificada.'''
)

content = content.replace(
    '''### Gaps Críticos para Próxima Reunião
1. **Modelagem Fechada de Custos Extras** — Mensurar impacto de B2C Support (£5k-7k) + Xtreme Push CRM (Setup + per message) + APIs.
2. **Provedor de Dados Opcional** — Low6 tem fornecedor padrão de mercado no pricing ou a CazéTV fecha Opta em separado?
3. **App vs. Web (Engajamento)** — Aceite final se iremos sem push notification nativo com app stores.
4. **LGPD Consentimento** — Aprovação jurídica sobre os termos simplificados no Checkbox de Idade/Registro perante órgãos brasileiros.''',
    '''### Gaps Críticos para Próxima Reunião
1. **Modelagem de Custos CRM Variáveis (XtremePush)** — Mensurar impacto financeiro do CRM (MAU e Volume) escalado para 15 Milhões de usuários, visto que as tabelas enviadas têm teto em 1M no pricing sheet. (Pode inviabilizar o add-on se não houver um *Unlimited Tier*).
2. **Provedor de Dados Opcional** — Low6 tem fornecedor padrão de mercado no pricing ou a CazéTV fecha Opta em separado?
3. **App vs. Web (Engajamento)** — Aceite final se iremos sem push notification nativo com app stores (dependendo ainda mais do CRM).
4. **LGPD Consentimento** — Aprovação jurídica sobre os termos simplificados no Checkbox de Idade/Registro perante órgãos brasileiros.'''
)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated low6_evaluation file successfully.")
