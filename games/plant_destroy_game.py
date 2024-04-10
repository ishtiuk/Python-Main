import pygame

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('background.png')
bulet = pygame.image.load('bulet.png')

planet_lst = ['planet1.png', 'planet2.png', 'planet3.png', 'planet4.png', 'planet5.png', 'planet6.png', 'planet7.png', 'planet8.png']
spaceship = pygame.image.load('spaceship.png')


planet_id = 0
planet_x = 145
bulet_y = 500
planet_direction = 'right'

alive = True
fired = False
score = 0

clock = pygame.time.Clock()

while alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()

    screen.blit(background, [0, 0])
    planet = pygame.image.load(planet_lst[planet_id])
    screen.blit(planet, [planet_x, 50])
    screen.blit(bulet, [165, bulet_y])
    screen.blit(spaceship, [150, 500])
    

    if planet_direction == 'right':
        planet_x += 5

        if planet_x == 300:
            planet_direction = 'left'

    if planet_direction == 'left':
        planet_x -= 5

        if planet_x == 0:
            planet_direction = 'right'


    if bulet_y == 95 and planet_x >= 120 and planet_x <= 170:
        planet_id += 1
        score += 10
        if planet_id == len(planet_lst):
            print("| Game Over |\nYOur Score:", score,"\nHigh Score:", score)
            alive = False

    if keys[pygame.K_SPACE] == True:
        fired = True

    if fired == True:
        bulet_y -= 5

        if bulet_y == 90:
            bulet_y = 500
            fired = False

    pygame.display.update()
    clock.tick(50)



#        Score Indexer Database  

high_score = open('High_Score.txt', 'w')
high_score.write(f"         High Score          \n          {score}")
high_score.close()





    