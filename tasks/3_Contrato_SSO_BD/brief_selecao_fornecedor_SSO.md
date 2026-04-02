# Brief de Seleção — Fornecedor de SSO e Banco de Dados de Usuários
**Projeto:** Bolão CazéTV Copa do Mundo 2026
**Data:** Abril de 2026
**Status:** 🔴 Urgente — Bloqueador crítico da integração LiveLike

---

## 1. Contexto do Projeto

A CazéTV está desenvolvendo um **bolão digital para a Copa do Mundo 2026**, uma plataforma de engajamento de fãs onde os usuários podem fazer previsões de jogos, acumular pontos, competir em ligas e receber premiações.

A plataforma de engajamento será construída sobre a **LiveLike**, uma solução SaaS americana especializada em fan engagement (clientes: Yahoo Sports, Bleacher Report, PFL, Chelsea FC). A LiveLike gerencia toda a lógica do bolão — leaderboards, ligas, badges, AI Guess e live predictions.

**A LiveLike não armazena dados de identidade (PII).** Ela opera com um modelo de identidade federada: recebe um token de autenticação gerado pelo nosso próprio sistema de identidade (SSO), cria um mapeamento interno (LiveLike ID ↔ CazéTV ID) e mantém apenas os dados de gameplay. **Toda a identidade do usuário — cadastro, login, autenticação — é de responsabilidade da CazéTV.**

---

## 2. O Desafio

Precisamos contratar um fornecedor PJ que assuma integralmente a responsabilidade de:

1. **Projetar e implementar** o sistema de identidade digital e banco de dados de usuários da CazéTV
2. **Manter e sustentar** essa infraestrutura durante todo o período do projeto (Copa 2026 e pós-copa)
3. **Garantir SLA de disponibilidade e escalabilidade**, especialmente durante picos de tráfego extremo

### Por que é complexo

Este não é um projeto de SSO corporativo padrão (100 usuários internos). Estamos falando de:

- **Público B2C de massa** — fãs de futebol no Brasil, sem perfil técnico
- **Pico de cadastro imprevisível** — expectativa de **milhões de criações de conta em poucos minutos** durante a divulgação dos jogos e estreia da plataforma
- **Janela de entrega agressiva** — MVP precisa estar pronto e integrado com a LiveLike antes do início da Copa 2026
- **Extensibilidade futura** — a arquitetura deve suportar a eventual inclusão de um sponsor (potencialmente iFood), o que pode requerer federação de um segundo provedor de identidade sem refatoração completa

---

## 3. Escopo Esperado do Fornecedor

### 3.1 Implementação (Fase 1 — Crítica)

| Entregável | Descrição |
|---|---|
| **Banco de dados de usuários** | Banco escalável para armazenar identidade, PII e credenciais dos usuários CazéTV |
| **Fluxo de cadastro** | Criação de conta via email/senha e login social (Google, Apple — a definir) |
| **Autenticação e sessão** | Emissão de token JWT/OIDC compatível com o padrão esperado pela LiveLike |
| **SSO endpoint** | Endpoint de autenticação que a LiveLike chama para validar o usuário e receber o token |
| **Handshake LiveLike** | Integração e certificação do fluxo completo: CazéTV Auth → LiveLike ID mapping |
| **Gestão de pico** | Estratégia de auto-scaling e warm-up para suportar criação massiva de contas simultâneas |

### 3.2 Sustentação (Fase 2 — Ongoing)

| Entregável | Descrição |
|---|---|
| **Monitoramento 24/7** | Dashboards de saúde do sistema com alertas proativos |
| **SLA de uptime** | Mínimo 99,9% de disponibilidade — especialmente durante os jogos |
| **Suporte a incidentes** | Resposta máxima de 30 min para incidentes P1 (auth down = bolão down) |
| **Atualizações de segurança** | Patches e manutenção preventiva incluídos no contrato |
| **Documentação completa** | Toda a arquitetura documentada e entregue à CazéTV (sem lock-in) |

---

## 4. Requisitos Técnicos Mínimos

> O fornecedor **não precisa estar amarrado** a uma solução específica (Auth0, Firebase, Cognito, ou stack própria). O que importa é o resultado e a responsabilidade contratual.

- Suporte nativo a **OIDC / OAuth 2.0 / JWT** — obrigatório para a integração LiveLike
- Arquitetura em **cloud pública** (AWS, GCP ou Azure) com auto-scaling configurado
- Capacidade comprovada de suportar **picos de 100k+ req/min** de autenticação
- Conformidade com **LGPD** — PII armazenado no Brasil ou com acordo de tratamento de dados
- Arquitetura extensível para **federação de identidade futura** (ex: iFood como IdP secundário)
- Entrega de **MVP funcional em até 15 dias** a partir do kick-off

---

## 5. O que NÃO está no escopo deste fornecedor

Para evitar ambiguidade na proposta:

- ❌ Desenvolvimento de frontend ou UI do bolão (responsabilidade da LiveLike + CazéTV)
- ❌ CRM, push notifications ou régua de comunicação (escopo separado)
- ❌ Lógica de negócio do bolão (palpites, leaderboard, ligas) — 100% LiveLike
- ❌ Suporte ao usuário final (L1) — operado pela CazéTV

---

## 6. Critérios de Avaliação dos Propostos

| Critério | Peso |
|---|---|
| Velocidade de entrega do MVP | 🔴 Alto |
| Cases comprovados em B2C de alto volume | 🔴 Alto |
| Modelo de SLA e responsabilidade contratual clara | 🔴 Alto |
| Custo total de implementação + sustentação | 🟡 Médio |
| Experiência com LiveLike ou plataformas similares | 🟡 Médio |
| Flexibilidade de arquitetura para sponsor futuro | 🟡 Médio |

---

## 7. O que esperamos na proposta

Pedimos que o fornecedor inclua em sua resposta:

1. **Arquitetura proposta** — visão técnica da solução de identidade
2. **Timeline detalhado** — do kick-off ao MVP integrado com LiveLike
3. **Cases de referência** — projetos B2C com picos de tráfego similares
4. **Modelo de SLA** — uptime, tempo de resposta a incidentes, manutenção
5. **Custo** — implementação (fase 1) e sustentação mensal (fase 2), separados
6. **Plano de extensibilidade** — como suportariam a adição de um IdP secundário (sponsor) sem refatoração

---

## 8. Contato e Próximos Passos

Interessados devem enviar proposta para **[contato a definir]**.

Após recebimento das propostas, o processo será:
1. Triagem inicial com base nos critérios acima
2. Call técnico de 1h com os finalistas
3. Decisão e kick-off

**Prazo para recebimento de propostas:** a definir
**Prazo alvo de kick-off:** o mais breve possível — este item é bloqueador crítico do projeto
