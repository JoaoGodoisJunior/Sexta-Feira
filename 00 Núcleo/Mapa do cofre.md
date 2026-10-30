# Mapa do cofre

A Sexta-Feira vive no GitHub (repositório privado `JoaoGodoisJunior/sexta-feira`). Os originais pesados ficam no OneDrive.

| Onde | Pasta | O que guarda | Quem escreve |
|---|---|---|---|
| OneDrive | `Godois Consultoria/` | Documentos de clientes | ✖ fora da Sexta-Feira |
| OneDrive | `Estudos/` | Faculdade (FSG) e cursos, originais | João |
| OneDrive | `Base Contábil/` | Livros, normas (CPC/NBC), especializações, modelos | João |
| GitHub | `00 Núcleo/` | Regras, mapa, modelos de nota, registro de correções | Claude (João aprova) |
| GitHub | `01 Entrada/` | Caixa de entrada: qualquer coisa a classificar | João |
| GitHub | `03 Legislação/` | Leis, Notas Técnicas e jurisprudência (súmulas, repetitivos, repercussão geral) | Claude |
| GitHub | `04 Conhecimento/` | Notas por tema, interligadas | Claude |
| GitHub | `05 Godois/` | Modelos, procedimentos e ferramentas, sem dados de cliente | João e Claude |
| GitHub | `07 Biblioteca/` | Doutrina por tema: livros, artigos e textos em ABNT | Claude |
| GitHub | `08 Casos Godois/` | Casos de clientes anonimizados: a jurisprudência interna | Claude (João aprova) |
| GitHub | `09 Manutenção/` | Relatórios semanais de atualização da base | Rotina automática |
| GitHub | `06 Estudos/` | Desempenho, revisões espaçadas e calendário de provas | Claude |

## Fluxo
1. João salva o original no OneDrive (`Estudos/` ou `Base Contábil/`) ou anexa na conversa.
2. Claude lê e escreve/atualiza a nota do tema em `04 Conhecimento/`.
3. A nota liga para a lei, para o original (caminho no OneDrive) e para os temas vizinhos.
4. Toda alteração vira um commit: dá para ver o histórico e voltar versões.

## Nunca no repositório
XML de notas, certificados digitais, documentos ou dados de clientes (o `.gitignore` bloqueia XML e certificados).
