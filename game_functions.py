import sys
import pygame

def check_events():
    """Обрабатывает нажатия клавишь и события мыши"""

    # отслеживание событий клавиатуры и мыши:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
     # при каждом проходе цикла перерисовывается весь экран:
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # отображение последнего прорисованного экрана:
    pygame.display.flip()
    