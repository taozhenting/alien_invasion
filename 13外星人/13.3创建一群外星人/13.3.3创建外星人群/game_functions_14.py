import sys
import pygame

from bullet_1 import Bullet
from alien_1 import Alien

#编组bullets传递给了check_keydown_events()
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    # 读取属性event.key，检查按下是否右箭头(pygame.K_RIGHT)
    if event.key == pygame.K_RIGHT:
        # 按下右箭头不直接移动，而是将moving_right设置为True
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    #按q键退出
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 将moving_right设置为False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

#添加形参bullets
def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # pygame检测到KEYDOWN事件时做出响应
        elif event.type == pygame.KEYDOWN:
            #调用check_keydown_events时，需要将bullets作为实参传递给它
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        # 响应KEYUP事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

#在屏幕上绘制子弹的update_screen()添加了形参bullets
def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    #方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵(子弹)
    #为在屏幕上绘制发射的所有子弹，我们遍历编组bullets中的精灵
    for bullet in bullets.sprites():
        #并对每个精灵调用draw_bullet()
        bullet.draw_bullet()
    ship.blitme()
    #对编组调用draw()时，pygame自动绘制编组的每个元素
    #绘制位置由元素的属性rect决定。
    aliens.draw(screen)
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        #检查每颗子弹，看看它是否已从屏幕消失。
        if bullet.rect.bottom <= 0:
            #从bullets中删除
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没达到限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    #计算可用于放置外星人的水平空间
    available_space_x = ai_settings.screen_width - 2 * alien_width
    #可容纳多少个外星人，函数int()将小数部分丢弃
    number_aliens_x = int(available_space_x / (2 * alien_width))
    #创建第一行外星人
    #循环从零数到创建外星人数
    for alien_number in range(number_aliens_x):
        #创建一个新的外星人，并通过设置x坐标将其加入当前行
        alien = Alien(ai_settings,screen)
        #每个外星人都右推一个外星人宽度
        #接下来，将外星人宽度乘以2，得到每个外星人占据的空间(其中包括其右边的空白区域)
        #再据此计算当前外星人再当前行的位置
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        #将每个新创建的外星人都添加到编组aliens
        aliens.add(alien)