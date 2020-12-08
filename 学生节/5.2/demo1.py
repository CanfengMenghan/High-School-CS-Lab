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
#myimage=pygame.image.load("D:\\ball.jpg")#把变量myimage赋给导入的图片

# 定义几个颜色
WHITE = (255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 128)
status=1

while True:
    while status==1:
     
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口
        fontObj = pygame.font.Font('SIMYOU.TTF', 96)# 通过字体文件获得字体对象

        textSurfaceObj1 = fontObj.render('疯狂猜猜猜', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj1 = textSurfaceObj1.get_rect()# 获得要显示的对象的rect
        textRectObj1.center = (680, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)# 绘制字体

        fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象
        
        describeSurface2 = fontObj.render('要开始游戏，请在任意位置左键单击。要开始教学，请右键单击。', True, (255,255,255), (0,74,128))# 配置要显示的文字
        describeRect2 = describeSurface2.get_rect()# 获得要显示的对象的rect
        describeRect2.center = (680, 650)# 设置显示对象的坐标
        DISPLAYSURF.blit(describeSurface2, describeRect2)# 绘制字体

        myimage=pygame.image.load("untitled.png")#把变量myimage赋给导入的图片
        myimage1 = myimage.get_rect()# 获得要显示的对象的rect
        myimage1.center = (680, 350)# 设置显示对象的坐标
        DISPLAYSURF.blit(myimage,myimage1) #在100,100的地方画出这个图片（100和100为左部和上部）

        pygame.display.update()# 绘制屏幕内容

        while status==1:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]==1: #and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=4
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]==1:  #and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=6
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type == pygame.QUIT:
                    pygame.quit()


    while status==6:

        DISPLAYSURF.fill([0,74,128])#用白色填充窗口    
        fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象

        textSurfaceObj6 = fontObj.render("正确数：0", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
        textRectObj6.center = (980, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

        textSurfaceObj9 = fontObj.render("退出", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
        textRectObj9.center = (1310, 675)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

        textSurfaceObj5 = fontObj.render("时间：0", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
        textRectObj5.center = (1180, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体

        fontObj = pygame.font.Font('SIMYOU.TTF', 80)# 通过字体文件获得字体对象
        textSurfaceObj7 = fontObj.render("左键单击表示正确,请单击以继续", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
        textRectObj7.center = (680,350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

        

        pygame.display.update()# 绘制屏幕内容

        while status==6:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]==1: #and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=7
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass

    while status==7:

        DISPLAYSURF.fill([0,74,128])#用白色填充窗口    
        fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象

        textSurfaceObj6 = fontObj.render("正确数：1", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
        textRectObj6.center = (980, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

        textSurfaceObj9 = fontObj.render("退出", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
        textRectObj9.center = (1310, 675)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

        textSurfaceObj5 = fontObj.render("时间：0", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
        textRectObj5.center = (1180, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体

        fontObj = pygame.font.Font('SIMYOU.TTF', 80)# 通过字体文件获得字体对象
        textSurfaceObj7 = fontObj.render("右键单击表示跳过,请单击以继续", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
        textRectObj7.center = (680,350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

        

        pygame.display.update()# 绘制屏幕内容

        while status==7:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]==1: #and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=8
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass

    while status==8:

        DISPLAYSURF.fill([0,74,128])#用白色填充窗口    
        fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象

        textSurfaceObj6 = fontObj.render("正确数：1", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
        textRectObj6.center = (980, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

        textSurfaceObj9 = fontObj.render("退出", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
        textRectObj9.center = (1310, 675)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

        textSurfaceObj5 = fontObj.render("时间：0", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
        textRectObj5.center = (1180, 50)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体


        fontObj = pygame.font.Font('SIMYOU.TTF', 80)# 通过字体文件获得字体对象
        textSurfaceObj7 = fontObj.render("右上角有时间与正确数，请单击以继续", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
        textRectObj7.center = (680,350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

        
        pygame.display.update()# 绘制屏幕内容

        while status==8:
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN: #and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=1
                    pygame.display.flip() 
                    #做需要做的事情，如开始游戏。
                    pass



    while status==4:

        currenttime=0
        time0=float(time.time())
        
        
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口
        fontObj = pygame.font.Font('SIMYOU.TTF', 48)# 通过字体文件获得字体对象
        
        textSurfaceObj9 = fontObj.render('成语', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
        textRectObj9.center = (907, 175)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

        textSurfaceObj10 = fontObj.render('古诗词', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj10 = textSurfaceObj10.get_rect()# 获得要显示的对象的rect
        textRectObj10.center = (907, 350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj10, textRectObj10)# 绘制字体

        textSurfaceObj11 = fontObj.render('中高考古诗词', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj11 = textSurfaceObj11.get_rect()# 获得要显示的对象的rect
        textRectObj11.center = (907, 525)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)# 绘制字体

        textSurfaceObj12 = fontObj.render('初中理化', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
        textRectObj12.center = (453, 525)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体

        textSurfaceObj12 = fontObj.render('世界地名', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
        textRectObj12.center = (453, 175)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体

        textSurfaceObj12 = fontObj.render('论语集锦', True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
        textRectObj12.center = (453, 350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体



        pygame.display.update()# 绘制屏幕内容

        while status==4:
            pasttime=int(float(time.time())-time0)

            if pasttime!=int(currenttime) and int(currenttime)%2==0:
                currenttime=pasttime
                #print(pasttime)

                textSurfaceObj9 = fontObj.render('成语', True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
                textRectObj9.center = (907, 175)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

                textSurfaceObj10 = fontObj.render('古诗词', True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj10 = textSurfaceObj10.get_rect()# 获得要显示的对象的rect
                textRectObj10.center = (907, 350)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj10, textRectObj10)# 绘制字体

                textSurfaceObj11 = fontObj.render('中高考古诗词', True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj11 = textSurfaceObj11.get_rect()# 获得要显示的对象的rect
                textRectObj11.center = (907, 525)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)# 绘制字体

                textSurfaceObj12 = fontObj.render('初中理化', True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
                textRectObj12.center = (453, 525)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体

                textSurfaceObj12 = fontObj.render('世界地名', True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
                textRectObj12.center = (453, 175)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体

                textSurfaceObj12 = fontObj.render('论语集锦', True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
                textRectObj12.center = (453, 350)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体



                pygame.display.update()# 绘制屏幕内容

            if pasttime!=int(currenttime) and int(currenttime)%2==1:
                currenttime=pasttime
                #print(pasttime)

                textSurfaceObj9 = fontObj.render('成语', True, (255,0,0), (0,74,128))# 配置要显示的文字
                textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
                textRectObj9.center = (907, 175)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

                textSurfaceObj10 = fontObj.render('古诗词', True, (255,0,0), (0,74,128))# 配置要显示的文字
                textRectObj10 = textSurfaceObj10.get_rect()# 获得要显示的对象的rect
                textRectObj10.center = (907, 350)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj10, textRectObj10)# 绘制字体

                textSurfaceObj11 = fontObj.render('中高考古诗词', True, (255,0,0), (0,74,128))# 配置要显示的文字
                textRectObj11 = textSurfaceObj11.get_rect()# 获得要显示的对象的rect
                textRectObj11.center = (907, 525)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)# 绘制字体

                textSurfaceObj12 = fontObj.render('初中理化', True, (255,0,0), (0,74,128))# 配置要显示的文字
                textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
                textRectObj12.center = (453, 525)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体

                textSurfaceObj12 = fontObj.render('世界地名', True, (255,0,0), (0,74,128))# 配置要显示的文字
                textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
                textRectObj12.center = (453, 175)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体

                textSurfaceObj12 = fontObj.render('论语集锦', True, (255,0,0), (0,74,128))# 配置要显示的文字
                textRectObj12 = textSurfaceObj12.get_rect()# 获得要显示的对象的rect
                textRectObj12.center = (453, 350)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)# 绘制字体



                pygame.display.update()# 绘制屏幕内容
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN and 957>=event.pos[0]>=857 and 150<=event.pos[1]<=200: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=4852
                    column=0
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 957>=event.pos[0]>=857 and 325<=event.pos[1]<=375: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=3486
                    column=2
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 957>=event.pos[0]>=857 and 500<=event.pos[1]<=550: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=1271
                    column=4
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 503>=event.pos[0]>=403 and 150<=event.pos[1]<=200: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=860
                    column=8
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 503>=event.pos[0]>=403 and 325<=event.pos[1]<=375: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=2906
                    column=10
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 503>=event.pos[0]>=403 and 500<=event.pos[1]<=550: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=5
                    pygame.display.flip()
                    total=330
                    column=6
                    #做需要做的事情，如开始游戏。
                    pass
                
                if event.type == pygame.QUIT:
                    pygame.quit()

    while status==5:
        
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口
        fontObj = pygame.font.Font('SIMYOU.TTF', 48)# 通过字体文件获得字体对象
        
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
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=2
                    pygame.display.flip()
                    totaltime=60
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 325<=event.pos[1]<=375: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=2
                    pygame.display.flip()
                    totaltime=120
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type==pygame.MOUSEBUTTONDOWN and 630<=event.pos[0]<=730 and 500<=event.pos[1]<=550: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=2
                    pygame.display.flip()
                    totaltime=300
                    #做需要做的事情，如开始游戏。
                    pass

                if event.type == pygame.QUIT:
                    pygame.quit()

    
    while status==2:

        correct=0
        currenttime=0
        time0=float(time.time())
    
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口    
        fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象
        

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

        textSurfaceObj9 = fontObj.render("退出", True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
        textRectObj9.center = (1310, 675)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

        fontObj = pygame.font.Font('SIMYOU.TTF', 96)# 通过字体文件获得字体对象
        number=random.randint(0,total)
        show=sheet.cell_value(number,column)
        textSurfaceObj7 = fontObj.render(str(show), True, (255,255,255), (0,74,128))# 配置要显示的文字
        textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
        textRectObj7.center = (680,350)# 设置显示对象的坐标
        DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

        pygame.display.update()# 绘制屏幕内容

        while currenttime<totaltime and status==2:
            pasttime=int(float(time.time())-time0)
           # print(pasttime)
    
            if pasttime!=int(currenttime):
                currenttime=pasttime
                #print(pasttime)

                fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象
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

                    fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象
                    textSurfaceObj5 = fontObj.render("时间："+str(totaltime-pasttime), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
                    textRectObj5.center = (1180, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体

                    textSurfaceObj6 = fontObj.render("正确数："+str(correct), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
                    textRectObj6.center = (980, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

                    textSurfaceObj9 = fontObj.render("退出", True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
                    textRectObj9.center = (1310, 675)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

                    fontObj = pygame.font.Font('SIMYOU.TTF', 96)# 通过字体文件获得字体对象
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

                    fontObj = pygame.font.Font('SIMYOU.TTF', 36)# 通过字体文件获得字体对象
                    textSurfaceObj5 = fontObj.render("时间："+str(totaltime-pasttime), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
                    textRectObj5.center = (1180, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体

                    textSurfaceObj6 = fontObj.render("正确数："+str(correct), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
                    textRectObj6.center = (980, 50)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

                    textSurfaceObj9 = fontObj.render("退出", True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj9 = textSurfaceObj9.get_rect()# 获得要显示的对象的rect
                    textRectObj9.center = (1310, 675)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)# 绘制字体

                    fontObj = pygame.font.Font('SIMYOU.TTF', 96)# 通过字体文件获得字体对象
                    number=random.randint(0,total)
                    show=sheet.cell_value(number,column)
                    textSurfaceObj7 = fontObj.render(str(show), True, (255,255,255), (0,74,128))# 配置要显示的文字
                    textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
                    textRectObj7.center = (680,350)# 设置显示对象的坐标
                    DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

                    pygame.display.update()# 绘制屏幕内容

                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type==pygame.MOUSEBUTTONDOWN and 1260<=event.pos[0]<=1360 and 650<=event.pos[1]<=700: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=3
                    correct=correct-pygame.mouse.get_pressed()[0]
                    pygame.display.flip()
                    pass

        status=3

    while status==3:
        DISPLAYSURF.fill([0,74,128])#用白色填充窗口    
        fontObj = pygame.font.Font('SIMYOU.TTF', 96)# 通过字体文件获得字体对象

        currenttime=0
        time0=float(time.time())

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

            pasttime=int(float(time.time())-time0)

            if pasttime!=int(currenttime) and int(currenttime)%2==0:
                currenttime=pasttime

                textSurfaceObj7 = fontObj.render("正确数："+str(correct), True, (255,0,0), (0,74,128))# 配置要显示的文字
                textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
                textRectObj7.center = (680,350)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体
                
                pygame.display.update()# 绘制屏幕内容

            if pasttime!=int(currenttime) and int(currenttime)%2==1:
                currenttime=pasttime

                textSurfaceObj7 = fontObj.render("正确数："+str(correct), True, (255,255,255), (0,74,128))# 配置要显示的文字
                textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
                textRectObj7.center = (680,350)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体
                pygame.display.update()# 绘制屏幕内容

    
    
            for event in pygame.event.get():#获得事件
        
                if event.type==pygame.MOUSEBUTTONDOWN: #判断鼠标位置以及是否摁了下去。
                    #print(1)
                    #DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                    status=1
                    pygame.display.flip() 
                #做需要做的事情，如开始游戏。
                    pass

                if event.type == pygame.QUIT:
                    pygame.quit()
