import os
import sys
import pygame
from random import randint
import os.path
import car_game_sprites as CGS


width, height = 1600, 1000

#: Creating a window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car game")
pygame.init()
font = pygame.font.Font(None, 20)


#: Loading sprite
script_dir = os.path.dirname(__file__)
background = CGS._background("Venator.jpg")
main_sprite = CGS._main_sprite("boss_body.png")
enemy_sprite = CGS._enemy_sprite("ring.png")


#: sprites coords
rand_x, rand_y = randint(0, 900), randint(0, 600)
main_x, main_y = 100, 100
print(f"Enemy sprite coords: {rand_x, rand_y}")


#: Hitpoints
main_sprite_hp = 100
timer = 100
print(type(enemy_sprite))


#: Collision of sprites
main_sprite_rect = main_sprite[0].get_rect(centerx=int(main_x), centery=int(main_y))
enemy_sprite_rect = enemy_sprite.get_rect(center=(rand_x, rand_y))


#: Logical arguments for moving
up = False
down = False
left = False
right = False
running = True


#: Game loop
while running:
    screen.blit(background, (0, 0)) #: Background initialization
    screen.blit(main_sprite[0], (main_x, main_y)) #: Main sprite initialization
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
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_DOWN:
                down = False


    #: Main sprite moving
    if up == True:
        main_y -= 5
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[270], (main_x, main_y))
    if down == True:
        main_y += 5
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[90], (main_x, main_y))
    if right == True:
        main_x += 5
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[180], (main_x, main_y))
    if left == True:
        main_x -= 5
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[0], (main_x, main_y))

    #: Walls
    if main_x < 0:
        main_x = 1590
    if main_x > 1600:
        main_x = 10
    if main_y < 0:
        main_y = 990
    if main_y > 1000:
        main_y = 10


    #: Sprite transformation
    if up and right == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[225], (main_x, main_y))
    if down and right == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[135], (main_x, main_y))
    if up and left == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[315], (main_x, main_y))
    if down and left == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[45], (main_x, main_y))

    #: Game over
    if rand_x and rand_y != main_x and main_y:
        if rand_x <= main_x:
            rand_x += 2
        if rand_y <= main_y:
            rand_y += 2
        if rand_x >= main_x:
            rand_x -= 2
        if rand_y >= main_y:
            rand_y -= 2     
        #rand_x, rand_y = 800, 500
    #if main_sprite_rect.collidepoint(enemy_sprite_rect):
        #main_sprite_hp -= 10
        #print()
    if main_sprite_hp == 0:
        sys.exit()
    
    pygame.display.update()
    pygame.display.flip()
