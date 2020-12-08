from snownlp import SnowNLP
import xlrd
import xlwt

name=["体育类实践活动","创新成果","游学经历","社团活动","艺术成果展示","艺术类实践活动"]

for j in range(0,6):
    tempname="附中G17级2018.2-9 指定维度的记录数据/"+name[j]+".xlsx"
    ExcelFile=xlrd.open_workbook(tempname)
    sheet=ExcelFile.sheet_by_name('Sheet1')
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    rows_num = sheet.nrows

    for i in range (1,rows_num):
        temp = str(sheet.cell(i,0).value)
        s = SnowNLP(temp)
        sentiment=s.sentiments
        worksheet.write(i, 0, label = str(sentiment))

    tempname="附中G17级2018.2-9 指定维度的记录数据/情感/"+name[j]+"Excel_Workbook.xls"
    workbook.save(tempname)
    
    
