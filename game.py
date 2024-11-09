import pygame
import sys
from bullet import Bullet
from enemy import Enemy
from ship import Ship
from scoreboard import Scoreboard  # Импортируем для отображения счета

# Инициализация Pygame и основных параметров
pygame.init()
screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Цвет фона
bg_color = (0, 0, 0)  # Черный фон

# Создаем объект корабля игрока и группы для пуль и врагов
ship = Ship(screen)
bullets = pygame.sprite.Group()
enemys = pygame.sprite.Group()
scoreboard = Scoreboard(screen)  # Счетчик очков

def events(ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.mright = True
            elif event.key == pygame.K_a:
                ship.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.mright = False
            elif event.key == pygame.K_a:
                ship.mleft = False

def update_bullet(bullets, enemys):
    for bullet in bullets.sprites():
        bullet.update_pos()
        bullet.rendering()

    # Удаление пуль, вышедших за пределы экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Проверка столкновений пуль и врагов, удаление при попадании
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)
    if collisions:
        scoreboard.increment_score()  # За каждый попадание увеличиваем счет

def update_enemys(ship, enemys):
    for enemy in enemys:
        enemy.update_pos()
        if enemy.rect.bottom >= screen.get_rect().bottom:
            enemy.kill()  # Удаляем врага, если он дошел до низа экрана

    if pygame.sprite.spritecollideany(ship, enemys):
        print("Game Over!")  # Сообщение об окончании игры
        pygame.quit()  # Закрытие игры
        sys.exit()  # Завершаем процесс игры

def update_screen():
    screen.fill(bg_color)
    bullets.draw(screen)
    enemys.draw(screen)
    ship.rendering()
    scoreboard.render_score()  # Отображаем текущий счет
    pygame.display.flip()

def spawn_army(screen, enemys):
    screen_w = screen.get_rect().width
    screen_h = screen.get_rect().height
    enemy = Enemy(screen)
    enemy_w = enemy.rect.width
    space_btwn = 6
    num_enemy_x = int((screen_w - 2 * enemy_w) / (enemy_w + space_btwn))
    indent_x = int(((screen_w - num_enemy_x * (enemy_w + space_btwn)) + space_btwn) / 2)
    enemy_h = enemy.rect.height
    num_enemy_y = int((screen_h - 89 - 2 * enemy_h) / (enemy_h + space_btwn))
    indent_y = int(((screen_h - 89 - num_enemy_y * (enemy_h + space_btwn)) + space_btwn) / 3)

    for i_row in range(num_enemy_y - 1):
        for i_enemy in range(num_enemy_x):
            enemy = Enemy(screen)
            enemy.x = indent_x + (enemy_w + space_btwn) * i_enemy
            enemy.y = indent_y + (enemy_h + space_btwn) * i_row
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y 
            enemys.add(enemy)

# Основной игровой цикл
def start_game():
    spawn_army(screen, enemys)

    while True:
        events(ship, bullets)
        ship.update_pos()
        update_bullet(bullets, enemys)
        update_enemys(ship, enemys)
        update_screen()
