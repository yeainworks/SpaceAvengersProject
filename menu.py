import pygame
import sys

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 128, 255)
HOVER_COLOR = (0, 100, 200)

# Класс кнопки
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen):
        # Рисуем кнопку
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        # Проверка, если мышь наведена на кнопку
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, HOVER_COLOR, self.rect)
        # Текст на кнопке
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_pressed(self):
        # Проверка на клик мышью
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False


def show_menu(screen):
    # Логотип (уменьшаем его размер)
    logo = pygame.image.load('images/gamelogo.png')
    logo = pygame.transform.scale(logo, (700, 500))  #размер лого
    logo_rect = logo.get_rect(center=(screen.get_width() // 2, 100))  # Центрируем логотип по горизонтали и ставим его на верх

    # Кнопки
    play_button = Button(400, 400, 200, 50, 'Играть', action="play")
    settings_button = Button(400, 480, 200, 50, 'Настройки', action="settings")
    quit_button = Button(400, 560, 200, 50, 'Выйти', action="quit")
    
    buttons = [play_button, settings_button, quit_button]
    
    running = True
    while running:
        screen.fill(BLACK)
        
        # Отображаем логотип
        screen.blit(logo, logo_rect)

        # Рисуем кнопки
        for button in buttons:
            button.draw(screen)

        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Если кнопка нажата
        if play_button.is_pressed():
            return "play"
        elif settings_button.is_pressed():
            return "settings"
        elif quit_button.is_pressed():
            pygame.quit()
            sys.exit()

        pygame.display.update()