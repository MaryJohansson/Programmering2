from myclasses import *
window.borderless = False


def update():
    pass

app = Ursina()
sky = Sky()


window.fps_counter.enabled = False
window.exit_button.visible = True

for y in range(10):
    for x in range(10):
        voxel = Voxel((x, y, 0))


#for _ in range(5):
#    Target(mygame)


app.run()
