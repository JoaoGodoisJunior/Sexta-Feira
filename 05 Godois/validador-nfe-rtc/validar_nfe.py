#!/usr/bin/env python3
"""
Validador de NF-e/NFC-e - Reforma Tributaria (IBS/CBS/IS) - Sexta-Feira / Godois

Camada 1: estrutura contra o schema oficial (pacote PL_010g).
Camada 2: verificacoes de consistencia dos grupos IBS/CBS (somatorios e calculos).
Camada 3: alertas de coerencia (ano-teste 2026, grupo ausente etc.).

As camadas 2 e 3 sao verificacoes da Sexta-Feira inspiradas na NT 2025.002-RTC;
nao substituem a validacao oficial da SEFAZ. Codigos oficiais de rejeicao so sao
citados quando a regra foi conferida no texto da NT.

Uso: python3 validar_nfe.py arquivo.xml [pasta_schemas]
"""
import sys, os, json
from decimal import Decimal, InvalidOperation
from lxml import etree

NS = {"n": "http://www.portalfiscal.inf.br/nfe"}
TOL = Decimal("0.01")


def d(node, path):
    """Decimal do primeiro elemento encontrado no caminho, ou None."""
    if node is None:
        return None
    r = node.find(path, NS)
    if r is None or r.text is None:
        return None
    try:
        return Decimal(r.text.strip())
    except InvalidOperation:
        return None


def t(node, path):
    r = node.find(path, NS) if node is not None else None
    return r.text.strip() if r is not None and r.text else None


def achado(lista, nivel, camada, local, problema, como_corrigir, regra=None):
    lista.append({"nivel": nivel, "camada": camada, "local": local,
                  "problema": problema, "como_corrigir": como_corrigir,
                  "regra": regra})


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from regras_produto import anexo_i, lei_10925_xix  # noqa: E402


def verificar_produto(achados, n, ncm, produto, det, ibscbs):
    """Camada 4: tratamento tributário esperado pelo NCM (cesta básica e alíquota zero)."""
    local = f"item {n} · NCM {ncm}"
    ctrib = t(ibscbs, "n:cClassTrib") if ibscbs is not None else None
    cst = t(ibscbs, "n:CST") if ibscbs is not None else None

    a = anexo_i(ncm)
    if a:
        it, desc, tipo = a
        if ctrib != "200003":
            if tipo == "certo":
                achado(achados, "erro", "Cadastro tributário", local,
                       f"{produto}: NCM no Anexo I da LC 214 (item {it}, {desc}), mas a nota usa CST {cst} / cClassTrib {ctrib}.",
                       "Cesta básica nacional: IBS e CBS com alíquota zero (CST 200, cClassTrib 200003, redução de 100%). "
                       "Corrigir o cadastro do produto no emissor.",
                       regra="LC 214/2025, art. 125 e Anexo I (texto expresso)")
            else:
                achado(achados, "alerta", "Cadastro tributário", local,
                       f"{produto}: NCM pode estar no Anexo I da LC 214 (item {it}, {desc}), dependendo da descrição do produto.",
                       "Confira se o produto é exatamente o descrito no Anexo I; se for, usar CST 200 / cClassTrib 200003.",
                       regra="LC 214/2025, art. 125 e Anexo I")
    elif ctrib == "200003":
        achado(achados, "alerta", "Cadastro tributário", local,
               f"{produto}: cClassTrib 200003 (cesta básica) para NCM que não encontrei no Anexo I da LC 214.",
               "Confira o NCM e a classificação; redução indevida gera imposto a recolher.",
               regra="LC 214/2025, art. 125 e Anexo I")

    pis = det.find("n:imposto/n:PIS", NS)
    pis_cst = None
    if pis is not None and len(pis):
        pis_cst = t(pis[0], "n:CST")
    l = lei_10925_xix(ncm)
    if l and pis_cst in ("01", "02"):
        alinea, tipo = l
        nivel = "erro" if tipo == "certo" else "alerta"
        achado(achados, nivel, "Cadastro tributário", local,
               f"{produto}: PIS/COFINS tributado (CST {pis_cst}), mas o NCM tem alíquota zero (Lei 10.925/2004, art. 1º, XIX, alínea {alinea}).",
               "Usar CST 06 (alíquota zero) no PIS e na COFINS. Se foi recolhido, avaliar restituição/compensação via PER/DCOMP.",
               regra="Lei 10.925/2004, art. 1º, XIX (texto expresso)")


def validar(caminho_xml, pasta_schema):
    achados = []
    resumo = {}
    try:
        doc = etree.parse(caminho_xml)
    except etree.XMLSyntaxError as e:
        achado(achados, "erro", "Estrutura", f"linha {e.lineno}",
               f"XML mal formado: {e.msg}",
               "O arquivo está corrompido ou foi editado manualmente. Baixe o XML original de novo.")
        return resumo, achados

    raiz = doc.getroot()
    nfe = raiz if etree.QName(raiz).localname == "NFe" else raiz.find(".//n:NFe", NS)
    if nfe is None:
        achado(achados, "erro", "Estrutura", "raiz", "Não encontrei o elemento NFe.",
               "Confirme que é um XML de NF-e/NFC-e (e não de evento ou NFS-e).")
        return resumo, achados

    # ---------- Camada 1: schema ----------
    xsd_path = os.path.join(pasta_schema, "nfe_v4.00.xsd")
    if os.path.exists(xsd_path):
        schema = etree.XMLSchema(etree.parse(xsd_path))
        if not schema.validate(nfe):
            for err in schema.error_log:
                msg = err.message.replace("{http://www.portalfiscal.inf.br/nfe}", "")
                achado(achados, "erro", "Estrutura (schema)", f"linha {err.line}", msg,
                       "Corrija o campo indicado no sistema emissor; a SEFAZ rejeita por erro de schema (Rejeição 225).")
    else:
        achado(achados, "aviso", "Estrutura (schema)", "-", "Pasta de schemas não encontrada; camada 1 não executada.",
               "Informe a pasta do pacote PL_010g/NFe.")

    inf = nfe.find("n:infNFe", NS)
    ide = inf.find("n:ide", NS)
    emit = inf.find("n:emit", NS)
    dh = t(ide, "n:dhEmi") or ""
    ano = dh[:4]
    resumo.update({
        "chave": (inf.get("Id") or "")[3:],
        "modelo": t(ide, "n:mod"), "numero": t(ide, "n:nNF"), "serie": t(ide, "n:serie"),
        "emissao": dh, "natureza": t(ide, "n:natOp"), "finalidade": t(ide, "n:finNFe"),
        "crt": t(emit, "n:CRT"), "uf_emitente": t(emit, "n:enderEmit/n:UF"),
    })

    # ---------- Camada 2: itens ----------
    soma = {k: Decimal("0") for k in ["vBC", "vIBSUF", "vIBSMun", "vIBS", "vCBS"]}
    itens = []
    sem_grupo = []
    for det in inf.findall("n:det", NS):
        n = det.get("nItem")
        prod = det.find("n:prod", NS)
        ibscbs = det.find("n:imposto/n:IBSCBS", NS)
        item = {"nItem": n, "produto": t(prod, "n:xProd"), "ncm": t(prod, "n:NCM"),
                "cfop": t(prod, "n:CFOP"), "vProd": str(d(prod, "n:vProd") or 0)}
        verificar_produto(achados, n, item["ncm"], item["produto"], det, ibscbs)
        if ibscbs is None:
            sem_grupo.append(n)
            itens.append(item)
            continue
        item["cst"] = t(ibscbs, "n:CST")
        item["cClassTrib"] = t(ibscbs, "n:cClassTrib")
        g = ibscbs.find("n:gIBSCBS", NS)
        if g is not None:
            vbc = d(g, "n:vBC") or Decimal("0")
            pairs = [("gIBSUF", "pIBSUF", "vIBSUF"), ("gIBSMun", "pIBSMun", "vIBSMun"), ("gCBS", "pCBS", "vCBS")]
            for grp, p, v in pairs:
                gg = g.find(f"n:{grp}", NS)
                aliq, val = d(gg, f"n:{p}"), d(gg, f"n:{v}")
                item[p], item[v] = str(aliq) if aliq is not None else None, str(val) if val is not None else None
                if aliq is None or val is None:
                    continue
                tem_reducao = gg.find("n:gRed", NS) is not None or gg.find("n:gDif", NS) is not None
                esperado = (vbc * aliq / 100).quantize(Decimal("0.01"))
                if not tem_reducao and abs(esperado - val) > TOL:
                    achado(achados, "erro", "Cálculo", f"item {n} · {v}",
                           f"{v} = {val}, mas base {vbc} × {aliq}% = {esperado}.",
                           f"Recalcule {v} no emissor (base × alíquota), ou informe o grupo de redução/diferimento se houver.")
                soma[v] += val
                if ano == "2026" and grp == "gCBS" and aliq not in (Decimal("0.9"), Decimal("0.90"), Decimal("0.9000")) and not tem_reducao:
                    achado(achados, "alerta", "Coerência", f"item {n} · pCBS",
                           f"Alíquota de CBS {aliq}% em nota de 2026.",
                           "No ano-teste de 2026 a CBS é de 0,9%. Confira se há redução, isenção ou outro tratamento que justifique.")
                if ano == "2026" and grp == "gIBSUF" and aliq not in (Decimal("0.1"), Decimal("0.10"), Decimal("0.1000")) and not tem_reducao:
                    achado(achados, "alerta", "Coerência", f"item {n} · pIBSUF",
                           f"Alíquota de IBS estadual {aliq}% em nota de 2026.",
                           "No ano-teste de 2026 o IBS é de 0,1%. Confira se há redução, isenção ou outro tratamento que justifique.")
            soma["vBC"] += vbc
            vibs = d(g, "n:vIBS")
            if vibs is not None:
                soma["vIBS"] += vibs
                comp = (d(g, "n:gIBSUF/n:vIBSUF") or 0) + (d(g, "n:gIBSMun/n:vIBSMun") or 0)
                if abs(comp - vibs) > TOL:
                    achado(achados, "erro", "Cálculo", f"item {n} · vIBS",
                           f"vIBS = {vibs}, mas IBS UF + IBS Município = {comp}.",
                           "O vIBS do item deve ser a soma das parcelas estadual e municipal.")
        itens.append(item)

    if sem_grupo:
        achado(achados, "alerta", "Coerência", "itens " + ", ".join(sem_grupo),
               f"{len(sem_grupo)} item(ns) sem o grupo IBSCBS.",
               "Em 2026 o preenchimento ainda não é exigido por regra de validação (UB12-10 em implementação futura), "
               "mas é obrigatório pela legislação para o Regime Normal. Confira o cadastro tributário do produto.",
               regra="UB12-10 (implementação futura)")

    # ---------- Camada 2: totais ----------
    tot = inf.find("n:total/n:IBSCBSTot", NS)
    if tot is not None:
        comparar = [("n:vBCIBSCBS", "vBC", "base IBS/CBS"),
                    ("n:gIBS/n:gIBSUF/n:vIBSUF", "vIBSUF", "IBS estadual"),
                    ("n:gIBS/n:gIBSMun/n:vIBSMun", "vIBSMun", "IBS municipal"),
                    ("n:gIBS/n:vIBS", "vIBS", "IBS total"),
                    ("n:gCBS/n:vCBS", "vCBS", "CBS")]
        totais = {}
        for path, chave, nome in comparar:
            vt = d(tot, path)
            totais[chave] = str(vt) if vt is not None else None
            if vt is not None and abs(vt - soma[chave]) > TOL:
                achado(achados, "erro", "Totais", f"total · {path.split('/')[-1][2:]}",
                       f"Total de {nome} = {vt}, mas a soma dos itens = {soma[chave]}.",
                       "O total da nota precisa ser a soma exata dos itens. Recalcule os totais no emissor.")
        resumo["totais_ibscbs"] = totais
    elif any(soma.values()):
        achado(achados, "erro", "Totais", "total", "Itens têm IBS/CBS, mas falta o grupo IBSCBSTot no total.",
               "Inclua o grupo de totais do IBS/CBS.")

    resumo["soma_itens"] = {k: str(v) for k, v in soma.items()}
    resumo["vNF"] = str(d(inf, "n:total/n:ICMSTot/n:vNF"))
    resumo["vNFTot"] = str(d(inf, "n:total/n:vNFTot")) if inf.find("n:total/n:vNFTot", NS) is not None else None
    resumo["itens"] = itens
    return resumo, achados


if __name__ == "__main__":
    xml = sys.argv[1]
    pasta = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "schemas", "NFe")
    resumo, achados = validar(xml, pasta)
    print(json.dumps({"resumo": resumo, "achados": achados}, ensure_ascii=False, indent=2))
