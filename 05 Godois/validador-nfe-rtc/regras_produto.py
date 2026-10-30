"""
Regras por NCM usadas pelo validador (camada 4 - coerência fiscal).

Fontes (conferidas no texto em 03 Legislação/):
- LC 214/2025, art. 125 e Anexo I (cesta básica nacional: IBS e CBS com alíquota zero),
  texto "norma atualizada" da Câmara, PDF de 28/08/2026.
- Lei 10.925/2004, art. 1º, XIX (carnes: PIS/COFINS com alíquota zero), texto compilado.

Os códigos estão sem pontos e são comparados por prefixo do NCM de 8 dígitos.
Códigos "condicionais" dependem da descrição do produto (ex.: 1905.90.90 só vale para o
pão francês), por isso geram apenas aviso para conferência.
"""

# (item do Anexo I, descrição, incluídos, excluídos, condicionais)
ANEXO_I_LC214 = [
    (1, "Arroz", ["100620", "100630", "10064000"], [], []),
    (2, "Leite", ["04011010", "04011090", "04012010", "04012090", "04014010", "04015010"], [], []),
    (3, "Leite em pó", ["04021010", "04021090", "04022110", "04022120", "04022910", "04022920"], [], []),
    (4, "Fórmulas infantis", ["19011010", "19011090"], [], ["21069090"]),
    (5, "Manteiga", ["04051000"], [], []),
    (6, "Margarina", ["15171000"], [], []),
    (7, "Feijões", ["07133319", "07133329", "07133399", "07133590"], [], []),
    (8, "Café", ["0901", "21011"], [], []),
    (9, "Óleo de babaçu", ["15132120"], [], []),
    (10, "Farinha de mandioca e tapioca", ["11062000", "19030000"], [], []),
    (11, "Farinha, grumos e sêmolas de milho", ["11022000", "11031300"], [], []),
    (12, "Grãos de milho", ["11041900", "11042300"], [], []),
    (13, "Farinha de trigo", ["11010010"], [], []),
    (14, "Açúcar", ["17011400", "17019900"], [], []),
    (15, "Massas alimentícias", ["19021"], [], []),
    (16, "Pão francês e pré-mistura", ["19012010", "19012090"], [], ["19059090"]),
    (17, "Grãos de aveia", ["11041200", "11042200"], [], []),
    (18, "Farinha de aveia", ["11029000"], [], []),
    (19, "Carnes bovina, suína, ovina, caprina e de aves",
     ["0201", "0202", "02061000", "02062", "02102000",
      "0203", "02063000", "02064", "020910", "02101",
      "0204", "02109920", "02109990", "02068000", "02069000",
      "0207", "02099000", "0210991"],
     ["02074300", "02075300"], []),
    (20, "Peixes e carnes de peixes",
     ["0302", "0303", "0304"],
     ["03021", "03023", "03025100", "03025200", "03025300", "03029",
      "03031", "03034", "03036300", "03036400", "03036500", "03039",
      "03044", "03045", "03047", "03048", "03049"], []),
    (21, "Queijos", ["04061010", "04061090", "04062000", "04069010", "04069020", "04069030"], [], []),
    (22, "Sal", ["25010020", "25010090"], [], []),
    (23, "Mate", ["0903"], [], []),
    (24, "Farinha com baixo teor de proteína", [], [], ["19019090"]),
    (26, "Fórmulas dietoterápicas", [], [], ["21069090"]),
]

# Lei 10.925/2004, art. 1º, XIX (carnes) - PIS/COFINS alíquota zero
LEI_10925_XIX = {
    "a": ["0201", "0202", "02061000", "02062", "02102000", "05069000", "05100010", "1502101"],
    "b": ["0203", "02063000", "02064", "0207", "0209", "02101"],
    "c": ["0204", "02068000"],
}
LEI_10925_XIX_CONDICIONAL = {"02109900": "só carne de frango (alínea b)"}


def _casa(ncm, codigos):
    return any(ncm.startswith(c) for c in codigos)


def anexo_i(ncm):
    """Retorna (item, descrição, 'certo'|'condicional') se o NCM está no Anexo I da LC 214."""
    ncm = (ncm or "").replace(".", "")
    for item, desc, inc, exc, cond in ANEXO_I_LC214:
        if _casa(ncm, exc):
            continue
        if _casa(ncm, inc):
            return item, desc, "certo"
        if _casa(ncm, cond):
            return item, desc, "condicional"
    return None


def lei_10925_xix(ncm):
    """Retorna (alínea, 'certo'|'condicional') se o NCM tem PIS/COFINS zero pelo art. 1º, XIX."""
    ncm = (ncm or "").replace(".", "")
    for alinea, cods in LEI_10925_XIX.items():
        if _casa(ncm, cods):
            return alinea, "certo"
    for cod, obs in LEI_10925_XIX_CONDICIONAL.items():
        if ncm.startswith(cod):
            return obs, "condicional"
    return None
