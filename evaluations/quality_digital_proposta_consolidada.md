# Quality Digital – Proposta Consolidada
## Bolão Digital Cazé TV / Omni55

**Fornecedor:** Quality Digital (Quality Software S.A.) — *Software House, Outsourcing*
**Proposta Nº:** 101876
**Data:** 20/02/2026
**Responsável:** Antonio Filgueiras (Quality)
**Validade:** 30 dias

> ⚠️ **MODELO DIFERENTE:** Quality Digital é uma **software house** (body shop / outsourcing), NÃO fornecedor de produto SaaS. Entrega mão de obra + código-fonte proprietário do cliente.

---

## 📋 Resumo Executivo

Quality propõe **construir do zero** uma plataforma de bolão digital como software proprietário da Cazé TV. O escopo é um **MVP limitado** que cobre apenas o core (palpites, ligas, ranking). Todas as funcionalidades de gamificação (quiz, missões, sorteios, lucky numbers, badges) ficam para uma **"Fase 2"** sem orçamento nem cronograma definidos.

**Pontos-chave:**
- 💰 **Custo visível:** R$ 626.777,50 (dev + sustentação)
- 💰 **Custo real estimado:** R$ 1.2M+ (com infra AWS, OPTA, design, Fase 2)
- 📅 **Go-live:** 04/Maio/2026 (kick-off leva 30-45 dias → timeline no limite)
- 🏗️ **Modelo:** Squad dedicado de desenvolvimento, NÃO plataforma pronta
- 📱 **Plataforma:** Web responsiva (mobile-first). SEM apps nativos (iOS/Android)
- 🔐 **LGPD:** Melhor detalhamento entre todos os fornecedores
- 📊 **Dados:** 100% proprietários do cliente (código + dados + infra)

---

## 💰 Investimento

| Item | Valor | Observação |
| :--- | :--- | :--- |
| **Desenvolvimento MVP** | R$ 444.205,98 | 2 meses de desenvolvimento |
| **Sustentação Copa** | R$ 182.571,52 | 45 dias durante a Copa |
| **TOTAL VISÍVEL** | **R$ 626.777,50** | ~$105k USD |
| Infraestrutura AWS | ❓ | **Custo do CLIENTE** (variável) |
| Licenciamento OPTA | ❓ | **Custo do CLIENTE** |
| Designer/UX | ❓ | **Não incluso no squad** |
| Notificações/CRM | ❓ | **Fora do escopo** |
| Fase 2 (gamificação) | ❓ | **Sem orçamento** |
| **CUSTO REAL ESTIMADO** | **R$ 1.2M+** | ~$200k+ USD |

**Pagamento:** Entrada 15% (não reembolsável) + mensalidades (30 dias). Horas extras = +100%.

---

## 🏗️ Arquitetura Técnica

| Componente | Tecnologia | Observação |
| :--- | :--- | :--- |
| Frontend | **Next.js (React)** | Web responsiva, mobile-first |
| Hosting Frontend | **Vercel** | CDN global, edge cache |
| Backend | **NestJS (Node.js/TypeScript)** | Containers AWS ECS Fargate |
| Banco de Dados | **Aurora PostgreSQL (MultiAZ)** | Alta disponibilidade |
| Cache/Ranking | **Redis (ElastiCache)** | Sorted Sets para ranking |
| Mensageria | **AWS SQS + DLQ** | Pipeline assíncrono |
| CMS | **Strapi (Headless)** | Gestão de conteúdo |
| Dados Esportivos | **OPTA** | Contratação pelo cliente |
| Observabilidade | **CloudWatch** | Logs, metrics, alertas |
| Segurança | **WAF, TLS, Secrets Manager** | Rate limit, criptografia at-rest |

✅ Arquitetura moderna e cloud-native. Auto-scaling via Fargate.
⚠️ Nunca testada para escala Copa do Mundo.

---

## ✅ O que ESTÁ no MVP

- Cadastro/Login (e-mail + senha)
- Consentimentos LGPD (com auditoria: user_id, timestamp, IP, versão)
- Palpites de placar (A x B) para todos os jogos
- Motor de pontuação (acerto exato, vencedor, empate)
- Ligas Públicas (Base CazéTV + Premium Sponsor)
- Ligas Privadas (criação via link/código)
- Ranking global e por liga (tempo real via Redis)
- Integração OPTA (polling → SQS → Worker → ranking)
- CMS Strapi (benefícios, regras, conteúdo)
- Classificação Base/Premium (sponsor-ready, feature flag)

## ❌ O que NÃO está no MVP (Fase 2 – sem orçamento)

- ❌ Quiz / Missões funcionais (apenas placeholder visual)
- ❌ Lucky Numbers / Números da sorte
- ❌ Sorteios / Premiações regulamentadas
- ❌ Gamificação avançada (badges, níveis, insígnias)
- ❌ IA / LLM (oráculo, recomendações)
- ❌ Estatísticas avançadas
- ❌ Push notifications / Email automation
- ❌ Integração CRM / CDP
- ❌ Marketing automation
- ❌ Social sharing
- ❌ Apps nativos (iOS / Android)
- ❌ Busca na plataforma
- ❌ Multi-idioma / expansão internacional

---

## 📅 Cronograma

| Fase | Duração | Observação |
| :--- | :--- | :--- |
| Assinatura do Contrato (MSA) | - | Pré-requisito |
| Kick-off (montagem do squad) | **30-45 dias** | ⚠️ Muito longo |
| Desenvolvimento MVP | **2 meses** | ~8 semanas |
| **Go-Live alvo** | **04/Maio/2026** | ⚠️ Para viabilizar, contrato deveria ter sido assinado em início de fev |
| Sustentação Copa | **45 dias** | Pós-launch, incluso no orçamento |

> ⚠️ **ALERTA DE PRAZO:** Em 20/02/2026, o prazo já está comprometido. Kick-off de 30-45 dias + 2 meses dev = go-live ~meados de junho. **Go-live em 04/maio é INVIÁVEL** no cenário atual.

---

## 🔐 Segurança e LGPD

**✅ Melhor detalhamento de LGPD entre TODOS os fornecedores avaliados:**

- Consentimentos no cadastro com persistência em banco (auditoria completa)
- Registro: user_id, timestamp, versão do termo, IP
- Checkboxes para: Termos de Uso, Comunicações CazéTV, Compartilhamento sponsor
- WAF + rate limit nas rotas críticas
- TLS end-to-end
- Secrets Manager para credenciais
- Criptografia at-rest (Aurora/Redis)
- Logs sem dados sensíveis (masking: CPF, e-mail, telefone)

**❌ Não coberto:** Verificação de idade, fluxo para menores, portal de privacidade completo (Fase 2).

---

## 📊 Dados e Propriedade

| Aspecto | Status | Observação |
| :--- | :--- | :--- |
| **Propriedade dos dados** | **100% CLIENTE** | Melhor modelo possível |
| **Código-fonte** | **100% CLIENTE** | Entregue a cada sprint |
| **Infraestrutura** | **100% CLIENTE** | Conta AWS do cliente |
| **Repositório** | GitLab (acesso total p/ tech lead) | Quality administra durante projeto |
| **Lock-in** | **ZERO** | Nenhuma dependência |

---

## ⚖️ Responsabilidades

| Responsabilidade | Quem |
| :--- | :--- |
| Desenvolvimento (código) | Quality |
| Design / UX | **❓ CLIENTE (não incluso)** |
| Infraestrutura AWS (custos) | **CLIENTE** |
| Licenciamento OPTA (custos) | **CLIENTE** |
| APIs de Sponsors (docs, sandbox) | **CLIENTE** |
| Operação / Monitoramento pós-Copa | **CLIENTE** |
| Suporte ao Usuário | **CLIENTE** |
| Product Owner (PO) | **CLIENTE (obrigatório)** |
| Sustentação durante Copa (45d) | Quality |

---

## 🏢 Sobre a Empresa

- **Fundação:** 1989 (37 anos)
- **Tipo:** Software House / Outsourcing de TI
- **Listada:** B3 – BOVESPA MAIS (QUSW3)
- **Acionistas:** BNDES Participações, Invest Tech
- **Sede:** Rio de Janeiro
- **Filiais:** SP, PR, México, NYC, Barcelona
- **Aquisição:** ACCT Global (2022) – líder VTEX, Great Place to Work
- **DNA:** TI corporativa, e-commerce, outsourcing
- **Cases esportivos/gaming:** ❌ ZERO

---

## 🔍 Avaliação Geral

### ✅ Forças
1. **Propriedade total** – Código, dados e infra 100% do cliente. Zero lock-in.
2. **LGPD detalhada** – Melhor implementação de consentimento e compliance entre todos os fornecedores.
3. **Arquitetura moderna** – Stack cloud-native (Next.js, NestJS, AWS Fargate, Aurora, Redis, SQS).
4. **Empresa sólida** – 37 anos, B3, BNDES. Governança corporativa forte.
5. **Presença local** – 100% brasileiro, equipe nativa.

### ⚠️ Riscos
1. **❌ Modelo errado** – Software house ≠ plataforma de produto. Cliente opera TUDO.
2. **❌ MVP muito limitado** – ~40% das features necessárias. Gamificação toda fora do escopo.
3. **❌ Zero experiência no domínio** – Nenhum case de gaming/esporte/predictor em escala.
4. **❌ Custos ocultos** – R$ 626k visível, R$ 1.2M+ real. Infra, OPTA, design, Fase 2 são extras.
5. **❌ Timeline inviável** – Kick-off 30-45 dias + 2 meses dev. Go-live maio praticamente impossível.
6. **❌ Zero re-engagement** – Sem notificações, CRM, email, push. Fora do escopo.
7. **❌ Sem apps nativos** – Apenas web responsiva.

### 📊 Rating: **2.5/5**

### 🚨 Recomendação: **DISCARD**
Quality Digital é uma empresa competente, mas é **o tipo errado de fornecedor** para este projeto. O projeto precisa de uma **plataforma pronta e gerenciada** com experiência comprovada em eventos massivos, não uma software house construindo do zero com escopo limitado.

**Possível uso alternativo:** Quality poderia ser um **parceiro complementar** para desenvolver integrações customizadas, apps nativos, ou features específicas – trabalhando junto a um fornecedor primário de plataforma (Genius Sports ou Fan Arena).
