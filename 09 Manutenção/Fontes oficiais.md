---
tipo: manutenção
descricao: Onde a Sexta-Feira procura normas novas e como elas entram na base.
---

# Fontes oficiais monitoradas

| O que | Onde procurar |
|---|---|
| Leis, LCs, decretos federais (texto e compilação) | Planalto — www.planalto.gov.br/legislacao · normas.leg.br (Câmara) · LexML (www.lexml.gov.br) |
| Publicação diária de atos | Diário Oficial da União — www.in.gov.br |
| Instruções normativas, soluções de consulta | Receita Federal — normas.receita.fazenda.gov.br |
| IBS e Comitê Gestor | Atos do Comitê Gestor do IBS (site oficial) e DOU |
| ICMS no RS | Receita Estadual RS — receita.fazenda.rs.gov.br (legislação, RICMS, instruções normativas) |
| NF-e, NFC-e e documentos fiscais | Portal Nacional da NF-e — www.nfe.fazenda.gov.br (notas técnicas e pacotes de schema) |
| Normas contábeis | CFC — cfc.org.br (NBCs) · CPC — www.cpc.org.br |
| Precedentes | STF, STJ, TST, TRF4 e Banco Nacional de Precedentes do CNJ |
| Jurisprudência administrativa | CARF (federal) · TARF-RS (ICMS) |

## Como uma norma nova entra na base
1. **Detectar (automático)**: a rotina de segunda-feira faz buscas na internet nessas fontes e lista o que saiu ou mudou na semana.
2. **Sinalizar (automático)**: marca como "revisar" as notas afetadas e grava o relatório em `09 Manutenção/Relatórios/`, com o **link oficial** de cada norma.
3. **Incorporar (com o João)**: o ambiente do Claude não consegue baixar o texto integral desses sites. O João abre o link do relatório, salva a página (Ctrl+S) ou o PDF e envia no chat. A Sexta-Feira converte, confere se está completo, substitui a versão antiga na `03 Legislação/` (o histórico do GitHub guarda a anterior) e atualiza o índice.
4. **Revisar as notas (com o João)**: a Sexta-Feira propõe a atualização das notas afetadas, o João aprova, e o status volta a "válida".

Enquanto o passo 3 não acontece, a regra 4 do núcleo vale com mais força: a resposta avisa que a norma da base pode estar desatualizada e cita a novidade encontrada.
