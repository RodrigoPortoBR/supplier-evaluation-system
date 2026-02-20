# Genius Sports – Proposta Consolidada
**Projeto:** World Cup Predictor 2026
**Documentos base:** Meeting Notes + Transcrição (12/02/2026) + **Proposta Formal (20/02/2026)**
**Contato:** Christian Abbonizio (Genius Sports)
**Preço:** 💰 **$150.000 – $225.000 USD (Licença Anual)**

---

## 1. Infraestrutura técnica e robustez

- **Cloud:** Infraestrutura proprietária e escalável. Proposta: "stress-tested infrastructure and dedicated hosting environments."
- **Capacidades declaradas:**
  - **Experiência comprovada:** Operam o **FIFA PlayZone**, lidando com milhões de usuários simultâneos.
  - **Escala:** Testes de carga de **10 milhões de usuários simultâneos**. Meta de **até 15 milhões de cadastros**.
  - **Arquitetura:** Solução enterprise customizada com "tournament-scale architecture."
- **Load test:** Suportam stress tests para picos massivos. Relatório específico não fornecido.

> ✅ **Ponto forte:** Único fornecedor com experiência comprovada em operar copa do mundo para a própria FIFA nessa escala.

---

## 2. Suporte Local

- **Suporte em português:** ✅ Sim. Confirmado atendimento em português.
- **Equipe:** Genius pode assumir o suporte N1 completo ou criar uma ponte com o time do parceiro.
- **Disponibilidade:** **24/7** durante períodos de pico.
- **Escalonamento:** Caminhos claros de escalonamento de bugs e triagem N2/N3.

---

## 3. SLA em caso de incidentes

- **SLA:** Padrões de indústria para uptime (detalhes específicos a confirmar na proposta formal).
- **Incidentes:** Caminhos de escalonamento definidos para triagem de bugs.
- **War-room:** Não detalhado explicitamente na call, mas implícito pela operação FIFA.

---

## 4. Segurança da informação

- `[Não informado]` – LGPD, GDPR e Compliance não foram discutidos detalhadamente na reunião inicial.
- **Observação:** Como fornecedor oficial da FIFA e empresa de capital aberto (NYSE), espera-se conformidade rigorosa, mas precisa ser validada.

---

## 5. Dados

- **Propriedade:** **Co-Controladoria (Co-Controller)**.
  - Dados vivem nos bancos da Genius.
  - Cliente e Genius compartilham propriedade e privilégios de acesso irrestritos.
- **Acesso:** Cliente tem acesso total e irrestrito aos dados de usuários.
- **Portabilidade:** Garantia de exportação completa dos dados ao final do contrato.
- **Analytics:** Genius coleta e compartilha todos os analytics com o parceiro.

> ⚠️ **Ponto de atenção:** Modelo de co-controladoria significa que o cliente não é o único dono dos dados. Necessário revisão jurídica.

---

## 6. Features previstas

### ✅ Disponível (Built-in / Já desenvolvido):
- **Predictor:** 1x2, Placar Exato, previsões de torneio (campeão, artilheiro, classificação do Brasil).
- **Bracket Challenges** (Mata-mata).
- **Gamificação:** Missões diárias, Trivia/Quiz com "Lucky Numbers", missões semanais exclusivas para premium.
- **Ligas:** Públicas, Privadas (5 grátis / 100 premium) e Premium.
- **Sorteios:** "Lucky Numbers" (acumulação de números da sorte para sorteios semanais patrocinados).
- **Ativação de Patrocinadores:** Espaços dedicados e integrados ao jogo.
- **Compartilhamento Social:** Compartilhar nas redes dobra os lucky numbers ganhos.

### 🔧 Customização:
- Modelo **100% Custom Build** (não é white-label de prateleira).
- Proposta: "enterprise-scale engagement ecosystem" – não um produto template.
- Missões premium vinculadas a momentos de transmissão, influenciadores ou patrocinadores.

### ❓ A definir:
- Regras específicas de pontuação (customizáveis).
- Previsões ao vivo (Live Predictions) – não mencionado.

---

## 7. Customização UX / Front-end

- **Nível:** **100% Custom**. Genius entrega a experiência completa "end-to-end".
- **Design:** Genius fornece designers e UX. Cliente fornece apenas guia de marca.
- **Front-end:** Desenvolvimento nativo (React Native disponível, mas recomendam **Web View** mobile para menor fricção).
- **Domínio:** Customizável (ex: subdomínio do cliente).

---

## 8. Integração / Login

- **SSO (Single Sign-On):** Suporte robusto a múltiplos provedores de identidade (ex: Google, Facebook, Login do Parceiro).
- **Múltiplos Patrocinadores:** Capacidade de integrar logins de diferentes patrocinadores para verificar status de assinatura.
- **Gate de Conteúdo:** Usuários com assinatura ativa (verificada via SSO do patrocinador) entram direto como Premium.

---

## 9. Comunicações

- **Canais:** Proposta confirma: "CRM systems, analytics tracking, notification infrastructure."
- **Automação:** Integração com stack do cliente (CRM, e-mail marketing, analytics). Não possui engine nativa de push.
- **Engajamento diário:** Mecânica de trivia diário + lucky numbers reduz dependência de push notifications.

---

## 10. Compartilhamento com Redes

- **Funcionalidades:** Mecânicas virais integradas.
- **Exemplo:** Compartilhar resultado do Trivia nas redes sociais dobra os "Lucky Numbers" ganhos.

---

## 11. Restrição Geolocalização

- `[Não informado]`

---

## 12. Tempo de implementação

- **Prazo:** **Crítico**. Target de Go-Live para **meados de Maio**.
- **Proposta:** "If we confirm scope quickly and align on design decisions, we can achieve a mid-May go-live."
- **Risco:** Se houver atraso na aprovação, o escopo pode ser reduzido.
- **Necessidade:** Assinatura de contrato **o mais rápido possível** para entregar o conjunto completo de features.

---

## 13. Modelo de precificação + o que está incluso

- **Modelo:** **Licença Anual Fixa**.
- **Custo:** 💰 **$150.000 – $225.000 USD por ano.**
- **O que inclui:** Design, desenvolvimento, operação, suporte 24/7 em português, hosting, dados esportivos.
- **Escopo Flexível:** Range de $75k provavelmente reflete diferentes níveis de escopo.
- **Vantagem:** Custo fixo = previsibilidade. Sem surpresas por picos de tráfego ou uso de API.
- **Custo por registro:** Se atingir 15M cadastros = ~$0.01-$0.015/usuário.

---

## 14. O que está fora do escopo

- **Cumprimento de Prêmios (Fulfillment):** Genius gerencia os ganhadores, mas a entrega física/logística dos prêmios é responsabilidade do cliente.

---

## ⚠️ Avaliação geral da proposta

A Genius Sports é a opção **"Grife" / Best-in-Class**.
**Preço:** $150.000 – $225.000 USD (licença anual).
**Nota média:** 4.2/5 (blocos avaliados).

### Pontos Fortes:
- 🏆 **Pedigree:** Operam o produto oficial da FIFA. Risco técnico de escala é mínimo.
- 🛠️ **Produto:** Conjunto de features mais completo (Quiz, Lucky Numbers, Predictor, Bracket, Missions integrados).
- 🤝 **Serviço:** Modelo "concierge" (fazem design, dev, operação). Menor esforço para o time interno.
- 📊 **Dados:** São donos da fonte de dados esportivos (zero dependência de terceiros).
- 💵 **Previsibilidade:** Licença anual fixa – sem custos surpresa por tráfego.

### Riscos:
- 💰 **Custo:** O mais alto ($150k-$225k USD). Porém inclui TUDO.
- ⏳ **Prazo:** Cronograma apertado para um build customizado (meados de maio).
- 🔒 **Dados:** Modelo de co-controladoria precisa de revisão jurídica.
- 🔐 **LGPD:** ⚠️ **NÃO CONFIRMADO** – Compliance, residência de dados e verificação de idade não foram abordados.

### Próximos Passos:
1. ~~Revisar proposta~~ ✅ Feito – Preço confirmado.
2. **Confirmar LGPD/GDPR** – Compliance, ISO, SOC, pen test, verificação de idade.
3. **Contrato de dados** – Definir limites claros de co-controladoria.
4. **Load test** – Evidência concreta de stress tests.
5. **Cronograma detalhado** – Design → Build → UAT → Go-Live.
6. **Decisão de budget** – Apresentar $150k-$225k para liderança.

> **Veredito:** Se houver budget e LGPD for confirmado, é a escolha mais segura tecnicamente e com melhor produto final. Se o budget for restrito, Fan Arena permanece a alternativa funcional.
