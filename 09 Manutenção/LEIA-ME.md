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
   - procura normas novas ou alteradas (Planalto, DOU, Receita Federal, Comitê Gestor do IBS, SEFAZ-RS, Portal da NF-e, CFC/CPC e tribunais);
   - para cada novidade traz: o que é, o que muda em 1 ou 2 linhas, a área, quais notas da base **poderiam** ser afetadas e o **link oficial**;
   - lista as notas com `revisar_em` vencido;
   - grava o relatório em `09 Manutenção/Relatórios/AAAA-MM-DD.md` e envia o resumo ao João;
   - **não altera nenhuma nota nem a legislação**.
3. **Fontes e fluxo de incorporação**: ver `Fontes oficiais.md` nesta pasta.
4. **Quem decide é o João.** Ele avalia cada novidade; o que interessar, ele salva pelo link e envia no chat. Só então a base é atualizada e as notas revisadas, com a aprovação dele.
