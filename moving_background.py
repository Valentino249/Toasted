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
        self.speed = 6

        self.state = "up"

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.state = "move-up"
            print("up")
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.state = "move-down"
            print("down")

    def shift(self):
        if self.state == 'move-up':
            self.direction.y = 2
        elif self.state == 'move-down':
            self.direction.y = -2
        elif self.state == 'up' or self.state == 'down':
            self.direction.y = 0

        self.rect.y += self.direction.y

    def check_finished(self):
        if self.rect.bottom >= screen_height:
            self.state = "down"
        elif self.rect.top <= 0:
            self.state = "up"

    def update(self):
        print("update")
        self.get_input()
        self.shift()

