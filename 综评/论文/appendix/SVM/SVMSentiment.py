#encoding=utf-8
# _*_ coding:utf-8 _*_
import time
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from sklearn import cross_validation
from sklearn import metrics
import jieba
from jieba import analyse
jieba.load_userdict("./data/ntusd-negative.txt")
jieba.load_userdict("./data/neg_basic.txt")
jieba.load_userdict("./data/ntusd-positive.txt")
jieba.load_userdict("./data/pos_basic.txt")


def timeDecor(func):
    def innerDef(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        t = t2-t1
        print ("{0}函数部分运行时间：{1}s".format(str(func.__name__),t))  #下划线是两个
        return result
    return innerDef

# 支持向量机SVM分类器
@timeDecor
def svm_classify(X_train, y_train, X_test, y_test):
    from sklearn import svm
    print ("************************\n SVM\n************************")
    # param_grid = {
    #     # 'C': [1e3, 5e3, 1e4, 5e4, 1e5],
    #     'kernel': ['rbf', 'linear', 'poly', 'sigmoid']
    #     # 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
    # }
    t0 = time.time()
    clf = svm.SVC()
    clf.fit(X_train, y_train)

    print("svm done in %0.3fs" % (time.time()-t0))
    pre_y_test = clf.predict(X_test)
    print("SVM Metrics: {0}".format(precision_recall_fscore_support(y_test, pre_y_test)))
    print(metrics.classification_report(y_test, pre_y_test))
    print("accurary\t"+str(np.mean(pre_y_test == y_test)))

# 朴素贝叶斯分类器
@timeDecor
def nb_classify(X_train, y_train, X_test, y_test):
    from sklearn.naive_bayes import GaussianNB
    print("************************\n NB\n************************")
    t0 = time.time()
    clf = GaussianNB()
    clf.fit(X_train, y_train)

    print("nb done in %0.3fs" % (time.time()-t0))
    pre_y_test = clf.predict(X_test)
    print("nb Metrics: {0}".format(precision_recall_fscore_support(y_test, pre_y_test)))
    print(metrics.classification_report(y_test, pre_y_test))
    print("accurary\t"+str(np.mean(pre_y_test == y_test)))

def extractFeatures():
    tpk = 250
    rt = 1.5
    path = './data/'
    file1 = open(path+'pos_'+ strs +'.txt', 'rb')
    data = file1.read()
    w1={}
    for w in sorted(analyse.extract_tags(data,withWeight=True,topK=tpk),key=lambda d:d[1], reverse=True):
        w1[w[0]] = w[1]

    file2 = open(path+'neg_'+ strs +'.txt', 'rb')
    data = file2.read()
    w2={}
    for w in sorted(analyse.extract_tags(data,withWeight=True,topK=tpk),key=lambda d:d[1],reverse=True):
        w2[w[0]]=w[1]


    wtp=[]
    for w in w1:
        if not w in w2:
            pass
        else:
            f=True
            if w2[w]*rt>w1[w]:
                f=False
            if f:
                wtp.append(w)
    w11=wtp

    wtp=[]
    for w in w2:
        if not w in w1:
            pass
        else:
            f=True
            if w in w1:
                if w1[w]*rt>w2[w]:
                    f=False
            if f:
                wtp.append(w)
    w22=wtp


    tow = open(path+'keywords_'+ strs +'.txt', 'wb')
    for w in w11:
        tow.write(w.encode("utf-8")+b" ")
    for w in w22:
        tow.write(w.encode("utf-8")+b" ")



# strs = "hotel"
strs = "book"
# strs = "elec"
extractFeatures()

worddt={}

for line in open("./data/ntusd-positive.txt",encoding='UTF-8'):
    worddt[line.strip()] = 0.5
for line in open("./data/ntusd-negative.txt",encoding='UTF-8'):
    worddt[line.strip()] = -0.5
for line in open("./data/pos_basic.txt",encoding='UTF-8'):
    worddt[line.strip()] = 0.5
for line in open("./data/neg_basic.txt",encoding='UTF-8'):
    worddt[line.strip()] = -0.5
linenum = 0
for line in open("./data/keywords_"+ strs +".txt",encoding='UTF-8'):
    linenum+=1
    if linenum == 1:
        for w in line.split():
            worddt[w] = 0.5
    else:
        for w in line.split():
            worddt[w] = -0.5


onehotlen=len(worddt)
wordindex={}
for i,key in enumerate(worddt):
    wordindex[key]=i

keyword_feature=[]
onehotfeature=[]
onehotvalue=[]
c = 0
for i,line in enumerate(open("./data/pos_"+ strs +".txt",encoding='UTF-8')):
    temp=[0]*(onehotlen+2)
    for word in jieba.cut(line.strip()):
        if word in worddt:
            c+=1
            temp[wordindex[word]] = 1
            if worddt[word] > 0:
                temp[-2] += 1
            elif worddt[word] < 0:
                temp[-1] += 1

    onehotfeature.append(temp[:])
    onehotvalue.append(1)
    if i>1000:
        break

for i,line in enumerate(open("./data/neg_"+ strs +".txt",encoding='UTF-8')):
    temp = [0] * (onehotlen + 2)
    for word in jieba.cut(line.strip()):
        if word in worddt:
            c+=1
            temp[wordindex[word]] = 1
            if worddt[word] > 0:
                temp[-2] += 1
            elif worddt[word] < 0:
                temp[-1] += 1

    onehotfeature.append(temp[:])
    onehotvalue.append(-1)
    if i>1000:
        break



X = onehotfeature
y = onehotvalue
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)
svm_classify(X_train, y_train, X_test, y_test)
nb_classify(X_train, y_train, X_test, y_test)
