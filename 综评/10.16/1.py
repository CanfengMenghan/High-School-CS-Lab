import xlrd
ExcelFile=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\TestData.xlsx')
print (sheet.cell(1,0).value.encode('utf-8'))
