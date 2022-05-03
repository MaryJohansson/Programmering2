from MyClasses import *
from ursinanetworking import *

Client = UrsinaNetworkingClient("10.154.198.116", 25565)
Easy = EasyUrsinaNetworkingClient(Client)

Players = {}

window.borderless = False

@Client.event
def onConnectionEstablished():
    print("Connected")

@Easy.event
def onReplicatedVariableCreated(variable):
    print(variable)
    Players[variable.name] = PlayerRepresentation(name = variable.name, position = variable.content["Position"])

@Easy.event
def onReplicatedVariableUpdated(variable):
    Players[variable.name].position = variable.content["Position"]

@Easy.event
def onReplicatedVariableRemoved(variable):
    destroy(Players[variable.name])

def Move(Vec):
    Client.send_message("Move", Vec)

def update():
    Client.process_net_events()
    Easy.process_net_events()
    Move(mygame.player.position)

app = Ursina()
sky = Sky()


window.fps_counter.enabled = False
window.exit_button.visible = True

for z in range(20):
    for x in range(20):
        voxel = Voxel((x, 0, z))



mygame = Game()

#for _ in range(5):
#    Target(mygame)
app.run()
