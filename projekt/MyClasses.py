from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class PlayerRepresentation(Entity):

    def __init__(self, position, name):
        super(PlayerRepresentation, self).__init__(model="yoda.obj", position=position, gravity=0, scale=0.3)
        self.name = name

class Game:

    def __init__(self):
        self.player = FirstPersonController( position=(10,10,10), scale = 0.3)


class Voxel(Button):
    def __init__(self, position):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture="yoda.jpg",
            color=color.white,
            scale=0.989)

class Ground(Entity):

    def __init__(self, scale=(1, 1, 1), position=(0, 0, 0)):
        super(Ground, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            color=rgb(128, 128, 0),
            collider='box',
            scale=scale
        )

class Target(Entity):

    def __init__(self, game):
        test = random.random()
        self.game = game
        if test < 0.25:
            position = (20, random.randrange(3, 7), random.randrange(0, 20))

        elif test < 0.5:
            position = (0, random.randrange(3, 7), random.randrange(0, 20))

        elif test < 0.75:
            position = (random.randrange(0, 20), random.randrange(3, 7), 20)

        else:
            position = (random.randrange(0, 20), random.randrange(3, 7), 0)

        self.speed = 5
        super(Target, self).__init__(
            parent=scene,
            model="cube",
            texture="ursula.jpg",
            position=position,
            collider='cube',

        )

    def input(self, key):
        if self.hovered and key == 'left mouse down':
            destroy(self)

    def update(self):
        self.lookAt(self.game.player.position + (0, 3, 0))
        self.position += self.forward * self.speed * time.dt

class Enemy(Entity):

    def __init__(self, scale=(1, 1, 1), position=(0, 0, 0)):
        super(Enemy, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            color=rgb(128, 128, 0),
            collider='box',
            scale=scale
        )