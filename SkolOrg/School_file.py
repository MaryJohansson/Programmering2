class School:

    def __init__(self,id, name, adress, *programs):
        self.id = id
        self.name = name
        self.adress = adress
        self.programs = programs

        def __str__(self):
            return f"Id:{self.id} Name:{self.name} Adress:{self.adress}  Programs:{self.programs}"

nti=School("1","NTI Vetenskapsgymnasiet Solna", "Tomtebodavägen 5", "Science", "Technology" )
print(nti)

