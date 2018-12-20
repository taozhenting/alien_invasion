
import pygame
from pygame.sprite import Group

from settings_3 import Settings
from ship_5 import Ship
import game_functions_7 as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #创建Settings实例存储在ai_settings变量中
    ai_settings = Settings()
    #使用ai_settings的属性screen_width和screen_height
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    #需要传入实参ai_settings
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    #pygame.sprite.Group类创建一个编组，存储所有有效子弹，类似列表。
    bullets = Group()
    #开始游戏的循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        #飞船的位置在检测到键盘事件后(但在更新屏幕前)更新。
        ship.update()
        #当对编组调用update()时，编组将自动对其中每个精灵(子弹)调用update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()