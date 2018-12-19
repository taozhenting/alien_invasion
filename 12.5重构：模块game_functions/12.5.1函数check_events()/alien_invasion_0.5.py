#导入模块game_functions,并将事件循环替换为对函数check_events()的调用
import pygame

from settings import Settings
from ship import Ship
import game_functions_1 as gf

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
        #使用ai_settings访问背景色
        screen.fill(ai_settings.bg_color)
        #将飞船绘制到屏幕上，确保它出现在背景前面
        ship.blitme()
        #最近绘制的屏幕可见，每次执行while循环时都绘制一个空屏幕。
        #我们移动游戏元素时，pygame.display.flap()将不断更新屏幕，以显示元素的新位置。
        #并在原来的位置隐藏元素，从而营造平滑移动的效果。
        pygame.display.flip()
run_game()