import pygame, sys # 声明 导入需要的模块

from pygame.locals import *

import time

pygame.init()# 初始化pygame

DISPLAYSURF = pygame.display.set_mode((400,300))# 设置窗口的大小，单位为像素

pygame.display.set_caption('Font')# 设置窗口的标题


# 定义几个颜色
WHITE = (255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 128)


fontObj = pygame.font.Font('C:\Windows\Fonts\simkai.ttf', 48)# 通过字体文件获得字体对象

textSurfaceObj = fontObj.render('你好', True, (0,0,0), (255,255,255))# 配置要显示的文字

textRectObj = textSurfaceObj.get_rect()# 获得要显示的对象的rect

textRectObj.center = (200, 150)# 设置显示对象的坐标

DISPLAYSURF.fill((255,255,255))# 设置背景

DISPLAYSURF.blit(textSurfaceObj, textRectObj)# 绘制字体

pygame.display.update()# 绘制屏幕内容


time0=float(time.time())
currenttime=0
while True:
    pasttime=int(float(time.time())-time0)
       # print(pasttime)
    
    if pasttime!=int(currenttime):
        currenttime=pasttime
        print(pasttime)
        textSurfaceObj = fontObj.render(str(60-pasttime), True, (0,0,0), (255,255,255))# 配置要显示的文字

        textRectObj = textSurfaceObj.get_rect()# 获得要显示的对象的rect

        textRectObj.center = (200, 150)# 设置显示对象的坐标

        DISPLAYSURF.fill((255,255,255))# 设置背景

        DISPLAYSURF.blit(textSurfaceObj, textRectObj)# 绘制字体

        pygame.display.update()# 绘制屏幕内容
