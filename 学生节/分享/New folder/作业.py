
# -*- coding:utf-8 -*-  
import sys 
 
import pygame 
from pygame.locals import *
from sys import exit

#初始化pygame，为使用硬件做准备  
pygame.init()

#定义背景图像和鼠标图像名称
#background_image_filename = "background.jpg" 
#mouse_image_filename = "object.jpg"  
screen_size = (640, 480)   
  
#创建一个窗口  
screen = pygame.display.set_mode(screen_size, 0, 32)  
#设置窗口标题  
pygame.display.set_caption("Hello, World!") 

#加载图片  
#background = pygame.image.load(background_image_filename).convert()  
#mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()  


    

def play_ball(): 
     
     #窗口大小  
    window_size = (width, height) =(640, 480)
    
    #小球运行偏移量[水平，垂直]，值越大，移动越快  
    speed = [1, 1] 
     
     
     
    #设置窗口模式  
    screen = pygame.display.set_mode(window_size) 
     
    
     
    #加载小球图片  
    ball_image = pygame.image.load('ball.jpg') 
    ban_image = pygame.image.load('object.jpg') 
    #获取小球图片的区域开状  
    ball_rect = ball_image.get_rect() 
    ban_rect=ban_image.get_rect()
    ban_rect.top=280
    ball_rect.left=0
    ball_rect.top=0
    color_b=(0,0,90)
    
    while True:
     if ball_rect.bottom == 480:
            pygame.quit()
            sys.exit()
     screen.fill(color_b)
     for event in pygame.event.get():
        #添加背景图像  
        #screen.blit(background, (0, 0))  
        #获取鼠标位置，并且移到图像中心  
        y = pygame.mouse.get_pos()
        #添加鼠标图像
        
        if (event.type==pygame.QUIT ):
            pygame.quit()
            sys.exit()
        #更新窗口内容
     ban_rect.left=y[0] 
     ball_rect = ball_rect.move(speed)
     screen.blit(ban_image,ban_rect)
     screen.blit(ball_image, ball_rect)
     pygame.display.update()


    
        #使小球移动，速度由speed变量控制  
         
        #当小球运动出窗口时，重新设置偏移量  
     if (ball_rect.left < 0) or (ball_rect.right > width): 
            speed[0] =- speed[0] 
     if (ball_rect.top < 0) or (ball_rect.bottom > height ) : 
            speed[1] =- speed[1]
            
     if (ball_rect.bottom == ban_rect.top):
            if (ball_rect.right > ban_rect.left and ball_rect.left < ban_rect.right):
                speed[1] =- speed[1]

    

        #77
         
        #在背景Surface上绘制 小球  
        
         

     #更新窗口内容  
     pygame.display.update()

         
         


 
if __name__ == '__main__': 
    play_ball() 


