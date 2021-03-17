import sys
import pygame


def check_events(ship):
    """Обрабатывает нажатия клавишь и события мыши"""

    # отслеживание событий клавиатуры и мыши:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    # при каждом проходе цикла перерисовывается весь экран:
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # отображение последнего прорисованного экрана:
    pygame.display.flip()
