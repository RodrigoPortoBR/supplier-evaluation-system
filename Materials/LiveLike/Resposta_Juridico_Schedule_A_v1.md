# Resposta ao Jurídico — Validação Técnica e Operacional do Schedule A
**Data:** 09/04/2026  
**De:** Rodrigo (PMO / CazéTV × LiveMode)  
**Para:** Jurídico CazéTV  
**Ref.:** Schedule A — Bolão Copa do Mundo 2026 × LiveLike

---

## Contexto

Conforme solicitado, realizamos a revisão técnica e operacional do Schedule A gerado pelo jurídico. O documento está bem estruturado e cobre os principais aspectos do produto. Abaixo listamos os pontos que precisam ser **corrigidos**, **complementados** ou **esclarecidos** antes da assinatura.

---

## 1. CORREÇÕES OBRIGATÓRIAS — Devem ser ajustadas no documento antes da assinatura

### 1.1 Lógica de Pontuação — AUSENTE NO DOCUMENTO

O Schedule A menciona "scoring logic mutuamente acordada" (Seção 3.2), mas não a define. Essa é a regra central do produto. A pontuação acordada internamente é a seguinte e deve ser incluída como Apêndice ou tabela na Seção 3.2:

**Fase de Grupos:**

| Resultado do Palpite | Pontos |
|---|---|
| Placar exato | 50 pts |
| Vencedor + nº de gols do vencedor | 35 pts |
| Empate (qualquer placar) | 25 pts |
| Vencedor (sem acertar gols) | 10 pts |
| Errou vencedor / empate | 0 pts |

> **Regra especial:** Jogos do Brasil na fase de grupos valem **2x** os pontos acima.

**Multiplicadores por fase (base: pontos da fase de grupos × multiplicador):**

| Fase | Multiplicador | Placar exato | Vencedor + gols | Empate | Vencedor |
|---|---|---|---|---|---|
| Fase de grupos | 1,0x | 50 | 35 | 25 | 10 |
| 2ª fase / Mata-mata | 1,2x | 60 | 42 | 30 | 12 |
| Oitavas de final | 1,4x | 70 | 49 | 35 | 14 |
| Quartas de final | 1,6x | 80 | 56 | 40 | 16 |
| Semifinal / 3º e 4º lugar | 1,8x | 90 | 63 | 45 | 18 |
| Final | 2,0x | 100 | 70 | 50 | 20 |

**Critérios de desempate no leaderboard (nessa ordem):**
1. Quantidade de placares exatos
2. Quantidade de perguntas respondidas no trivia
3. Quantidade de acertos de vencedor + nº de gols do vencedor
4. Data e hora de cadastro no Bolão (mais antigo vence)

---

### 1.2 Número de Jogos — Discrepância com o escopo real

A Seção 3.1 (Feature #1) estabelece "ao menos 3 jogos do catálogo padrão da LiveLike." O escopo real do produto contempla **apenas 2 modalidades**:

- **Prediction Game** (palpite de placares)
- **Trivia**

O texto deve ser corrigido para refletir exatamente esses 2 jogos, eliminando a referência a um mínimo de 3. Qualquer adição futura de jogos será tratada como escopo adicional.

---

### 1.3 Capacidade e Teste de Carga — Números criticamente subestimados

A Seção 4 (Acceptance Criteria) exige teste de carga com **500.000 usuários simultâneos**, e a Seção 6 garante capacidade mínima de **300.000 usuários simultâneos** em Match Days.

Esses números estão **significativamente abaixo** da expectativa operacional real:

> **Capacidade exigida:** picos de até **5.000.000 (cinco milhões) de usuários simultâneos**, com capacidade de suportar **200.000 requests por segundo** nos picos de jogo do Brasil.

Os números das Seções 4 e 6 devem ser revisados para refletir esses parâmetros. A LiveLike precisa confirmar contratualmente que sua infraestrutura suporta essa escala, ou apresentar um plano de capacidade aprovado pela CazéTV antes da assinatura.

---

### 1.4 Integração Stats Perform / OPTA — Responsabilidade mal atribuída

A Seção 3.2 atribui à LiveLike a responsabilidade pela integração Stats Perform, incluindo obtenção das credenciais de acesso. Na prática, **a CazéTV já possui contrato vigente com a OPTA (Stats Perform)** e fornecerá o acesso à LiveLike.

O texto deve ser ajustado para refletir que:
- A integração técnica é responsabilidade da LiveLike
- O fornecimento das credenciais de acesso OPTA é responsabilidade da CazéTV
- A troca de credenciais é condição do Milestone Week 1 e deverá ser formalizada em até 48h

---

### 1.5 SSO — Dependência de Sponsor não prevista

A Seção 3.2 trata o SSO como uma integração direta entre CazéTV e LiveLike (OAuth 2.0 / JWT). O cenário real é mais complexo e dependente de uma variável comercial:

**Cenário A — SSO próprio LiveMode:** Caso não haja sponsor de autenticação, a LiveMode desenvolverá SSO próprio integrado ao banco de dados da LiveLike, com identificação de usuários premium/comum via API.

**Cenário B — SSO de Sponsor (ex: iFood):** Caso um sponsor de autenticação seja fechado, o SSO poderá ser do parceiro (ex: iFood). Nesse caso, a diferenciação premium/comum virá do sistema do sponsor, integrada via API à LiveLike.

O Schedule A deve prever ambos os cenários ou incluir uma cláusula de adaptação do SSO sem custo adicional caso o protocolo mude em função de parceria comercial, desde que notificado com antecedência mínima acordada.

---

### 1.6 Milestone Week 1 — Status parcial

O Milestone Week 1 (deadline 07/Abr/2026) foi parcialmente cumprido. Para registro e efeito das penalidades previstas na Seção 5:

| Entregável | Status |
|---|---|
| Kickoff realizado | ✅ Concluído |
| Tech stack confirmado | ✅ Concluído |
| Protocolo SSO alinhado | ⚠️ Em negociação (dependência de sponsor) |
| Credenciais OPTA trocadas | ❌ Não realizado |
| Sprint schedule aprovado | ⚠️ Recebido — em validação pela CazéTV |

Recomendamos registrar formalmente esse status junto à LiveLike para definir se há aplicação de crédito automático de 5% conforme cláusula de penalidade por atraso de 1–7 dias.

---

## 2. COMPLEMENTOS — Informações a adicionar ao documento

### 2.1 Assets de Comentaristas — Prazo e formato a definir

A Feature #6 (Seção 3.1) prevê integração de perfis de comentaristas, narradores e influenciadores da CazéTV na Copa do Mundo, com assets (nome, foto, bio) fornecidos pela CazéTV.

Dois pontos precisam ser incluídos no Schedule A:
- **Formato dos assets:** especificações técnicas (dimensões de imagem, limite de caracteres de bio, etc.) a serem alinhadas com a LiveLike no Milestone Week 2
- **Deadline de entrega:** a ser definido com a LiveLike — recomendamos até o Milestone Week 3 (21/Abr/2026) para constar no protótipo navegável

### 2.2 Suporte L1/L2 — Fluxo não está no documento

O Schedule A define os SLAs de resposta da LiveLike, mas não descreve o fluxo de suporte ao usuário final. O modelo definido internamente é:

- **L1 (atendimento ao usuário):** LiveMode — responsável pelo primeiro atendimento via canal a ser definido
- **Escalada para LiveLike (L2):** apenas para problemas de natureza técnica na plataforma que não possam ser resolvidos pelo L1

Sugerimos incluir uma subseção na Seção 7 (SLA) formalizando esse fluxo e o canal de comunicação LiveMode → LiveLike para escalada de incidentes (ex: canal dedicado no Slack, e-mail técnico, PagerDuty).

### 2.3 Mini-Leagues — Remover ou esclarecer "Symbolic Prizes"

A Feature #9 menciona "configurable symbolic prizes" nas ligas entre amigos. **A CazéTV não oferecerá premiação nas mini-leagues.** O termo precisa ser esclarecido: se "symbolic prizes" se refere a alguma funcionalidade nativa da plataforma LiveLike (badges virtuais, títulos), isso deve ser explicitado. Caso não haja essa funcionalidade no escopo contratado, o trecho deve ser removido.

### 2.4 Exhibit C (DPA) — Lista de Subprocessadores não recebida

O DPA faz referência a um Exhibit C com a lista de subprocessadores da LiveLike. Esse documento **não foi enviado junto aos arquivos**. Solicitamos que a LiveLike encaminhe o Exhibit C para análise antes da assinatura do DPA.

---

## 3. PONTOS CONFIRMADOS — Sem alteração necessária

Os seguintes pontos foram revisados e estão alinhados com a operação prevista:

- **CRM:** Integração com CRM **não faz parte do escopo** deste contrato.
- **SLA Match Days (Seção 7):** 99,9% uptime, resposta a incidente crítico em 30 min, penalidade 5x pro-rata — considerado adequado, desde que os números de capacidade (item 1.3) sejam corrigidos.
- **Propriedade dos dados (Seção 8):** Todos os dados gerados pelos usuários no Bolão são de propriedade exclusiva da CazéTV. A proibição de uso dos dados para treinar modelos de IA da LiveLike está alinhada com o DPA.
- **Proteção durante o Torneio (TC Seção 5d):** A cláusula que proíbe suspensão do serviço durante o período Jun-Jul/2026 sem consentimento da CazéTV é favorável e deve ser mantida.
- **LGPD no DPA:** A inclusão explícita da Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018) e referência à ANPD está correta e necessária para operação no Brasil.

---

## 4. RESUMO DE AÇÕES PARA O JURÍDICO

| # | Ação | Tipo | Prioridade |
|---|---|---|---|
| 1 | Incluir tabela completa de pontuação e desempate no Schedule A | Complemento | 🔴 Urgente |
| 2 | Corrigir Feature #1: de "mínimo 3 jogos" para "Prediction Game + Trivia" | Correção | 🔴 Urgente |
| 3 | Revisar Seções 4 e 6: capacidade de 5M usuários simultâneos / 200k req/s | Correção | 🔴 Urgente |
| 4 | Ajustar Seção 3.2: CazéTV fornece credenciais OPTA, LiveLike faz a integração | Correção | 🔴 Urgente |
| 5 | Incluir cláusula de flexibilidade de SSO vinculada a sponsor comercial | Complemento | 🟡 Importante |
| 6 | Registrar status parcial do Milestone Week 1 e definir se há penalidade | Ação comercial | 🟡 Importante |
| 7 | Definir formato e prazo de entrega dos assets de comentaristas | Complemento | 🟡 Importante |
| 8 | Incluir fluxo L1 (LiveMode) / L2 (LiveLike) na Seção 7 | Complemento | 🟡 Importante |
| 9 | Esclarecer ou remover "symbolic prizes" da Feature #9 | Correção | 🟢 Normal |
| 10 | Solicitar Exhibit C (lista de subprocessadores) do DPA à LiveLike | Solicitação | 🟡 Importante |

---

*Documento preparado com base na revisão técnica e operacional do Schedule A realizada em 09/04/2026.*
