from UrsinaClasses import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = True

def update():
    pass



for z in range(20):
	for x in range(20):
		voxel = Voxel((x,0,z))

player = FirstPersonController()

app.run()