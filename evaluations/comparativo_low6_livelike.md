# Comparativo: Low6 vs. LiveLike
### Decisão de Tecnologia — Bolão CazéTV Copa do Mundo 2026

---

| Tópico | Low6 | LiveLike | Vantagem |
|---|---|---|:---:|
| **1. Escala e Infra** | >1M simultâneos (BBC). Azure. No Q&A, **descartaram a possibilidade de 10M de usuários no pico**, subestimando o tráfego da CazéTV. | >10M simultâneos (Yahoo Sport, Bleacher Report). Arquitetura clara baseada em AWS, JWT session e RDS Postgres detalhada no Q&A. | LiveLike |
| **2. Suporte Operacional** | UK (fuso –4h). SLA P1 ≤10 min. Promete suporte B2C (L1) via chat PT-BR, mas o time de TI vê risco na governança técnica. | EUA (fuso –2h). SLA P1 = 2h comercial. L1 B2C **fica com a CazéTV**, decisão aceita internamente pela TI para mitigar riscos técnicos. | LiveLike (Confiabilidade) |
| **3. Suporte ao Usuário Final** | Low6 se propôs a assumir integralmente o L1 B2C, mas a falta de profundidade em engenharia gerou desconforto irrecuperável. | CazéTV montará e operará 100% do L1 internamente. LiveLike atua como L2/L3 especialista. | CazéTV/LiveLike |
| **4. Segurança e LGPD** | ISO 27001. Processa dados pessoais. | SOC 2 Tipo 2. Não armazena PII — opera apenas com hash IDs. Risco LGPD quase zero. | LiveLike |
| **5. Propriedade dos Dados** | 100% CazéTV via Snowflake e Azure Data Factory. | 100% CazéTV. API First e Webhooks (detalhado no Q&A). | Empate |
| **6. Funcionalidades Core** | Entrega completa, mas respostas sobre fluxos técnicos foram evasivas sob pressão. | Entrega completa mais out-of-the-box. Motor validado e flexível. | LiveLike |
| **7. Gestão de Ligas** | Pública, privada, premium. Anti-bot XtremePush (custo extra). | Pública, privada, premium. Anti-bot via JWT nativo — gratuito e robusto. | LiveLike |
| **8. Operação do Jogo** | Tempo real via feed OPTA. | Tempo real via OPTA. | Empate |
| **9. Customização e UX** | Produto construído do zero baseado no protótipo. | CMS 100% themeable. Produto base customizado (não do zero). | Empate |
| **10. Integrações (SSO)** | Propôs assumir o login via Snowflake, mas **falhou em explicar os fluxos no Q&A** ("nós cuidaremos do login" repetido 10 vezes). | API First robusto. CazéTV fará o SSO IdP. LiveLike explicou detalhadamente o handshake OIDC/JWT. | LiveLike |
| **11. CRM e Notificações** | CRM e Push (XtremePush) operado pela Low6. | Fornece webhooks/triggers. CazéTV assumirá a operação internamente. | CazéTV/LiveLike |
| **12. Viralidade e Social** | Plataformas confirmadas de forma genérica. | WhatsApp confirmado + redes convencionais. | LiveLike |
| **13. Georrestrição** | Capacidade técnica existe (Bet365). | Restrição por IP/geofencing disponível. | LiveLike |
| **14. Cronograma** | ~8 semanas. Risco médio/alto devido à falta de clareza técnica. | ~7 semanas. Baixo risco de integração técnica devido à maturidade das APIs. | LiveLike |
| **15. Custo Total (TCO)** | Proposta ~$365k-400k (incluindo suporte). Aparentemente mais barata, mas muito arriscada tecnicamente. | ~US$ 325–425k. Sem L1 e DB. Requer esforço interno da CazéTV, mas é o investimento seguro técnico. | LiveLike (Segurança de Entrega) |
| **16. Profundidade Técnica (Q&A)**| **Crítico:** Respostas extremamente rasas. Omitiu explicações de failover, cache e infraestrutura, focando em "nós resolvemos". | **Excelente:** Explicou detalhadamente o isolamento da CazéTV após o login (JWT), telemetria, fallback e SOC 2. | LiveLike |

---

## Decisão Interna de TI e Resumo Analítico

**O Veredito:** A equipe de TI da CazéTV decidiu avançar com a **LiveLike**.

Durante o processo de Q&A técnico profundo, a **Low6** apresentou respostas muito rasas e evasivas para o nível de complexidade exigido pelo projeto. Para perguntas críticas sobre picos absurdos de tráfego (10 milhões de acessos), a Low6 apenas repetiu que "cuidaria do login" e chegou a questionar a viabilidade dos 10 milhões de usuários (indicando que não esperam esse tráfego no pico). Embora a proposta original fosse tentadora (Low6 assumindo o suporte ao usuário e gestão de banco de dados), a equipe interna de tecnologia não se sente confortável em terceirizar a estabilidade primária do Bolão em um evento crítico como a Copa do Mundo para uma empresa que não demonstrou profundidade nas respostas de engenharia.

A **LiveLike**, por outro lado, apresentou respostas de engenharia precisas, baseadas na nuvem AWS, explicando com clareza o fluxo de autenticação via OIDC, a independência das sessões (JWT) após o login, proteção contra quedas e arquitetura de telemetria. 

Portanto, ficou decidido que **faz mais sentido a CazéTV absorver internamente as frentes de suporte L1 e banco de dados de identidade**, garantindo a fundação com a **LiveLike**, que provou ser uma parceira SaaS altamente confiável em termos de entrega tecnológica de escalabilidade massiva.
