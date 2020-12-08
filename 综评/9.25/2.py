import sys
import importlib
importlib.reload(sys)
import jieba
import jieba.analyse
import xlrd
import xlwt #写入Excel表的库
 
if __name__=="__main__":
 
    wbk = xlwt.Workbook(encoding = 'ascii')
    sheet = wbk.add_sheet("wordCount")#Excel单元格名字
    word_lst = []
    key_list=[]
    for line in open('1.txt'):#1.txt是需要分词统计的文档
 
        item = line.strip('\n\r').split('\t') #制表格切分
        # print item
        tags = jieba.analyse.extract_tags(item[0]) #jieba分词
        for t in tags:
            word_lst.append(t)
 
    word_dict= {}
    with open("wordCount.txt",'w') as wf2: #打开文件
 
        for item in word_lst:
            if item not in word_dict: #统计数量
                word_dict[item] = 1
            else:
                word_dict[item] += 1
 
        orderList=list(word_dict.values())
        orderList.sort(reverse=True)
        # print orderList
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key]==orderList[i]:
                    wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                    key_list.append(key)
                    word_dict[key]=0
    
    
    for i in range(len(key_list)):
        sheet.write(i, 1, label = orderList[i])
        sheet.write(i, 0, label = key_list[i])
    wbk.save('wordCount.xls') #保存为 wordCount.xls文件

ExcelFile1=xlrd.open_workbook(r'C:\Users\tianzhy\Desktop\wordCount.xls')
readoutcampus=ExcelFile1.sheet_by_name('wordCount')
ExcelFile2=xlrd.open_workbook(r'C:\Users\tianzhy\Desktop\提取类目.xlsx')
incampuscategory=ExcelFile2.sheet_by_name('校内')
outcampuscategory=ExcelFile2.sheet_by_name('校外合并')
delete=ExcelFile2.sheet_by_name('删除')

for i in range (0,12):
    temp=0
    print(i)
    for j in range (0,859):
        print(j)
        if str(incampuscategory.cell(i,0).value) in str(readoutcampus.cell(j,0)):
            sheet.write(i, 3, label = str(incampuscategory.cell(i,0).value))
            sheet.write(i, 4, label = readoutcampus.cell(j,1).value+ int(readoutcampus.cell(i,4).value))
        
    
    

sheet.cell(i,7).value
worksheet.write(i, 0, label = str(1))
