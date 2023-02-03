import sys
import pygame
import time
import loader_game_sprites as LGS
from random import randint
from pygame.locals import *


#: Creating a window
width, height = 1600, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")
pygame.init()
clock = pygame.time.Clock()


#: Loading sprite
background = LGS._background("Venator.jpg")
main_sprite = LGS._main_sprite("boss_body.png")
enemy_sprite = LGS._enemy_sprite("ring.png")
main_menu = LGS._main_menu("menu.jpg")
loose_scr = LGS._main_menu("menu.jpg")


#: sprites coords
rand_x, rand_y = randint(0, 900), randint(0, 600)   #: enemy sprite coords
main_x, main_y = 100, 100   #: main_sprite coords
print(f"Enemy sprite coords: {rand_x, rand_y}")


#: Hitpoints
main_sprite_hp = 100
enemy_sprite_hp = 100
_timer = 100
print(type(enemy_sprite))
rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(100, 100)

#: Text
font = pygame.font.Font(None, 100)


#: Collision of sprites
main_sprite_rect = main_sprite[0].get_rect(centerx=int(main_x), centery=int(main_y))
enemy_sprite_rect = enemy_sprite.get_rect(center=(rand_x, rand_y))
print(f"sprite hp: {str(main_sprite_hp)}")

#: Logical arguments for moving
up = False
down = False
left = False
right = False
running = True
menu_lounch = True
loose_ef = False
shoot = True


#: Game loop
while running:
    screen.blit(background, (0,0))
    screen.blit(main_sprite[0], (main_x, main_y))
    screen.blit(enemy_sprite, (rand_x, rand_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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
            if shoot == True:
                if event.key == pygame.K_SPACE:
                    enemy_sprite_hp -= 10
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_DOWN:
                down = False

        #collide = rect.collidepoint(main_sprite_rect)

    #screen.blit(background, (0, 0)) #: Background initialization
    #screen.blit(main_sprite[0], (main_x, main_y)) #: Main sprite initialization
     #: Enemy sprite initialization

    
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
    if main_x < -50:
        main_x = 1620
    if main_x > 1650:
        main_x = -20
    if main_y < -50:
        main_y = 1020
    if main_y > 1050:
        main_y = -20


    #: Text box (sprite hp)
    text = str(f"Your hp: {main_sprite_hp}")
    _text = font.render(text , True, (255, 255, 255)) #: Text render

    enemy_hp = str(f"Enemy hp: {enemy_sprite_hp}")
    _enemy_hp = font.render(enemy_hp , True, (255, 255, 255))

    loosing_text = "Sorry.., you're lost. Press esc to exit."   #: Loosing
    _loosing_text = font.render(loosing_text, True, (255, 255, 255))

    win_text = "You won. Press esc to exit."
    _win_text = font.render(win_text, True, (255, 255, 255))

    screen.blit(_text, (1000, 50))
    screen.blit(_enemy_hp, (1000, 900))

    #: Sprite transformation
    if up and right == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[225], (main_x, main_y))
        screen.blit(_text, (1000, 50))
        screen.blit(_enemy_hp, (1000, 900))

    if down and right == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[135], (main_x, main_y))
        screen.blit(_text, (1000, 50))
        screen.blit(_enemy_hp, (1000, 900))
        
    if up and left == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[315], (main_x, main_y))
        screen.blit(_text, (1000, 50))
        screen.blit(_enemy_hp, (1000, 900))

    if down and left == True:
        screen.blit(background, (0, 0))
        screen.blit(enemy_sprite, (rand_x, rand_y))
        screen.blit(main_sprite[45], (main_x, main_y))
        screen.blit(_text, (1000, 50))
        screen.blit(_enemy_hp, (1000, 900))


    #: Enemy movements
    if rand_x and rand_y != main_x and main_y:
        if rand_x <= main_x:
            rand_x += 3
        if rand_y <= main_y:
            rand_y += 3
        if rand_x >= main_x:
            rand_x -= 3
        if rand_y >= main_y:
            rand_y -= 3
        if rand_x and rand_y == main_x and main_y:
            main_sprite_hp -= 100
        #rand_x, rand_y = 800, 500  #: Enemy moving close


    #if main_sprite_rect.colliderect(enemy_sprite_rect):    #: collision
        #main_sprite_hp -= 10
        #print(main_sprite_hp)
    #if collide:    
        #sys.exit()
    

    #: Game over
    if main_sprite_hp == 0:
        screen.blit(loose_scr, (0, 0))
        up = False
        down = False
        left = False
        right = False
        screen.blit(_loosing_text, (1600/len(loosing_text), 500))

    if enemy_sprite_hp == 0:
        screen.blit(loose_scr, (0, 0))
        up = False
        down = False
        left = False
        right = False
        shoot = False
        screen.blit(_win_text, (1600/len(win_text), 500))

    pygame.display.update()
    pygame.display.flip()

