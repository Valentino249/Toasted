import pygame
from settings import screen_height, screen_width
from face import Face


class Toast(pygame.sprite.Sprite):
    def __init__(self, side, white_img, golden_image, brown_img, black_img, flaming_img):
        super().__init__()
        # Image Imports
        self.white_img = white_img
        self.golden_img = golden_image
        self.brown_img = brown_img
        self.black_img = black_img
        self.flaming_img = flaming_img

        self.face = 0
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 20
        self.pos = 'up'
        self.side = side

        self.image = self.white_img
        self.rect = self.image.get_rect(topleft=(0, (screen_height - self.image.get_height())))

        self.face_1 = Face(0, 'white')
        self.face_2 = Face(0, 'white')
        self.face_down = 1

        self.setup_toast()

    def setup_toast(self):
        if self.side == 'right':
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(
                topleft=((screen_width - self.image.get_width()), (screen_height - self.image.get_height())))

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
            self.direction.y = -1
        elif self.pos == 'move-down':
            self.direction.y = 1
        elif self.pos == 'up' or self.pos == 'down':
            self.direction.y = 0

        self.rect.y += self.direction.y * self.speed

    def stop_movement(self):
        if self.rect.top >= screen_height:
            self.pos = 'down'
        elif self.rect.bottom <= screen_height:
            self.pos = "up"

    def cook(self):
        if self.pos == 'up':
            if self.face_down == 1:
                self.face_1.update()
            elif self.face_down == 2:
                self.face_2.update()

    def update(self):
        self.stop_movement()
        self.get_input()
        self.shift()
        self.cook()
        print(self.face_1.state, self.face_1.heat_level)
        # print(self.pos)