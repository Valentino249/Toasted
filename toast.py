import pygame
from settings import screen_height, screen_width
from face import Face
import time
from support import *


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

        self.face_1 = Face(0, 'white', '1')
        self.face_2 = Face(0, 'white', '2')
        self.face_down = self.face_1
        self.face_up = self.face_2
        # Keeps flip [SPACE] from double triggering
        self.flip_count = 0

        self.import_toast_assets()
        self.animation_speed = 0.125
        self.frame_index = 0
        self.image = self.animations['white_idle'][self.frame_index]
        self.animation_status = 'white_idle'
        self.setup_toast()


    def import_toast_assets(self):
        toast_path = 'assets/toast/'
        self.animations = {'white_idle':[], 'white_rotate':[]}

        for animation in self.animations.keys():
            full_path = toast_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.animation_status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            if self.animation_status == 'white_rotate':
                self.animation_status = 'white_idle'

        print(self.frame_index)
        image = animation[int(self.frame_index)]
        self.image = image


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
        if keys[pygame.K_SPACE]:
            self.animation_status = 'white_rotate'
            self.toggle_face_down()
            self.flip_count += 1
        else:
            self.flip_count = 0

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
            self.face_down.update()

    def toggle_face_down(self):
        if self.flip_count == 1 and self.pos == "up":
            if self.face_down == self.face_1:
                self.face_down = self.face_2
                self.face_up = self.face_1
            else:
                self.face_down = self.face_1
                self.face_up = self.face_2
            self.set_image()

    def set_image(self):
        if self.face_up.state == 'white':
            print('setting image to white')
            self.image = self.white_img
        if self.face_up.state == 'golden':
            print('setting image to golden')
            self.image = self.golden_img
        if self.face_up.state == 'brown':
            self.image = self.brown_img
        if self.face_up.state == 'black':
            self.image = self.black_img
        if self.face_up.state == 'flaming':
            self.image = self.flaming_img

    def update(self):
        self.stop_movement()
        self.get_input()
        self.shift()
        self.cook()
        self.animate()
        # print(self.pos)