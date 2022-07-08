from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image('main1.png')

ws.add_image(img,'A1')

wb.save('d.xlsx')
wb.close()