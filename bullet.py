# bullet.py
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ship, image_path="bullet.png"):
        """
        screen - экран на котором отрисовывается пуля
        ship - объект из которого вылетает пуля
        image_path - путь к изображению пули
        """
        super().__init__()
        self.screen = screen

        # Загружаем изображение пули
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Используем float для y-координаты для плавного движения
        self.y = float(self.rect.y)
        self.speed = 5

    def update_pos(self):
        """Обновление позиции пули"""
        self.y -= self.speed  # Двигаем пулю вверх
        self.rect.y = self.y

    def rendering(self):
        """Отображение пули на экране"""
        self.screen.blit(self.image, self.rect)
