from ursina import *
from ursinanetworking import *

Server = UrsinaNetworkingServer("10.154.198.116", 25565)
Easy = EasyUrsinaNetworkingServer(Server)

@Server.event
def onClientConnected(Client):
    Easy.create_replicated_variable(Client.name, {"Position" : (10, 20, 10) })

@Server.event
def onClientDisconnected(Client):
    Easy.remove_replicated_variable_by_name(Client.name)

@Server.event
def Move(Client, NewPos):
    Easy.update_replicated_variable_by_name(Client.name, "Position" , NewPos)


def createworld():
    Easy.create_replicated_variable("World", {"Position":(0,0,0), "Scale":(10,1,10)})


createworld()
while True:
    Server.process_net_events()
    Easy.process_net_events()