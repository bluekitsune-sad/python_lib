from openpyxl import load_workbook

wb = load_workbook('sample.xlsx')
print(wb.sheetnames)