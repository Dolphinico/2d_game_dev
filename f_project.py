import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Инициализирует игру и создает объект экрана"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Allien Invasion')
    ship = Ship(screen)
    
# запуск нового цикла игры:
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        pygame.display.update()
        
        
       
        
        
run_game()