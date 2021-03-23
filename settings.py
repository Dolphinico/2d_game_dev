import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # параметры экрана:
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (123, 123, 123)
        # настройки корабля:
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # настройки пули:
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 100
        # настройки пришельцев:
        self.aliens_speed_factor = 1 
        self.fleet_drop_speed = 3.3 
        # fleet_direction = 1 обозначает движение вправо, -1 влево
        self.fleet_direction = 1
        
