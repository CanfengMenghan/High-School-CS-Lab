import xlrd
import xlwt
ExcelFile=xlrd.open_workbook(r'C:\Users\tianzhy\Desktop\sumai.xlsx')
sheet=ExcelFile.sheet_by_name('速卖')
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
for i in range (1,2291):
    temp = sheet.cell(i,5).value
    temp = temp.split('|')
    length=len(temp)
    count=0
    for j in range (0,length):
        if temp[j]=='Adventure'or temp[j]=='xiaomi'or temp[j]=='XIAOMI':
            worksheet.write(i, 0, label = 1)
        '''
        else:
            worksheet.write(i, 0, label = 0)
        '''
        if temp[j]=='Animation'or temp[j]=='HUAWEI'or temp[j]=='huawei':
            worksheet.write(i, 1, label = 1)
        else:
            worksheet.write(i, 1, label = 0)
        if temp[j]=='Children'or temp[j]=='meizu'or temp[j]=='Meizu':
            worksheet.write(i, 2, label = 1)
        else:
            worksheet.write(i, 2, label = 0)
        if temp[j]=='Comedy'or temp[j]=='Lenovo'or temp[j]=='lenovo':
            worksheet.write(i, 3, label = 1)
        else:
            worksheet.write(i, 3, label = 0)
        if temp[j]=='Fantasy'or temp[j]=='iphone'or temp[j]=='iPhone':
            worksheet.write(i, 4, label = 1)
        else:
            worksheet.write(i, 4, label = 0)
        if temp[j]=='Romance'or temp[j]=='Oppo'or temp[j]=='oppo':
            worksheet.write(i, 5, label = 1)
        else:
            worksheet.write(i, 5, label = 0)
        if temp[j]=='Drama'or temp[j]=='vivo'or temp[j]=='VIVO':
            worksheet.write(i, 6, label = 1)
        else:
            worksheet.write(i, 6, label = 0)
        if temp[j]=='Action'or temp[j]=='NUBIA'or temp[j]=='nubia':
            worksheet.write(i, 7, label = 1)
        else:
            worksheet.write(i, 7, label = 0)
        if temp[j]=='Crime'or temp[j]=='Samsung'or temp[j]=='SAMSUNG':
            worksheet.write(i, 8, label = 1)
        else:
            worksheet.write(i, 8, label = 0)
        if temp[j]=='Thriller'or temp[j]=='zte':
            worksheet.write(i, 9, label = 1)
        else:
            worksheet.write(i, 9, label = 0)
        if temp[j]=='Horror'or temp[j]=='homtom'or temp[j]=='Homtom':
            worksheet.write(i, 10, label = 1)
        else:
            worksheet.write(i, 10, label = 0)
        if temp[j]=='Mystery'or temp[j]=='Doogee'or temp[j]=='doogee':
            worksheet.write(i, 11, label = 1)
        else:
            worksheet.write(i, 11, label = 0)
        if temp[j]=='Sci-Fi'or temp[j]=='LeTv'or temp[j]=='letv' or temp[j]=='LETV':
            worksheet.write(i, 12, label = 1)
        else:
            worksheet.write(i, 12, label = 0)
        if temp[j]=='Musical'or temp[j]=='BLACKVIEW'or temp[j]=='blackview':
            worksheet.write(i, 13, label = 1)
        else:
            worksheet.write(i, 13, label = 0)
        if temp[j]=='Documentary'or temp[j]=='Nokia'or temp[j]=='nokia':
            worksheet.write(i, 14, label = 1)
        else:
            worksheet.write(i, 14, label = 0)
        if temp[j]=='War'or temp[j]=='Nokia'or temp[j]=='nokia':
            worksheet.write(i, 15, label = 1)
        else:
            worksheet.write(i, 15, label = 0)

workbook.save('Excel_Workbook.xls')
