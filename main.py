import pygame, sys, os
from settings import screen_height, screen_width, scene_map
from display import Display
from scene import Scene
from cooking_scene import CookingScene

class GameState:
    """This class holds all the different game states (screens) that the game needs to display."""
    def __init__(self):
        self.state = 'title_screen'
        self.current_event = "none"
        self.sail_fixed = True
        self.tsunami_showing = False
        self.seagulls_showing = False
        self.wind_showing = False

    def title_screen(self):
        """Displays the title screen of the game."""
        # For loop below explained under main_game() method.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')
        title_display.view()
        if start_button.draw_btn(start_inverted_img):
            self.state = 'cooking_view'
        if exit_button.draw_btn(exit_inverted_img):
            pygame.quit()
            sys.exit()
        pygame.display.update()

    def main_game(self):
        """Displays all the gameplay while activated."""
        # This for loop cycles through all events and checks if the quit button was pressed.
        for event in pygame.event.get():
            # If we press quit the program stops running
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Displaying the background
        background_display.view()
        scene.run()
        pygame.display.update()

    def cooking_view(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        cooking_scene.run()
        pygame.display.update()


    def state_manager(self):
        """When the state_manager() method is run, the "state" attribute is checked and the corresponding screen is
            displayed."""
        if self.state == 'title_screen':
            self.title_screen()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'winning_screen':
            self.winning_screen()
        if self.state == 'losing_screen':
            self.losing_screen()
        if self.state == 'cooking_view':
            self.cooking_view()

# Setting up pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('You are on a B.O.A.T.')
clock = pygame.time.Clock()
fps = 60
game_state = GameState()

# Menu assets
start_img = pygame.image.load(os.path.join('assets', 'play_1.png')).convert_alpha()
start_inverted_img = pygame.image.load(os.path.join('assets', 'play_inverted_1.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join('assets', 'quit_1.png')).convert_alpha()
exit_inverted_img = pygame.image.load(os.path.join('assets', 'quit_inverted_1.png')).convert_alpha()
play_again_img = pygame.image.load(os.path.join('assets', 'play_again_1.png')).convert_alpha()
play_again_inverted_img = pygame.image.load(os.path.join('assets', 'play_again_inverted_1.png')).convert_alpha()
x_img = pygame.image.load(os.path.join('assets', 'x_1.png')).convert_alpha()
x_inverted_img = pygame.image.load(os.path.join('assets', 'x_2.png')).convert_alpha()
title_img = pygame.image.load(os.path.join('assets', 'title_1.png')).convert_alpha()
you_won_img = pygame.image.load(os.path.join('assets', 'you_won_1.png')).convert_alpha()
game_over_img = pygame.image.load(os.path.join('assets', 'game_over_1.png')).convert_alpha()

# Tile Sprites
char_img = pygame.image.load(os.path.join('assets', 'main_char_2.png')).convert_alpha()
tile_img = pygame.image.load(os.path.join('assets', 'whats_above_tile_2.png')).convert_alpha()
background_img = pygame.image.load(os.path.join('assets', 'background_3.png')).convert_alpha()
cooking_background_img = pygame.image.load(os.path.join('assets', 'bg_5.png')).convert_alpha()

# Creating Display instances
start_button = Display((100, screen_height - 225), start_img, screen, True)
exit_button = Display((screen_width - (100 + exit_img.get_width()), screen_height - 225), exit_img, screen, True)
play_again_button = Display((100, screen_height - 225), play_again_img, screen, True)
title_display = Display((0, 0), title_img, screen, False)
you_won_display = Display((screen_width / 2 - (you_won_img.get_width() / 2), 200), you_won_img, screen, False)
game_over_display = Display((screen_width / 2 - (game_over_img.get_width() / 2), 200), game_over_img, screen, False)
background_display = Display((0, 0), background_img, screen, False)

# Creating a scene instance
scene = Scene(scene_map, screen, char_img, tile_img)
cooking_scene = CookingScene(screen, cooking_background_img)

# Main game loop
while True:
    game_state.state_manager()
    clock.tick(fps)
