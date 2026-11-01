---
tipo: conhecimento
area: Tributário
temas: [ICMS-RS, substituição tributária, autopeças, Decreto 57.848/2024, antecipação sem encerramento, diferencial de alíquota, Simples Nacional, DeSTDA, Domínio]
fontes: [lcp-123-2006-12-14, lei-8820-1989-id19585, Decreto RS 57.848/2024 (não está na base), RICMS-RS Decreto 37.699/1997 (não está na base)]
status: válida
revisar_em: 2027-01-31
vigencia_conferida_em: 2026-11-01 (LC 123 compilada na base em 13/10/2026; Decreto 57.848 e RICMS-RS conferidos só em fontes secundárias e no portal da Receita Estadual, não no LEGIS-RS)
certeza: texto expresso (LC 123); entendimento predominante (regras do RS, por fonte secundária)
origem: pergunta do João em 01/11/2026 (configuração de cliente de autopeças do Simples na Domínio)
---

# ICMS-RS: autopeças fora da ST e antecipação nas compras interestaduais

## Em uma frase
Desde **01/11/2024** as autopeças saíram da substituição tributária no RS (Decreto 57.848/2024). Com isso, a compra interestadual para revenda de autopeças por empresa do Simples passou a sofrer **antecipação sem encerramento da tributação** (diferença entre alíquota interna e interestadual), e a revenda passou a ser tributada normalmente pelo ICMS dentro do DAS.

## Fundamento
- [[lcp-123-2006-12-14]] — **art. 13, § 1º, XIII, "g"**: o ICMS fora do DAS, nas aquisições de outros Estados sujeitas a antecipação, pode ser:
  - item 1: **com encerramento** da tributação (ST);
  - item 2: **sem encerramento**, cobrando só a **diferença entre a alíquota interna e a interestadual**, **sem agregar valor** (sem MVA). *Texto expresso, redação compilada na base em 13/10/2026.*
- **Art. 13, § 1º, XIII, "h"**: diferencial de alíquota nas aquisições interestaduais não sujeitas à antecipação.
- **Decreto RS 57.848/2024** (DOE 25/10/2024, efeitos a partir de 01/11/2024): revoga o item XX da Seção III do Apêndice II do RICMS-RS (autopeças), seguindo os Protocolos ICMS 32/24 e 33/24. *Não está na base; conferido no portal da Receita Estadual RS e em fonte secundária.*
- **RICMS-RS, Livro III, art. 37**, e **IN DRP 45/98**: antecipação para o destinatário gaúcho do Simples. *Não está na base; dispositivos citados pelo resumo de operações interestaduais da Receita Estadual RS (17/02/2022).*

## Como funciona na prática
**Compra interestadual de autopeças para revenda (Simples Nacional, RS)**
- Recolhe antecipação **sem encerramento**: Guia de Arrecadação **código 379**.
- Prazo: **dia 23 do 2º mês subsequente**, segundo a Receita Estadual (2022). Circular de 2009 indicava dia 15. **Conferir o prazo vigente.**
- DeSTDA (SEDIF): aba **ICMS Entrada**, campo **"Antecipação SEM encerramento"**.

**Revenda**
- A saída volta a ser tributada pelo ICMS **dentro do DAS**. O acumulador de venda **não** pode continuar marcado como ICMS-ST no Simples.

**Exceções (continuam na ST)**
- Item com o mesmo NCM, mas outro **CEST**, ou que esteja em outro segmento, convênio ou protocolo (ex.: lubrificantes, no segmento de combustíveis e lubrificantes). Nesse caso: ICMS-ST, Guia **código 270**, campo "Antecipação COM encerramento".

**Estoque em 31/10/2024 recebido com ICMS retido**
- Inventariar, relacionar as notas de aquisição e apurar o imposto a restituir (RICMS-RS, Livro III, art. 23, §§ 2º e 3º).
- **Simples Nacional:** pedido de restituição (Livro III, art. 22).
- **Regime geral:** crédito em 12 parcelas mensais.

**Configuração na Domínio** (procedimento genérico do imposto 27; a solução publicada é a do MA)
1. **Controle > Parâmetros** — nova vigência; em Geral > Impostos incluir **1 – ICMS** e **27 – ICMSA**.
2. **Arquivos > Impostos > 27 – ICMSA** — Tipo "Lançado por nota"; tabela de alíquota interestadual; em Recolhimentos, código **379**, periodicidade mensal.
3. **Acumulador de compra interestadual para revenda** — incluir 1 e 27; regra na Configuração de Importação para o CFOP 2102.
4. Conferir em **Relatórios > Impostos > Demonstrativos > 27 – ICMS Antecipado** e bater com a DeSTDA.

## Exemplo numérico
Compra de SP (alíquota interestadual 7%) de autopeças por R$ 10.000,00. Alíquota interna RS de 17%, **a conferir** para o produto.
- Antecipação = 10.000 × (17% − 7%) = **R$ 1.000,00**, pela Guia 379, sem MVA.
- Na revenda, o ICMS entra no DAS pela alíquota efetiva do Anexo I.

## Pontos de atenção
- Cliente que ainda trata autopeças como ST nas saídas está **recolhendo ICMS a menor no DAS** desde 11/2024.
- A antecipação sem encerramento **não** encerra a tributação: o ICMS da revenda continua devido no DAS.
- Conferir NCM e CEST de itens limítrofes (lubrificantes, pneus, baterias) antes de tirar da ST.
- Restituição do estoque de 31/10/2024: verificar se foi pedida e qual o prazo.
- **Reforma tributária**: o ICMS começa a reduzir em 2029 e é extinto em 2033. Revisar esta nota quando houver regulamentação estadual da transição.

## Pendências (conferir)
- Incluir na base o **Decreto 57.848/2024** e o **RICMS-RS** (Livro III, arts. 22, 23 e 37; Apêndice II).
- Confirmar o prazo vigente da Guia 379 (dia 23 × dia 15).
- Confirmar a alíquota interna aplicável a cada NCM de autopeças.

## Fontes
- Receita Estadual RS: [Legislação alterada na exclusão de produtos da ST a partir de 1º/11/24](https://atendimento.receita.rs.gov.br/qual-foi-a-legislacao-alterada-relativa-a-exclusao-dos-produtos-da-st-a-partir-de-1-de-novembro-de-24)
- Receita Estadual RS: [Resumo de operações interestaduais (17/02/2022)](https://atendimento.receita.rs.gov.br/upload/arquivos/202203/10114448-resumo-de-operacoes-interestaduais-atual-17-02-2022.pdf)
- Contábeis: [Exclusão do segmento das autopeças da ST – Decreto 57.848/2024](https://www.contabeis.com.br/noticias/67723/exclusao-do-segmento-das-autopecas-da-substituicao-tributaria-decreto-no-57-848-2024/)
- CCA: [ICMS/RS – Antecipação nas aquisições interestaduais (2009)](https://www.cca.com.br/circulares/1527/icms-rs-antecipacao-do-recolhimento-nas-aquisicoes-interestaduais/)
- Domínio: [MA – Imposto 27-ICMS Antecipado por nota](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=8998)

## Relacionadas
- [[lei-8820-1989-id19585]] — Lei do ICMS-RS
- [[lcp-87-1996-09-13]] — Lei Kandir
