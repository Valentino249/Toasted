import pygame

class Face():

    def __init__(self, heat_level, state):
        self.heat_level = heat_level
        self.state = state

    def cook(self):
        self.heat_level += 1

    def change_state(self):
        if self.heat_level >= 3120:
            self.state = 'flaming'
        elif 2700 <= self.heat_level < 3120:
            self.state = 'black'
        elif 1800 <= self.heat_level < 2700:
            self.state = 'brown'
        elif self.heat_level > 1800:
            self.state = 'golden'

    def update(self):
        self.cook()
        self.change_state()
