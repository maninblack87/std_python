from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws.title = "JeonSheet"

wb.save("sample.xlsx")

wb.close()
