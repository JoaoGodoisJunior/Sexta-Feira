---
tipo: caso
area: Tributário
temas: [NF-e, cesta básica, IBS/CBS, PIS/COFINS alíquota zero, cadastro tributário]
data: 2026-10
regime: Real (indício: PIS/COFINS não cumulativo)
setor: distribuição de carnes (RS)
resultado: em andamento
---
# Cadastro tributário de carnes na NF-e

## Situação
Distribuidor de carnes do RS emitiu NF-e de venda para restaurante com dois itens de carne bovina.

## Pergunta ou problema
A nota estava correta quanto ao IBS/CBS e ao PIS/COFINS?

## Análise (fundamento)
- Item de coxão mole (NCM 0201.30.00) tributado no IBS/CBS (CST 000), mas está no Anexo I da LC 214, item 19: alíquota zero (art. 125). Ver [[lcp-214-2025-01-16]].
- Item de carne moída (NCM 0210.20.00) com PIS/COFINS tributado (CST 01), mas tem alíquota zero pela [[lei-10925-2004-07-23]], art. 1º, XIX, "a".
- NCM do item 2 suspeito (carne moída congelada costuma ser 0202.30.00).
- Validador: `05 Godois/validador-nfe-rtc` acusa os dois erros automaticamente desde 30/10/2026.

## Solução adotada
Apontados os dois erros de cadastro e a possibilidade de recuperar PIS/COFINS pago a maior via PER/DCOMP, se o emitente for cliente.

## Resultado
(pendente)

## O que aprendemos
Cada produto acertou um tributo e errou o outro: o cadastro tributário precisa ser revisado **por tributo**, não só por produto. Vale oferecer revisão de cadastro a clientes de alimentos.
