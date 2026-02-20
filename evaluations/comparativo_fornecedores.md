# Comparativo de Fornecedores: World Cup Predictor 2026

Comparação consolidada das propostas de **Rooster**, **Fan Arena**, **Genius Sports** e **Quality Digital**.

| Critério | **Rooster** 🇧🇷 | **Fan Arena** 🇧🇪 | **Genius Sports** 🇬🇧 | **Quality Digital** 🇧🇷 |
| :--- | :--- | :--- | :--- | :--- |
| **Investimento Total** | **R$ 1.154.000**<br>*(~€ 185k)* | **Opção A:** ~€ 545k<br>**Opção B:** ~€ 359k<br>*(R$ 2.2M - 3.4M)* | **$150k – $225k USD**<br>*(Licença Anual)* 💰 | **R$ 626.777**<br>*(Dev + Sustentação)*<br>⚠️ Real: **R$ 1.2M+** |
| **Modelo de Custo** | **Custo Fixo All-Inclusive** 🆕<br>*(Dev + Infra + Ops Copa)*<br>50/30/20 | Setup + Fee Mensal (A) ou<br>Licença Flat Fee (B) | **Licença Anual Fixa**<br>*(Inclui design, dev, ops, suporte)* | **Squad Dedicado**<br>*(Body Shop + Sustentação 45d)*<br>Infra/OPTA/Design = EXTRA |
| **Prazo / Go-Live** | **14-18 semanas** 🆕<br>Kick 2w + Dev 8-12w + Test 4w<br>Go-live antes da Copa | 8-12 Semanas | **Crítico (Maio)** ⚠️<br>Requer assinatura em fev. | **04/Maio** ⚠️<br>Kick-off 30-45d + 2 meses<br>**Prazo INVIÁVEL** |
| **Escala Comprovada** | Genérico ("Dezenas de Milhões")<br>⚠️ Sem evidência | Nunca operou nessa escala.<br>*(Maior case: ~300k)* | **Comprovada (FIFA)** 🏆<br>*(PlayZone: Milhões)* | ❌ **ZERO**<br>Software house de TI/e-commerce |
| **Infraestrutura** | Cloud Genérica 🆕<br>Auto-scaling horizontal<br>SLA 99.9% target | AWS São Paulo<br>Load Test 15M users | Infra Proprietária/Custom<br>Testado p/ 10M users | **AWS Fargate + Aurora**<br>Auto-scaling<br>⚠️ Nunca testada p/ Copa |
| **Equipe & Suporte** | **7 FTE (BR)** 🆕<br>War-room + Plantão<br>SLA: 15min/1h | Treinamento L1 Local<br>Suporte N2/N3 Remoto | Suporte 24/7 (PT-BR)<br>Modelo Concierge | **Squad BR (RJ/SP)**<br>Sustentação 45d<br>⚠️ Pós-Copa = cliente opera |
| **Produto / UX** | Plataforma Custom 🆕<br>Placar exato + Especiais<br>Ligas ilimitadas + Antifraude | White-label Flexível<br>Design Customizado | **100% Custom Build**<br>Experiência "FIFA-like" | **MVP Limitado**<br>~40% das features<br>❌ Gamificação = Fase 2 |
| **Dados** | **100% Cliente** 🆕<br>APIs + Export + Portabilidade | 100% Cliente<br>Export Garantido | **Co-Controladoria**<br>Acesso irrestrito | **100% CLIENTE** ✅<br>Código + Dados + Infra<br>ZERO lock-in |
| **Segurança** | Consent menores 🆕<br>⚠️ Sem LGPD detalhada<br>Sem certificações | GDPR via SSO<br>Sem ISO/SOC | Em conformidade c/ FIFA<br>*(A confirmar detalhes)* | **LGPD detalhada** ✅<br>Consentimentos, masking,<br>WAF, TLS, criptografia |
| **Integrações** | **SSO + Parceiros** 🆕<br>Benefícios confirmados | SSO, Dados Esportivos,<br>Loyalty (A confirmar) | **SSO Multi-Partner**<br>Dados Proprietários | **Condicionais** ⚠️<br>OPTA + Sponsor = extras<br>❌ CRM/Email fora do escopo |
| **Principal Risco** | **Sem cases/evidência** ⚠️<br>Claims ambiciosos<br>sem comprovação. | **Risco Operacional**<br>(Escala não testada). | **Custo & Cronograma**<br>(Atraso inviabiliza). | **Modelo Errado** ❌<br>Body shop p/ projeto que<br>precisa de plataforma. |
| **Veredito** | **Aposta Local** 🆕<br>Melhorou muito na v2.<br>Preço bom, falta evidência. | **Custo-Benefício**<br>Produto sólido, preço médio, risco de escala. | **Grife (Best-in-Class)**<br>Melhor tech/produto, se couber no budget. | **DISCARD** ❌<br>Empresa competente, tipo errado de fornecedor. |

---

## 🚦 Resumo Executivo

### 1. **Genius Sports** (A escolha "Segura" tecnicamente) – **$150k–$225k USD/ano**
Se o orçamento permitir e o contrato for assinado rápido, é a opção com **menor risco técnico** e **maior qualidade de produto**. Eles já fazem isso para a FIFA. ⚠️ LGPD ainda não confirmado.

### 2. **Fan Arena** (O meio-termo equilibrado)
Traz um produto de prateleira robusto adaptado para a Copa. O preço é competitivo (principalmente na Opção B). O risco é **nunca terem operado 15M de usuários**. Exige due diligence técnica rigorosa e testes de carga pesados.

### 3. **Rooster** (A aposta econômica – **melhorou na v2**) – **R$ 1.154.000 (custo fixo)**
Menor custo absoluto e equipe local dedicada. **v2 melhorou significativamente**: SLAs definidos (15min/1h), war-room, dados 100% do cliente com APIs, SSO, cronograma (14-18 semanas), custo fixo all-inclusive. Porém, **zero cases/evidência de escala**, provedor cloud não identificado, LGPD superficial, notificações/social sharing ausentes. Recomendado apenas após validação técnica profunda e obtenção de evidências de capacidade.

### 4. **Quality Digital** (❌ DISCARD – Modelo incompatível) – **R$ 626k visível / R$ 1.2M+ real**
Quality é uma **software house** sólida (37 anos, B3, BNDES), mas é o **tipo errado de fornecedor** para este projeto. Entrega um MVP muito limitado (~40% das features), sem gamificação, sem notificações, sem apps nativos. **Zero experiência em gaming/esportes massivos.** O cliente assume TODA a operação. Único destaque: melhor compliance LGPD e propriedade 100% dos dados/código.

> **Possível uso alternativo:** Quality poderia ser um **parceiro complementar** para construir integrações customizadas ou apps nativos, trabalhando junto ao fornecedor primário de plataforma.
