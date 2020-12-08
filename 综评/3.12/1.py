import xlrd
import xlwt
workbook = xlrd.open_workbook(r'艺术类实践活动.xlsx')
sheet1 = workbook.sheet_by_name('Sheet1')
test=['合唱节','艺术节','电声乐']

for i in range (0,len(test)):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Worksheet')
    count=0
    for j in range (0,555):
        string=str(sheet1.cell(j,0).value)
        result = string.find(test[i])
        if int(result)!=int(-1):
            worksheet.write(count, 0, label = str(sheet1.cell(j,0).value))
            worksheet.write(count, 1, label = str(sheet1.cell(j,1).value))
            count+=1
    tempname=str(test[i])+".xls"
    workbook.save(tempname)
