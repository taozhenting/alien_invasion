import pygame
class Ship():
    #screen参数指定了飞船绘制到什么地方
    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        #加载飞船图像并获取其外接矩形
        #调用pygame.image.load()这个函数返回一个表示飞船的surface并存储到了self.image
        self.image = pygame.image.load('images/ship.bmp')

        #rect处理对象是矩形，即便它们形状并非矩形。使用get_rect()获取相应surface的属性rect
        self.rect = self.image.get_rect()
        #将表示屏幕的矩形存储在self.screen_rect
        self.screen_rect = screen.get_rect()
        #将每艘新飞船放在屏幕中央
        #将self.rect.centerx(飞船中心的x坐标)设置为表示屏幕的矩形的属性centerx
        self.rect.centerx = self.screen_rect.centerx
        #将self.rect.bottom（飞船下边缘的y坐标)设置为表示屏幕的矩形的属性bottom
        self.rect.bottom = self.screen_rect.bottom

    #定义了方法blitme(),它根据self.rect指定的位置将图像绘制到屏幕上
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)