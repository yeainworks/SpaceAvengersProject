import pygame, controls
#import sys
from ship import Ship
from pygame.sprite import Group
#from enemy import Enemy

def run():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Защитник космичского пространства")
    bg_color = (0, 0, 0)
    spaceship = Ship(screen)
    bullets = Group()
    #enemy = Enemy(screen)
    enemys = Group() 
    controls.spawn_army(screen, enemys)

    while 42: #отсылка
        controls.events(screen, spaceship, bullets)
        spaceship.update_pos()
        
        print(len(bullets))
        controls.update(bg_color, screen, spaceship, enemys, bullets)

run()