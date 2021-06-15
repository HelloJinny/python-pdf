from reportlab.lib import colors
from reportlab.pdfgen   import canvas

def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800') 

pdf = canvas.Canvas('Correlophus_ciliatus.pdf')
# drawMyRuler(pdf)

# 1) 파일 / 파일에 제목 추가

pdf.setTitle('Crested_gecko')

# 2) 제목 추가

# for font in pdf.getAvailableFonts():
#     print(font)

from reportlab.pdfbase.ttfonts  import TTFont
from reportlab.pdfbase          import pdfmetrics

pdfmetrics.registerFont(TTFont('aminhafonte', 'Formula 1.ttf'))

pdf.setFont('aminhafonte', 54)

pdf.setFillColor('black')
pdf.drawCentredString(300, 770, 'Crested_gecko')
pdf.setFillColor('red')
pdf.drawCentredString(298, 772, 'Crested_gecko')

# 3) 부제목 추가

from reportlab.lib      import colors

pdf.setFont('Helvetica-Bold', 24)
pdf.setFillColor(colors.black)
pdf.drawCentredString(300, 740, 'My pet')

# 4) 수평선 추가

pdf.setStrokeColor(colors.lightgrey)
pdf.setLineWidth(3)
pdf.line(30, 730, 550, 730)

# 5) 단락 추가

from reportlab.platypus import Paragraph

p = Paragraph('The Crested Gecko is also known as the New Caledonian Gecko, or even an Eyelash Gecko due to its pronounced ridges that mimic eyelashes. This arboreal lizard was once though to be extinct, but it wasn\'t until the early 1990\'s that a breeding group was imported into the United States. These animals are easy to keep and breed easily in captivity. Selective breeding has introduced a wide variety of colors, patterns, and markings making this one of the most popular reptiles available today.')

p.wrapOn(pdf, 400, 100)
p.drawOn(pdf, 100, 625)

# 6) 이미지 추가

pdf.drawInlineImage(
    'C:\workspaces\Git\python-pdf\myPet.jpg',
    180, 380,
    300, 300,
    preserveAspectRatio= True
    )

# 7) 하이퍼 링크 추가

pdf.linkURL(
    'https://en.wikipedia.org/wiki/Crested_gecko',  
    (180, 450, 180 + 250, 450 + 150),
    relative=1
)

# pdf.rect(180, 450, 250, 150)

pdf.save()