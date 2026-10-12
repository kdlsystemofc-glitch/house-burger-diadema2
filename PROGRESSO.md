# PROGRESSO

Etapa atual: FASE 2 (aguardando aprovação visual da Fase 1)

## Etapas concluídas
- FASE 0 (2026-10-12): Análise e DESIGN.md.
  - Decisão do humano: `CLIENTE.MD` vale como bruto e real (`CLIENTE-bruto.md` não existe).
- FASE 1 (2026-10-12): Site construído, estático, sem animação. Commits:
  - c69ceb2 design pronto
  - 14e5e5e fundação (tokens, base, assets, scripts)
  - 0de74e7 hero pronta
  - 8c9814c manifesto pronta
  - 1609f07 cardapio pronta
  - 1070467 ambiente pronta
  - d60451f visite e rodape pronta
  - 39c586d ajustes finais + screenshots 1440/768/390
  - Push: NÃO feito (GH_TOKEN ausente).

## Seções (CHECK-SEÇÃO mecânico: todas passaram em 1440 e 390)
| Seção | Check | Problema aberto |
|---|---|---|
| S1 Hero (#inicio) | OK | foto desktop F03 tem 1280 px (A2 não recebido); horário completo pendente |
| S2 Manifesto (#casa) | OK | título sem slogan (PENDÊNCIA) |
| S3 Cardápio (#cardapio) | OK | burger sem recorte (fallback do A1 com máscara); preços; grafia "Harmburguer"; direito de uso das fotos |
| S4 Ambiente (#ambiente) | OK | autorização da nota e das avaliações |
| S5 Visite + rodapé (#visite) | OK | foto da fachada mostra pessoa e o letreiro "Club Burger"; logo 150 px |

## Pendências abertas
- Aprovação visual da Fase 1 pelo humano.
- Respostas às 5 perguntas do DESIGN.md §8 (adotei os padrões, revisáveis).
- A1 / A2 / A3 não recebidos (fallbacks ativos, registrados em assets.md).
- GH_TOKEN não definido (sem push).
- 18 itens do cliente em PENDENCIAS-CLIENTE.md.

## Próxima etapa
FASE 2: Responsivo.
