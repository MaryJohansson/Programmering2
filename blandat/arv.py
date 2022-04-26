class Fordon:

    def __init__(self, märke,modell, årsmodell, vikt,motor):
        self.märke = märke
        self.modell = modell
        self.årsmodell = årsmodell
        self.vikt = vikt
        self.motor = motor

class Bil(Fordon):

    def __init__(self, märke,modell, årsmodell, vikt,motor):
        super(Bil, self).__init__(märke,modell, årsmodell, vikt,motor)


class Motorcykel(Fordon):

    def __init__(self, märke, modell, årsmodell, vikt, motor):
        super(Motorcykel, self).__init__(märke, modell, årsmodell, vikt, motor,"Motorcykel")


class Flygplan(Fordon):

    def __init__(self, märke, modell, årsmodell, vikt, motor):
        super(Flygplan, self).__init__(märke, modell, årsmodell, vikt, motor,"Flygplan")



bil="Mercedes-Benz", "G63", "2020", "2560kg", "4,0 l V8"
print(bil)