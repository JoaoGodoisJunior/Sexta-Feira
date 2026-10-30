---
tipo: manutenção
descricao: Como a Sexta-Feira se mantém atualizada — status das notas, revisões periódicas e a rotina semanal de monitoramento de normas.
---

# Manutenção da base

## Por que existe
Base desatualizada dá resposta errada com cara de certa. Na área tributária isso é risco profissional.

## Como funciona
1. **Toda nota** em `04 Conhecimento/` tem `status` (válida · revisar · desatualizada) e `revisar_em` (padrão: 3 meses após a última conferência).
2. **Rotina semanal automática** (tarefa agendada, segunda-feira de manhã):
   - procura normas novas ou alteradas (Planalto, DOU, Receita Federal, SEFAZ-RS, Portal da NF-e, CFC/CPC);
   - compara com `03 Legislação/_Índice e status da legislação.md`;
   - aponta quais notas de `04 Conhecimento/` são afetadas e muda o status delas para **revisar** (nunca reescreve o conteúdo sozinha);
   - lista as notas com `revisar_em` vencido;
   - grava o relatório em `09 Manutenção/Relatórios/AAAA-MM-DD.md` e envia um resumo ao João.
3. **Fontes e fluxo de incorporação**: ver `Fontes oficiais.md` nesta pasta.
4. **Quem decide é o João.** A rotina só sinaliza; a atualização do conteúdo acontece numa conversa, com a aprovação dele.
