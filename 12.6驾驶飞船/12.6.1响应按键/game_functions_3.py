import sys
import pygame

#包含了形参ship，因为玩家按右箭头时，需要将飞船向右移动。
def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #pygame检测到KEYDOWN事件时做出响应
        elif event.type == pygame.KEYDOWN:
            #读取属性event.key，检查按下是否右箭头(pygame.K_RIGHT)
            if event.key == pygame.K_RIGHT:
                #向右移动飞船
                #将ship.rect.centerx的值加1，从而将飞船向右移动
                ship.rect.centerx += 1

def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()