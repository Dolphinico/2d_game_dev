import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий врага"""

    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его изначальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('arts\game_arts\ship_1.png')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в верхнем левом углу экрана:
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции пришельца:
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращение True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """"Перемещает пришельца влево или вправо"""
        self.x += (self.ai_settings.alien_speed_factor * 
                self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)
