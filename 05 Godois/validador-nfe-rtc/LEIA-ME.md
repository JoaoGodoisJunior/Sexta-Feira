# Validador de NF-e/NFC-e — Reforma Tributária

Ferramenta da Sexta-Feira para apontar erros em XML de NF-e/NFC-e antes (ou depois) da SEFAZ.

## O que ele confere
1. **Estrutura**: valida o XML contra o schema oficial (pacote PL_010g v1.03), igual à entrada da SEFAZ. Erro aqui = Rejeição 225.
2. **Cálculo**: base × alíquota de IBS estadual, IBS municipal e CBS em cada item; vIBS = UF + Município.
3. **Totais**: soma dos itens × grupo IBSCBSTot (base, IBS UF, IBS Mun, IBS, CBS).
4. **Coerência**: itens sem o grupo IBSCBS; alíquotas diferentes do ano-teste em 2026 (CBS 0,9% e IBS 0,1%) sem redução ou diferimento informados.

As camadas 2 a 4 são verificações da Sexta-Feira inspiradas na NT 2025.002-RTC. Não substituem a validação oficial.

## Como usar
- No chat: anexe o XML e peça "valida essa nota". O Claude roda o script e devolve os erros explicados e um painel.
- No computador: `python validar_nfe.py nota.xml schemas/NFe`

## Privacidade
XML de cliente é analisado na hora e **não** é guardado no cofre.

## Próximas melhorias
- Regras oficiais da NT (códigos UB…, VC…) cadastradas uma a uma, com o código de rejeição.
- Coerência CST × cClassTrib pela tabela oficial de classificação tributária.
- Leiaute do Simples Nacional (NT 2026.005) e do split payment (NT 2026.006).
- NFS-e nacional.
