import pygame
import controls
from ship import Ship
from pygame.sprite import Group
from menu import show_menu
from enemy import Enemy

def run():
    """Основная функция игры"""
    pygame.init()
    
    # Настройки экрана
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("TheSpaceAvengers")

    # Цвет фона
    bg_color = (0, 0, 0)

    # Создание объектов игры
    spaceship = Ship(screen)
    bullets = Group()
    enemies = Group()
    
    # Спавн врагов
    controls.spawn_army(screen, enemies)

    # Показ меню
    menu_result = show_menu(screen)
    if menu_result == "quit":
        pygame.quit()
        return  # Закрываем игру

    # Главный игровой цикл
    while True:
        controls.events(screen, spaceship, bullets)
        spaceship.update_pos()

        controls.update(bg_color, screen, spaceship, enemies, bullets)

run()