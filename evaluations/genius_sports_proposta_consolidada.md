# Genius Sports – Proposta Consolidada
**Projeto:** World Cup Predictor 2026
**Documento base:** Meeting Notes + Transcrição (12/02/2026)
**Contato:** Christian Abbonizio (Genius Sports)

---

## 1. Infraestrutura técnica e robustez

- **Cloud:** Não especificado detalhadamente, mas operam infraestrutura proprietária e escalável.
- **Capacidades declaradas:**
  - **Experiência comprovada:** Operam o **FIFA PlayZone**, lidando com milhões de usuários simultâneos.
  - **Escala:** Confirmaram capacidade para testes de carga de **10 milhões de usuários simultâneos** (5 min antes do jogo).
  - **Arquitetura:** Solução enterprise customizada.
- **Load test:** Suportam stress tests para picos massivos.

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
- **Predictor:** 1x2, Placar Exato.
- **Bracket Challenges** (Mata-mata).
- **Gamificação:** Missões diárias, Trivia/Quiz (always-on).
- **Ligas:** Públicas, Privadas e Premium.
- **Sorteios:** "Lucky Numbers" (acumulação de números da sorte para sorteios semanais).
- **Ativação de Patrocinadores:** Espaços dedicados e integrados ao jogo.

### 🔧 Customização:
- Modelo **100% Custom Build** (não é white-label de prateleira).
- Reutilizam códigos e módulos de produtos existentes (FIFA PlayZone) para criar um produto novo sob medida.

### ❓ A definir:
- Regras específicas de pontuação (customizáveis).

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

- **Canais:** Integração com sistemas de CRM e e-mail marketing do cliente.
- **Automação:** Genius não detalhou ferramentas próprias de disparo, focando na integração com as do cliente.

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
- **Risco:** Christian (Genius) alertou que o cronograma é a maior preocupação.
- **Necessidade:** Assinatura de contrato em **~2 semanas** (fevereiro) é mandatória para viabilizar.

---

## 13. Modelo de precificação + o que está incluso

- **Modelo:** **Premium / Enterprise**.
- **Custo:** Explicitamente posicionado como "não somos a opção barata". Solução para grandes orçamentos.
- **Valores:** Proposta financeira pendente (esperada para antes de 20/02).
- **Escopo Flexível:** Se o orçamento estourar, sugerem remover features para adequar.

---

## 14. O que está fora do escopo

- **Cumprimento de Prêmios (Fulfillment):** Genius gerencia os ganhadores, mas a entrega física/logística dos prêmios é responsabilidade do cliente.

---

## ⚠️ Avaliação geral da proposta

A Genius Sports é a opção **"Grife" / Best-in-Class**.

### Pontos Fortes:
- 🏆 **Pedigree:** Operam o produto oficial da FIFA. Risco técnico de escala é mínimo.
- 🛠️ **Produto:** Conjunto de features mais completo (Quiz, Lucky Numbers e Predictor integrados).
- 🤝 **Serviço:** Modelo "concierge" (fazem design, dev, operação). Menor esforço para o time interno.
- 📊 **Dados:** São donos da fonte de dados esportivos (zero dependência de terceiros).

### Riscos:
- 💰 **Custo:** Provavelmente o mais alto (CAPEX elevado).
- ⏳ **Prazo:** Cronograma apertado para um build customizado.
- 🔒 **Dados:** Modelo de co-controladoria precisa de análise.

> **Veredito:** Se houver budget, é a escolha mais segura tecnicamente e com melhor produto final. Se o budget for restrito, Fan Arena é a alternativa funcional.
