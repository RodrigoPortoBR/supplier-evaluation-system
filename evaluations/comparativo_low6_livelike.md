# Comparativo de Fornecedores: Low6 vs. LiveLike
### Decisão de Tecnologia para o Bolão CazéTV — Copa do Mundo 2026

---

## Tabela Comparativa

### 1. 🏗️ Robustez, Escala e Confiabilidade

| Critério | Low6 | LiveLike |
|---|---|---|
| **Pico máximo testado** | >1M simultâneos (BBC Champions League) | >10M simultâneos (Yahoo Sport, Bleacher Report) |
| **Infraestrutura** | Azure com auto-scaling e equipe DevOps dedicada | AWS com auto-scaling nativo |
| **SLA de Uptime** | Não informado formalmente | Documento SLA completo será enviado |
| **App Nativo** | ❌ Apenas Web (Mobile Web App) | ❌ Apenas Web (Mobile Web App) |
| **Escala p/ 15M usuários** | ✅ Confirmado (meta corrigida para total, não simultâneos) | ✅ Confirmado com comprometimento de teste de carga |

**Low6** — Escala comprovada com referências sólidas, mas menor que a LiveLike. Confiança razoável para 15M de usuários totais.  
**LiveLike** — Casos de uso com dezenas de milhões de usuários simultâneos em publishers globais. Margem de segurança maior.

> **Vantagem:** LiveLike (escala bruta superior e SLA formal prometido)

---

### 2. 🛎️ Suporte Local e Cobertura Operacional

| Critério | Low6 | LiveLike |
|---|---|---|
| **Escritório/equipe no Brasil** | ❌ Não (UK) | ❌ Não (EUA) |
| **Fuso Horário** | ⚠️ Diferença de 3–4h (UK vs BR) | ✅ EST alinhado com BR (diferença 1–2h) |
| **Suporte em Português** | ✅ Chat PT-BR confirmado na proposta (B2C L1) | ✅ Renato Drumond e equipe fluente (B2B) |
| **SLA para P1 (incidentes críticos)** | ✅ ≤10 min escalate direto para devs (24/7) | ⚠️ P1: 2h em horário comercial — 24/7 precisa ser negociado |
| **Estrutura de war room em eventos** | Não detalhado | Não detalhado |

**Low6** — Apesar de estar no UK, o SLA de P1 ≤10 min e o suporte 24/7 formal mitigam o fuso. Cobrem também o L1 B2C (usuário final) via chat em PT-BR.  
**LiveLike** — Fuso mais favorável (EST ≈ BR), mas SLA de P1 restrito ao horário comercial é preocupante para jogos noturno/fins de semana. L1 B2C fica 100% com a CazéTV.

> **Vantagem:** Low6 (SLA 24/7 documentado + L1 B2C op. pelo fornecedor)

---

### 3. 👥 Suporte ao Usuário Final e Gestão de Incidentes

| Critério | Low6 | LiveLike |
|---|---|---|
| **Quem cuida do usuário final (L1)** | ✅ Low6 — chat PT-BR incluso por $15k | ❌ CazéTV — LiveLike não opera B2C |
| **Bugs técnicos (L2)** | ✅ Low6 — equipe interna + hot fixes | ✅ LiveLike — corrige via API/Engenharia |
| **Falhas de infra (L3)** | ✅ Low6 DevOps + Azure | ✅ LiveLike + AWS |
| **Fluxo de escalação** | P1/P2/P3 24/7 estruturado | P1/P2/P3 via Slack com SLA comercial |
| **Carga operacional p/ CazéTV** | ✅ Mínima — quase zero | ⚠️ Alta — CazéTV monta time de L1 interno |

**Low6** — Remove completamente a "bucha" do suporte B2C da CazéTV. ~87% dos chamados são problemas de login/senha, e a Low6 absorve tudo.  
**LiveLike** — Filosofia clara: "its your customers, not ours." A CazéTV precisará montar, treinar e operar uma equipe de suporte ao usuário, além de definir email de contato, FAQ, etc.

> **Vantagem:** Low6 (suporte B2C turn-key remove carga interna)

---

### 4. 🔐 Segurança, LGPD, Governança e Compliance

| Critério | Low6 | LiveLike |
|---|---|---|
| **Certificação** | ISO 27001 | SOC 2 |
| **LGPD/GDPR** | ✅ Sim (via ISO 27001) | ✅ Sim — não retém PII, apenas IDs hashados |
| **Risco LGPD** | ⚠️ Médio — processa dados pessoais como Data Processor | ✅ Mínimo — não toca PII, SSO fica na CazéTV |
| **Verificação de Idade** | Checkbox simples na entrada, KYC apenas no resgate | Via SSO do cliente |
| **Proteção de menores** | Não detalhado | Delegado ao SSO da CazéTV |

**Low6** — ISO 27001 é sólido, mas como atuam como Data Processor processando dados pessoais, o risco LGPD é real e exige DPA robusto.  
**LiveLike** — Arquitetura elegante: como só operam com hash IDs e o SSO fica no cliente, o risco legal cai drasticamente. SOC 2 é padrão do mercado americano.

> **Vantagem:** LiveLike (design arquitetural limpo — PII nunca toca o fornecedor)

---

### 5. 🗄️ Propriedade, Acesso e Portabilidade de Dados

| Critério | Low6 | LiveLike |
|---|---|---|
| **Propriedade dos dados** | ✅ 100% CazéTV (Low6 = Data Processor via DPA) | ✅ 100% CazéTV (LiveLike opera apenas hash IDs) |
| **Acesso em tempo real** | Via Tableau dashboards | APIs em tempo real ("API First Company") |
| **Pipeline de dados** | Fivetran → Snowflake (acesso irrestrito) | APIs diretas + exports automatizados |
| **Portabilidade na saída** | ✅ Via acesso livre ao Snowflake | ✅ Exportado ou deletado na saída |
| **APIs para integração de dados** | Não detalhado | ✅ Robusto — múltiplos endpoints |

**Low6** — Solução de dados madura com Fivetran+Snowflake. CazéTV pode baixar tudo a qualquer momento. Tableau para visualização.  
**LiveLike** — "API First" em essência. Dados sempre acessíveis via endpoints. Por não guardar PII, a portabilidade é praticamente imediata.

> **Empate** (ambos oferecem propriedade plena e portabilidade garantida)

---

### 6. 🎮 Funcionalidades Core e Prontidão do Produto

| Critério | Low6 | LiveLike |
|---|---|---|
| **Predição de Placar Exato** | ✅ Out-of-the-box | ✅ Out-of-the-box |
| **Predições Especiais** | ✅ (Campeão, artilheiro, fase de saída) | ✅ (Campeão, artilheiro, fase de saída) |
| **Live Predictions** | ❓ Não discutido | ✅ Disponível |
| **AI Guess / Oráculo** | ❌ Não disponível (desenvolvimento custom) | ✅ Out-of-the-box (case PFL demonstrado) |
| **Scoring configurável** | ✅ Multiplicadores por fase | ✅ Multiplicadores por fase |
| **Missões / Desafios Diários** | ✅ Quiz diário + missões premium | ✅ Out-of-the-box |
| **Badges e conquistas** | ✅ (raras, épicas, lendárias com animações) | ✅ Nativo |
| **Sorteiro (Lucky Numbers)** | ✅ Mecânica incluída | ✅ Mencionado via missões |

**Low6** — Maturidade em Score Predictor. Já opera plataformas similares (Bet365, NHL). Gamificação rica com digital rewards animadas.  
**LiveLike** — Excedeu expectativas: AI Guess nativo, live predictions, e todo o core do produto disponível. Motor mais completo out-of-the-box.

> **Vantagem:** LiveLike (AI Guess nativo + live predictions + cobertura mais completa)

---

### 7. 🏆 Gestão de Ligas e Infraestrutura Premium

| Critério | Low6 | LiveLike |
|---|---|---|
| **Ligas públicas** | ✅ | ✅ |
| **Ligas privadas** | ✅ (criar: só Premium; participar: até 5 free) | ✅ (configurável por nível de usuário) |
| **Ligas premium** | ✅ (leaderboard separado para assinantes) | ✅ (via tags SSO do patrocinador) |
| **Limite de ligas privadas** | Free: 5 / Premium: 100 | Sem limite arquitetônico |
| **Ferramentas de moderação** | ⚠️ Parcial (aprovação, senha) | ✅ Built-in robusto |
| **Proteção anti-bot** | ⚠️ Via XtremePush — custo de SMS por uso | ✅ JWT nativo — sem custo extra |

**Low6** — Estrutura de ligas bem pensada e discussão detalhada. Anti-bot é possível mas tem custo adicional por SMS.  
**LiveLike** — Arquitetura JWT é elegante e resolve anti-bot nativamente sem custo. Sem limite de ligas privadas é vantagem operacional importante.

> **Vantagem:** LiveLike (anti-bot JWT nativo gratuito, sem limite de ligas)

---

### 8. ⚽ Operação do Jogo e Pontuação

| Critério | Low6 | LiveLike |
|---|---|---|
| **Atualização em tempo real** | ✅ Via feed OPTA (CazéTV já possui) | ✅ Via feed OPTA (CazéTV já possui) |
| **Atualização pós-jogo** | ✅ | ✅ |
| **Batch diário** | Não detalhado | ✅ |
| **Custos de hosting** | $5k–$10k/mês dependendo de MAU | Embutido no pacote de $200k de uso |

**Low6** — Feed OPTA já resolvido (CazéTV possui). Custos de Azure são pass-through, o que dá visibilidade mas cria variabilidade.  
**LiveLike** — Idem OPTA. Custo de uso embutido no pacote (mais fácil de orçar para a Copa, mas mais caro no total).

> **Empate** (ambos resolvem identicamente a operação do jogo via OPTA)

---

### 9. 🎨 Customização, UX e Design Front-End

| Critério | Low6 | LiveLike |
|---|---|---|
| **Design do zero** | ✅ Plataforma construída baseada no protótipo | ⚠️ Solução base customizável via CMS/tema |
| **Designers dedicados** | ✅ 2 rodadas de revisão incluídas | ✅ Equipe Professional Services |
| **Custom domain (CNAME)** | ✅ Confirmado (subdomain dedicado externo) | ✅ Implícito |
| **Responsabilidade de design** | ✅ Low6 fornece tudo (cliente dá brand guidelines) | ✅ Idem — apenas guidelines necessárias |
| **Grau de customização** | Alto — produto construído do zero | Alto — CMS 100% themeable |

**Low6** — Abordagem "full custom" sobre o framework deles é atraente, pois o produto será construído fielmente ao protótipo Lovable enviado.  
**LiveLike** — CMS themeable robusto, mas a base é uma solução pré-existente customizada, não construída do zero. Pode haver limitações visuais.

> **Vantagem leve:** Low6 (produto construído do zero seguindo o protótipo)

---

### 10. 🔗 Ecossistema de Integrações e Conectividade com Parceiros

| Critério | Low6 | LiveLike |
|---|---|---|
| **SSO** | ✅ Próprio + integração com SSO do parceiro (Low6 opera) | ✅ Fortemente dependente do SSO do cliente |
| **Integração com parceiros (ex: iFood)** | ✅ Via SSO — Low6 assume a implementação | ✅ Via tags dinâmicas no backend |
| **Verificação de assinatura (ex: Amazon Prime)** | ✅ Via SSO | ✅ Via atributos no JWT |
| **APIs documentadas** | ⚠️ Não demonstradas publicamente | ✅ "API First Company" |
| **Ligas por parceiro (ex: Liga iFood)** | ✅ Via SSO | ✅ Via user groups/tags |

**Low6** — Diferencial importante: a Low6 **assume a implementação do SSO do parceiro**, trabalhando diretamente com o parceiro. Reduz carga técnica da CazéTV.  
**LiveLike** — Arquitetura mais flexível e documentada (API First), mas a CazéTV precisa ter ou construir seu próprio SSO — um gap de risco tecnicamente relevante.

> **Vantagem:** Low6 (responsabilidade de SSO do parceiro operada pelo fornecedor)

---

### 11. 📣 Canais, Notificações e Comunicação com Usuário

| Critério | Low6 | LiveLike |
|---|---|---|
| **Push Notifications** | ✅ Out-of-the-box via XtremePush | ✅ Possível via webhooks — CRM da CazéTV |
| **Email Automation** | ✅ Via XtremePush/CRM | ✅ CazéTV opera |
| **Quem gerencia CRM** | ✅ Low6 ("CRM Integration & Management" na proposta) | ❌ CazéTV — LiveLike apenas fornece triggers |
| **Quem gerencia templates** | ✅ Low6 | ❌ CazéTV |
| **Custo de CRM** | Incluído (XtremePush stack) | Custo externo adicional (CRM próprio da CazéTV) |

**Low6** — CRM completamente operado pela Low6 (XtremePush). Push, email e in-app saem automaticamente baseados em eventos (gols, fechamento de liga). Zero carga para a CazéTV.  
**LiveLike** — Fornece webhooks/triggers mas o envio efetivo precisa de um CRM próprio da CazéTV (custo e operação adicionais não previstos no pacote).

> **Vantagem:** Low6 (CRM e notificações turn-key eliminam carga operacional)

---

### 12. 📱 Viralidade e Compartilhamento Social

| Critério | Low6 | LiveLike |
|---|---|---|
| **Compartilhamento nativo** | ✅ (quizzes dobram lucky numbers) | ✅ (redes sociais + WhatsApp) |
| **Plataformas suportadas** | ⚠️ Mencionado genericamente ("social media") | ✅ WhatsApp explicitamente confirmado |
| **Cards personalizados / stories** | Não detalhado | Não detalhado |

**Low6** — Mecânica de compartilhamento vinculada à gamificação (lucky numbers), mas plataformas específicas não confirmadas.  
**LiveLike** — WhatsApp explicitamente confirmado, o que é crucial para o mercado brasileiro.

> **Vantagem leve:** LiveLike (WhatsApp confirmado — canal dominante no Brasil)

---

### 13. 🌎 Georrestrição

| Critério | Low6 | LiveLike |
|---|---|---|
| **Restrição por país** | ⚠️ Capacidade existe (Bet365), não discutida para este projeto | ✅ Disponível e facilmente implementável |
| **Restrição por IP/geofencing** | Provável mas não confirmado | ✅ Confirmado por intervalo de IP |

> **Vantagem:** LiveLike (confirmado e detalhado)

---

### 14. 🗓️ Cronograma e Capacidade de Evolução

| Critério | Low6 | LiveLike |
|---|---|---|
| **Go-Live** | **18 de Maio** (3 semanas antes da Copa) | **11 de Maio** (4 semanas antes da Copa) |
| **Kick-off** | 23 de Março | Imediato |
| **Duração do desenvolvimento** | ~8 semanas (sprint + UAT) | Imediato → Maio |
| **Customização de features** | ✅ Flexível para escopo fechado | ✅ Flexível via Professional Services |
| **Risco de conflito com outros clientes** | ⚠️ Médio (opera Bet365, NHL simultaneamente) | ✅ Baixo |
| **Projeto pós-Copa** | Contrato típico de 12 meses | Expansão natural para Série A, Paulistão etc. |

**Low6** — Cronograma agressivo mas realista, com UAT incluído. Kick-off em 23/03 é crítico — não pode ser atrasado.  
**LiveLike** — Go-Live 1 semana antes — vantagem na captação de base. Menor risco de sobrecarga de capacidade interna do fornecedor.

> **Vantagem:** LiveLike (Go-Live mais cedo, menor risco de capacidade compartilhada)

---

### 15. 💰 Custo, Contrato e Risco Financeiro

| Critério | Low6 | LiveLike |
|---|---|---|
| **Custo total estimado** | **~US$ 165–200k** (US$ 150k plataforma + US$ 15k L1 suporte + hosting Azure ~US$ 5–10k/mês) | **~US$ 325–425k** (US$ 325k pacote base; US$ 20k por cada 1M de usuários acima de 10M) |
| **Modelo de precificação** | Fixo + pass-through de hosting | Híbrido (fixo + usage tiers acima de 10M usuários) |
| **Previsibilidade orçamentária** | ✅ Alta — escopo fechado; variável é só o Azure | ⚠️ Média — risco de overage acima de 10M usuários |
| **CRM / Suporte B2C incluído** | ✅ Sim (XtremePush + Chat PT-BR = $15k) | ❌ Não — CazéTV arca com ambos externamente |
| **Custo real para CazéTV (TCO)** | ~US$ 200k + CRM externo baixo | ~US$ 325–425k + CRM próprio + time de L1 |

**Low6** — Proposta madura e fechada. US$ 165k cobre plataforma + operação B2C. Hosting Azure variável mas com teto previsível.  
**LiveLike** — Custo premium (~2x Low6). O pacote de $200k de usage é robusto, mas não inclui CRM nem L1 — o TCO real é mais alto que parece.

> **Vantagem clara:** Low6 (custo ~2x menor no TCO total)

---

### 16. 🏅 Equipe, Experiência e Referências

| Critério | Low6 | LiveLike |
|---|---|---|
| **Referências de escala** | Bet365 América (~2M registrados), BBC Champions League (>1M simultâneos), Sportsbet Austrália (App #1 grátis na Copa 2022) | Yahoo Sport, Bleacher Report, PFL, Chelsea FC, Tomorrow Golf League |
| **Experiência em Copa do Mundo** | ✅ Sportsbet case Copa 2022 (direto) | ✅ Indireto — publishers de mídia esportiva |
| **Prêmios do setor** | SBC Awards, EGR Awards, #23 empresa de crescimento mais rápido do UK | Background forte em Audience Engagement Software |
| **Foco de mercado** | F2P Games / Betting Entertainment | Audience Engagement / Media Publishers |

**Low6** — Case de Copa 2022 com Sportsbet na Austrália valida diretamente a tese: App #1 grátis, 4x média de logins, 34% signups via indicação. Prêmios do setor em F2P Games.  
**LiveLike** — Referências mais alinhadas editorialmente (publishers de mídia). Sem case direto de Copa, mas escala com Yahoo/Bleacher Report é inquestionável.

> **Empate com leve vantagem Low6** (case direto de Copa 2022 é diferencial relevante)

---

## Placar Geral

| Bloco | Low6 | LiveLike |
|---|:---:|:---:|
| 1. Escala e Confiabilidade | 4 | **5** |
| 2. Suporte Local e Cobertura | **4** | 3 |
| 3. Suporte ao Usuário Final | **4** | 3 |
| 4. Segurança, LGPD, Compliance | 3 | **5** |
| 5. Propriedade e Portabilidade de Dados | 5 | 5 |
| 6. Funcionalidades Core | 4 | **5** |
| 7. Ligas e Infraestrutura Premium | 4 | **5** |
| 8. Operação do Jogo | 4 | 5 |
| 9. Customização e UX | **4** | 4 |
| 10. Integrações e Parceiros | **4** | 5 |
| 11. Notificações e CRM | **5** | 3 |
| 12. Viralidade e Social | 3 | **4** |
| 13. Georrestrição | 2 | **4** |
| 14. Cronograma e Evolução | 4 | **5** |
| 15. Custo e Risco Financeiro | **4** | 3 |
| 16. Experiência e Referências | 5 | 5 |
| **Média Geral** | **3.87** | **4.37** |

---

## Resumo Executivo dos Fornecedores

### 🔵 Low6 — O Pacote Turn-Key

A **Low6** entra nesta disputa como um fornecedor **altamente operacional e completo**. Sua proposta por US$ 165k (plataforma + suporte B2C) não vende apenas uma licença de software — ela entrega um **estúdio virtual** que assume a gestão técnica, o CRM, as notificações push, o chat ao usuário em português e o suporte P1/P2/P3 em regime 24/7. Para uma empresa de mídia como a CazéTV, que não é uma empresa de tecnologia, isso é estruturalmente valioso.

O **case da Copa 2022 com a Sportsbet na Austrália** é o argumento mais poderoso da Low6: App grátis #1 do país, 4x a média de logins diários, 34% de novos usuários via indicação. Eles já fizeram exatamente isso que a CazéTV quer fazer — e funcionou.

As fraquezas existem: ausência de app nativo (e as limitações de push notification que isso traz), plataforma construída do zero (risco de desenvolvimento), SLA com fuso desfavorável (UK) e a dependência do stack XtremePush para CRM. A proposta de preço fechada e a baixa carga operacional interna, contudo, fazem da Low6 uma escolha pragmática, previsível e eficiente para a Copa do Mundo.

---

### 🟣 LiveLike — A Plataforma de Excelência

A **LiveLike** é, tecnicamente, a plataforma mais completa e sofisticada. Seu motor de engagement cobre **todas as funcionalidades desejadas out-of-the-box** — incluindo o AI Guess (Oráculo), live predictions, anti-bot via JWT sem custo adicional, georrestrição nativa, e uma arquitetura API First que facilita integrações complexas. Sua robustez de escala é incontestável (Yahoo Sport, Bleacher Report), e o design arquitetural (não tocar em PII) elimina praticamente o risco LGPD.

O problema da LiveLike é o **modelo de responsabilidade compartilhada**. Por US$ 325–425k, a plataforma entrega a infraestrutura e o software — mas a CazéTV precisa montar e operar seu próprio suporte B2C, seu CRM, suas notificações push e idealmente seu SSO. Isso implica em custo oculto, carga operacional relevante e risco de execução paralela que a CazéTV precisará dar conta durante a Copa.

A LiveLike é a escolha certa se a CazéTV tivesse um time de tecnologia maduro, um CRM já contratado e capacidade de operar B2C internamente. Sem isso, a plataforma mais sofisticada pode se tornar o parceiro mais trabalhoso.

---

## 🏆 Veredito Final

### **Escolha: Low6**

#### Racional da Decisão

A decisão foi tomada com base em **dois eixos principais: contexto operacional da CazéTV e realidade do projeto**.

**1. A CazéTV não é uma empresa de tecnologia.**
O modelo da LiveLike pressupõe que o cliente opera CRM, Push, SSO e L1 de suporte. Isso requer investimento em ferramentas, contratos adicionais e um time técnico interno que a CazéTV não dispõe para montar em 8 semanas. A Low6 **absorve esse peso integralmente**, entregando um produto gerenciado de ponta a ponta.

**2. O budget importa.**
A diferença de custo entre os fornecedores é de US$ 160–260k a mais na LiveLike — e esse custo ainda não conta o CRM externo, a operação de L1 e a eventualidade de um SSO contratado à parte. A Low6 entrega mais por menos, e com previsibilidade orçamentária superior.

**3. O case de Copa da Low6 é determinante.**
A Sportsbet Australia (Copa 2022) valida com precisão a tese do projeto CazéTV: aquisição massiva de usuários via bolão free-to-play durante uma Copa do Mundo, com retenção por gamificação e compartilhamento social. A LiveLike tem cases impressionantes, mas nenhum diretamente equiparável a esse contexto.

**4. O cronograma exige segurança operacional.**
Com Go-Live em 18 de Maio e Kick-off em 23 de Março, não há espaço para montar operação paralela de CRM, suporte e SSO. A Low6 elimina essas variáveis do caminho crítico.

**5. As limitações da Low6 são gerenciáveis.**
- **Sem app nativo**: Já definido que o projeto será 100% web — isso não é uma desvantagem exclusiva, pois a LiveLike também não entrega app nativo.
- **Anti-bot via SMS com custo**: Risco real mas gerenciável com controles de rate-limit e monitoring.
- **Fuso UK**: Mitigado pelo SLA de P1 ≤10 min e cobertura 24/7 documentada.

#### Gaps que precisam ser resolvidos imediatamente com a Low6:
1. ✅ Cruzar o `Low6_MarComm_Pricing_USD.pdf` e validar custo do XtremePush para 15M de usuários
2. ✅ Negociar cláusula contratual de portabilidade e saída pós-Copa
3. ✅ Confirmar estratégia de web push para usuários sem app nativo (PWA / Web Push API)
4. ✅ Iniciar Kick-off em **23 de Março** — qualquer atraso compromete o Go-Live de 18 de Maio
