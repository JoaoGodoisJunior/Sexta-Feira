#!/usr/bin/env python3
"""
Gera o painel visual da Sexta-Feira (HTML autocontido) a partir do repositório.
Uso: python3 gerar_painel.py [raiz_do_repo] [saida.html]
"""
import os, re, sys, json, html, datetime

RAIZ = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SAIDA = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "painel.html")
HOJE = datetime.date.today()


def md_files(pasta):
    out = []
    for r, _, fs in os.walk(pasta):
        for f in fs:
            if f.endswith(".md") and not f.startswith(("_", "LEIA-ME")):
                out.append(os.path.join(r, f))
    return out


def frontmatter(texto):
    m = re.match(r"^---\n(.*?)\n---", texto, re.S)
    fm = {}
    if m:
        for linha in m.group(1).splitlines():
            if ":" in linha:
                k, v = linha.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def ler(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


# Legislação
leg_dir = os.path.join(RAIZ, "03 Legislação")
legislacao = {}
for d in sorted(os.listdir(leg_dir)):
    p = os.path.join(leg_dir, d)
    if os.path.isdir(p) and d != "Jurisprudência":
        legislacao[d] = len(md_files(p))
juris = {}
jdir = os.path.join(leg_dir, "Jurisprudência")
if os.path.isdir(jdir):
    for d in sorted(os.listdir(jdir)):
        p = os.path.join(jdir, d)
        if os.path.isdir(p):
            juris[d] = len([f for f in os.listdir(p) if f.endswith(".md")])
indice = ler(os.path.join(leg_dir, "_Índice e status da legislação.md"))
pend_leg = re.findall(r"^- \*\*(.+?)\*\*", indice.split("## ⚠ Pendentes")[1].split("##")[0], re.M) if "## ⚠ Pendentes" in indice else []

# Conhecimento
con_dir = os.path.join(RAIZ, "04 Conhecimento")
areas = {}
notas = []
for a in sorted(os.listdir(con_dir)):
    p = os.path.join(con_dir, a)
    if not os.path.isdir(p):
        continue
    fs = md_files(p)
    areas[a] = len(fs)
    for f in fs:
        t = ler(f)
        fm = frontmatter(t)
        abertas = len(re.findall(r"^- \[ \]", t, re.M))
        feitas = len(re.findall(r"^- \[x\]", t, re.M))
        rev = fm.get("revisar_em", "")
        vencida = False
        try:
            vencida = datetime.date.fromisoformat(rev[:10]) < HOJE
        except Exception:
            pass
        status = fm.get("status", "sem status")
        if vencida and status == "válida":
            status = "revisar"
        notas.append({"titulo": os.path.splitext(os.path.basename(f))[0], "area": a, "status": status,
                      "revisar_em": rev, "pendencias": abertas, "resolvidas": feitas})

# Casos, biblioteca
casos = len(md_files(os.path.join(RAIZ, "08 Casos Godois")))
biblio = len(md_files(os.path.join(RAIZ, "07 Biblioteca")))

# Estudos
rev_txt = ler(os.path.join(RAIZ, "06 Estudos", "Revisões.md"))
revisoes = []
for linha in rev_txt.splitlines():
    c = [x.strip() for x in linha.strip().strip("|").split("|")]
    if len(c) == 7 and re.match(r"\d{4}-\d{2}-\d{2}", c[2]):
        prox = next((d for d in c[3:6] if d >= HOJE.isoformat()), None)
        revisoes.append({"assunto": c[0], "materia": c[1], "proxima": prox, "situacao": c[6]})
des_txt = ler(os.path.join(RAIZ, "06 Estudos", "Desempenho.md"))
sessoes = []
for linha in des_txt.splitlines():
    c = [x.strip() for x in linha.strip().strip("|").split("|")]
    if len(c) >= 6 and re.match(r"\d{4}-\d{2}-\d{2}", c[0]):
        try:
            sessoes.append({"data": c[0], "materia": c[1], "acertos": int(c[3]), "erros": int(c[4])})
        except ValueError:
            pass

# Manutenção
rel_dir = os.path.join(RAIZ, "09 Manutenção", "Relatórios")
relatorios = sorted([f for f in os.listdir(rel_dir) if f.endswith(".md")]) if os.path.isdir(rel_dir) else []

dados = {
    "gerado_em": HOJE.isoformat(),
    "legislacao": legislacao, "juris": juris, "pend_leg": pend_leg,
    "areas": areas, "notas": notas, "casos": casos, "biblio": biblio,
    "revisoes": revisoes, "sessoes": sessoes,
    "ultimo_relatorio": relatorios[-1][:-3] if relatorios else None,
}

modelo = ler(os.path.join(os.path.dirname(__file__), "modelo_painel.html"))
with open(SAIDA, "w", encoding="utf-8") as f:
    f.write(modelo.replace("/*__DADOS__*/null", json.dumps(dados, ensure_ascii=False)))
print(SAIDA)
