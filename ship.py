import pygame

class Ship():
    """Класс модели корабля"""

    def __init__(self,screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen

        # загрузка изображения корабля и получение прямоугольника:
        self.image = pygame.image.load("arts\game_arts\ship_2.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # строка отвечающая за появление каждого нового корабля и его позиции:
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)