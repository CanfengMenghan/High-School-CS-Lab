import pygame, sys # 声明 导入需要的模块

from pygame.locals import *

import time


pygame.init()# 初始化pygame

DISPLAYSURF = pygame.display.set_mode((640,480))# 设置窗口的大小，单位为像素
pygame.display.set_caption('Font')# 设置窗口的标题
DISPLAYSURF.fill([255,255,255])#用白色填充窗口
myimage=pygame.image.load("D:\\ball.jpg")#把变量myimage赋给导入的图片

# 定义几个颜色
WHITE = (255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 128)
status=1

while status==1:
    
    DISPLAYSURF.fill([255,255,255])#用白色填充窗口
    fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 48)# 通过字体文件获得字体对象

    textSurfaceObj1 = fontObj.render('你好', True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj1 = textSurfaceObj1.get_rect()# 获得要显示的对象的rect
    textRectObj1.center = (200, 150)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)# 绘制字体

    textSurfaceObj2 = fontObj.render('开始', True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj2 = textSurfaceObj1.get_rect()# 获得要显示的对象的rect
    textRectObj2.center = (500, 400)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)# 绘制字体

    pygame.display.update()# 绘制屏幕内容

    while status==1:
    
        for event in pygame.event.get():#获得事件
        
            if event.type==pygame.MOUSEBUTTONDOWN and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                print(1)
                DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                status=2
                pygame.display.flip() 
                #做需要做的事情，如开始游戏。
                pass

while status==2:

    correct=0
    currenttime=0
    time0=float(time.time())
    
    DISPLAYSURF.fill([255,255,255])#用白色填充窗口    
    fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 48)# 通过字体文件获得字体对象

    textSurfaceObj3 = fontObj.render('正确', True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj3 = textSurfaceObj3.get_rect()# 获得要显示的对象的rect
    textRectObj3.center = (400, 400)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)# 绘制字体

    textSurfaceObj4 = fontObj.render('跳过', True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj4 = textSurfaceObj4.get_rect()# 获得要显示的对象的rect
    textRectObj4.center = (550, 400)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)# 绘制字体

    textSurfaceObj6 = fontObj.render(str(correct), True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
    textRectObj6.center = (400, 50)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

    textSurfaceObj7 = fontObj.render(str(correct), True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
    textRectObj7.center = (320,240)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

    pygame.display.update()# 绘制屏幕内容

    while currenttime<60:
        pasttime=int(float(time.time())-time0)
       # print(pasttime)
    
        if pasttime!=int(currenttime):
            currenttime=pasttime
            print(pasttime)
            
            textSurfaceObj5 = fontObj.render(str(60-pasttime), True, (0,0,0), (255,255,255))# 配置要显示的文字
            textRectObj5 = textSurfaceObj5.get_rect()# 获得要显示的对象的rect
            textRectObj5.center = (500, 50)# 设置显示对象的坐标
            DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)# 绘制字体
            pygame.display.update()# 绘制屏幕内容

        for event in pygame.event.get():#获得事件
        
            if event.type==pygame.MOUSEBUTTONDOWN and 400<=event.pos[0]<=550 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                print(1)
                correct+=1
                pygame.display.flip() 
                #做需要做的事情，如开始游戏。
                pass
            
                textSurfaceObj6 = fontObj.render(str(correct), True, (0,0,0), (255,255,255))# 配置要显示的文字
                textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
                textRectObj6.center = (400, 50)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

                textSurfaceObj7 = fontObj.render(str(correct), True, (0,0,0), (255,255,255))# 配置要显示的文字
                textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
                textRectObj7.center = (320,240)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

                pygame.display.update()# 绘制屏幕内容

            if event.type==pygame.MOUSEBUTTONDOWN and 550<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                print(1)
                correct-=1
                pygame.display.flip() 
                #做需要做的事情，如开始游戏。
                pass
            
                textSurfaceObj6 = fontObj.render(str(correct), True, (0,0,0), (255,255,255))# 配置要显示的文字
                textRectObj6 = textSurfaceObj6.get_rect()# 获得要显示的对象的rect
                textRectObj6.center = (400, 50)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)# 绘制字体

                textSurfaceObj7 = fontObj.render(str(correct), True, (0,0,0), (255,255,255))# 配置要显示的文字
                textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
                textRectObj7.center = (320,240)# 设置显示对象的坐标
                DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

                pygame.display.update()# 绘制屏幕内容

    status=3

while status==3:
    DISPLAYSURF.fill([255,255,255])#用白色填充窗口    
    fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 48)# 通过字体文件获得字体对象

    textSurfaceObj7 = fontObj.render(str(correct), True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj7 = textSurfaceObj7.get_rect()# 获得要显示的对象的rect
    textRectObj7.center = (320,240)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)# 绘制字体

    textSurfaceObj8 = fontObj.render('重来', True, (0,0,0), (255,255,255))# 配置要显示的文字
    textRectObj8 = textSurfaceObj8.get_rect()# 获得要显示的对象的rect
    textRectObj8.center = (500, 400)# 设置显示对象的坐标
    DISPLAYSURF.blit(textSurfaceObj8, textRectObj8)# 绘制字体

    pygame.display.update()# 绘制屏幕内容

    while status==3:
    
        for event in pygame.event.get():#获得事件
        
            if event.type==pygame.MOUSEBUTTONDOWN and 500<=event.pos[0]<=640 and 400<=event.pos[1]<=480: #判断鼠标位置以及是否摁了下去。
                print(1)
                DISPLAYSURF.blit(myimage,[200,200]) #在100,100的地方画出这个图片（100和100为左部和上部）
                status=1
                pygame.display.flip() 
                #做需要做的事情，如开始游戏。
                pass
