import pygame
from settings import screen_height, screen_width


class Toast(pygame.sprite.Sprite):
    def __init(self, side, white_img, golden_image, brown_img, black_img, flaming_img):
        super().__init__()
        # Image Imports
        self.white_img = white_img
        self.golden_img = golden_image
        self.brown_img = brown_img
        self.black_img = black_img
        self.flaming_img = flaming_img

        self.side = side
        self.image = white_img
        if side == 'right':
            self.image = pygame.transform.flip(self.image, True, False)

        self.face = 0
        self.rect = self.image.get_rect(topleft=(0, (screen_height - self.image.get_height())))
        if side == 'right':
            self.rect = self.image.get_rect(topleft=((screen_width - self.image.get_width()), (screen_height - self.image.get_height())))

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 12

        self.pos = "up"

    def get_input(self):
        keys = pygame.key.get_pressed()
        if self.side == 'left':
            toggle = keys[pygame.K_a]
            arrow_toggle = keys[pygame.K_LEFT]
        else:
            toggle = keys[pygame.K_d]
            arrow_toggle = keys[pygame.K_RIGHT]
        if toggle or arrow_toggle:
            if self.pos == 'down':
                self.pos = 'move-up'
            elif self.pos == 'up':
                self.pos = 'move-down'

    def shift(self):
        if self.pos == 'move-up':
            self.direction.y = 1
        elif self.pos == 'move-down':
            self.direction.y = -1
        elif self.pos == 'up' or self.pos == 'down':
            self.direction.y = 0

        self.rect.y += self.direction.y * self.speed

    def stop_movement(self):
        if self.rect.top >= screen_height:
            self.pos = 'down'
        elif self.rect.bottom <= screen_height:
            self.pos = "up"

    def update(self):
        self.get_input()
        self.stop_movement()
        self.shift()
