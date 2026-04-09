# Fan Arena – Proposta Consolidada
**Projeto:** CazéTV World Cup Predictor  
**Documento base:** Proposta recebida em 16/02/2026  
**Contato:** Octavian Susnea – Founder & CEO (octavian@fanarena.com)

---

## 1. Infraestrutura técnica e robustez

- **Cloud:** AWS São Paulo (sa-east-1) – infra na região Brasil
- **Arquitetura proposta para a Copa:**
  - CDN global + cache na borda para assets estáticos
  - Fila de escrita (queue-based buffering) para picos próximos ao deadline de palpites
  - Auto-scaling horizontal de serviços stateless
  - Camada de leitura otimizada (réplicas/cache) para leaderboards
  - Modo de degradação graciosa: leaderboards "somente leitura" como fallback; atualização de rankings com delay se necessário
  - Runbook de "burst readiness" pré-deadline: scale-up antecipado + aquecimento de cache
- **Load test planejado (pré go-live):**
  - Baseline: 15M usuários / 1.5M requisições por segundo (RPS) com dataset completo da Copa
  - Teste de pico (burst): simulando o "minuto do deadline" (~1 hora)
  - Soak test: tráfego alto sustentado durante janelas de jogos ao vivo
- **Capacidades declaradas:**
  - 1 milhão de RPM (requisições por minuto)
  - 15 milhões de contas de usuário
  - 150 milhões de palpites
  - Tudo a ser validado via load testing

> ⚠️ **Observação:** Fan Arena nunca operou nessa escala antes (maior case: ~300K). A arquitetura parece sólida no papel, mas os números são **projeções ainda não comprovadas** – o load test é obrigatório antes do go-live.

---

## 2. Suporte Local

- **Suporte em português:** Incluído — localização em PT-BR + treinamento de pod de suporte ao consumidor L1
- **Suporte técnico:** Fan Arena lida com investigação e correção de bugs técnicos
- **Estrutura de suporte:**
  - Reclamações/dúvidas de usuários: centralizadas em canal Slack
  - Bugs técnicos: investigação e correção pela Fan Arena
  - Time dedicado reservado para o projeto da Copa
- **Garantia:** Bug-free guarantee – se um bug for descoberto no código, a Fan Arena corrige sem custo adicional

> ⚠️ **Observação:** Fan Arena é baseada na Europa (Bélgica). Suporte local é via treinamento de equipe L1 contratada localmente, não equipe própria no Brasil.

---

## 3. SLA em caso de incidentes

- **Workflow para bugs críticos:** Escalonamento por severidade (P0 → P3) com:
  - Rollback toggles / feature flags
  - Passos de reprodução + avaliação de impacto
  - Lane de hotfix (com aprovação + testes automatizados)
- **Workflow para incidentes em larga escala:**
  - Estrutura de comando de incidente:
    - Communications lead → **Cliente**
    - Incident Resolver → **Fan Arena**
    - Data provider liaison → **Fan Arena**
    - Infrastructure liaison → **Fan Arena**
- **SLA de uptime:** A ser definido no SOW (Statement of Work) da Copa
- **War-room:** Planejamento e ensaio de war-room incluídos no escopo

---

## 4. Segurança da informação

- **LGPD/GDPR:** Suporte a GDPR compliance. Como autenticação é via SSO do cliente, a Fan Arena **não processa dados pessoais** além de UUID (ID único do usuário) e nomes de jogo (dados públicos)
- **Hospedagem dos dados:** AWS São Paulo (sa-east-1) – **Brasil**
- **Certificações (ISO, SOC):** Não possuem – alegam que a natureza do produto (jogo) não demanda
- **Verificação de idade / Segurança de menores:** Fora do escopo da Fan Arena – responsabilidade do SSO do cliente
- **Consentimento parental:** Fora do escopo – tratado via SSO

> ⚠️ **Observação:** A posição de segurança é minimalista. A abordagem "não processamos PII" via SSO é inteligente (reduz exposição), mas a falta de certificações formais e a externalização total de verificação de idade/LGPD para o cliente devem ser consideradas.

---

## 5. Dados

- **Propriedade:** 100% do cliente. Fan Arena usa dados apenas para operar o jogo e entregar relatórios (formalizado em DPA/SOW)
- **Restrições:** Nenhuma para uso first-party do cliente
- **Acesso:**
  - Base de usuários: via BI / exports (com SSO, Fan Arena armazena apenas UUID anônimo)
  - Dados comportamentais: via tag de analytics do cliente (ex: GA4) integrada pela Fan Arena
  - Histórico de palpites: logs armazenados no Grafana Loki (escala petabyte, sem audit trail direto)
- **Extração:**
  - Exports pela ferramenta BI: JSON, CSV, XLSX
  - APIs em tempo real: feeds de jogos + web services custom (rankings, resultados, dados de rodada)
  - Dumps agendados: diários/hora durante o torneio para cálculo de leaderboard pós-jogo
- **Cenário de saída:**
  - Contas de usuário: identidade fica com o cliente (SSO); Fan Arena deleta referências anônimas imediatamente, incluindo backups
  - Dados históricos: export completo via BI + dumps; confirmação de deleção após transferência
  - **Export completo garantido** usando schemas e canais de entrega acordados

---

## 6. Features previstas

### ✅ Disponível out-of-the-box:
- Web app responsivo multi-dispositivo
- Interface multi-idioma (incluindo PT-BR)
- Ligas privadas
- Boosters, troféus, bônus de pontos
- SSO integrado + data supplier + pagamentos (opcional)
- Insights/reporting, monitoramento de KPIs

### 🔧 Customizável (recomendado para diferenciação):
- Regras de pontuação, critérios de desempate, pesos de pontos
- Design do jogo (segundo guidelines de marca)
- Períodos do torneio (fase de grupos / oitavas / quartas / semis / final)
- Lógica de premiação branded + posicionamentos de patrocinadores

### ⏳ A ser definido:
- ❓ **Quizzes** – fora do escopo atual
- ❓ **Desafios diários / outros jogos não-predictor** – fora do escopo atual
- ❓ **Loteria (Lucky Numbers)** – fora do escopo atual

### Tipos de palpite:
| Tipo | Suporte |
|:---|:---|
| Resultado (1x2) | ✅ Sim |
| Placar exato | ✅ Sim |
| Apostas especiais (props) | ✅ Sim |
| Palpites ao vivo | 🔧 Pode ser desenhado (depende de dados live) |

### Rankings:
- Global (geral)
- Por região/estado
- Ligas públicas (patrocinadores)
- Ligas privadas (amigos/família/colegas)
- Por período (fase de grupos / mata-mata)

### Engajamento:
- Boosters (ex: X2 para dobrar pontos de uma partida)
- Troféus / conquistas
- Estrutura de prêmios configurável

### Tempo real:
- Atualizações de stats em tempo real durante jogos
- Leaderboards atualizados pós-jogo (~15 min de processamento)
- Monitoramento de KPIs near real-time via BI

> ⚠️ **Nota importante:** A Copa 2026 terá **104 jogos**. Fan Arena alerta que adicionar props/perguntas extras pode desmotivar participação.

---

## 7. Customização UX / Front-end

- **Nível:** 100% custom game design, não apenas skin/branding
- **CSS/temas:** Incluído no escopo de design custom
- **Domínio:** Suporta subdomínio (ex: `predictor.cazetv.com.br`) com espelhamento de header/footer para experiência seamless
- **Design:** Fan Arena inclui design e setup no fluxo padrão de implementação + consultoria de marketing
- **Desenvolvimento front-end:** Sim, Fan Arena constrói e embede o jogo
- **Recursos do cliente:** Opcionais – normalmente necessários apenas brand guidelines e assets

---

## 8. Integração / Login

- **SSO:** OpenID Connect e OAuth 2.0 (fornecido pelo cliente)
- **Modelo freemium/premium:** SSO atribui role de usuário (free ou premium) — features e ligas controladas por role
- **Pagamentos:** Fora do escopo (pagamento ocorre fora da plataforma); Fan Arena pode integrar Stripe/Mollie se necessário (fornecido pelo cliente)
- **Feeds de dados esportivos:** 100% gerenciado pela Fan Arena; suportam Stats Perform (Opta), Genius Sports, Gracenote, Sportmonks, InStat e outros
- **Integrações externas (a serem fornecidas pelo cliente se aplicável):**
  - Programa de fidelidade
  - Base de assinaturas (via SSO claims + endpoint de verificação)
- **Controle de acesso premium:** Gate por role de usuário autenticado; features, ligas e prêmios configurados no jogo

---

## 9. Comunicações

- **Email marketing:** ❌ **Não incluído** – responsabilidade do CRM/plataforma de automação de marketing do cliente. Fan Arena integra conforme necessidade
- **Push notifications (web):** Pode ser integrado como parte da plataforma de automação de marketing
- **Mensagens in-game:** Pode ser integrado como parte da plataforma de automação de marketing
- **Templates:** Cliente define tom de voz e aprovações; Fan Arena implementa + suporte de localização
- **Agendamento de campanhas:** Calendário conjunto; Fan Arena configura triggers (deadlines, alertas de início de jogo)

> ⚠️ **Observação:** Fan Arena NÃO fornece plataforma de comunicação/CRM. Todo o envio de emails, push e mensagens precisa vir de ferramenta do cliente (ex: Braze, CleverTap, etc.)

---

## 10. Compartilhamento com Redes

- **Funcionalidades propostas:**
  - Links "convide para liga privada"
  - Compartilhar via WhatsApp / Instagram / X (Twitter) / Facebook

---

## 11. Restrição Geolocalização

- **Posição da Fan Arena:** Fora do escopo – parte do SSO
- **Recomendação:** Não limitar uso do jogo (expats brasileiros, etc.)
- **Alternativas sugeridas:**
  - Modo "view-only" fora do Brasil (restringindo criação de conta)
  - Rate limiting por IP para segurança balanceada
- **Nota:** Time Fan Arena precisa ser whitelisted ou compartilhar conta para acesso ao ambiente de produção

---

## 12. Tempo de implementação

- **Timeline estimada:** **8 a 12 semanas** (pesquisa → specs → design/setup → marketing → go-live/support)
- **Inclui:**
  - Localização em português
  - Treinamento de suporte L1
  - Integrações (SSO/loyalty)
  - Load testing em escala de Copa do Mundo
  - Planejamento e ensaio de war-room
- **Time dedicado:** Fan Arena reserva equipe dedicada para suporte e treinamento L1

---

## 13. Modelo de precificação + o que está incluso

### Opção A – Setup + taxa de operações (sem custo de infra incluso)
| Item | Valor |
|:---|:---|
| **Setup único** (design + requisitos especiais + setup) | **€59.000** |
| **AWS** – compartilhado transparentemente com cliente (100% + 20% fee de gestão Fan Arena) | Veja tabela abaixo |

**Custos AWS estimados (por mês):**

| Componente | Custo mensal |
|:---|:---|
| Software License (Fan Arena) | €20.000 |
| Client Application (CDN) | €20.000 |
| API (Kubernetes & Networking) | €15.000 |
| Game Database | €20.000 |
| Leaderboard Dataset | €40.000 |
| Orchestration | €17.500 |
| Logging | €2.500 |
| **Total mensal estimado** | **~€135.000** |

> **Custo total estimado Opção A (3 meses):** ~€59K setup + ~€405K infra (3 meses) + 20% fee = **~€545K total**

### Opção B – Licença Fan Arena (infra inclusa, risco mitigado)
| Item | Valor |
|:---|:---|
| **Preço por usuário** | €0,020/usuário |
| **15 milhões de usuários** | **€300.000** |

> **Custo total estimado Opção B:** **~€359K** (€300K licença + €59K setup)

### ✅ Incluído em ambas as opções:
- Design personalizado, web app responsivo conforme especificações
- Implementação de SSO com restrições freemium/premium
- Feed de dados esportivos
- Atualizações da plataforma
- Suporte técnico & SLAs
- Consultoria de marketing
- BI/Reporting

### Contrato:
- **Duração mínima proposta:** 3 meses (build + torneio + janela de retenção pós-torneio)
- **Portabilidade de dados garantida:** via exports BI + dumps agendados

---

## 14. O que está fora do escopo

| Item | Responsável |
|:---|:---|
| **Cumprimento de prêmios (prizing fulfillment)** | Cliente |
| **Quizzes / Trivia diária** | A ser discutido – fora do MVP |
| **Loteria / Lucky Numbers** | A ser discutido – se incluído, precisa ser provisionado como jogo separado |
| **Desafios diários** | A ser discutido – fora do MVP |
| **Plataforma de CRM / Email / Push** | Cliente (Fan Arena integra) |
| **Pagamentos / Subscription** | Cliente (transação fora da plataforma) |
| **Verificação de idade / LGPD compliance** | Cliente (via SSO) |
| **Geo-restrição** | Cliente (via SSO) |
| **Certificações de segurança (ISO, SOC)** | Não possuem |

---

## Próximos passos (propostos pela Fan Arena)

1. Confirmar opção de precificação (A ou B)
2. Escolher formato do jogo: só Predictor ou Predictor + Quizzes
3. Definir modelo de pontuação + prêmios + inventário de patrocinadores + brand guidelines
4. Workshop de integração (SSO, assinaturas, loyalty, analytics)
5. Travar plano de entrega + rodar load tests + agendar planejamento de war-room
