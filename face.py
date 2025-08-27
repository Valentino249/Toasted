import pygame

class Face():

    def __init__(self, heat_level, state, num):
        self.heat_level = heat_level
        self.state = state
        self.num = num

    def cook(self):
        self.heat_level += 1

    def change_state(self):
        if self.heat_level >= 3300:
            self.state = 'flaming'
        elif 3120 <= self.heat_level < 3300:
            self.state = 'black'
        elif 2700 <= self.heat_level < 3120:
            self.state = 'brown'
        elif 800 <= self.heat_level < 2700:
            self.state = 'golden'

    def update(self):
        self.cook()
        self.change_state()
