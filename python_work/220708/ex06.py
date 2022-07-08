from openpyxl import Workbook
import numpy as np

wb = Workbook()
ws = wb.active

# index = 1
for r in range(1,11):
    for c in range(1,11):
        ws.cell(row=r,column=c).value = np.random.randint(0,100)
        # index += 1

wb.save('b.xlsx')
wb.close()