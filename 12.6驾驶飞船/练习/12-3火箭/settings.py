#增加飞船移动像素
class Settings():
    """"火箭移动"""
    def __init__(self):
        """初始化游戏的设置"""
        #飞船的设置
        self.ship_speed_factor = 3.5
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
