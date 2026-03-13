# Comparativo: Low6 vs. LiveLike
### Decisão de Tecnologia — Bolão CazéTV Copa do Mundo 2026

---

| Tópico | Low6 | LiveLike | Vantagem |
|---|---|---|:---:|
| **1. Escala e Infra** | >1M simultâneos (BBC). Azure com auto-scaling e DevOps dedicado. Confiança declarada para 15M usuários totais. | >10M simultâneos (Yahoo Sport, Bleacher Report). AWS com auto-scaling. SLA formal será enviado. | LiveLike |
| **2. Suporte Operacional** | UK (fuso –4h). SLA P1 ≤10 min, 24/7 documentado. Suporte B2C (L1) **operado pela Low6** via chat PT-BR ($15k). | EUA (fuso –2h, melhor alinhamento). SLA P1 = 2h em horário comercial — 24/7 precisa ser negociado. L1 B2C **fica com a CazéTV**. | Low6 |
| **3. Suporte ao Usuário Final** | Low6 assume integralmente o L1 B2C (chat PT incluso). ~87% dos chamados são login/senha — resolvidos sem envolver a CazéTV. | CazéTV monta e opera 100% do L1. LiveLike só toca L2/L3 (bugs técnicos). Carga operacional interna alta. | Low6 |
| **4. Segurança e LGPD** | ISO 27001. Atua como Data Processor (processa dados pessoais) — exige DPA robusto. Risco LGPD médio. | SOC 2. Não armazena PII — opera apenas com hash IDs. Risco LGPD praticamente zero por design. | LiveLike |
| **5. Propriedade dos Dados** | 100% CazéTV. Pipeline Fivetran → Snowflake com acesso irrestrito. Export garantido em caso de saída. | 100% CazéTV. API First — múltiplos endpoints em tempo real. Export garantido. Não guarda PII desde o dia 1. | Empate |
| **6. Funcionalidades Core** | Score Predictor, Leaderboards, Badges, Missões, Lucky Numbers, SSO. AI Guess (**não disponível** — custom). Live Predictions não confirmado. | Mesmo escopo + **AI Guess nativo** (case PFL), Live Predictions, Quizzes, Polls, Missões e Badges out-of-the-box. Motor mais completo. | LiveLike |
| **7. Gestão de Ligas** | Pública, privada, premium. Free: participa até 5 ligas. Premium: cria até 100. Anti-bot via XtremePush (**custo extra por SMS**). | Pública, privada, premium. Sem limite arquitetônico de ligas. Anti-bot via JWT nativo — gratuito e mais robusto. | LiveLike |
| **8. Operação do Jogo** | Tempo real via feed OPTA (CazéTV já possui). Hosting Azure pass-through: ~$5–10k/mês por faixa de MAU. | Tempo real via OPTA (idem). Custo de uso embutido no pacote de $200k — sem variável mensal de hosting. | Empate |
| **9. Customização e UX** | Produto construído **do zero** baseado no protótipo Lovable. 2 rodadas de revisão de design incluídas. Subdomain dedicado externo. | CMS 100% themeable com Professional Services. Produto base customizado (não do zero). Design por guidelines. | Low6 (leve) |
| **10. Integrações e Parceiros** | Low6 **assume a implementação do SSO do parceiro** (ex: Amazon Prime, iFood), trabalhando diretamente com o parceiro. | API First robusto. SSO **fica sob responsabilidade da CazéTV** — exige infra própria ou contratação de parceiro SSO (custo extra). | Low6 |
| **11. CRM e Notificações** | CRM Integration & Management **incluído**. Push, Email e In-app out-of-the-box via XtremePush. Operado pela Low6. | Fornece webhooks/triggers. CRM externo, Push Provider e templates são **responsabilidade da CazéTV** — custo e operação adicionais. | Low6 |
| **12. Viralidade e Social** | Compartilhamento via mecânica de Lucky Numbers. Plataformas confirmadas de forma genérica ("social media"). | WhatsApp explicitamente confirmado + redes convencionais. Crucial para o mercado brasileiro. | LiveLike (leve) |
| **13. Georrestrição** | Capacidade técnica existe (Bet365), mas não foi discutida para este projeto. | Confirmado — restrição por IP/geofencing disponível e de fácil implementação. | LiveLike |
| **14. Cronograma** | Kick-off 23/mar → Go-Live **18/mai** (~8 semanas). UAT incluído. Risco médio de concorrência de capacidade com outros clientes. | Kick-off imediato → Go-Live **11/mai** (1 semana antes). Baixo risco de sobrecarga de capacidade interna. | LiveLike |
| **15. Custo Total (TCO)** | Proposta oficial ~US$ 165–200k (plataforma $150k + L1 suporte $15k + hosting Azure $5–10k/mês). **Valor de hosting não validado. Considerar $200k. Valor Total $365k-400k. Suporte incluído.** | Pacote base + overage acima de 10M usuários.**~US$ 325–425k**  Sem suporte e banco de dados — CazéTV arca com ambos externamente. | Low6 |
| **16. Experiência e Cases** | Case direto Copa 2022 (Sportsbet Austrália): App grátis #1, 4x logins diários, 34% signups via indicação. Premiado SBC/EGR. | Yahoo Sport, Bleacher Report, PFL, Chelsea FC. Background forte em publishers de mídia. Sem case direto de Copa. | Low6 (leve) |
| **Média Avaliação (1–5)** | **3.87** | **4.37** | LiveLike (técnico) |

---

## Resumo dos Fornecedores

**Low6** — Proposta turn-key onde o fornecedor opera a plataforma de ponta a ponta: CRM, push notifications, suporte B2C em PT-BR e design estão incluídos. Custo ~2x menor que a LiveLike no TCO total. O case da Copa 2022 com a Sportsbet Austrália valida diretamente a tese (App #1 grátis, aquisição massiva via bolão F2P). As limitações (sem app nativo, anti-bot com custo extra, fuso UK) são gerenciáveis. Ideal para quem quer um parceiro que execute.

**LiveLike** — Plataforma tecnicamente mais completa e sofisticada. AI Guess nativo, live predictions, anti-bot JWT sem custo, LGPD quasi-zero por design e maior escala comprovada. O problema: o modelo presupõe que a CazéTV opera CRM, push, SSO e suporte B2C internamente — implicando custo oculto e carga operacional adicional numa janela de 8 semanas. O custo premium (~US$ 325–425k) não inclui essas peças.

---

## 🏆 Veredito: **Low6**

**A CazéTV não é uma empresa de tecnologia** — e a Low6 é o único fornecedor que leva esse ponto a sério. Em vez de entregar infraestrutura e devolver a "bucha" operacional para o cliente, a Low6 assume integralmente CRM, suporte B2C, notificações e design num único pacote de ~US$ 165k.

A diferença técnica da LiveLike (AI Guess, anti-bot JWT, escala superior) é real, mas **não é determinante** para a Copa 2026. O case direto da Copa 2022 com a Sportsbet valida precisamente o que está sendo construído aqui; o cronograma agressivo não comporta montar CRM, SSO e time de L1 em paralelo; e o orçamento economizado (~US$ 160–260k) pode ir para marketing e aquisição de usuários — onde o impacto é muito maior.

**Próximos passos imediatos:**
1. Cruzar custo do XtremePush (`Low6_MarComm_Pricing_USD.pdf`) para 15M de usuários
2. Negociar cláusula de portabilidade e saída pós-Copa no contrato
3. Confirmar estratégia de web push para usuários sem app nativo (PWA)
4. Iniciar Kick-off em **23 de Março** — sem atraso
