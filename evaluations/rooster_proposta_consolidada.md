# Rooster – Proposta Consolidada
**Projeto:** Bolão Copa do Mundo 2026 – CazéTV
**Documentos base:**
- Proposta v1 recebida em 18/02/2026 (Apresentação, 10 slides)
- **Proposta v2 recebida em 20/02/2026** (Apresentação atualizada, 13 páginas)

---

## 1. Infraestrutura técnica e robustez

- **Cloud:** Infraestrutura cloud "altamente resiliente" (provedor não especificado)
- **Capacidades declaradas:**
  - Auto-scaling horizontal para picos massivos
  - Balanceamento global de carga
  - Sistemas redundantes
  - Monitoramento em tempo real e redundância automática de serviços
  - **🆕 v2:** "Plataforma projetada para escalar elasticamente e suportar picos massivos de audiência, podendo atingir ordem de **dezenas de milhões de usuários simultâneos**, conforme dimensionamento de infraestrutura."
  - **🆕 v2:** "Testes de carga contínuos realizados em cenários de alta concorrência"
- **Uptime:** **🆕 v2:** Target de disponibilidade ~**99,9%** durante períodos críticos
- **Plataformas:** **🆕 v2:**
  - ✅ Web Desktop e Web Mobile (totalmente responsivos)
  - ✅ iOS e Android via **WebView/SDK** (integração em apps existentes)
  - ❌ Apps nativos: "podem ser avaliados como evolução futura, não fazendo parte do escopo atual"

> ⚠️ **Observação:** v2 melhorou significativamente: meta de uptime 99.9%, claim de dezenas de milhões de usuários, testes de carga contínuos, e plataformas mobile via WebView. Porém, ainda genérico: sem provedor cloud especificado (AWS? GCP?), sem números concretos de RPS, sem evidência de load test, sem cases anteriores de grande escala.

---

## 2. Suporte Local

- **Equipe dedicada:** ~7 profissionais full-time exclusivos
  - **Tecnologia (4):** Desenvolvimento, performance, monitoramento e escalabilidade
  - **Operação e Produto (3):** Interface direta com CazéTV, ajustes operacionais e suporte técnico
- **Plantão:** Regime de plantão técnico contínuo durante dias de jogos
- **🆕 v2:** Estrutura de **war-room operacional** para monitoramento e resposta a incidentes
- **🆕 v2:** Cobertura contínua durante dias de jogos e janelas críticas
- **Idioma:** Empresa brasileira – suporte nativo em português

> ✅ **Ponto positivo:** v2 confirma war-room operacional. Empresa brasileira, sem barreira de idioma ou fuso.

---

## 3. SLA em caso de incidentes

**🆕 v2 – SLAs CONFIRMADOS:**

| Tipo de Incidente | Tempo de Resposta |
| :--- | :--- |
| **Incidentes críticos** | ≤ **15 minutos** |
| **Incidentes alta prioridade** | ≤ **1 hora** |

- **🆕 v2:** Escalonamento estruturado em 3 níveis: operacional, técnico e infraestrutura
- **🆕 v2:** Níveis de serviço e condições operacionais formalizados em contrato

> ✅ **Melhoria significativa:** v1 não tinha NENHUM SLA. V2 define tempos de resposta e estrutura de escalonamento. Ainda falta: SLA de resolução (não apenas resposta), workflow detalhado, feature flags/rollback.

---

## 4. Segurança da informação

**🆕 v2 – Seção nova "Segurança, Compliance & Governança de Dados":**

- **Proteção de Dados:** Mencionada como foco, mas sem detalhamento específico
- **🆕 v2 – Proteção de Menores:**
  - ✅ "Mecanismos de consentimento aplicáveis a **menores de idade**"
  - ✅ "Controles adicionais de privacidade e governança"

**Ainda NÃO informado:**
- ❓ Conformidade LGPD/GDPR (mencionado implicitamente mas não detalhado)
- ❓ Residência de dados (país/região)
- ❓ Certificações (ISO, SOC)
- ❓ Testes de penetração
- ❓ Criptografia (at-rest, in-transit)
- ❓ WAF / rate limiting

> ⚠️ **Melhoria parcial:** v2 adicionou seção de segurança com menção a consentimento para menores (único fornecedor além de Quality a mencionar). Porém, ainda falta detalhamento de LGPD, certificações e controles técnicos de segurança.

---

## 5. Dados

**🆕 v2 – Seção nova "Propriedade e Acesso aos Dados":**

- ✅ **100% dos dados** gerados na plataforma pertencem à CazéTV
- ✅ Acesso integral à base de usuários e dados comportamentais
- ✅ **Exportação completa** garantida mediante solicitação
- ✅ **APIs disponíveis** para integração e extração de dados
- ✅ **Portabilidade integral** dos dados e históricos garantida ao término da parceria

> ✅ **Melhoria excelente:** v1 não tinha NADA sobre dados. V2 garante propriedade 100%, acesso, exportação, APIs e portabilidade. Posição forte de data ownership.

---

## 6. Features previstas

### ✅ Confirmado (v1 + v2):
- ✅ Sistema de palpites e rankings em tempo real
- ✅ Ligas públicas e privadas
- ✅ Gamificação, missões e benefícios
- ✅ Integrações com parceiros
- ✅ IA de sugestões e estatísticas
- **🆕 v2:**
  - ✅ **Palpites de resultado, placar exato e previsões especiais**
  - ✅ Rankings globais + ligas públicas e privadas
  - ✅ **Criação ilimitada de ligas** e convites via link
  - ✅ **Gestão administrativa e controles antifraude**
  - ✅ Atualizações em "tempo próximo ao real"
  - ✅ Suporte a milhões de usuários registrados

### Ainda não detalhado:
- ❓ Ranking por período (dia/rodada/torneio)
- ❓ Boosters, troféus, conquistas
- ❓ Lógica de pontuação (configurável? regras?)
- ❓ Estrutura de prêmios / sorteios / lucky numbers
- ❓ Quizzes / trivia diária
- ❓ Modelo freemium vs premium

> ⚠️ **Melhoria:** v2 confirmou palpite de placar exato + previsões especiais, ligas ilimitadas, antifraude e gestão admin. Ainda falta detalhamento de lógica de pontuação, quizzes, lucky numbers e modelo premium.

---

## 7. Customização UX / Front-end

- **🆕 v2:** Web Desktop e Mobile totalmente responsivos
- **🆕 v2:** Compatível com integração em apps iOS/Android via WebView/SDK
- Ainda não detalhado: CSS/temas, domínio, quem faz design

---

## 8. Integração / Login

**🆕 v2 – Seção nova "Integrações":**

- ✅ **APIs para autenticação e SSO**
- ✅ Integração com sistemas de parceiros e bases externas (mediante definição técnica conjunta)
- ✅ Compatibilidade com programas de benefícios e plataformas externas

> ✅ **Melhoria:** v1 não tinha detalhes. V2 confirma SSO, integração com parceiros e programas de benefícios.

---

## 9. Comunicações

- `[Não informado]` – v2 também **não menciona:**
  - Email
  - Push notifications
  - Mensagens in-game
  - CRM

---

## 10. Compartilhamento com Redes

- `[Não informado]` – v2 não adiciona informação de social sharing.

---

## 11. Restrição Geolocalização

- `[Não informado]`

---

## 12. Tempo de implementação

**🆕 v2 – Cronograma CONFIRMADO:**

| Fase | Duração |
| :--- | :--- |
| Kickoff e planejamento técnico | **~2 semanas** |
| Desenvolvimento e customizações | **~8–12 semanas** |
| Testes de carga e preparação operacional | **~4 semanas** |
| **Go-live** | **Antes do início da Copa** |

**Total estimado:** ~14–18 semanas (3.5–4.5 meses)

> ✅ **Melhoria excelente:** v1 não tinha cronograma. V2 define fases claras. Para go-live antes da Copa (~11 junho 2026), contrato precisaria ser assinado entre fevereiro e março. Cronograma é **viável** se iniciado em breve.

---

## 13. Modelo de precificação + o que está incluso

### Investimento total: **R$ 1.154.000,00** (mantido de v1)

| Parcela | % | Valor | Quando |
|:---|:---|:---|:---|
| 1ª parcela | 50% | R$ 577.000 | Na assinatura do contrato |
| 2ª parcela | 30% | R$ 346.200 | Antes do início da Copa |
| 3ª parcela | 20% | R$ 230.800 | Após encerramento do evento |

### 🆕 v2 – Modelo de custo FIXO confirmado:
- ✅ **Estrutura de investimento fixa, incluindo infraestrutura e operação**
- ✅ **Custos NÃO variam em função do volume de usuários**
- ✅ Níveis de serviço e condições operacionais formalizados em contrato

> ✅ **Melhoria significativa:** v2 confirma que R$ 1.154.000 é custo FIXO all-inclusive (dev + infra + operação Copa). Sem custos variáveis por tráfego. Isso é um diferencial importante vs Quality Digital (onde infra é extra).

---

## 14. O que está fora do escopo

- `[Não informado]` – v2 **continua sem listar** explicitamente o que está fora do escopo:

| Item | Status v1 | Status v2 |
|:---|:---|:---|
| Cumprimento de prêmios | ❓ | ❓ |
| Quizzes / Trivia | ❓ | ❓ |
| Loteria / Lucky Numbers | ❓ | ❓ |
| CRM / Email / Push | ❓ | ❓ |
| Pagamentos | ❓ | ❓ |
| Verificação de idade | ❓ | ✅ Consentimento para menores (v2) |
| Geo-restrição | ❓ | ❓ |
| Feeds de dados esportivos | ❓ | ❓ |
| Apps nativos | ❓ | ❌ Fora do escopo atual (v2) |

---

## ⚠️ Avaliação geral da proposta

V2 da Rooster endereçou **várias das lacunas críticas** da v1. A proposta evoluiu de uma apresentação comercial vaga para uma proposta com substância operacional.

### ✅ O que MELHOROU na v2:
- ✅ SLAs definidos (15min critical, 1h high priority)
- ✅ War-room operacional confirmado
- ✅ Uptime target 99.9%
- ✅ Propriedade de dados 100% + APIs + portabilidade
- ✅ SSO/autenticação + integrações com parceiros
- ✅ Cronograma detalhado (14-18 semanas)
- ✅ Custo fixo all-inclusive (sem variação por tráfego)
- ✅ Plataformas: Web + Mobile via WebView/SDK
- ✅ Features: placar exato, previsões especiais, ligas ilimitadas, antifraude
- ✅ Consentimento para menores de idade

### ❌ O que AINDA FALTA:
- ❌ **Provedor cloud não especificado** (AWS? GCP? Azure?)
- ❌ **LGPD/GDPR detalhamento** (mencionado implicitamente, sem detalhes)
- ❌ **Certificações** (ISO, SOC) e pen tests
- ❌ **Cases de escala** anteriores (nenhuma referência)
- ❌ **Dados esportivos** (provedor e custo não especificados)
- ❌ **Notificações** (push, email, CRM) não mencionadas
- ❌ **Social sharing** não mencionado
- ❌ **Quizzes/Lucky Numbers/Sorteios** não confirmados
- ❌ **Modelo premium/freemium** não detalhado
- ❌ **Design/UX** (quem faz?) não especificado
- ❌ **Escopo do que está EXCLUÍDO** não definido

> 🟡 **Recomendação atualizada:** Rooster evolui de "proposta tecnicamente vazia" para **"proposta com substância mas ainda incompleta"**. Os SLAs, propriedade de dados, cronograma e custo fixo são positivos. Porém, a ausência de cases de escala, detalhes de LGPD/certificações e provedor cloud continuam sendo riscos. Necessário: (1) solicitar detalhamento de infra/cloud, (2) evidence de load tests, (3) LGPD/certificações, (4) clarificação sobre quizzes/sorteios e notificações.
