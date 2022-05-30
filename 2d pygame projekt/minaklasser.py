import random

import pygame

class Spelare:
    def __init__(self, namn, x, y):
        self.x = x
        self.y = y
        self.namn = namn
        self.bild = pygame.image.load(namn)
        self.x_förändring = 0
        self.y_förändring = 0

class Yoda(Spelare):
    def __init__(self, namn, x, y):
        super(Yoda, self).__init__(namn, x, y)


class Mimmii(Spelare):
    def __init__(self, namn, x, y):
        super(Mimmii, self).__init__(namn, x, y)

class Fiender:

    def __init__(self):
        self.x = random.randint(50,750)
        self.y = 50
        self.bild = pygame.image.load('ursula64.png')
        self.x_förändring = 4
        self.y_förändring = 40

class Skott:

    def __init__(self):
        self.x = 0
        self.y = 480
        self.bild = pygame.image.load('lightsaber.png')
        self.y_förändring = 5
