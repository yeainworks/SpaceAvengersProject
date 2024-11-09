import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.15

    def rendering(self):
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        self.y += self.speed
        self.rect.y = self.y
