import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        # Main setup
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


class Lookout(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # Main setup
        self.image = pygame.Surface((size, size))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft=pos)


class Fire(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        # Main setup
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)