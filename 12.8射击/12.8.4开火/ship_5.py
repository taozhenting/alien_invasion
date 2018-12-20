#调整飞船活动范围
import pygame
class Ship():
    #screen参数指定了飞船绘制到什么地方
    #增加了ai_settings参数，让飞船获取其速度设置。
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        #我们将形参ai_settings的值存储在一个属性中，以便能够在update()中使用它。
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        #调用pygame.image.load()这个函数返回一个表示飞船的surface并存储到了self.image
        self.image = pygame.image.load('images/ship.bmp')

        #rect处理对象是矩形，即便它们形状并非矩形。使用get_rect()获取相应surface的属性rect
        self.rect = self.image.get_rect()
        #将表示屏幕的矩形存储在self.screen_rect
        self.screen_rect = screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        #将self.rect.centerx(飞船中心的x坐标)设置为表示屏幕的矩形的属性centerx
        self.rect.centerx = self.screen_rect.centerx
        #将self.rect.bottom（飞船下边缘的y坐标)设置为表示屏幕的矩形的属性bottom
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新飞船的center值，而不是rect
        #self.rect.right返回飞船右边坐标，小于self.screen_rect.right说明未触及屏幕右边缘
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        #添加了if而不是elif，因为如果同时按下左右箭头，先增加再减少self.rect.centerx
        #如果用elif，右箭头将始终处于优先地位
        #左边缘坐标大于零，说明飞船未触及屏幕左边缘
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        #有时飞船位置没在底部中央，所以注释并更改
        #self.rect.centerx = self.center

    #定义了方法blitme(),它根据self.rect指定的位置将图像绘制到屏幕上
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)