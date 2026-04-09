# Análise do Protótipo Lovable: Bolão CazéTV

**Data:** 08 de Abril de 2026
**Objetivo:** Cruzar o protótipo UX/UI navegável (Lovable) com as documentações técnicas de fornecedores (LiveLike) e o backlog de requisitos do projeto (Project Master Map).

---

## 1. Visão Geral
O protótipo do Bolão CazéTV atende primorosamente ao direcionamento do projeto. Ele tangibiliza, com excelente gamificação, as integrações técnicas que foram mapeadas e negociadas com o fornecedor da infraestrutura (LiveLike). O mockup servirá perfeitamente como referência de "Brand Assets / UI Guidelines" exigida formalmente pela equipe de Professional Services da LiveLike, conforme alertado no `project_master_map.md`.

## 2. Pontos de Forte Alinhamento (O Que Está Correto)
Requisitos documentados que já foram contemplados e resolvidos de forma exemplar no design:

* **Integração de SSO e Patrocinador (iFood):** A diferenciação entre o público geral ("Liga CazéTV" - 1.9M) e assinantes premium ("Clube iFood" - 5.7M) demonstra muito bem a mecânica técnica de segregação de ligas por `Partner Status` baseada no token do Single Sign-On, exigida na documentação da LiveLike.
* **Mecânicas de Predição Suportadas:**
  * **Placar Exato:** (Ex: palpites na fase de grupos).
  * **Special Predictions (Outrights):** O fluxo de prever o Campeão, Top Scorer (Artilheiro, ex: Vini Jr.) e Progresso do Brasil na competição utiliza as categorias nativas mapeadas na infraestrutura da plataforma LiveLike.
* **Recursos Avançados ("AI Guess"):** A funcionalidade nomeada "IA Palpiteira" mapeia perfeitamente a demanda técnica apresentada e validada no Q&A chamada de "AI Guess/Oráculo".
* **Missões (Missions & Challenges):** O menu "Missões" contemplando o "Desafio do Cazé" está perfeitamente alinhado com as capacidades de engajamento do módulo extra do Gaming Hub da LiveLike.
* **LGPD e Compliance de Idade:** O Onboarding contém de imediato uma confirmação de Termos e Condições, auxiliando no compliance legal (fator fundamental visto que PII e segurança legal recaem sobre a CazéTV, já que a LiveLike só armazena hashing).
* **Ligas (Públicas e Privadas):** As telas de "Rankings" cobrem corretamente o escopo global (CazéTV/iFood) e as ligas restritas "Entre Amigos" (Private Leagues via código/link).

## 3. Gaps e Sugestões de Melhoria (O Que Falta no UX)
Considerando os relatórios de operação (ex: "Project Master Map" e "LiveLike Evaluation"), sugerimos pequenos ajustes e adições ao protótipo para cobrir pontos operacionais críticos não visualizados:

1. **Central de Ajuda / Tickets (L1 Support):** 
   * **Por quê:** A LiveLike não oferece suporte B2C. A documentação exige que a CazéTV opere 100% os chamados operacionais ("meus pontos não atualizaram", "esqueci minha senha"). 
   * **Recomendação:** É vital ter uma área gráfica óbvia de "Ajuda" (FAQ) com um formulário de contato no menu "Perfil". Se isso não for claro, os usuários inundarão as redes sociais (operadas pelo Respond.io) via DM, e não os canais de suporte técnico corretos.

2. **Opt-In de Push / Permissão de CRM:** 
   * **Por quê:** A LiveLike oferece "Webhooks", mas o envio de e-mails/Push recai num fornecedor CRM da própria CazéTV. Sem notificação para lembrar as pessoas de voltarem pra jogar diariamente, a taxa de retorno (retenção) vai afundar. 
   * **Recomendação:** O fluxo de Onboarding precisa ter uma tela (ou banner hero na Home) focada em "Ativar Notificações", destacando que a IA ou o próprio Cazé vão "te avisar antes do jogo começar". É a métrica mais importante após a conversão inicial (registro).

3. **Viralização Orgânica Evidente (Deep Links WhatsApp):** 
   * **Por quê:** As lógicas são confirmadas tecnicamente pela LL. 
   * **Recomendação:** Fazer o botão "Compartilhar via WhatsApp" transbordar em destaque após a confirmação de um placar "ousado", ou na tela de convidar na Liga de Amigos, para impulsionar aquisição sem custo B2C extra.

4. **Desconexão com o Teste ao Vivo de Domingo:** 
   * **Atenção:** As documentações (`livelike_sunday_test_brief.md`) afirmam que o pico de teste na transmissão exigirá uma entrada *anônima ("no account, no login, no friction")*. O protótipo focado na Copa exige naturalmente o Auth via iFood. 
   * **Recomendação:** Fique atento para garantir que o front-end entregue o widget de domingo completamente expurgado desse fluxo complexo de Onboarding retratado aqui. Ele deve ser estritamente "Lander and Predict".
