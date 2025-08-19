import pygame, os
from settings import tile_size
from tile import Tile
from player import Player

class Scene:
    def __init__(self, scene_data, surface, char_img, tile_img):
        self.display_surface = surface

        # Images
        self.char_img = char_img
        self.tile_img = tile_img

        self.tile_coordinate_list = []

        # Making sprite groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        #Other
        self.player_life = "alive"

        self.setup_scene(scene_data)

    def setup_scene(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x,y), self.tile_img)
                    self.tiles.add(tile)
                    self.tile_coordinate_list.append((x, y))
                if cell == 'P':
                    # Places the player at the defined x and y positions if the cell contained 'P'.
                    player_sprite = Player((x, y), self.char_img)
                    # The respawn position of the player is set to the coordinates x, y.
                    self.player.respawn = (x, y)
                    self.player.add(player_sprite)

    def horizontal_movement_collision(self):
        """Handles the player movement updates and all horizontal collisions."""
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        # Checks every tile in the level.
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        """Handles vertical movement updates (applying gravity) and all vertical collisions."""
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.can_jump = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
            elif player.direction.y != 0:
                player.can_jump = False

    def run(self):
        # Level
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        if self.player_life == "dead":
            return "Game Over"

