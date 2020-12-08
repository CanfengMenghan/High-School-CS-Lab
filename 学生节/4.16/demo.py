import pygame, sys # 声明 导入需要的模块

from pygame.locals import *

import time

import xlrd

import random

workbook = xlrd.open_workbook("data.xlsx")
sheet = workbook.sheet_by_name("Sheet1")


pygame.init()# 初始化pygame

DISPLAYSURF = pygame.display.set_mode((1360,700))# 设置窗口的大小，单位为像素
pygame.display.set_caption('疯狂猜猜猜')# 设置窗口的标题
DISPLAYSURF.fill([0,74,128])#用白色填充窗口
myimage=pygame.image.load("D:\\ball.jpg")#把变量myimage赋给导入的图片

# 定义几个颜色
WHITE = (255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 128)
status=1

while True:
    while status==1:
     
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口
        fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 96)# 通过字体文件获得字体对象

        textSurfaceObj1 = fontObj.render('疯狂猜猜猜', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj1 = textSurfaceObj1.get_rect()# 获得要显示的对象的rect
        textRectObj1.center = (680, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)# 绘制字体

        fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 36)# 通过字体文件获得字体对象

        describeSurface1 = fontObj.render('本游戏是一个猜词游戏。开始游戏后，屏幕会显示一些词语或诗句。一人在电脑', True, (255,255,255), (0,74,128))# 配置要显示的文字
        describeRect1 = describeSurface1.get_rect()# 获得要显示的对象的rect
        describeRect1.center = (680, 200)# 设置显示对象的坐标
        DISPLAYSURF.blit(describeSurface1, describeRect1)# 绘制字体

        describeSurface2 = fontObj.render('面前描述这个词语，另外一人面对电脑背面，通过描述者的提示猜出屏幕上显示', True, (255,255,255), (0,74,128))# 配置要显示的文字
        describeRect2 = describeSurface2.get_rect()# 获得要显示的对象的rect
        describeRect2.center = (680, 250)# 设置显示对象的坐标
        DISPLAYSURF.blit(describeSurface2, describeRect2)# 绘制字体
        
        describeSurface2 = fontObj.render('的内容。正确则描述者单击鼠标左键。跳过则描述者单击鼠标右键。接下来有', True, (255,255,255), (0,74,128))# 配置要显示的文字
        describeRect2 = describeSurface2.get_rect()# 获得要显示的对象的rect
        describeRect2.center = (680, 300)# 设置显示对象的坐标
        DISPLAYSURF.blit(describeSurface2, describeRect2)# 绘制字体
        
        describeSurface2 = fontObj.render('词库和时长可选。要开始游戏，请在任意位置单击鼠标。', True, (255,255,255), (0,74,128))# 配置要显示的文字
        describeRect2 = describeSurface2.get_rect()# 获得要显示的对象的rect
        describeRect2.center = (680, 350)# 设置显示对象的坐标
        DISPLAYSURF.blit(describeSurface2, describeRect2)# 绘制字体

        pygame.display.update()# 绘制屏幕内容

        while status==1:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN: #and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=4
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass

    while status==4:
        
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口
        fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 48)# 通过字体文件获得字体对象
        
        textSurfaceObj9 = fontObj.render('成语', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
        textRectObj9.center = (680, 175)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

        textSurfaceObj10 = fontObj.render('古诗词', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj10 = textSurfaceObj10.get_rect()# 获得要显示的对象的rect
        textRectObj10.center = (680, 350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj10, textRectObj10)# 绘制字体

        textSurfaceObj11 = fontObj.render('中高考古诗词', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj11 = textSurfaceObj11.get_rect()# 获得要显示的对象的rect
        textRectObj11.center = (680, 525)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)# 绘制字体

        pygame.display.update()# 绘制屏幕内容

        while status==4:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 150<=event.pos[1]<=200: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=4852
                    column=0
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 325<=event.pos[1]<=375: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=3486
                    column=2
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 500<=event.pos[1]<=550: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=1271
                    column=4
                    #做需要做的事情，如开始游戏。
                    pass

    while status==5:
        
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口
        fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 48)# 通过字体文件获得字体对象
        
        textSurfaceObj9 = fontObj.render('60秒', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
        textRectObj9.center = (680, 175)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

        textSurfaceObj10 = fontObj.render('120秒', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj10 = textSurfaceObj10.get_rect()# 获得要显示的对象的rect
        textRectObj10.center = (680, 350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj10, textRectObj10)# 绘制字体

        textSurfaceObj11 = fontObj.render('300秒', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj11 = textSurfaceObj11.get_rect()# 获得要显示的对象的rect
        textRectObj11.center = (680, 525)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)# 绘制字体

        pygame.display.update()# 绘制屏幕内容

        while status==5:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 150<=event.pos[1]<=200: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=2
                    pygame.display.flip()
                    totaltime=60
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 325<=event.pos[1]<=375: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=2
                    pygame.display.flip()
                    totaltime=120
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 500<=event.pos[1]<=550: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=2
                    pygame.display.flip()
                    totaltime=300
                    #做需要做的事情，如开始游戏。
                    pass

    
    while status==2:

        correct=0
        currenttime=0
        time0=float(time.time())
    
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口    
        fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 36)# 通过字体文件获得字体对象
        

        #textSurfaceObj3 = fontObj.render('正确', True, (255,255,255), (0,74,128))# 配置要显示的文字
        #textRectObj3 = textSurfaceObj3.get_rect()# 获得要显示的对象的rect
        #textRectObj3.center = (400, 400)# 设置显示对象的坐标
        #DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)# 绘制字体

        #textSurfaceObj4 = fontObj.render('跳过', True, (255,255,255), (0,74,128))# 配置要显示的文字
        #textRectObj4 = textSurfaceObj4.get_rect()# 获得要显示的对象的rect
        #textRectObj4.center = (550, 400)# 设置显示对象的坐标
        #DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)# 绘制字体'''


        textSurfaceObj6 = fontObj.render("正确数："+str(correct), True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
        textRectObj6.center = (980, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

        fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 96)# 通过字体文件获得字体对象
        number=random.randint(0,total)
        show=sheet.cell_value(number,column)
        textSurfaceObj7 = fontObj.render(str(show), True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
        textRectObj7.center = (680,350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

        pygame.display.update()# 绘制屏幕内容

        while currenttime<totaltime:
            pasttime=int(float(time.time())-time0)
           # print(pasttime)
    
            if pasttime!=int(currenttime):
                currenttime=pasttime
                print(pasttime)

                fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 36)# 通过字体文件获得字体对象
                textSurfaceObj5 = fontObj.render("时间："+str(totaltime-pasttime), True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
                textRectObj5.center = (1180, 50)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体
                pygame.display.update()# 绘制屏幕内容

            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]==1: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    correct+=1
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass

                    DISPLAYSURF.fill([0,74,128])#用白色填充窗口

                    fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 36)# 通过字体文件获得字体对象
                    textSurfaceObj5 = fontObj.render("时间："+str(totaltime-pasttime), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
                    textRectObj5.center = (1180, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体

                    textSurfaceObj6 = fontObj.render("正确数："+str(correct), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
                    textRectObj6.center = (980, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

                    fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 96)# 通过字体文件获得字体对象
                    number=random.randint(0,total)
                    show=sheet.cell_value(number,column)
                    textSurfaceObj7 = fontObj.render(str(show), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
                    textRectObj7.center = (680,350)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

                    pygame.display.update()# 绘制屏幕内容

                if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]==1: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #correct-=1
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass
    
                    DISPLAYSURF.fill([0,74,128])#用白色填充窗口

                    fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 36)# 通过字体文件获得字体对象
                    textSurfaceObj5 = fontObj.render("时间："+str(totaltime-pasttime), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
                    textRectObj5.center = (1180, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体

                    textSurfaceObj6 = fontObj.render("正确数："+str(correct), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
                    textRectObj6.center = (980, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

                    fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 96)# 通过字体文件获得字体对象
                    number=random.randint(0,total)
                    show=sheet.cell_value(number,column)
                    textSurfaceObj7 = fontObj.render(str(show), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
                    textRectObj7.center = (680,350)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

                    pygame.display.update()# 绘制屏幕内容

        status=3

    while status==3:
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口    
        fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 96)# 通过字体文件获得字体对象

        textSurfaceObj7 = fontObj.render("正确数："+str(correct), True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
        textRectObj7.center = (680,350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

        #textSurfaceObj8 = fontObj.render('重来', True, (255,255,255), (0,74,128))# 配置要显示的文字
        #textRectObj8 = textSurfaceObj8.get_rect()# 获得要显示的对象的rect
        #textRectObj8.center = (500, 400)# 设置显示对象的坐标
        #DISPLAYSURF.blit(textSurfaceObj8, textRectObj8)# 绘制字体

        pygame.display.update()# 绘制屏幕内容

        while status==3:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN: #判断鼠标位置以及是否摁了下去。
                    print(1)
                    DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=1
                    pygame.display.flip() 
                #做需要做的事情，如开始游戏。
                    pass
