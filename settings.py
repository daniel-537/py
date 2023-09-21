class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (253, 253, 253)
        # 飞船的速度
        self.ship_speed = 3
        self.ship_limit = 2
        # 子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bulltes_allowed = 10
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 为1 表示向右移动，为-1表示想做移动
        self.fleet_direction = 1
        # 以什么速度加快游戏的节奏
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # 音乐的音量
        self.ser_volume = 0.2

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction 为1 表示向右，为-1 表示向左
        self.fleet_direction = 1

        # 记分设置
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置的值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
