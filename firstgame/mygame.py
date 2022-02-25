from UrsinaClasses import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Game:

    def __init__(self):
        self.player = FirstPersonController()


app = Ursina()
mygame = Game()

window.fps_counter.enabled = False
window.exit_button.visible = True

sky = Sky()


def update():
    pass


for z in range(20):
    for x in range(20):
        voxel = Voxel((x, 0, z))
Target(mygame)

app.run()
