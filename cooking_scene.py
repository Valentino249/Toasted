import pygame, os
from settings import tile_size
from tile import Tile
from moving_background import MovingBackground
from toast import Toast

class CookingScene:
    def __init__(self, surface, moving_background_img, white_img, golden_img, brown_img, black_img, flaming_img):
        self.display_surface = surface

        # Images
        self.moving_background_image = moving_background_img
        self.white_img = white_img
        self.golden_img = golden_img
        self.brown_img = brown_img
        self.black_img = black_img
        self.flaming_img = flaming_img

        # Making sprite groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.background = pygame.sprite.GroupSingle()
        self.toasts = pygame.sprite.Group()

        self.setup_scene()

    def setup_scene(self):
        bg_sprite = MovingBackground(self.moving_background_image)
        self.background.add(bg_sprite)
        left_toast_sprite = Toast('left', self.white_img, self.golden_img, self.brown_img, self.black_img, self.flaming_img)
        right_toast_sprite = Toast('right', self.white_img, self.golden_img, self.brown_img, self.black_img, self.flaming_img)
        self.toasts.add(left_toast_sprite)
        self.toasts.add(right_toast_sprite)

    def run(self):
        self.background.update()
        self.background.draw(self.display_surface)

        self.toasts.update()
        self.toasts.draw(self.display_surface)
