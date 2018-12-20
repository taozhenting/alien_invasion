#增加飞船移动像素
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #飞船的设置
        self.ship_speed_factor = 1.5
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #子弹设置,设置创建宽3像素，高15像素的深灰色的子弹。子弹速度比飞船稍低
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
