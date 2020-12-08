import jieba
import numpy as np
import xlrd
import xlwt



def open_dict(Dict = 'hahah', path=r'D:\学习\学习\高中\学校事情\高二\高研\论文\appendix\Textming'):
    path = path + '%s.txt' % Dict
    dictionary = open(path, 'r', encoding='utf-8')
    dict = []
    for word in dictionary:
        word = word.strip('\n')
        dict.append(word)
    return dict



def judgeodd(num):
    if (num % 2) == 0:
        return 'even'
    else:
        return 'odd'



deny_word = open_dict(Dict = 'deny_word', path= r'')
posdict = open_dict(Dict = 'positive', path= r'')
negdict = open_dict(Dict = 'negative', path= r'')

degree_word = open_dict(Dict = 'degree_word', path= r'')
mostdict = degree_word[degree_word.index('extreme')+1 : degree_word.index('very')]
verydict = degree_word[degree_word.index('very')+1 : degree_word.index('more')]
moredict = degree_word[degree_word.index('more')+1 : degree_word.index('ish')]
ishdict = degree_word[degree_word.index('ish')+1 : degree_word.index('last')]



def sentiment_score_list(dataset):
    seg_sentence = dataset.split('。')

    count1 = []
    count2 = []
    for sen in seg_sentence: 
        segtmp = jieba.lcut(sen, cut_all=False)  
        i = 0 
        a = 0 
        poscount = 0 
        poscount2 = 0 
        poscount3 = 0 
        negcount = 0
        negcount2 = 0
        negcount3 = 0
        for word in segtmp:
            if word in posdict:  
                poscount += 1
                c = 0
                for w in segtmp[a:i]:  
                    if w in mostdict:
                        poscount *= 4.0
                    elif w in verydict:
                        poscount *= 3.0
                    elif w in moredict:
                        poscount *= 2.0
                    elif w in ishdict:
                        poscount *= 0.5
                    elif w in deny_word:
                        c += 1
                if judgeodd(c) == 'odd':  
                    poscount *= -1.0
                    poscount2 += poscount
                    poscount = 0
                    poscount3 = poscount + poscount2 + poscount3
                    poscount2 = 0
                else:
                    poscount3 = poscount + poscount2 + poscount3
                    poscount = 0
                a = i + 1  

            elif word in negdict: 
                negcount += 1
                d = 0
                for w in segtmp[a:i]:
                    if w in mostdict:
                        negcount *= 4.0
                    elif w in verydict:
                        negcount *= 3.0
                    elif w in moredict:
                        negcount *= 2.0
                    elif w in ishdict:
                        negcount *= 0.5
                    elif w in degree_word:
                        d += 1
                if judgeodd(d) == 'odd':
                    negcount *= -1.0
                    negcount2 += negcount
                    negcount = 0
                    negcount3 = negcount + negcount2 + negcount3
                    negcount2 = 0
                else:
                    negcount3 = negcount + negcount2 + negcount3
                    negcount = 0
                a = i + 1
            elif word == '！' or word == '!': 
                for w2 in segtmp[::-1]: 
                    if w2 in posdict or negdict:
                        poscount3 += 2
                        negcount3 += 2
                        break
            i += 1 


            
            pos_count = 0
            neg_count = 0
            if poscount3 < 0 and negcount3 > 0:
                neg_count += negcount3 - poscount3
                pos_count = 0
            elif negcount3 < 0 and poscount3 > 0:
                pos_count = poscount3 - negcount3
                neg_count = 0
            elif poscount3 < 0 and negcount3 < 0:
                neg_count = -poscount3
                pos_count = -negcount3
            else:
                pos_count = poscount3
                neg_count = negcount3

            count1.append([pos_count, neg_count])
        count2.append(count1)
        count1 = []

    return count2

def sentiment_score(senti_score_list):
    score = []
    for review in senti_score_list:
        score_array = np.array(review)
        Pos = np.sum(score_array[:, 0])
        Neg = np.sum(score_array[:, 1])
        AvgPos = np.mean(score_array[:, 0])
        AvgPos = float('%.1f'%AvgPos)
        AvgNeg = np.mean(score_array[:, 1])
        AvgNeg = float('%.1f'%AvgNeg)
        StdPos = np.std(score_array[:, 0])
        StdPos = float('%.1f'%StdPos)
        StdNeg = np.std(score_array[:, 1])
        StdNeg = float('%.1f'%StdNeg)
        score.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return score

name=["体育类实践活动","创新成果","游学经历","社团活动","艺术成果展示","艺术类实践活动"]

for j in range(0,6):
    tempname="内容/"+name[j]+".xlsx"
    ExcelFile=xlrd.open_workbook(tempname)
    sheet=ExcelFile.sheet_by_name('Sheet1')
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    rows_num = sheet.nrows

    for i in range (1,rows_num):
        temp = str(sheet.cell(i,0).value)
        #print(i)
        s = sentiment_score(sentiment_score_list(temp))
        length=len(s[0])
        positiv=0
        negativ=0
        for k in range (0,length,2):
            positiv=positiv+s[0][k]
        for k in range (1,length+1,2):
            negativ=negativ+s[0][k]
        worksheet.write(i, 0, label = str(positiv))
        worksheet.write(i, 1, label = str(negativ))

    tempname="内容/正负分/"+name[j]+"Excel_Workbook.xls"
    workbook.save(tempname)
