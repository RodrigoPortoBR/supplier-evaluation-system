# Demanda de Analytics — Bolão Copa do Mundo FIFA 2026 CazéTV
**Documento de requisitos para LiveLike e iFood**
*Versão 1.0 — Maio/2026*

---

## 1. Contexto e objetivos

O Bolão está distribuído em dois ambientes com fontes de dados distintas:

- **iFood** — responsável pelo topo do funil: impressões do banner, cliques de entrada no Bolão e dados de assinatura do Clube iFood
- **LiveLike** — responsável por toda a experiência dentro do Bolão: cadastro, palpites, ligas, missões, rankings e conversão para Clube iFood

Para que a CazéTV opere o produto com autonomia estratégica, precisamos que **LiveLike entregue um conjunto estruturado de métricas, eventos e segmentos de audiência** com granularidades específicas por contexto de uso.

Este documento organiza essa demanda em quatro blocos:
1. Funil end-to-end (jornada completa do usuário)
2. Monitoramento em tempo real (operação ao vivo)
3. Métricas operacionais diárias
4. Eventos e segmentos para CRM

---

## 2. Fontes de dados e responsabilidades

| Etapa da jornada | Fonte dos dados | Responsável pela entrega |
|---|---|---|
| Impressões do banner do Bolão no app iFood | iFood | iFood |
| Cliques no banner (entrada no Bolão) | iFood | iFood |
| Sessões iniciadas na plataforma do Bolão | LiveLike | LiveLike |
| Cadastro (apelido + aceite) | LiveLike | LiveLike |
| Palpites (preenchimento, edição, taxa) | LiveLike | LiveLike |
| Ligas privadas (criação, participação) | LiveLike | LiveLike |
| Missões e badges | LiveLike | LiveLike |
| Rankings (posição, variação) | LiveLike | LiveLike |
| Cliques no CTA "Virar Clube iFood" | LiveLike | LiveLike |
| Novas assinaturas Clube iFood | iFood + LiveLike | Ambos (reconciliação) |
| Status Clube iFood por usuário | iFood → LiveLike via SSO | LiveLike |

---

## 3. Funil end-to-end — jornada completa do usuário

O funil completo tem **sete estágios** mapeados entre iFood e LiveLike. Cada estágio precisa de volume, taxa de conversão para o próximo e breakdown por tipo de usuário (Basic / Clube iFood).

```
[1] IMPRESSÃO DO BANNER
         ↓  (taxa: cliques / impressões)
[2] ACESSO AO BOLÃO
         ↓  (taxa: iniciaram cadastro / acessaram)
[3] CADASTRO CONCLUÍDO
         ↓  (taxa: fizeram ≥1 palpite / cadastrados)
[4] PRIMEIRO PALPITE
         ↓  (taxa: preenchem palpites diariamente / cadastrados)
[5] ENGAJAMENTO RECORRENTE
         ↓  (taxa: clicaram no CTA Clube iFood / Basic ativos)
[6] INTENÇÃO DE UPGRADE
         ↓  (taxa: converteram / clicaram no CTA)
[7] CONVERSÃO CLUBE iFOOD
```

### 3.1 Métricas por estágio do funil

**Estágio 1 — Impressão do banner** *(fonte: iFood)*
- Total de impressões do banner/card do Bolão no app iFood
- Impressões únicas (usuários únicos que viram)
- Segmentação: Clube iFood vs não-Clube iFood

**Estágio 2 — Acesso ao Bolão** *(fonte: LiveLike)*
- Total de sessões iniciadas
- Usuários únicos que acessaram
- Origem da sessão (banner iFood, link direto, notificação push)
- Taxa de conversão: clique no banner → sessão iniciada
- Breakdown: Clube iFood vs Basic (já identificados via SSO)

**Estágio 3 — Cadastro concluído** *(fonte: LiveLike)*
- Usuários que completaram o cadastro (apelido + aceite)
- Drop-off por etapa do onboarding:
  - Acessou mas não iniciou cadastro
  - Iniciou mas não escolheu apelido
  - Escolheu apelido mas não aceitou os termos
  - Concluiu o cadastro mas não preencheu nenhum palpite inicial
- Tempo médio de conclusão do onboarding
- Breakdown: Clube iFood vs Basic

**Estágio 4 — Primeiro palpite** *(fonte: LiveLike)*
- Usuários que fizeram ≥1 palpite
- Usuários que preencheram todos os palpites da fase de grupos no cadastro (64 pontos iniciais)
- Tempo mediano entre cadastro e primeiro palpite
- Breakdown: Clube iFood vs Basic

**Estágio 5 — Engajamento recorrente** *(fonte: LiveLike)*
- Ver seção 5 (métricas operacionais diárias)

**Estágio 6 — Intenção de upgrade** *(fonte: LiveLike)*
- Cliques no CTA "Virar Clube iFood" (total e únicos)
- Contexto do clique: de qual tela veio (ranking, palpite, missão, liga)
- Usuários que clicaram mas não converteram

**Estágio 7 — Conversão Clube iFood** *(fonte: iFood + LiveLike)*
- Novas assinaturas Clube iFood atribuídas ao Bolão
- Tempo entre primeiro acesso ao Bolão e conversão
- Contexto da conversão: fase do torneio, posição no ranking no momento da conversão

---

## 4. Monitoramento em tempo real

### Contexto de uso
A CazéTV fará chamadas ao vivo durante a transmissão dos jogos convocando usuários a entrar no Bolão. Nesses momentos, picos de acesso simultâneo são esperados e precisamos de visibilidade em **tempo real, com granularidade de 1 minuto**, para operar com segurança e mensurar o impacto das chamadas ao vivo.

### 4.1 Painel de tempo real — requisitos mínimos

| Métrica | Granularidade | Breakdown obrigatório |
|---|---|---|
| Usuários ativos (sessão aberta) | Por minuto | Clube iFood / Basic |
| Novos cadastros | Por minuto | Clube iFood / Basic |
| Palpites submetidos | Por minuto | Clube iFood / Basic |
| Palpites editados | Por minuto | — |
| Cliques no CTA Clube iFood | Por minuto | — |
| Novas assinaturas Clube iFood | Por minuto | — |
| Taxa de erro / falhas na plataforma | Por minuto | Por tipo de erro |

### 4.2 Métricas de pico e capacidade

- Pico de usuários simultâneos (janela de 1 min, 5 min e 15 min)
- Tempo de resposta do servidor (p50, p95, p99) por minuto
- Taxa de sucesso de submissão de palpites (% de tentativas que completaram)

### 4.3 Janelas críticas de monitoramento

As janelas abaixo exigem atenção redobrada e o painel em tempo real deve estar ativo:

| Momento | Janela de monitoramento |
|---|---|
| Abertura da plataforma (09/06) | Dia inteiro |
| 15 min antes de cada jogo do Brasil | Início até 15 min após apito |
| Chamadas ao vivo na transmissão CazéTV | Durante a chamada + 30 min após |
| Abertura do mata-mata (32-avos) | 2h antes do primeiro jogo |
| Final da Copa | Dia inteiro |
| Encerramento do período de palpites (19/07, 23h59) | Últimas 3h |

---

## 5. Métricas operacionais diárias

Estas métricas devem estar disponíveis no CMS da LiveLike com atualização diária (fechamento às 6h do dia seguinte, horário de Brasília).

### 5.1 Métricas de usuário

| Métrica | Definição | Breakdown |
|---|---|---|
| DAU | Usuários únicos com ≥1 sessão no dia | Clube iFood / Basic |
| MAU | Usuários únicos com ≥1 sessão nos últimos 30 dias | Clube iFood / Basic |
| DAU/MAU ratio | Stickiness do produto | Clube iFood / Basic |
| Novos cadastros | Usuários que concluíram onboarding no dia | Clube iFood / Basic |
| Cadastros acumulados | Total histórico | Clube iFood / Basic |
| Retenção D1 | % dos cadastrados no dia anterior que voltaram | Clube iFood / Basic |
| Retenção D7 | % dos cadastrados 7 dias atrás que voltaram | Clube iFood / Basic |
| Retenção D14 | % dos cadastrados 14 dias atrás que voltaram | Clube iFood / Basic |
| Upgrades para Clube iFood | Novos assinantes que vieram do Bolão no dia | — |
| Upgrades acumulados | Total histórico de conversões via Bolão | — |

### 5.2 Métricas de palpites

| Métrica | Definição | Breakdown |
|---|---|---|
| Total de palpites submetidos no dia | Contagem de submissões | Clube iFood / Basic |
| Usuários que preencheram todos os palpites do dia | % do total ativo | Clube iFood / Basic |
| Usuários com ≥1 palpite do dia | % do total ativo | Clube iFood / Basic |
| Usuários sem nenhum palpite do dia | Absoluto e % | Clube iFood / Basic |
| Taxa de preenchimento por partida | % de cadastrados que palpitaram em cada jogo | — |
| Palpites editados | Volume de edições (último palpite que contou) | — |
| Usuários que preencheram palpites especiais | Campeão e artilheiro | Clube iFood / Basic |

### 5.3 Métricas de engajamento

| Métrica | Definição | Breakdown |
|---|---|---|
| Missões diárias completadas | Total de completions no dia | Clube iFood / Basic |
| Taxa de conclusão da missão diária | % dos ativos que completaram | Clube iFood / Basic |
| Compartilhamentos sociais | Resultados compartilhados no dia | Por rede social |
| Ligas criadas | Novas ligas privadas criadas | Clube iFood / Basic |
| Participações em ligas | Usuários que entraram em nova liga | Clube iFood / Basic |
| Badges desbloqueados no dia | Por tipo de badge | — |
| Sessões por usuário ativo | Média de sessões no dia | Clube iFood / Basic |
| Duração média da sessão | Em minutos | Clube iFood / Basic |

### 5.4 Métricas de ranking

| Métrica | Definição |
|---|---|
| Distribuição do ranking | Contagem de usuários por faixa: top 100 / 101-1k / 1k-10k / 10k-100k / acima de 100k |
| Pontuação média por faixa de ranking | Por posição e por tipo de usuário |
| Variação de posição média no dia | Movimentação geral do ranking |

---

## 6. Eventos para CRM — segmentos e audiências

Esta é a seção mais crítica para a operação de CRM. Precisamos que a LiveLike entregue **audiências exportáveis** (lista de user_ids com atributos) atualizadas diariamente ou sob demanda, para acionamento via canais da CazéTV e do iFood (push, e-mail, WhatsApp, in-app).

### 6.1 Estrutura mínima de cada usuário exportável

Cada usuário exportado deve conter obrigatoriamente:

```
user_id (ID LiveLike)
cpf_hash (hash do CPF para reconciliação com iFood)
status: BASIC | CLUBE_IFOOD
ranking_brasil: posição atual
ranking_clube_ifood: posição atual (null se Basic)
palpites_preenchidos_hoje: true | false
total_palpites_preenchidos: número
total_palpites_possiveis: número
taxa_preenchimento: %
streak_dias_consecutivos: número
badges: lista de badges conquistados
data_cadastro: timestamp
ultimo_acesso: timestamp
cta_clube_ifood_clicado: true | false
```

### 6.2 Segmentos pré-configurados (atualização diária)

Os segmentos abaixo devem estar disponíveis como audiências exportáveis no CMS da LiveLike todo dia até 7h (horário de Brasília):

---

**SEG-01 — Cadastrados sem nenhum palpite ainda**
```
status: BASIC ou CLUBE_IFOOD
total_palpites_preenchidos = 0
```
*Ação CRM:* onboarding push — "Você se cadastrou mas ainda não fez nenhum palpite. Os jogos já começaram!"

---

**SEG-02 — Ativos sem palpite do(s) jogo(s) do dia**
```
ultimo_acesso >= hoje - 3 dias
palpites_preenchidos_hoje = false
há jogo disponível para palpite hoje
```
*Ação CRM:* lembrete diário pré-jogo — "Tem jogo hoje! Não perca seus pontos."

---

**SEG-03 — Basic com palpites em dia (candidatos a upgrade)**
```
status: BASIC
palpites_preenchidos_hoje = true
taxa_preenchimento >= 70%
```
*Ação CRM:* pitch Clube iFood — "Você está engajado. Sabia que no Clube iFood o 1º lugar ganha R$ 1.000.000?"

---

**SEG-04 — Basic no top 10.000 do Ranking Brasil**
```
status: BASIC
ranking_brasil <= 10.000
```
*Ação CRM:* urgência de upgrade — "Você está entre os 10.000 melhores do Brasil. No Clube iFood, sua posição vale até R$ 1.000.000."

---

**SEG-05 — Basic no top 1.000 do Ranking Brasil**
```
status: BASIC
ranking_brasil <= 1.000
```
*Ação CRM:* urgência máxima — "Você está no top 1.000 do Brasil. No Clube iFood, o prêmio é 10x maior."

---

**SEG-06 — Basic que clicou no CTA mas não converteu**
```
status: BASIC
cta_clube_ifood_clicado = true
data do clique >= hoje - 48h
```
*Ação CRM:* retargeting — "Você quase virou Clube iFood. Ainda dá tempo."

---

**SEG-07 — Clube iFood sem palpite do dia (risco de churn de engajamento)**
```
status: CLUBE_IFOOD
palpites_preenchidos_hoje = false
há jogo disponível para palpite hoje
```
*Ação CRM:* lembrete premium — "Seus pontos do Clube iFood estão esperando. Palpite agora."

---

**SEG-08 — Clube iFood no top 100 (VIPs)**
```
status: CLUBE_IFOOD
ranking_clube_ifood <= 100
```
*Ação CRM:* reconhecimento e retenção — "Você está brigando pelo prêmio. Não perca momentum."

---

**SEG-09 — Usuários inativos há 3+ dias (risco de abandono)**
```
ultimo_acesso < hoje - 3 dias
total_palpites_preenchidos >= 1
```
*Ação CRM:* reativação — "Faz 3 dias que você não entra. Veja o que perdeu."

---

**SEG-10 — Usuários inativos há 7+ dias**
```
ultimo_acesso < hoje - 7 dias
total_palpites_preenchidos >= 1
```
*Ação CRM:* reativação com urgência — "A Copa não para. Você está perdendo pontos todo dia."

---

**SEG-11 — Basic com streak alto (3+ dias consecutivos)**
```
status: BASIC
streak_dias_consecutivos >= 3
```
*Ação CRM:* upgrade com contexto de consistência — "Você entrou 3 dias seguidos. Usuários consistentes como você estão dominando o Clube iFood."

---

**SEG-12 — Usuários que acertaram placar exato recentemente**
```
palpites com pontuação = 50pts nos últimos 3 jogos
```
*Ação CRM:* reconhecimento + push social — "Você acertou o placar exato! Compartilhe antes que os outros descubram."

---

**SEG-13 — Basic sem palpite dos jogos do Brasil**
```
status: BASIC
sem palpite válido nos últimos jogos da Seleção Brasileira
```
*Ação CRM:* urgência Brasil — "Jogo do Brasil é 2x mais pontos. Não fique de fora."

---

**SEG-14 — Novos cadastrados nas últimas 24h sem palpite**
```
data_cadastro >= hoje - 24h
total_palpites_preenchidos = 0
```
*Ação CRM:* ativação imediata — "Bem-vindo ao Bolão! Seu primeiro palpite está esperando."

---

### 6.3 Eventos pontuais para comunicação em tempo real

Além das audiências diárias, precisamos de **webhooks ou triggers** que disparem no momento do evento para comunicação imediata:

| Evento | Trigger | Canal sugerido |
|---|---|---|
| Cadastro concluído | Imediato após aceite | Push / WhatsApp |
| Primeiro palpite feito | Imediato | Push in-app |
| Badge desbloqueado | Imediato | Push in-app |
| Usuário entrou no top 1.000 | Imediato | Push |
| Usuário entrou no top 100 | Imediato | Push |
| CTA Clube iFood clicado (sem conversão em 30 min) | 30 min após clique | Push / WhatsApp |
| Jogo do Brasil começando (usuário sem palpite) | 2h antes do jogo | Push / WhatsApp |
| Encerramento de palpites do dia (usuário sem palpite) | 1h antes do último jogo | Push |
| Missão diária disponível | 10h de cada dia | Push in-app |

---

## 7. Régua de CRM sugerida

### 7.1 Régua de ativação (primeiros 7 dias do usuário)

| Dia | Segmento alvo | Mensagem / objetivo |
|---|---|---|
| D+0 | SEG-14 (cadastrado sem palpite) | Ativação: "Faça seu primeiro palpite" |
| D+1 | Cadastrados ontem que fizeram ≥1 palpite | Reforço positivo + missão do dia |
| D+1 | SEG-14 ainda sem palpite | Reativação de onboarding |
| D+3 | Ativos com taxa < 50% de preenchimento | Dica de como pontuar mais |
| D+7 | Basic ativos com boa taxa de preenchimento | Pitch Clube iFood (SEG-03) |

### 7.2 Régua de jornada — Brasil em campo

Ativada sempre que a Seleção Brasileira joga:

| Momento | Segmento | Mensagem |
|---|---|---|
| 24h antes | Todos sem palpite do jogo | "Amanhã é jogo do Brasil. Palpite vale 2x." |
| 2h antes | Todos sem palpite do jogo | "2 horas para o jogo do Brasil. Ainda dá tempo." |
| Apito inicial | Todos com palpite feito | "Jogo começando! Torcida + palpite = combinação perfeita." |
| Fim do jogo | Acertaram o resultado | Compartilhamento social do acerto |
| Fim do jogo | Erraram o resultado | Motivação + foco no próximo jogo |

### 7.3 Régua de conversão Basic → Clube iFood

| Gatilho | Segmento | Mensagem |
|---|---|---|
| Usuário entra no top 10k | SEG-04 | "Você chegou ao top 10.000. No Clube iFood vale muito mais." |
| Usuário entra no top 1k | SEG-05 | "Top 1.000! Você merece brigar pelo R$ 1.000.000." |
| 3 dias de streak | SEG-11 | "Consistência que dá dinheiro — no Clube iFood." |
| Fase muda (grupos → mata-mata) | Basic com boa posição | "O mata-mata começa. Os multiplicadores aumentam. O Clube iFood também." |
| Clique sem conversão | SEG-06 | Retargeting 30 min e 24h depois |

### 7.4 Régua de retenção e reativação

| Momento | Segmento | Mensagem |
|---|---|---|
| 3 dias sem acesso | SEG-09 | "Você perdeu X pontos nos últimos 3 dias. Ainda dá para recuperar." |
| 7 dias sem acesso | SEG-10 | "A Copa continua. Você sumiu do ranking." |
| Véspera do encerramento de palpites | Todos com palpites faltando | "Última chance de palpitar. O período fecha em X horas." |

---

## 8. Requisitos de entrega e infraestrutura

### 8.1 Dashboards requeridos da LiveLike

**Dashboard 1 — Operação em Tempo Real**
- Acesso: CazéTV (equipe de operações e transmissão)
- Atualização: a cada 1 minuto
- Conteúdo: métricas da seção 4.1

**Dashboard 2 — Painel Diário de Performance**
- Acesso: CazéTV (produto, marketing, dados)
- Atualização: diária (até 7h)
- Conteúdo: métricas das seções 5.1 a 5.4

**Dashboard 3 — Funil de Conversão**
- Acesso: CazéTV + iFood
- Atualização: diária
- Conteúdo: seção 3 (funil end-to-end completo)

### 8.2 Exportação de audiências para CRM

- **Formato:** CSV ou JSON com os campos da seção 6.1
- **Frequência:** diária, até 7h (horário de Brasília), ou sob demanda via API
- **Método de entrega:** endpoint de API REST autenticado ou SFTP
- **Identificador de reconciliação:** hash do CPF (SHA-256) para cruzamento com base iFood/CazéTV
- **Retenção:** dados de audiência disponíveis por até 30 dias

### 8.3 Webhooks para eventos em tempo real

- Protocolo: HTTPS POST para endpoint da CazéTV/iFood
- Autenticação: Bearer token
- Payload mínimo: user_id, event_type, timestamp, atributos relevantes do evento
- SLA: entrega em até 30 segundos do evento
- Retry: 3 tentativas com backoff exponencial

### 8.4 Reconciliação de dados iFood ↔ LiveLike

Para unir o funil completo (impressão de banner até conversão Clube iFood), é necessário:

1. **iFood fornece à LiveLike:** user_id iFood + status Clube iFood via SSO no momento do login
2. **LiveLike retorna ao iFood:** user_id LiveLike + hash CPF + atributos de engajamento (via API diária)
3. **CazéTV recebe de ambos:** relatório consolidado com funil completo (de responsabilidade conjunta iFood + LiveLike)

---

## 9. Perguntas estratégicas que este framework deve responder

As métricas e eventos acima foram desenhados para responder as seguintes perguntas de negócio no dia a dia:

**Aquisição**
- Quantas pessoas viram o banner e quantas entraram no Bolão?
- Qual é nossa taxa de conversão de visitante para cadastrado?
- As chamadas ao vivo estão trazendo picos de acesso mensuráveis?

**Ativação**
- Quantos cadastrados fizeram pelo menos 1 palpite?
- Onde está o maior drop-off no onboarding?

**Retenção**
- Qual a retenção D1, D7 e D14?
- Quais usuários estão em risco de abandono agora?
- O que diferencia usuários que ficam dos que somem?

**Receita / Conversão**
- Quantos Basic converteram para Clube iFood via Bolão?
- Qual o contexto de conversão mais comum? (fase do torneio, posição no ranking)
- Qual CTA converte mais? (de qual tela vem a maioria das conversões)

**Produto**
- Qual a taxa de preenchimento de palpites por jogo?
- Missões diárias aumentam o DAU?
- Ligas privadas aumentam a retenção?

---

*Este documento deve ser revisado antes do kick-off técnico com a LiveLike para validação de viabilidade de entrega de cada métrica e evento listado.*
