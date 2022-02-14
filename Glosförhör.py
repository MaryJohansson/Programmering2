import random
class Glosor:

    def __init__(self, Engelska, Svenska):
        self.Engelska = Engelska
        self.Svenska = Svenska

    def __str__(self):
        return f"Engelska: {self.Engelska} Svenska: {self.Svenska}"

glosor = []
with open("glosor.txt", "r",encoding="utf8") as file:
    for row in file:
        row = row.strip("\n")
        row_list = row.split(";")
        glosor.append(Glosor(row_list[0],row_list[1]))


choice=[]
print("Välkommen till vårt glosförhör, detta kan du göra:")
print("1. Kolla på glosor\n2. Öva på glosor (Engelska - Svenska)\n3. Öva på glosor (Svenska - Engelska)\n4. Lägg till glosa\n5. Ta bort glosa\n")

while (choices:=(input("Vad vill du göra?(välj en siffra)")).lower()) not in ["1","2","3","4","5"]:
    print("Välj vad du vill göra!")


if choices == "1":
    print(*glosor, sep="\n")

if choices == "2":
    glosa = random.choice(glosor)
    print(glosa.Engelska)
    while (choices:=(input("Vad är ordet på svenska?")).lower()) not in glosor:
        print("Prova igen!")

if choices == "3":
    print()

if choices == "4":
    print()

if choices == "5":
    print()




"""
    elif choice in ["2" , "look"]:
       print(*all_pokemon)
=======
        # Create a new X
        pass
    elif choice in ["2", "look"]:
        # Look at all X
        pass    
>>>>>>> 7497861dcf9b1d574652b621b4e691119adaafa2
    elif choice in ["3", "quit"]:
        break
    else:
        print("Not a case")"""