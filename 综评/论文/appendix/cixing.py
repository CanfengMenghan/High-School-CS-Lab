import jieba.posseg as psg
import xlrd
import xlwt
title=str('创新成果')
ExcelFile=xlrd.open_workbook(title+".xls")
sheet=ExcelFile.sheet_by_name('wordCount')
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
rows_num = sheet.nrows

for i in range (1,rows_num):
    temp = str(sheet.cell(i,0).value)
    worksheet.write(i, 0, label = temp)
    temp =psg.cut(temp)
    count=0
    for w in temp:
        count=count+1
        #print(w.flag)
        worksheet.write(i, count, label = str(w.flag))

workbook.save(title+"1.xls")
