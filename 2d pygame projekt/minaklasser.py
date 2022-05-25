import random

import pygame

class Spelare:

    def __init__(self):
        self.x = 440
        self.y = 480
        self.bild = pygame.image.load('yoda50')
        self.x_förändring = 0
        self.y_förändring = 0

class Spelare2:

    def __init__(self):
        self.x = 300
        self.y = 480
        self.bild = pygame.image.load('mimmii.png')
        self.x_förändring = 0
        self.y_förändring = 0

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
