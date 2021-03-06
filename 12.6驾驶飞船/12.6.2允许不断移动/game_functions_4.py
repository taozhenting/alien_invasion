import sys
import pygame

#包含了形参ship，现在不做移动，标志moving_right为True或Flase
def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #pygame检测到KEYDOWN事件时做出响应
        elif event.type == pygame.KEYDOWN:
            #读取属性event.key，检查按下是否右箭头(pygame.K_RIGHT)
            if event.key == pygame.K_RIGHT:
                #按下右箭头不直接移动，而是将moving_right设置为True
                ship.moving_right = True
            #响应KEYUP事件
        elif event.type == pygame.KEYUP:
            #松开的是右箭头
            if event.key == pygame.K_RIGHT:
                #将moving_right设置为False
                ship.moving_right = False

def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()