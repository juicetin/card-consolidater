from reportlab.graphics.barcode import code128
from reportlab.graphics.barcode import code39
from reportlab.graphics.barcode.eanbc import Ean13BarcodeWidget
from reportlab.graphics.barcode import itf
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

def read_barcodes():
    lines = tuple(open('barcodes.txt', 'r'))
    return lines


b_height=1.9*mm
b_width=0.27

c = canvas.Canvas('cards.pdf')
c.setPageSize((32.5*mm, 21.25*mm))

lines = read_barcodes()
for line in lines:
    line_parts = line.strip().split(':')

# Barcode
barcode = code128.Code128("9036013336378810238906", barHeight=b_height, barWidth=b_width)
barcode.drawOn(c, -5.7*mm, 18.5*mm)

# Text
textobject = c.beginText()
textobject.setTextOrigin(1.7, 16.7*mm)
textobject.setFont('Helvetica', 4.7)
textobject.textLines('Eckersley\'s Student')
c.drawText(textobject)

c.save()
