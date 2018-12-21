import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen = screen
        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        #子弹并非基于图形的，因此必须使用pygame.Rect()类从空白开始创建一个矩形
        #创建这个类的实例时，必须提供矩形左上角的x,y坐标，还有矩形的宽度和高度。
        #我们再0,0创建这个矩形，子弹宽度和高度从ai_settings中获取
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #子弹矩形x坐标（飞船当前位置）
        self.rect.centerx = ship.rect.centerx
        #子弹矩形y坐标,rect的top属性，让子弹看起来像是从飞船中射出。
        self.rect.centery = ship.rect.centery
        #存储用小数表示的子弹位
        self.r = float(self.rect.right)
        #子弹颜色设置
        self.color = ai_settings.bullet_color
        #子弹速度设置
        self.speed_factor = ai_settings.bullet_speed_factor
        #射击标志
        self.fire = False

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.r += self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.right = self.r

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)