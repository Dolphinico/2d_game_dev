import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # параметры экрана:
        self.screen_width = 1024
        self.screen_height = 720
        self.bg_color = (123, 123, 123)
        # настройки корабля:
        self.ship_speed_factor = 1.5
