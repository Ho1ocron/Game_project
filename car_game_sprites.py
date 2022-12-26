import pygame
import sys
import os.path

script_dir = os.path.dirname(__file__)


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def _main_sprite(main_sprite_name):
    main_sprite = pygame.image.load(os.path.join(script_dir, main_sprite_name)).convert_alpha()
    main_sprite = pygame.transform.scale(main_sprite, (100, 200))
    main_sprite_versions = {
        0: pygame.transform.rotate(main_sprite, 0), #: Zero degrees
        45: pygame.transform.rotate(main_sprite, 45),   #: 45 degrees
        90: pygame.transform.rotate(main_sprite, 90),   #: 90 degrees
        135: pygame.transform.rotate(main_sprite, 135), #: 135 degrees
        180: pygame.transform.rotate(main_sprite, 180), #: 180 degrees
        225: pygame.transform.rotate(main_sprite, 225), #: 225 degrees
        270: pygame.transform.rotate(main_sprite, 270), #: 279 degrees
        315: pygame.transform.rotate(main_sprite, 315)  #: 315 degrees
    }
    return main_sprite_versions


def _enemy_sprite(enemy_sprite_name):
    enemy_sprite = pygame.image.load(os.path.join(script_dir, enemy_sprite_name)).convert_alpha()
    enemy_sprite = pygame.transform.scale(enemy_sprite, (200, 200))
    return enemy_sprite


def _background(background_name):
    background_path = os.path.join(script_dir, background_name)
    background = load_image(background_path)
    background = pygame.transform.scale(background, (1920, 1080))
    return background

    
if __name__ == "__main__":
    _enemy_sprite()
    _main_sprite()
    _background()
