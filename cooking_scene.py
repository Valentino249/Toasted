import pygame, os
from settings import tile_size
from tile import Tile
from player import Player
from moving_background import MovingBackground

class CookingScene:
    def __init__(self, surface, moving_background_img):
        self.display_surface = surface

        # Images
        self.moving_background_image = moving_background_img

        # Making sprite groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.background = pygame.sprite.GroupSingle()
        self.setup_scene()

    def setup_scene(self):
        bg_sprite = MovingBackground(self.moving_background_image)
        self.background.add(bg_sprite)

    def run(self):
        self.background.update()
        self.background.draw(self.display_surface)
