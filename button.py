import pygame.font # импортирует модуль pygame font, который позволяет Pygame выводить текст на экран


class Button():
    """Кнопка Play"""
    def __init__(self, ai_settings, screen, msg):
        """Инициализирует атрибуты кнопки"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # назначение размеров и свойств кнопок:
        self.width, self.height = 200, 50
        self.button_color = (50, 205, 50)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48, bold=False, italic=False)

        # построение объекта rect кнопки и выравнивание по центру экрана:
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз:
        # Pygame выводит строку текста в виде графического изображения. 
        # Эта задача решается методом prep_msg(), код которого представлен ниже:
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник, выравнивает текст по центру"""
        # Вызов font.render() преобразует текст, хранящийся в msg, в изображение, которое затем сохраняется в msg_image. 
        # Методу font.render() также передается логический признак режима сглаживания текста(True).
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        # метод draw_button(), который может вызываться для отображения кнопки на экране:
    def draw_button(self):
        """Отображение пустой кнокпи и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



