import pygame
import time

screen_size = [750, 550]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('back.png')
side_robot = pygame.image.load('robot.png')
light2_vert = pygame.image.load('light2_vert.png')
light2_land = pygame.image.load('light2_land.png')
light2_vert_agin = pygame.image.load('light2_vert.png')

lights = ['1211.png', '12145454541.png']
lights_id = 0

light_x = 0
i = 0
direction = 'right'
light2_vert_y = 20
light2_land_x = 603
light2_vert_agin_y = 178
light2_vert_y_direction = 'down'


while True:
    light = pygame.image.load(lights[lights_id])
    screen.blit(background, [0, 0])
    screen.blit(light2_vert, [600, light2_vert_y])
    screen.blit(light2_land, [light2_land_x, 215])
    screen.blit(light2_vert_agin, [734, light2_vert_agin_y])
    screen.blit(side_robot, [600, 300])
    screen.blit(light, [light_x, 500])


    if light2_vert_y_direction == 'down':
        light2_vert_y += 5
        if light2_vert_y == 180:
            light2_vert_y_direction = 'up'

    if light2_vert_y_direction == 'up':
        light2_land_x += 5
        if light2_land_x == 703:
            light2_land_x = 603
            light2_vert_y_direction = 'upagain'

    if light2_vert_y_direction == 'upagain':
        light2_vert_agin_y -= 5
        if light2_vert_agin_y == 18:
            light2_vert_agin_y += 5
            
        

    if direction == 'right':
        lights_id = 0
        light_x += 5
    elif direction == 'left':
        lights_id = 1
        light_x -= 5

    if light_x == 710:
        direction = 'left'
        
    elif light_x == 0:
        direction = 'right'
        

    time.sleep(0.009)
    i += 1
    if i == 0:
        break
    pygame.display.update()

