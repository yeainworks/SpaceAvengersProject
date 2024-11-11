import pygame
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ship_x, ship_y, image_path="images/bullet.png"):
        """
        screen - экран, на котором отрисовывается пуля
        ship_x, ship_y - координаты корабля, из которого вылетает пуля
        image_path - путь к изображению пули
        """
        super().__init__()  # Наследуем инициализацию у родителя

        self.screen = screen

        # Путь к изображению пули, проверяем, существует ли файл
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Изображение {image_path} не найдено.")
        
        # Загружаем изображение пули
        self.image = pygame.image.load(image_path)  #Загружаем текстуру пули
        self.image = pygame.transform.scale(self.image, (10, 20))  #размер пули
        
        # Получаем прямоугольник для отрисовки пули
        self.rect = self.image.get_rect()  
        self.rect.centerx = ship_x  # Позиционируем пулю по центру корабля
        self.rect.top = ship_y  # Начальная позиция пули — сверху от корабля

        # Позиция пули, используем float для плавного движения
        self.y = float(self.rect.y)  

        self.speed = 3  # Скорость пули

    def render(self):
        """Отображение пули на экране"""
        self.screen.blit(self.image, self.rect)  # Отображаем изображение пули

    def update_pos(self):
        """Обновление позиции пули"""
        self.y -= self.speed  # Двигаем пулю вверх
        self.rect.y = self.y  # Обновляем позицию прямоугольника пули

    def off_screen(self):
        """Проверка, если пуля вышла за экран"""
        return self.rect.bottom < 0