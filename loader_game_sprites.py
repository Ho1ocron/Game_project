import pygame
import os.path

script_dir = os.path.dirname(__file__)


def _main_sprite(main_sprite_name):
    main_sprite = pygame.image.load(os.path.join(script_dir, main_sprite_name)).convert_alpha()
    main_sprite = pygame.transform.scale(main_sprite, (200, 150))
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
    background = pygame.image.load(os.path.join(script_dir, background_name)).convert_alpha()
    background = pygame.transform.scale(background, (1920, 1080))
    return background

def _main_menu(main_menu_name):
    main_menu = pygame.image.load(os.path.join(script_dir, main_menu_name)).convert_alpha()
    main_menu = pygame.transform.scale(main_menu, (1920, 1080))
    return main_menu

    
if __name__ == "__main__":
    _enemy_sprite()
    _main_sprite()
    _background()
    _main_menu()
