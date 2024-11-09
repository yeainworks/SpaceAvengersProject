import pygame
import sys
from bullet import Bullet
from enemy import Enemy

def events(screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                ship.mright = True
            #влево
            elif event.key == pygame.K_a:
                ship.mleft = True
            #атака
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen,ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                ship.mright = False
            #влево
            elif event.key == pygame.K_a:
                ship.mleft = False

def update_bullet(bullets, enemys):
    bullets.update()
    #спавн пули
    for bullet in bullets.sprites():
        bullet.rendering()
        bullet.update_pos()
    #удаление пули
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # не помню зачем это, оно сейчас не используется
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)

def update_enemys(screen, ship, enemys):
    screen_rect = screen.get_rect()
    for enemy in enemys:
        enemy.update_pos()
        if enemy.rect.bottom >= screen_rect.bottom:
            sys.exit()
    if pygame.sprite.spritecollideany(ship, enemys):
        sys.exit()


def update(bg_color, screen, ship, enemys, bullets):
    screen.fill(bg_color)
    update_bullet(bullets, enemys)
    update_enemys(screen, ship, enemys)

    ship.rendering()
    enemys.draw(screen)
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