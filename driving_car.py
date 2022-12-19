import os
import sys
import pygame
from random import randint

rand_x = randint(0, 900)
rand_y = randint(0, 600)
print(rand_x, rand_y)

def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


running = True
px = 20
chpx = 0
chpy = 0
py = 20
ex = 1000
ey = 600
loc_x = 0
loc_y = 0
screen = pygame.display.set_mode((ex, ey))
pygame.init()
stop = load_image("Darth_Vader.png")
car = load_image('sprite.png')
stop = pygame.transform.scale(stop, (200, 200))
car = pygame.transform.scale(car, (100, 200))
car0 = car
car45 = pygame.transform.rotate(car, 45)
car90 = pygame.transform.rotate(car, 90)
car135 = pygame.transform.rotate(car, 135)
car180 = pygame.transform.rotate(car, 180)
car225 = pygame.transform.rotate(car, 225)
car270 = pygame.transform.rotate(car, 270)
car315 = pygame.transform.rotate(car, 315)
ice_fon = load_image('space.jpg')
ice_fon = pygame.transform.scale(ice_fon, (1920, 1080))
menu = load_image('space.jpg')
menu = pygame.transform.scale(menu, (1920, 1080))
first_launch = True
up = False
down = False
left = False
right = False
while running:
    screen.blit(menu, (0, 0))
    screen.blit(car, (loc_x, loc_y))
    screen.blit(stop, (rand_x, rand_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_s:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_s:
                down = False

    if up == True:
        loc_y -= 2
        screen.blit(car, (loc_x, loc_y))
    if down == True:
        loc_y += 2
        screen.blit(car180, (loc_x, loc_y))
    if right == True:
        loc_x += 2
        screen.blit(car270, (loc_x, loc_y))
    if left == True:
        loc_x -= 2
        screen.blit(car90, (loc_x, loc_y))

    if loc_x <= 0:
        loc_x = 50
    if loc_x >= 1000:
        loc_x = 950
    if loc_y <= 0:
        loc_y = 20
    if loc_y >= 600:
        loc_y = 580


    #: Переворачиваем картинку 
    if up and right == True:
        screen.blit(car315, (loc_x, loc_y))
    if down and right == True:
        screen.blit(car225, (loc_x, loc_y))
    if up and left == True:
        screen.blit(car45, (loc_x, loc_y))
    if down and left == True:
        screen.blit(car135, (loc_x, loc_y))


    if loc_y and loc_x == rand_x and rand_y:
        running = False

    pygame.display.update()
    pygame.display.flip()

