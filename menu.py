import pygame
import sys
import game  # Импорт основного игрового файла, чтобы запускать игру

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Цвет фона меню
bg_color = (0, 0, 0)  # Черный фон

# Загрузка логотипа
logo = pygame.image.load("images/logo.png")  # Убедитесь, что путь правильный
logo = pygame.transform.scale(logo, (400, 200))  # Уменьшаем логотип (например, до 400x200)
logo_rect = logo.get_rect()
logo_rect.centerx = screen.get_rect().centerx
logo_rect.centery = screen.get_rect().top + 100  # Поднимаем логотип выше (100 пикселей от верхней границы)

# Шрифт для кнопки
font = pygame.font.SysFont(None, 48)
button_color = (0, 255, 0)  # Зеленый
button_hover_color = (0, 200, 0)  # Темно-зеленый
button_width = 200
button_height = 50
button_rect = pygame.Rect((screen.get_rect().centerx - button_width // 2, screen.get_rect().centery + 50), (button_width, button_height))

# Функция для отображения кнопки
def draw_button(text, color, x, y):
    button_image = font.render(text, True, (255, 255, 255))
    pygame.draw.rect(screen, color, (x, y, button_width, button_height))
    screen.blit(button_image, (x + (button_width - button_image.get_width()) // 2, y + (button_height - button_image.get_height()) // 2))

# Главный игровой цикл меню
def main_menu():
    while True:
        screen.fill(bg_color)
        screen.blit(logo, logo_rect)

        # Рисуем кнопку
        draw_button("Играть", button_color, button_rect.x, button_rect.y)

        # Проверка нажатий клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  # Если нажали на кнопку "Играть"
                    game.start_game()  # Запуск игры

        # Отображаем меню
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
