import pygame

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.score = 0

    def increment_score(self):
        """Увеличиваем счет на 10 очков за каждый сбитый враг."""
        self.score += 10

    def render_score(self):
        """Отображаем текущий счет в верхнем правом углу."""
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (self.screen_rect.right - score_text.get_width() - 10, 10))
