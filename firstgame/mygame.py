from UrsinaClasses import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Game:

    def __init__(self):
        self.player = Entity(model="yoda.obj", position=(1,1,1), scale = 0.90)
        self.player.gravity=0


app = Ursina()
mygame = Game()

window.fps_counter.enabled = False
window.exit_button.visible = True

sky = Sky()


def update():
    mygame.player.x += held_keys["d"] * time.dt
    mygame.player.x -= held_keys["a"] * time.dt
    mygame.player.z += held_keys["w"] * time.dt
    mygame.player.z -= held_keys["s"] * time.dt



for z in range(20):
    for x in range(20):
        voxel = Voxel((x, 0, z))

for _ in range(5):
    Target(mygame)

camera.parent = mygame.player
camera.position = (0, 11, -20)
camera.rotation = (30, 0, 0)
app.run()
