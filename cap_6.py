# -*- coding: utf-8 -*-
# Requisitos: pip install reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle, Paragraph,
                                 Spacer, PageBreak, KeepTogether, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

PAGE_W, PAGE_H = A4
CONTENT_W = PAGE_W - 2 * 2.2 * cm

INK = colors.HexColor("#2B2320")
GOLD = colors.HexColor("#9C7A3C")
CREAM = colors.HexColor("#FBF7F0")
SOFTLINE = colors.HexColor("#D8CBB0")
BOX_TIP_BG = colors.HexColor("#F3ECDD")
BOX_WARN_BG = colors.HexColor("#F6E9E4")
BOX_WARN_LINE = colors.HexColor("#B5573A")
BOX_ERR_BG = colors.HexColor("#EFEDE9")
BOX_INFO_BG = colors.HexColor("#E9EEF0")
BOX_INFO_LINE = colors.HexColor("#4B7B8C")
RECIPE_HEAD_BG = colors.HexColor("#EFE6D3")

chapter_kicker = ParagraphStyle("ChapterKicker", fontName="Times-Italic", fontSize=12,
                                 textColor=GOLD, alignment=TA_CENTER, spaceAfter=2)
chapter_title = ParagraphStyle("ChapterTitle", fontName="Times-Bold", fontSize=26, leading=30,
                                textColor=INK, alignment=TA_CENTER, spaceBefore=4, spaceAfter=10)
chapter_intro = ParagraphStyle("ChapterIntro", fontName="Times-Italic", fontSize=11.5, leading=16,
                                textColor=colors.HexColor("#4A4038"), alignment=TA_CENTER, spaceAfter=4)

toc_title = ParagraphStyle("TocTitle", fontName="Times-Bold", fontSize=13, textColor=GOLD, spaceAfter=8)
toc_item = ParagraphStyle("TocItem", fontName="Times-Roman", fontSize=10.5, leading=16, textColor=INK,
                           leftIndent=6)

h1 = ParagraphStyle("H1", fontName="Times-Bold", fontSize=17, leading=20, textColor=INK,
                     spaceBefore=16, spaceAfter=8)
h2 = ParagraphStyle("H2", fontName="Times-Bold", fontSize=12.5, leading=15, textColor=GOLD,
                     spaceBefore=10, spaceAfter=5)
h3 = ParagraphStyle("H3", fontName="Times-BoldItalic", fontSize=10.8, leading=13.5,
                     textColor=colors.HexColor("#5C4A28"), spaceBefore=7, spaceAfter=3)
body = ParagraphStyle("Body", fontName="Times-Roman", fontSize=10.3, leading=15.5, textColor=INK,
                       alignment=TA_JUSTIFY, spaceAfter=7)
body_list = ParagraphStyle("BodyList", parent=body, leftIndent=12, spaceAfter=3)

box_title_tip = ParagraphStyle("BoxTitleTip", fontName="Times-Bold", fontSize=10.5,
                                textColor=colors.HexColor("#7A5C22"), spaceAfter=3)
box_title_warn = ParagraphStyle("BoxTitleWarn", fontName="Times-Bold", fontSize=10.5,
                                 textColor=BOX_WARN_LINE, spaceAfter=3)
box_title_err = ParagraphStyle("BoxTitleErr", fontName="Times-Bold", fontSize=10.5,
                                textColor=colors.HexColor("#3D3A36"), spaceAfter=3)
box_title_info = ParagraphStyle("BoxTitleInfo", fontName="Times-Bold", fontSize=10.5,
                                 textColor=BOX_INFO_LINE, spaceAfter=3)
box_body = ParagraphStyle("BoxBody", fontName="Times-Roman", fontSize=9.7, leading=13.5,
                           textColor=INK, alignment=TA_JUSTIFY)


def callout(kind, titulo, texto_ou_lista):
    if kind == "dica":
        bg, line, tstyle, prefix = BOX_TIP_BG, GOLD, box_title_tip, "Dica do Chef — "
    elif kind == "atencao":
        bg, line, tstyle, prefix = BOX_WARN_BG, BOX_WARN_LINE, box_title_warn, "Atenção — "
    elif kind == "info":
        bg, line, tstyle, prefix = BOX_INFO_BG, BOX_INFO_LINE, box_title_info, "Nota — "
    else:
        bg, line, tstyle, prefix = BOX_ERR_BG, colors.HexColor("#8A8378"), box_title_err, "Erro comum — "

    if isinstance(texto_ou_lista, list):
        conteudo = "".join(f"• {item}<br/>" for item in texto_ou_lista)
    else:
        conteudo = texto_ou_lista

    inner = [Paragraph(prefix + titulo, tstyle), Paragraph(conteudo, box_body)]
    t = Table([[inner]], colWidths=[CONTENT_W - 12])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 1.1, line),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return KeepTogether([Spacer(1, 4), t, Spacer(1, 8)])


def gold_rule():
    return HRFlowable(width="100%", thickness=1, color=GOLD, spaceBefore=4, spaceAfter=14)


def bullets(items, style=body_list):
    return [Paragraph(f"• {i}", style) for i in items]


story = []

# ---------- Capa do Capítulo 6 ----------
story.append(Spacer(1, 4 * cm))
story.append(Paragraph("CAPÍTULO 6", chapter_kicker))
story.append(Paragraph("Arroz e Grãos", chapter_title))
story.append(HRFlowable(width="30%", thickness=1, color=GOLD, hAlign="CENTER"))
story.append(Spacer(1, 0.6 * cm))
story.append(Paragraph(
    "Arroz, macarrão, batata-doce, batata inglesa, polenta, cuscuz e aveia formam a base de carboidrato da "
    "sua dieta. Cada um tem uma proporção de água e um tempo de cozimento próprios — acertar isso é a "
    "diferença entre um arroz soltinho e uma papa grudenta.",
    chapter_intro))
story.append(Spacer(1, 1 * cm))

idx_data = [
    "6.1  Introdução",
    "6.2  Objetivos do Capítulo",
    "6.3  Conceitos Fundamentais",
    "6.4  Equipamentos e Utensílios",
    "6.5  Técnica: Arroz Branco Soltinho",
    "6.6  Técnica: Arroz Integral",
    "6.7  Técnica: Macarrão (Tradicional e Integral)",
    "6.8  Técnica: Batata-Doce Cozida",
    "6.9  Técnica: Batata Inglesa Sauté",
    "6.10 Técnica: Batata Baroa Cozida",
    "6.11 Técnica: Polenta",
    "6.12 Técnica: Cuscuz de Milho",
    "6.13 Técnica: Goma de Tapioca",
    "6.14 Aveia: Farelo x Flocos",
    "6.15 Erros Comuns",
    "6.16 Armazenamento e Congelamento",
    "6.17 Dicas do Chef",
    "6.18 Resumo do Capítulo",
]
idx_table = Table([[Paragraph("Neste capítulo", toc_title)]] + [[Paragraph(i, toc_item)] for i in idx_data],
                   colWidths=[CONTENT_W * 0.8])
idx_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), CREAM),
    ("BOX", (0, 0), (-1, -1), 0.8, SOFTLINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 16),
    ("TOPPADDING", (0, 0), (-1, -1), 9),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
]))
story.append(idx_table)
story.append(PageBreak())

# ============================================================
# 6.1 INTRODUÇÃO
# ============================================================
story.append(Paragraph("6.1 — Introdução", h1))
story.append(gold_rule())
story.append(Paragraph(
    "O carboidrato do seu almoço e jantar tem uma lista grande de opções — arroz branco, arroz integral, "
    "macarrão, batata-doce, batata inglesa, batata baroa, polenta e cuscuz de milho aparecem todos como "
    "substituições entre si. A boa notícia: a lógica de cocção se repete bastante entre eles. Este capítulo "
    "ensina cada técnica de forma que você nunca mais precise \"adivinhar\" o tempo de fogo.", body))

# ============================================================
# 6.2 OBJETIVOS
# ============================================================
story.append(Paragraph("6.2 — Objetivos do Capítulo", h1))
story.append(gold_rule())
story.extend(bullets([
    "Cozinhar arroz branco soltinho, grão por grão, sem empapar.",
    "Ajustar a técnica para o arroz integral (mais água, mais tempo).",
    "Cozinhar macarrão no ponto al dente, tradicional e integral.",
    "Cozinhar batata-doce, batata inglesa e batata baroa nos métodos certos para cada uma.",
    "Preparar polenta, cuscuz de milho e goma de tapioca corretamente.",
    "Entender a diferença entre farelo e flocos de aveia e quando usar cada um.",
]))

# ============================================================
# 6.3 CONCEITOS
# ============================================================
story.append(Paragraph("6.3 — Conceitos Fundamentais", h1))
story.append(gold_rule())
story.append(Paragraph("<b>Por que lavar o arroz antes de cozinhar</b>", h2))
story.append(Paragraph(
    "O grão de arroz é revestido por um pó fino de amido solto (gerado no processo de moagem/polimento). "
    "Esse excesso de amido é o que faz o arroz grudar e empapar quando cozido sem lavagem prévia. Lavar em "
    "água corrente até a água sair clara (não mais leitosa) remove esse excesso e é o primeiro passo para "
    "um arroz soltinho.", body))
story.append(Paragraph("<b>Método de absorção: a lógica por trás da proporção de água</b>", h2))
story.append(Paragraph(
    "A maioria dos grãos e tubérculos desta lista cozinha pelo \"método de absorção\": uma quantidade "
    "específica de água é absorvida completamente pelo grão durante a cocção, sem sobra de líquido a "
    "escorrer no final. Errar a proporção de água é a causa nº1 de arroz empapado (água demais) ou cru no "
    "centro (água de menos).", body))
story.append(Paragraph("<b>Integral x branco: por que o integral demora mais</b>", h2))
story.append(Paragraph(
    "O arroz integral mantém o farelo (a casca externa da semente), rico em fibra — essa camada retarda a "
    "entrada de água no grão, por isso o integral sempre precisa de mais água e mais tempo de cocção do que "
    "o branco (que já teve o farelo removido no polimento).", body))

# ============================================================
# 6.4 EQUIPAMENTOS
# ============================================================
story.append(Paragraph("6.4 — Equipamentos e Utensílios", h1))
story.append(gold_rule())
story.extend(bullets([
    "<b>Panela média com tampa que feche bem</b> — essencial para o método de absorção; tampa solta deixa "
    "vapor (e água) escapar, alterando a proporção.",
    "<b>Peneira</b> para lavar arroz e escorrer macarrão/batatas.",
    "<b>Garfo</b> para \"soltar\" o arroz depois de pronto e testar o ponto de batatas.",
    "<b>Espremedor de batata ou garfo</b> para a polenta/purês.",
]))

# ============================================================
# 6.5 ARROZ BRANCO
# ============================================================
story.append(Paragraph("6.5 — Técnica: Arroz Branco Soltinho", h1))
story.append(gold_rule())
story.extend([
    Paragraph("<b>1.</b> Lave o arroz em água corrente, mexendo com a mão, até a água sair praticamente "
              "transparente.", body),
    Paragraph("<b>2. (Opcional, mas recomendado)</b> Refogue o arroz escorrido numa panela com um fio de "
              "azeite em fogo médio por 1-2 minutos, mexendo sempre, antes de adicionar a água — isso sela "
              "levemente a parte externa do grão e ajuda a mantê-lo mais soltinho.", body),
    Paragraph("<b>3.</b> Adicione a água na proporção de <b>2 partes de água para 1 parte de arroz</b> "
              "(ex.: 2 xícaras de água para 1 xícara de arroz) e uma pitada de sal.", body),
    Paragraph("<b>4.</b> Leve para ferver em fogo alto, sem tampa.", body),
    Paragraph("<b>5.</b> Assim que ferver, abaixe para fogo baixo, tampe a panela e não abra mais durante "
              "a cocção — cada vez que a tampa abre, vapor (e proporção de água) escapa.", body),
    Paragraph("<b>6.</b> Cozinhe por 15-18 minutos. O arroz está pronto quando toda a água for absorvida "
              "(sem poças visíveis ao inclinar levemente a panela) e pequenos furos/buracos aparecerem na "
              "superfície (sinal de que o vapor está passando por igual pelo grão).", body),
    Paragraph("<b>7.</b> Desligue o fogo e deixe descansar tampado por 5 minutos antes de abrir — isso "
              "termina de distribuir a umidade por igual entre os grãos.", body),
    Paragraph("<b>8.</b> Solte os grãos com um garfo (nunca com colher, que amassa) antes de servir.", body),
])
story.append(callout("erro", "Por que seu arroz sempre empapa",
    "Na grande maioria das vezes, é água demais ou tampa aberta durante a cocção (deixando vapor escapar e "
    "levando você a compensar com mais água no meio do processo, o que nunca funciona direito). Meça a "
    "água com precisão e resista à tentação de abrir a tampa para ver como está indo."))

# ============================================================
# 6.6 ARROZ INTEGRAL
# ============================================================
story.append(Paragraph("6.6 — Técnica: Arroz Integral", h1))
story.append(gold_rule())
story.append(Paragraph(
    "Mesmo método do arroz branco (Seção 6.5), com dois ajustes:", body))
story.extend(bullets([
    "<b>Proporção de água:</b> 2,5 partes de água para 1 parte de arroz (um pouco mais que o branco).",
    "<b>Tempo de cozimento:</b> 30-35 minutos em vez de 15-18 — o farelo externo retarda a hidratação do "
    "grão, então precisa de bem mais tempo.",
]))
story.append(Paragraph(
    "O teste de ponto é o mesmo: água totalmente absorvida e pequenos furos na superfície. Se ao provar o "
    "grão ainda estiver com o centro duro/arenoso depois do tempo de água esgotado, adicione um pouco mais "
    "de água quente (nunca fria, que interrompe bruscamente a cocção) e continue por mais alguns minutos.", body))

# ============================================================
# 6.7 MACARRÃO
# ============================================================
story.append(Paragraph("6.7 — Técnica: Macarrão (Tradicional e Integral)", h1))
story.append(gold_rule())
story.extend([
    Paragraph("<b>1.</b> Use bastante água (o macarrão precisa de espaço para não grudar) — uma panela "
              "grande, cheia até cerca de 3/4.", body),
    Paragraph("<b>2.</b> Adicione sal generosamente à água antes de ferver (isso tempera o macarrão por "
              "dentro, coisa que não se consegue só temperando depois de pronto).", body),
    Paragraph("<b>3.</b> Espere ferver em fervura forte antes de adicionar o macarrão. Mexa nos primeiros "
              "30-60 segundos para evitar que grude no fundo ou entre si.", body),
    Paragraph("<b>4.</b> Siga o tempo indicado na embalagem como referência, mas comece a testar 1-2 "
              "minutos antes do tempo mínimo indicado.", body),
    Paragraph("<b>5. Ponto al dente:</b> morda um pedaço — deve oferecer uma leve resistência ao centro, "
              "sem ficar cru/duro, mas também sem estar mole por igual.", body),
    Paragraph("<b>6.</b> Escorra imediatamente (sem lavar em água fria, que só é indicado se for usar em "
              "salada fria) e sirva ou misture ao molho na sequência, sem deixar descansando escorrido por "
              "muito tempo — ele continua cozinhando com o calor residual e pode passar do ponto.", body),
])
story.append(callout("info", "Macarrão integral cozinha diferente",
    "O macarrão integral tende a precisar de 1-2 minutos a mais que o tradicional, e o ponto al dente é "
    "ligeiramente mais firme ao morder — é normal, faz parte da textura mais rústica da farinha integral, "
    "não é sinal de que está mal cozido."))

# ============================================================
# 6.8 BATATA-DOCE
# ============================================================
story.append(Paragraph("6.8 — Técnica: Batata-Doce Cozida", h1))
story.append(gold_rule())
story.extend([
    Paragraph("<b>1.</b> Lave bem a casca (pode cozinhar com casca, que solta facilmente depois de pronta, "
              "ou descascar antes — ambos funcionam).", body),
    Paragraph("<b>2.</b> Corte em pedaços/fatias de tamanho parecido, para cozinharem por igual.", body),
    Paragraph("<b>3.</b> Coloque numa panela, cubra com água fria (começar com água fria e não já fervendo "
              "ajuda a batata cozinhar por igual, de fora para dentro de forma mais gradual) e leve ao fogo "
              "alto até ferver.", body),
    Paragraph("<b>4.</b> Abaixe para fogo médio e cozinhe por 15-20 minutos, dependendo do tamanho dos "
              "pedaços.", body),
    Paragraph("<b>5. Ponto certo:</b> um garfo ou faca entra até o centro sem nenhuma resistência.", body),
])

# ============================================================
# 6.9 BATATA INGLESA SAUTÉ
# ============================================================
story.append(Paragraph("6.9 — Técnica: Batata Inglesa Sauté", h1))
story.append(gold_rule())
story.extend([
    Paragraph("<b>1.</b> Corte a batata inglesa em cubos ou rodelas de tamanho uniforme.", body),
    Paragraph("<b>2.</b> Pré-cozinhe em água fervente com sal por 5-7 minutos, só até amaciar levemente "
              "por fora mas ainda firme no centro (não até cozinhar totalmente) — isso garante que o "
              "interior cozinhe por completo depois, sem precisar de tanto tempo na frigideira que "
              "queimaria a parte externa.", body),
    Paragraph("<b>3.</b> Escorra bem e seque com papel-toalha (umidade excessiva impede o dourado no "
              "próximo passo — a água na superfície esfria o azeite e cozinha no vapor em vez de fritar).", body),
    Paragraph("<b>4.</b> Numa frigideira com azeite quente em fogo médio-alto, adicione os cubos numa "
              "camada única (sem amontoar, mesmo princípio do frango em cubos do Capítulo 2) e doure por "
              "todos os lados, virando ocasionalmente, por 8-10 minutos.", body),
])

# ============================================================
# 6.10 BATATA BAROA
# ============================================================
story.append(Paragraph("6.10 — Técnica: Batata Baroa Cozida", h1))
story.append(gold_rule())
story.append(Paragraph(
    "Mesmo processo da batata-doce (Seção 6.8): água fria, fervura, fogo médio. A batata baroa costuma "
    "cozinhar um pouco mais rápido (12-18 minutos, dependendo do tamanho dos pedaços) e amolece de forma "
    "mais uniforme, sendo uma ótima opção também para fazer purê.", body))

# ============================================================
# 6.11 POLENTA
# ============================================================
story.append(Paragraph("6.11 — Técnica: Polenta", h1))
story.append(gold_rule())
story.extend([
    Paragraph("<b>1.</b> Leve a água (proporção de aproximadamente 4 partes de água para 1 parte de fubá/"
              "farinha de milho) para ferver com uma pitada de sal.", body),
    Paragraph("<b>2.</b> Reduza para fogo baixo e despeje o fubá em fio fino e contínuo, mexendo sempre "
              "com um fouet ou colher de pau — despejar tudo de uma vez forma grumos que não desfazem "
              "depois.", body),
    Paragraph("<b>3.</b> Continue mexendo com frequência (a polenta gruda e queima no fundo com facilidade) "
              "por 15-25 minutos, dependendo do tipo de fubá (o fubá pré-cozido é mais rápido).", body),
    Paragraph("<b>4. Ponto certo:</b> a polenta engrossa a ponto de a colher \"desenhar\" um caminho no "
              "fundo da panela que demora alguns segundos para se fechar sozinho.", body),
])

# ============================================================
# 6.12 CUSCUZ DE MILHO
# ============================================================
story.append(Paragraph("6.12 — Técnica: Cuscuz de Milho", h1))
story.append(gold_rule())
story.extend([
    Paragraph("<b>1.</b> Numa tigela, misture a farinha de cuscuz (flocada) com uma pitada de sal.", body),
    Paragraph("<b>2.</b> Adicione água quente (não fervendo, apenas bem quente) aos poucos, mexendo com "
              "um garfo, até a farinha ficar toda umedecida mas ainda soltinha (não uma papa) — a proporção "
              "gira em torno de partes iguais de água e farinha, mas vá adicionando aos poucos e observando "
              "a textura.", body),
    Paragraph("<b>3.</b> Deixe descansar tampado (com um prato ou pano) por 5 minutos — o vapor termina de "
              "hidratar os flocos por igual.", body),
    Paragraph("<b>4.</b> Solte os grãos com um garfo antes de servir, como no arroz.", body),
])

# ============================================================
# 6.13 GOMA DE TAPIOCA
# ============================================================
story.append(Paragraph("6.13 — Técnica: Goma de Tapioca", h1))
story.append(gold_rule())
story.append(Paragraph(
    "Usada como substituição de pão e como ingrediente das crepiocas (Capítulos 2 e 4). A goma de tapioca "
    "já vem parcialmente hidratada de fábrica — o trabalho aqui é só de textura na frigideira.", body))
story.extend([
    Paragraph("<b>1.</b> Se estiver empelotada, passe por uma peneira, esfregando com as costas de uma "
              "colher, para soltar os grumos antes de usar.", body),
    Paragraph("<b>2.</b> Numa frigideira antiaderente aquecida em fogo médio (sem óleo — ela tem "
              "propriedade antiaderente própria), espalhe uma camada fina e uniforme.", body),
    Paragraph("<b>3.</b> Deixe firmar por 1-2 minutos sem mexer, até conseguir virar a placa inteira de "
              "uma vez (ela vira uma \"panqueca\" sólida, diferente do que se poderia imaginar de um pó).", body),
    Paragraph("<b>4.</b> Vire e doure o outro lado por mais 1 minuto.", body),
])

# ============================================================
# 6.14 AVEIA
# ============================================================
story.append(Paragraph("6.14 — Aveia: Farelo x Flocos", h1))
story.append(gold_rule())
story.append(Paragraph(
    "A sua dieta usa os dois: <b>farelo de aveia</b> e <b>aveia em flocos</b>. Não são a mesma coisa.", body))
story.extend(bullets([
    "<b>Farelo de aveia:</b> é a casca externa do grão, moída fina. Textura mais parecida com uma farinha "
    "grossa, com mais fibra concentrada e menos volume por grama.",
    "<b>Flocos de aveia:</b> é o grão inteiro (ou parte dele) achatado em flocos. Mais volumoso, dá mais "
    "\"corpo\" e mastigação em receitas como panquecas e vitaminas.",
]))
story.append(Paragraph(
    "Na prática culinária: farelo se dissolve mais facilmente em líquidos (bom para polvilhar sobre frutas, "
    "como pede a dieta) e flocos mantêm mais textura mesmo depois de misturados (bom para panquecas e "
    "mingaus com mordida).", body))

# ============================================================
# 6.15 ERROS COMUNS
# ============================================================
story.append(Paragraph("6.15 — Erros Comuns", h1))
story.append(gold_rule())
story.append(callout("erro", "Os erros mais frequentes com arroz e grãos", [
    "Não lavar o arroz antes de cozinhar, deixando-o empapado.",
    "Abrir a tampa da panela no meio da cocção do arroz — perde vapor e a proporção de água muda.",
    "Cozinhar batata inglesa direto na frigideira sem pré-cozinhar em água — fica crua por dentro e "
    "queimada por fora.",
    "Despejar o fubá de uma vez na água fervendo para a polenta — forma grumos difíceis de desfazer.",
    "Confundir farelo de aveia com flocos de aveia — resultado final muda bastante de textura.",
]))

# ============================================================
# 6.16 ARMAZENAMENTO
# ============================================================
story.append(Paragraph("6.16 — Armazenamento e Congelamento", h1))
story.append(gold_rule())
story.extend(bullets([
    "<b>Arroz e macarrão cozidos, geladeira:</b> até 4-5 dias, em pote fechado.",
    "<b>Arroz e macarrão cozidos, freezer:</b> até 1 mês; descongele e reaqueça com um fio de água para "
    "reidratar.",
    "<b>Batatas cozidas, geladeira:</b> até 3-4 dias.",
    "<b>Batatas cozidas, freezer:</b> não recomendado para a batata inglesa cozida em água (fica com textura "
    "arenosa ao descongelar); batata-doce e baroa toleram melhor o congelamento, especialmente já amassadas "
    "em purê.",
    "<b>Grãos secos (arroz cru, macarrão cru, fubá):</b> em recipiente fechado, longe de umidade, por "
    "meses — sempre confira a validade da embalagem.",
]))

# ============================================================
# 6.17 DICAS DO CHEF
# ============================================================
story.append(Paragraph("6.17 — Dicas do Chef", h1))
story.append(gold_rule())
story.append(callout("dica", "Cozinhe o carboidrato da semana de uma vez",
    "Arroz, arroz integral e batata-doce são ótimos candidatos a meal prep (Capítulo 15) — cozinham em "
    "quantidade, guardam bem por vários dias e só precisam de um reaquecimento rápido com um fio de água "
    "para voltarem à textura original."))
story.append(callout("dica", "Reaquecendo arroz sem ressecar",
    "Adicione 1 colher de sopa de água por porção antes de tampar e reaquecer (frigideira ou micro-ondas) "
    "— o vapor gerado reidrata os grãos que perderam umidade na geladeira."))

# ============================================================
# 6.18 RESUMO
# ============================================================
story.append(Paragraph("6.18 — Resumo do Capítulo", h1))
story.append(gold_rule())
story.extend(bullets([
    "Arroz branco: lave antes, 2:1 de água, fogo baixo tampado, sem abrir a tampa.",
    "Arroz integral: mesma lógica, 2,5:1 de água, quase o dobro do tempo.",
    "Macarrão: bastante água salgada, ponto al dente testado 1-2 min antes do tempo da embalagem.",
    "Batata inglesa: sempre pré-cozida antes de ir para a frigideira dourar.",
    "Farelo de aveia ≠ flocos de aveia — texturas diferentes, usos diferentes.",
    "Reaqueça carboidratos sempre com um pouco de água extra para repor a umidade perdida.",
]))
story.append(Spacer(1, 10))
story.append(Paragraph(
    "No próximo capítulo, seguimos para Feijões e Leguminosas — a outra metade do prato de almoço e jantar, "
    "com a técnica de deixar de molho e os tempos de cozimento de cada tipo.",
    ParagraphStyle("Closing", parent=body, fontName="Times-Italic")))


def draw_page_furniture(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(SOFTLINE)
    canvas.setLineWidth(0.6)
    canvas.line(2.2 * cm, 1.7 * cm, PAGE_W - 2.2 * cm, 1.7 * cm)
    canvas.setFont("Times-Italic", 8.5)
    canvas.setFillColor(colors.HexColor("#7A6F60"))
    canvas.drawString(2.2 * cm, 1.3 * cm, "O Livro da Cozinha de Performance")
    canvas.drawRightString(PAGE_W - 2.2 * cm, 1.3 * cm, f"Capítulo 6  •  Página {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate("Livro_Cozinha_Cap6_ArrozGraos.pdf", pagesize=A4,
                         leftMargin=2.2 * cm, rightMargin=2.2 * cm,
                         topMargin=2 * cm, bottomMargin=2.2 * cm,
                         title="O Livro da Cozinha de Performance - Capítulo 6")
doc.build(story, onFirstPage=draw_page_furniture, onLaterPages=draw_page_furniture)
print("done")