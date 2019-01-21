
import pygame
from pygame.sprite import Group

from settings_6 import Settings
from ship_5 import Ship
import game_functions_20 as gf

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
    #创建一个外星人编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏的循环
    while True:
        #主循环检查玩家的输入
        gf.check_events(ai_settings,screen,ship,bullets)
        #更新飞船的位置
        ship.update()
        #所有未消失的子弹位置
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,aliens)
        #使用更新后的位置来绘制新屏幕
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()