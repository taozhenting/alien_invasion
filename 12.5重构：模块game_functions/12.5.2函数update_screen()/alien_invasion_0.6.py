#将while循环中更新屏幕的代码替换为对函数update_screen()的调用
import pygame

from settings import Settings
from ship import Ship
import game_functions_2 as gf

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
    ship = Ship(screen)
    #开始游戏的循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)
run_game()