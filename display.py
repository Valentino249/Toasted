import pygame


class Display:
    def __init__(self, pos, image, display_surface, press_able):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = self.image.get_rect(topleft=pos)
        self.display_surface = display_surface
        self.press_able = press_able
        self.clicked = False

    def view(self):
        self.display_surface.blit(self.image, (self.rect.x, self.rect.y))

    def draw_btn(self, inverted_img):
        """Draws a button on the screen. Takes in an image that is displayed when the cursor is hovering over
        the button. Returns True if the button is pressed using the left mouse button. Returns False if the left
        mouse button is no longer clicking the button."""
        action = False
        pos = pygame.mouse.get_pos()
        self.display_surface.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.collidepoint(pos):
            self.display_surface.blit(inverted_img, (self.rect.x, self.rect.y))
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action