import pygame, os


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.width = image.get_width()
        self.rect = self.image.get_rect(topleft=pos)

        # Movement setup
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 0.6
        self.jump_speed = -12
        self.can_jump = False
        self.respawn

        self.action_state = "none"

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.can_jump:
            self.jump()
        if keys[pygame.K_LSHIFT] and self.direction.x == 0:
            self.action_state = "working"
        elif keys[pygame.K_w] and self.can_jump:
            self.action_state = "climbing"
        elif keys[pygame.K_s] and self.can_jump:
            self.action_state = "descending"
        else:
            self.action_state = "none"
        # print(self.action_state)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        """"When this method is called, self.direction.y is automatically set to the jump speed. Takes in the
                argument "negative", which can be used if the player's jump needs to be inverted. All changes in y are
                multiplied by the "negative" argument."""
        self.direction.y = self.jump_speed
        self.can_jump = False

    def get_direction_y(self):
        return self.direction.y

    def get_width(self):
        return self.width

    def respawn(self, pos):
        self.rect = self.image.get_rect(topleft=pos)
        self.direction.x = 0
        self.direction.y = 0

    def update(self):
        self.get_input()

