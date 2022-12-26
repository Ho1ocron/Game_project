import os
import sys
import pygame
from random import randint
import os.path
import car_game_sprites as CGS
import time


#: Loading sprite
def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


background = CGS._background("Venator.jpg")
main_sprite = CGS._main_sprite("lada0.png")
enemy_sprite = CGS._enemy_sprite("Darth_Vader.jpg")


#: Creating a window
screen = pygame.display.set_mode((1000, 600))
pygame.init()
font = pygame.font.Font(None, 20)


#: sprites coords
rand_x, rand_y = randint(0, 900), randint(0, 600)
loc_x, loc_y = 0, 0
print(f"Enemy sprite coords: {rand_x, rand_y}")


#: Hitpoints
main_sprite_hp = 100
timer = 100
hp_count = font.render("1", False, (0, 180, 0))
place = hp_count.get_rect(center=(200, 150))
pygame.display.update()


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
    if rand_x and rand_y != loc_x and loc_y:
        if rand_x >= loc_x:
            rand_x -= 1
        elif rand_x <= loc_x:
            rand_x += 1
        if rand_y >= loc_y:
            rand_y -= 1
        elif rand_y <= loc_y:
            rand_y += 1
        if rand_x and rand_y == loc_x and loc_y:
            main_sprite_hp -= 10
            print(f"Your HP: {main_sprite_hp}")
            if main_sprite_hp == 0:
                running = False
    
    pygame.display.update()
    pygame.display.flip()
