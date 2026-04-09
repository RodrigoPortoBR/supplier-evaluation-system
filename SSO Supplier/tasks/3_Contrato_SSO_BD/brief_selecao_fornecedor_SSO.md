# Brief de Seleção — Fornecedor de SSO e Banco de Dados de Usuários
**Projeto:** Bolão CazéTV Copa do Mundo 2026
**Data:** Abril de 2026
**Status:** 🔴 Urgente — Bloqueador crítico da integração LiveLike

---

## 1. Contexto do Projeto

A CazéTV está desenvolvendo um **bolão digital para a Copa do Mundo 2026**, uma plataforma de engajamento de fãs onde os usuários podem fazer previsões de jogos, acumular pontos, competir em ligas e receber premiações. São esperados mais de **15 milhões** de usuários com contas criadas durante a Copa do Mundo 2026.

A plataforma de engajamento será construída com a LiveLike. **A LiveLike não armazena dados de identidade (PII).** Ela opera com um modelo de identidade federada: recebe um token de autenticação gerado pelo nosso próprio sistema de identidade (SSO), cria um mapeamento interno (LiveLike ID ↔ CazéTV ID) e mantém apenas os dados de gameplay. **Toda a identidade do usuário — cadastro, login, autenticação — é o que estamos procurando montar com um fornecedor.**

---

## 2. O Desafio

Precisamos contratar um fornecedor que assuma integralmente a responsabilidade de:

1. **Projetar e implementar** o sistema de identidade digital e banco de dados de usuários da CazéTV
2. **Manter e sustentar** essa infraestrutura durante todo o período do projeto (Copa 2026 e pós-copa)
3. **Garantir SLA de disponibilidade e escalabilidade**, especialmente durante picos de tráfego extremo

Estamos falando de:

- **Público B2C de massa** — fãs de futebol no Brasil, sem perfil técnico
- **Pico de cadastro imprevisível** — expectativa de **milhões de criações de conta em poucos minutos** durante chamadas comerciais e estreia da plataforma
- **Janela de entrega agressiva** — O banco precisa estar pronto e integrado com a LiveLike ao final de Abril/26.
- **Extensibilidade futura** — a arquitetura deve suportar a eventual inclusão de um sponsor, o que pode requerer federação de um segundo provedor de identidade sem refatoração completa

---

## 3. Escopo Esperado do Fornecedor

### 3.1 Implementação (Fase 1 — Crítica)

| Entregável | Descrição |
|---|---|
| **Banco de dados de usuários** | Banco escalável para armazenar identidade, PII e credenciais dos usuários CazéTV |
| **Fluxo de cadastro** | Criação de conta via email/senha ou login social (Google, Apple, Facebook) |
| **Autenticação e sessão** | Emissão de token JWT/OIDC compatível com o padrão esperado pela LiveLike |
| **SSO endpoint** | Endpoint de autenticação que a LiveLike chama para validar o usuário e receber o token |
| **Handshake LiveLike** | Integração e certificação do fluxo completo: CazéTV Auth → LiveLike ID mapping |
| **Gestão de pico** | Estratégia de auto-scaling e warm-up para suportar criação massiva de contas simultâneas -> Qual o peak que o banco aguenta? |

### 3.2 Sustentação (Fase 2 — Ongoing)

| Entregável | Descrição |
|---|---|
| **Monitoramento 24/7** | Dashboards de saúde do sistema com alertas proativos |
| **SLA de uptime** | Mínimo 99,9% de disponibilidade — especialmente durante os jogos |
| **Suporte a incidentes** | Resposta máxima de 5 min para incidentes P1 (auth down = bolão down) |
| **Atualizações de segurança** | Patches e manutenção preventiva incluídos no contrato |
| **Documentação completa** | Toda a arquitetura documentada e entregue à CazéTV (sem lock-in) |

---

## 4. Requisitos Técnicos Mínimos

> **Não precisamos estar amarrados** a uma solução específica (Auth0, Firebase, Cognito, etc.). O que importa é o resultado e a responsabilidade contratual.

- Suporte nativo a **OIDC / OAuth 2.0 / JWT** — obrigatório para a integração LiveLike
- Arquitetura em **cloud pública** com auto-scaling configurado
- Capacidade comprovada de suportar **picos de 100k+ req/min** de autenticação
- Conformidade com **LGPD** — PII armazenado no Brasil ou com acordo de tratamento de dados
- Arquitetura extensível para **federação de identidade futura** (ex: Sponsor como IdP secundário)
- Entrega do **banco funcional até o final de Abril/26** 

## 5. O que esperamos na proposta

Pedimos que o fornecedor inclua em sua resposta:

1. **Arquitetura proposta** — visão técnica da solução de identidade
2. **Timeline detalhado** — do kick-off à integração com LiveLike
3. **Cases de referência** — projetos B2C com picos de tráfego similares
4. **Modelo de SLA** — uptime, tempo de resposta a incidentes, manutenção
5. **Custo** — implementação (fase 1) e sustentação mensal (fase 2), separados
6. **Plano de extensibilidade** — como suportariam a adição de um IdP secundário (sponsor) sem refatoração
7. **Robustez** - evidência de robustez da solução. Qual o pico de requisições/seg?

---

## 6. Prazo
**Prazo para recebimento de propostas:** 08/06
**Prazo alvo de kick-off:** o mais breve possível a partir de 09/06.
