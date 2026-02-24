# Genius Sports – Proposta Consolidada
**Projeto:** World Cup Predictor 2026
**Documentos base:** Meeting Notes + Transcrição (12/02/2026) + **Proposta Formal (20/02/2026)** + **Follow-Up Meeting (23/02/2026)**
**Contato:** Christian Abbonizio (Genius Sports)
**Preço:** 💰 **$150.000 – $225.000 USD (Licença Anual – Tudo Incluso)**

---

## 1. Infraestrutura técnica e robustez

- **Cloud:** Infraestrutura proprietária e escalável. Proposta: "stress-tested infrastructure and dedicated hosting environments."
- **Capacidades declaradas:**
  - **Experiência comprovada:** Operam o **FIFA PlayZone** e ativações do **IOC (Olimpíadas)**, lidando com milhões de usuários simultâneos.
  - **Escala:** Testes de carga de **10 milhões de usuários simultâneos**. Meta de **até 15 milhões de cadastros**.
  - **Arquitetura:** Solução enterprise customizada com "tournament-scale architecture."
  - **Custos de hosting:** ✅ Absorvidos pela licença anual – Genius assume o risco de escalonamento independente do número de usuários.
- **Load test:** Suportam stress tests para picos massivos. Relatório específico não fornecido.
- **Plataforma:** Solução **Web View** responsiva (mobile + desktop). App nativo **não é opção** para este timeline.

> ✅ **Ponto forte:** Único fornecedor com experiência comprovada em operar Copa do Mundo (FIFA) e Olimpíadas (IOC) nessa escala. Hosting incluso na licença.

---

## 2. Suporte Local e ao Usuário

- **Suporte em português:** ✅ Sim. Confirmado atendimento em português.
- **Modelo:** ✅ **Serviço 100% gerenciado pela Genius.** Genius opera seu próprio **ZenDesk** e canais de suporte para receber TODAS as mensagens dos usuários.
- **Equipe do cliente:** ❌ **NÃO é necessário** montar equipe de suporte interna. O envolvimento do cliente é **totalmente opcional** – apenas se quiser controle criativo sobre como interagir com usuários.
- **Escalonamento:** Genius resolve os problemas e apenas informa o cliente quando necessário ("hey, só para vocês saberem, isso está acontecendo e estamos resolvendo").
- **Disponibilidade:** **24/7** durante períodos de pico.

> ✅ **Ponto forte:** Suporte totalmente gerenciado. Cliente não precisa contratar time de suporte. Genius opera ZenDesk próprio com escalamento informativo.

---

## 3. SLA em caso de incidentes

- **SLA:** Padrões de indústria para uptime (detalhes específicos a confirmar no contrato).
- **Incidentes:** Caminhos de escalonamento definidos para triagem de bugs via ZenDesk.
- **War-room:** Não detalhado explicitamente, mas implícito pela operação FIFA e IOC.

---

## 4. Segurança da informação

- `[⚠️ Não informado]` – LGPD, GDPR e Compliance **NÃO foram discutidos em nenhuma das duas reuniões**.
- **Observação:** Como fornecedor oficial da FIFA/IOC e empresa de capital aberto (NYSE), espera-se conformidade rigorosa, mas **precisa ser validada obrigatoriamente**.

> ⚠️ **RISCO CRÍTICO:** Compliance, residência de dados e verificação de idade permanecem em aberto. Bloqueante para contrato.

---

## 5. Dados e Analytics

### Propriedade dos Dados
- **Modelo:** **Co-Controladoria (Co-Controller)**.
  - Dados vivem nos bancos da Genius.
  - Cliente e Genius compartilham propriedade e privilégios de acesso irrestritos.
- **Acesso:** Cliente tem acesso total e irrestrito aos dados de usuários.
- **Portabilidade:** Garantia de exportação completa dos dados ao final do contrato.

### Coleta de Dados (Follow-Up)
- **Dados de cadastro:** E-mail, nome, sobrenome, telefone – configurável no fluxo de registro.
- **Dados comportamentais:** Analytics sobre comportamento e uso do produto, compartilhados com o cliente.
- **Lookalike Audiences:** ✅ Genius pode cruzar os dados coletados com sua base global de fãs de esportes para criar audiências semelhantes para campanhas de marketing direcionadas.

### Analytics e KPIs (Follow-Up)
- **Dashboard:** ✅ Cliente terá acesso a **dashboards analytics completos** para rastrear comportamentos específicos dos usuários.
- **Insights:** Genius fornece insights sobre como os usuários estão usando o produto e recomendações de melhoria.
- **Monetização:** Genius ajuda a monetizar os dados de usuários via marketing direcionado usando sua base de dados de fãs global.

### Propriedade do Código ⚠️
- **⚠️ CÓDIGO NÃO PERTENCE AO CLIENTE.** Genius retém propriedade de todo o código-fonte.
- Cliente é **dono do branding, look & feel e identidade visual** – pode reutilizar/reposicionar a marca.
- Modelo de **licença** = dependência contínua da Genius para operação da plataforma.
- Para continuar usando o produto após o contrato, é necessário **renovar a licença**.

> ⚠️ **Ponto de atenção:** (1) Co-controladoria – necessária revisão jurídica. (2) Lock-in de código – cliente depende da Genius para operar.

---

## 6. Features previstas

### ✅ Disponível (Built-in / Já desenvolvido):
- **Predictor:** 1x2, Placar Exato, previsões de torneio (campeão, artilheiro, classificação do Brasil).
- **Bracket Challenges** (Mata-mata).
- **Gamificação:** Missões diárias, Trivia/Quiz com "Lucky Numbers", missões semanais exclusivas para premium.
- **Ligas:** Públicas, Privadas (5 grátis / 100 premium) e Premium.
- **Ligas Patrocinadas:** ✅ Ligas de patrocinadores (ex: "Liga Coca-Cola") **já estão no escopo** sem custo extra. Segmentação de dados por patrocinador incluída.
- **Sorteios:** "Lucky Numbers" (acumulação de números da sorte para sorteios semanais patrocinados).
- **Ativação de Patrocinadores:** Espaços dedicados e integrados ao jogo.
- **Compartilhamento Social:** Compartilhar nas redes dobra os lucky numbers ganhos.

### 🔧 Abordagem de Desenvolvimento (Follow-Up):
- **Modelo:** Principalmente **configuração** – "encaixar peças existentes de desenvolvimento em uma nova estrutura sob medida."
- **Back-end:** Tecnologia existente da Genius sendo reutilizada.
- **Front-end:** Build customizado completo (design, UX, prototipagem, front-end).
- **Resumo:** "Tudo o que estamos pedindo já foi feito antes" – a grande maioria das features é comprovada.

### ❓ Único item verdadeiramente novo:
- **WhatsApp In-App Predictions** – nunca feito pela Genius antes. Em investigação.
- **WhatsApp via link:** ✅ Envio de link via WhatsApp para redirecionar ao predictor = "quase zero preocupações."

### ❌ Fora do Escopo:
- Previsões ao vivo (Live Predictions) – não mencionado.
- Regras específicas de pontuação (customizáveis, a definir).

---

## 7. Customização UX / Front-end

- **Nível:** **100% Custom**. Genius entrega a experiência completa "end-to-end."
- **Design:** Genius fornece designers e UX. Cliente fornece apenas guia de marca.
- **Front-end:** Build customizado completo. Web View recomendado (não app nativo).
- **Domínio:** Customizável (ex: subdomínio do cliente).
- **Demo:** ✅ Christian vai enviar **links de demonstração** de jogos ao vivo ou ambientes de teste para o cliente experimentar.

---

## 8. Integração / Login

- **SSO (Single Sign-On):** Suporte robusto a múltiplos provedores de identidade (ex: Google, Facebook, Login do Parceiro).
- **Múltiplos Patrocinadores:** Integração de logins de diferentes patrocinadores ✅ **JÁ ESTÁ NO ESCOPO** – não muda o custo nem o escopo do projeto.
- **Gate de Conteúdo:** Usuários com assinatura ativa (verificada via SSO do patrocinador) entram direto como Premium.
- **Dependência técnica:** O range de $75k no preço depende parcialmente da complexidade das integrações técnicas (ex: documentação de assinaturas da CazeTV).

---

## 9. Comunicações

### ✅ Incluído na Licença:
- **Emails do jogo:** Score updates, lembretes ("não esqueça de fazer seus palpites"), resultados.
- **Integrações:** CRM systems, analytics tracking, notification infrastructure.

### 💰 Custo Adicional:
- **Campanhas de marketing** para aquisição de usuários.
- **Assets criativos** para publicidade (banners, redes sociais, YouTube).
- Genius pode ajudar com eficiências de custo se contratado junto com o produto.

### 🔍 Em investigação:
- **WhatsApp:** Integração com API Business oficial do WhatsApp em estudo.

---

## 10. Compartilhamento com Redes

- **Funcionalidades:** Mecânicas virais integradas.
- **Exemplo:** Compartilhar resultado do Trivia nas redes sociais dobra os "Lucky Numbers" ganhos.

---

## 11. Restrição Geolocalização

- `[Não informado]` – Não discutido em nenhuma das reuniões.

---

## 12. Tempo de implementação (Follow-Up – Detalhado)

| Fase | Período | Detalhes |
| :--- | :--- | :--- |
| **Contrato/LOI** | Até ~9 de março 2026 | Carta de intenção ou contrato necessário em ≈2 semanas |
| **Design & Prototipagem** | Março 2026 | Algumas semanas de design + início do desenvolvimento back-end |
| **Desenvolvimento** | Março–Maio 2026 | Desenvolvimento completo com prototipagem front-end finalizada |
| **Go-Live Alvo** | **11–18 de Maio 2026** | Preferência do Rodrigo. Christian: final de maio (2 sem. antes da Copa) |
| **Sprints V2** | Maio–Junho 2026 | Features adicionais entregues em sprints após o lançamento |

- **Estratégia de lançamento:** Priorização de features – abrir registro e palpites iniciais primeiro, mesmo que o conjunto completo de features não esteja disponível. Releases incrementais até a Copa.
- **Risco:** Se o contrato atrasar, o escopo pode ser reduzido para manter a data de lançamento.

---

## 13. Modelo de precificação + o que está incluso (Follow-Up – Significativamente Detalhado)

### 💰 Preço: **$150.000 – $225.000 USD/ano** (Licença Anual – Tudo Incluso)

### ✅ O que está DENTRO da licença:
| Item | Status |
| :--- | :--- |
| Hosting & Infraestrutura (custos variáveis absorvidos) | ✅ Incluso |
| Design, UX & Prototipagem | ✅ Incluso |
| Build Front-End Customizado Completo | ✅ Incluso |
| Desenvolvimento Back-End (tecnologia existente) | ✅ Incluso |
| Emails do jogo (lembretes, resultados, score updates) | ✅ Incluso |
| Suporte ao Usuário (ZenDesk gerenciado pela Genius) | ✅ Incluso |
| Operações & Monitoramento 24/7 | ✅ Incluso |
| Feed de Dados Esportivos | ✅ Incluso |
| Ligas Patrocinadas + Segmentação de Dados | ✅ Incluso |

### 💰 O que NÃO está incluso (custos adicionais):
| Item | Status |
| :--- | :--- |
| Campanhas de marketing para aquisição de usuários | 💰 Extra |
| Assets criativos para publicidade (banners, social media) | 💰 Extra (com eficiência de custo se contratado junto) |
| Desenvolvimento de App Nativo (iOS/Android) | 💰 Extra (não recomendado para este timeline) |
| Taxas de Payment Gateway (se ligas pagas) | 💰 Pass-on cost |
| Cumprimento de Prêmios (logistics/entrega) | 💰 Responsabilidade do cliente |
| Adaptações para outros esportes/competições | 💰 Licença expandida / change request |

### Gap de $75k ($150k → $225k):
- Depende do **escopo total de features** e da **complexidade das integrações técnicas** (principalmente documentação de assinaturas da CazeTV).
- Uma vez que as integrações forem definidas, o range pode ser estreitado.

---

## 14. Payment Gateway (Follow-Up – Novo)

- **Parceiros:** Stripe (experiência direta), Plucky (ligas pagas – jurisdição no Brasil incerta).
- **Modelo:** Pagamentos coletados em nome do cliente. Possível modelo híbrido: licença + revenue share.
- **Custo:** Taxas do gateway são pass-on costs (custo repassado).
- **Brasil:** ⚠️ Em investigação. ~40% de imposto em pagamentos cross-border. Genius consultando equipe financeira. Christian: "ficaria chocado se não encontrássemos uma solução."

---

## 15. Licença Multi-Ano / Multi-Esporte (Follow-Up – Novo)

- **Reutilização:** ✅ Produto pode ser adaptado para outras competições:
  - **Copa do Mundo Feminina 2027**
  - **Liga doméstica brasileira** (calendário anual)
  - Outros esportes
- **Custo:** Licença multi-ano com eficiências de custo pelo compromisso de longo prazo.
- **Adaptações:** Novos feeds de partidas, estruturas de previsão e fixtures = trabalho adicional, coberto na licença expandida.
- **Major deviations:** Costed como change request ou licença adicional.
- **Pós-Copa:** Se o cliente não quiser continuar, a plataforma pode ficar online por um período em **"estado dormante"** para visualização de resultados.

---

## 16. Clientes no Brasil (Follow-Up – Novo)

- **Free-to-play predictor games:** ❌ Nenhum cliente atual no Brasil neste modelo.
- **Dados esportivos:** ✅ Genius tem parcerias com todos os grandes sportsbooks do Brasil (direitos oficiais de dados da NFL, entre outros).
- **Abrangência:** Empresa muito global, presente em praticamente todos os territórios.

---

## ⚠️ Avaliação geral da proposta

A Genius Sports é a opção **"Grife" / Best-in-Class**.
**Preço:** $150.000 – $225.000 USD (licença anual – tudo incluso).
**Nota média:** ⬆️ **4.5/5** (blocos avaliados) – subiu de 4.2 após follow-up.

### Pontos Fortes:
- 🏆 **Pedigree:** Operam FIFA PlayZone + IOC Olimpíadas. Jogos de predição em escala de milhões.
- 🛠️ **Produto:** Features é configuração de tech existente, não desenvolvimento do zero.
- 🤝 **Serviço Completo:** Design, dev, operação, suporte via ZenDesk. Zero esforço para time interno.
- 📊 **Dados & Analytics:** Dashboards completos, dados comportamentais, lookalike audiences via base global.
- 💵 **Previsibilidade:** Licença all-encompassing. Sem custos surpresa de hosting/tráfego.
- 🏟️ **Ligas Patrocinadas:** Já no escopo, sem custo extra. Segmentação de dados por sponsor inclusa.

### Riscos:
- 🔐 **LGPD:** ⚠️ **NÃO CONFIRMADO** em nenhuma das 2 reuniões. **BLOQUEANTE.**
- 🔒 **Lock-in de Código:** ⚠️ **NOVO.** Genius é dona de todo o código. Cliente NÃO pode operar independentemente. Dependência perpétua via licença.
- 💰 **Custo:** O mais alto ($150k-$225k USD), porém tudo incluso.
- 🇧🇷 **Pagamento Brasil:** ~40% imposto cross-border em investigação.
- ⏳ **Prazo:** Contrato/LOI até ~9 de março para lançamento em maio.
- 📱 **WhatsApp:** Predições in-app nunca feitas. Link via WhatsApp = viável.

### Próximos Passos:
1. ~~Revisar proposta~~ ✅ Feito
2. ~~Follow-up meeting~~ ✅ Feito (23/02/2026)
3. **LGPD/GDPR** – Confirmar compliance, ISO, SOC, pen test, verificação de idade
4. **Lock-in de Código** – Negociar termos de escrow / acesso ao código na saída
5. **Pagamento Brasil** – Aguardar resposta da equipe financeira da Genius
6. **Demo Links** – Christian vai enviar links de produtos ao vivo / teste
7. **Statement of Work** – Christian vai detalhar features in/out por faixa de preço
8. **Opção Multi-Ano** – Christian vai preparar proposta multi-esporte
9. **WhatsApp** – Aguardar viabilidade técnica
10. **Decisão interna** – Rodrigo atualiza Christian até final da semana
11. **Contrato/LOI** – Assinar até ~9 de março para lançamento em maio

> **Veredito:** Se houver budget, LGPD for confirmado, e o lock-in de código for aceitável, é a **escolha mais segura tecnicamente e com melhor produto final**. A licença all-encompassing elimina riscos de custos variáveis. Se o budget for restrito ou o lock-in de código for inaceitável, Fan Arena permanece a alternativa funcional.
