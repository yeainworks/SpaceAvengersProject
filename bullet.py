import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ship, image_path="bullet.png"):
        """
        screen - экран на котором отрисовывается пуля
        ship - объект из которого вылетает пуля
        image_path - путь к изображению пули
        """
        super(Bullet, self).__init__()  # Наследуем инициализацию у родителя
        self.screen = screen

        # Загружаем изображение пули
        self.image = pygame.image.load(bullet.png)  # Загружаем текстуру пули
        self.image = pygame.transform.scale(self.image, (10, 20))  # Изменяем размер (ширина 10px, высота 20px)
        self.rect = self.image.get_rect()  # Получаем прямоугольник для отрисовки
        self.rect.centerx = ship.rect.centerx  # Позиционируем пулю по центру корабля
        self.rect.top = ship.rect.top  # Начальная позиция пули — сверху от корабля

        self.y = float(self.rect.y)  # Делаем y-координату пули плавной (с помощью float)

        self.speed = 5  # Скорость пули

    def rendering(self):
        """Отображение пули на экране"""
        self.screen.blit(self.image, self.rect)  # Отображаем изображение пули

    def update_pos(self):
        """Обновление позиции пули"""
        self.y -= self.speed  # Двигаем пулю вверх
        self.rect.y = self.y  # Обновляем позицию прямоугольника пули

    