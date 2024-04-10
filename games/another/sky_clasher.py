from typing import Mapping
import pygame
from pygame.display import set_mode 

screen_size = [853, 480]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('background.png')
man_rote1 = pygame.image.load('man1.png')
man_rote2 = pygame.image.load('man2.png')
rock = pygame.image.load('rock.png')

man_x = 425
man_y = 350
rock_y = 0

alive = True

direction = 'right'

clock = pygame.time.Clock()

while alive:
    screen.blit(background, [0, 0])
    screen.blit(rock, [5, rock_y])
    screen.blit(rock, [100, rock_y])

    rock_y += 5

    pygame.event.get()
    keys = pygame.key.get_pressed()    

    if keys[pygame.K_RIGHT] == True:
        direction = 'right'
        man_x += 3
    elif keys[pygame.K_LEFT] == True:
        direction = 'left'
        man_x -= 3
    elif keys[pygame.K_UP] == True:
        man_y -= 4

    if direction == 'right':
        screen.blit(man_rote1, [man_x, man_y])
    if direction == 'left':
        screen.blit(man_rote2, [man_x, man_y])

    pygame.display.update()
    clock.tick(120)

