import sys
import pygame
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #设置游戏分辨率，对象screen是个surface,在游戏中每个元素(如外星人或飞船)都是一个surface
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Alien Invasion")
    #开始游戏的循环
    while True:
        #监视键盘和鼠标事件
        #所有键盘和鼠标事件都将促使for循环运行
        for event in pygame.event.get():
            #如玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT
            if event.type == pygame.QUIT:
                #调用sys.exit()退出游戏
                sys.exit()
        #最近绘制的屏幕可见，每次执行while循环时都绘制一个空屏幕。
        #我们移动游戏元素时，pygame.display.flap()将不断更新屏幕，以显示元素的新位置。
        #并在原来的位置隐藏元素，从而营造平滑移动的效果。
        pygame.display.flip()
run_game()