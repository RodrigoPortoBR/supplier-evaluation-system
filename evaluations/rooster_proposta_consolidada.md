# Rooster – Proposta Consolidada
**Projeto:** Bolão Copa do Mundo 2026 – CazéTV  
**Documento base:** Proposta recebida em 18/02/2026  
**Formato:** Apresentação (slides) – 10 páginas

---

## 1. Infraestrutura técnica e robustez

- **Cloud:** Infraestrutura cloud "altamente resiliente" (provedor não especificado)
- **Capacidades declaradas:**
  - Auto-scaling para picos massivos
  - Balanceamento global de carga
  - Sistemas redundantes
  - Monitoramento em tempo real
  - "Suporte para milhões de acessos"
- **Testes de performance:** Mencionados como parte do escopo ("testes de performance" na frente de Infraestrutura)

> ⚠️ **Observação:** Informações muito genéricas. Não há detalhes sobre provedor cloud (AWS, GCP?), região de hospedagem, números concretos de capacidade (RPS, usuários simultâneos), plano de load test específico ou estratégia de degradação graciosa. Nenhuma referência a cases anteriores de grande escala.

---

## 2. Suporte Local

- **Equipe dedicada:** ~7 profissionais full-time alocados exclusivamente
  - **Tecnologia (4):** Desenvolvimento, performance, monitoramento e escalabilidade
  - **Operação e Produto (3):** Interface direta com CazéTV, ajustes operacionais e suporte técnico
- **Plantão:** Regime de plantão técnico contínuo durante dias de jogos
- **Idioma:** Empresa brasileira – suporte nativo em português

> ✅ **Ponto positivo:** Por ser empresa brasileira, não há barreira de idioma, fuso horário ou necessidade de treinamento de equipe local.

---

## 3. SLA em caso de incidentes

- `[Não informado]` – A proposta não detalha:
  - SLA de uptime
  - Tempos de resposta por severidade
  - Workflow de escalonamento
  - Estrutura de war-room
  - Feature flags / rollback

> ⚠️ **Observação:** Nenhum SLA concreto mencionado. Apenas "suporte técnico imediato" e "monitoramento contínuo" como declarações genéricas.

---

## 4. Segurança da informação

- `[Não informado]` – A proposta **não menciona**:
  - Conformidade LGPD/GDPR
  - Residência de dados
  - Certificações (ISO, SOC)
  - Testes de penetração
  - Verificação de idade / proteção de menores
  - Mecanismos de consentimento

> ⚠️ **Observação crítica:** Zero informação sobre segurança. Para um projeto com milhões de usuários no Brasil, isso é uma lacuna grave.

---

## 5. Dados

- `[Não informado]` – A proposta **não menciona**:
  - Propriedade dos dados
  - Modelo de acesso (API, exports)
  - Cenário de saída / portabilidade
  - Analytics / BI
  - Integração com ferramentas de analytics do cliente

> ⚠️ **Observação:** Nenhuma informação sobre dados, propriedade, acesso ou exportação.

---

## 6. Features previstas

### Mencionado na proposta:
- ✅ Sistema de palpites e rankings em tempo real
- ✅ Ligas públicas e privadas
- ✅ Gamificação, missões e benefícios
- ✅ Integrações com parceiros
- ✅ IA de sugestões e estatísticas

### Não detalhado:
- ❓ Tipos de palpite (1x2, placar exato, props, ao vivo)
- ❓ Tipos de ranking (global, por período, por região)
- ❓ Boosters, troféus, conquistas
- ❓ Lógica de pontuação configurável
- ❓ Estrutura de prêmios
- ❓ Quizzes / trivia diária
- ❓ Lucky numbers / loteria
- ❓ Modelo freemium vs premium

> ⚠️ **Observação:** As features são listadas em alto nível (bullet points de slide) sem qualquer detalhamento de funcionalidades, regras ou capacidades específicas. "IA de sugestões e estatísticas" é o único diferencial mencionado, mas sem explicação de como funciona.

---

## 7. Customização UX / Front-end

- `[Não informado]` – A proposta **não menciona**:
  - Nível de customização (white-label, full custom, skin)
  - CSS/temas
  - Domínio/subdomínio
  - Responsividade mobile
  - Quem faz o design (Rooster ou cliente)
  - App nativo vs web

---

## 8. Integração / Login

- **Mencionado:** "Integrações com parceiros" (genérico)
- **Não detalhado:**
  - SSO / OAuth / OpenID
  - Modelo freemium/premium
  - Feeds de dados esportivos (provedor?)
  - APIs documentadas
  - Integração com loyalty/CRM

> ⚠️ **Observação:** Apenas uma menção genérica a "integrações". Sem qualquer detalhe técnico.

---

## 9. Comunicações

- `[Não informado]` – A proposta **não menciona**:
  - Email
  - Push notifications
  - Mensagens in-game
  - CRM

---

## 10. Compartilhamento com Redes

- `[Não informado]` – A proposta **não menciona** funcionalidades de compartilhamento social.

---

## 11. Restrição Geolocalização

- `[Não informado]`

---

## 12. Tempo de implementação

- `[Não informado explicitamente]`
- **Inferido pela estrutura de pagamento:**
  - 50% na assinatura → início imediato do desenvolvimento
  - 30% antes do início da Copa → preparação final
  - 20% após encerramento do evento → operação completa
- A proposta menciona 3 frentes: Desenvolvimento → Infraestrutura → Operação durante a Copa

> ⚠️ **Observação:** Nenhum cronograma em semanas/meses. Não há menção a marcos, sprints, ou data estimada de go-live.

---

## 13. Modelo de precificação + o que está incluso

### Investimento total: **R$ 1.154.000,00**

| Parcela | % | Valor | Quando |
|:---|:---|:---|:---|
| 1ª parcela | 50% | R$ 577.000 | Na assinatura do contrato |
| 2ª parcela | 30% | R$ 346.200 | Antes do início da Copa |
| 3ª parcela | 20% | R$ 230.800 | Após encerramento do evento |

### O que está incluído:
- Desenvolvimento completo da plataforma
- Integrações
- Preparação de infraestrutura para alta escala
- Operação dedicada (~7 pessoas) durante toda a Copa
- Testes de performance

### Não está claro se inclui:
- ❓ Infraestrutura cloud (AWS/GCP) — custo incluído ou por conta do cliente?
- ❓ Feeds de dados esportivos (provedor? custo?)
- ❓ Design/UX
- ❓ Suporte pós-copa

> **Comparativo de custos (aproximado):**

| Fornecedor | Custo total estimado | Moeda |
|:---|:---|:---|
| **Rooster** | R$ 1.154.000 (~€185K) | BRL |
| **Fan Arena Opção B** | €359.000 (~R$ 2.240K) | EUR |
| **Fan Arena Opção A** | ~€545.000 (~R$ 3.400K) | EUR |
| **Genius Sports** | A definir (premium enterprise) | USD/EUR |

> ⚠️ **Nota:** A conversão usa taxa aproximada de €1 = R$6,24. Rooster é significativamente mais barato, mas o escopo detalhado é muito menor.

---

## 14. O que está fora do escopo

- `[Não informado]` – A proposta **não menciona** explicitamente o que está fora do escopo. Todos os itens abaixo ficam indefinidos:

| Item | Status |
|:---|:---|
| Cumprimento de prêmios | ❓ Não mencionado |
| Quizzes / Trivia | ❓ Não mencionado |
| Loteria / Lucky Numbers | ❓ Não mencionado |
| CRM / Email / Push | ❓ Não mencionado |
| Pagamentos | ❓ Não mencionado |
| Verificação de idade | ❓ Não mencionado |
| Geo-restrição | ❓ Não mencionado |
| Feeds de dados esportivos | ❓ Não claro se incluso |

---

## ⚠️ Avaliação geral da proposta

A proposta da Rooster é uma **apresentação comercial de alto nível** (10 slides), focada em posicionamento e investimento. **Faltam informações críticas** em praticamente todos os tópicos técnicos e operacionais.

### O que a proposta tem:
- ✅ Valor de investimento claro (R$ 1.154.000)
- ✅ Equipe dedicada definida (7 pessoas)
- ✅ Empresa brasileira (sem barreira de idioma/fuso)
- ✅ Features mencionadas em alto nível

### O que a proposta NÃO tem:
- ❌ Detalhamento técnico (infra, arquitetura, providers)
- ❌ Segurança / LGPD / compliance
- ❌ Dados (propriedade, acesso, portabilidade)
- ❌ SLAs concretos
- ❌ Cronograma detalhado
- ❌ Escopo explícito (o que inclui e o que não inclui)
- ❌ Cases/referências de projetos anteriores
- ❌ Detalhamento de features e regras de jogo
- ❌ Integrações técnicas (SSO, APIs, dados esportivos)

> 🔴 **Recomendação:** Antes de qualquer decisão, é necessário solicitar à Rooster um **documento técnico detalhado** que cubra os pontos acima. A proposta atual não permite comparação justa com Fan Arena ou Genius Sports.
