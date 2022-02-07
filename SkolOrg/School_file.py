class School:

    def __init__(self,id, name, adress, *programs):
        self.id = id
        self.name = name
        self.adress = adress
        self.programs = programs

    def __str__(self):
        return f"Id:{self.id} Name:{self.name} Adress:{self.adress}  Programs:{self.programs}"
school=[]
nti=School("1","NTI Vetenskapsgymnasiet Solna", "Tomtebodavägen 5", "Science", "Technology" )
lbs=School("2", "LBS Kreativa Norra", "Tomtebodavägen 5", "Technology", "Aesthete")
school.append(nti)
school.append(lbs)
print(*school,sep="\n")

