import os
import sys
import pygame
from random import randint
from pathlib import Path
import os.path
import car_game_sprites as CGS


#: Loading sprite
def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

#: Creating a window
screen = pygame.display.set_mode((1000, 600))
pygame.init()

#: sprites coords
rand_x, rand_y = randint(0, 900), randint(0, 600)
loc_x, loc_y = 0, 0

background = CGS._background("Venator.jpg")
main_sprite = CGS._main_sprite("lada0.png")
enemy_sprite = CGS._enemy_sprite("Darth_Vader.jpg")

#: Logical arguments for moving
up = False
down = False
left = False
right = False
running = True


#: Game loop
while running:
    screen.blit(background, (0, 0)) #: Background initialization
    screen.blit(main_sprite[0], (loc_x, loc_y)) #: Main sprite initialization
    screen.blit(enemy_sprite, (rand_x, rand_y)) #: Enemy sprite initialization

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_DOWN:
                down = False


    if up == True:
        loc_y -= 2
        screen.blit(main_sprite[180], (loc_x, loc_y))
    if down == True:
        loc_y += 2
        screen.blit(main_sprite[0], (loc_x, loc_y))
    if right == True:
        loc_x += 2
        screen.blit(main_sprite[90], (loc_x, loc_y))
    if left == True:
        loc_x -= 2
        screen.blit(main_sprite[270], (loc_x, loc_y))


    if loc_x <= 0:
        loc_x = 50
    if loc_x >= 1000:
        loc_x = 900
    if loc_y <= 0:
        loc_y = 20
    if loc_y >= 600:
        loc_y = 500


    #: Sprite transformation
    if up and right == True:
        screen.blit(main_sprite[135], (loc_x, loc_y))
    if down and right == True:
        screen.blit(main_sprite[45], (loc_x, loc_y))
    if up and left == True:
        screen.blit(main_sprite[225], (loc_x, loc_y))
    if down and left == True:
        screen.blit(main_sprite[315], (loc_x, loc_y))


    #: Game over
    if loc_y and loc_x == rand_x and rand_y:
        running = False

    pygame.display.update()
    pygame.display.flip()
