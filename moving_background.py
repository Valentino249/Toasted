import pygame
from settings import screen_height, screen_width


class MovingBackground(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.width = image.get_width()
        self.rect = self.image.get_rect(topleft=(0, 0))

        # Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 12

        self.state = "up"

    def get_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.state == "down":
            self.state = "move-up"
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.state == "up":
            self.state = "move-down"
    def shift(self):
        if self.state == 'move-up':
            self.direction.y = 1
        elif self.state == 'move-down':
            self.direction.y = -1
        elif self.state == 'up' or self.state == 'down':
            self.direction.y = 0

        self.rect.y += self.direction.y * self.speed

    def check_finished(self):
        if self.rect.bottom <= screen_height:
            self.state = "down"
        elif self.rect.top >= 0:
            self.state = "up"

    def update(self):
        print(self.state)
        self.check_finished()
        self.get_input()
        self.shift()

