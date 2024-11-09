import pygame

class Ship():

    def __init__(self, screen):
        """screen - экран на котором отрисовывается корабль"""

        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.mright = False
        self.mleft = False
        self.speed = 1.2
        self.attack = False

    def rendering(self):
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        elif self.mleft and self.rect.left > self.screen_rect.left: #0
            self.center -= self.speed

        self.rect.centerx = self.center