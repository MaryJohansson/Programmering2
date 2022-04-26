import random
class Glosor:

    def __init__(self, Engelska, Svenska):
        self.Engelska = Engelska
        self.Svenska = Svenska

    def __str__(self):
        return f"Engelska: {self.Engelska} Svenska: {self.Svenska}"

glosor = []
with open("glosor.txt", "r", encoding="utf8") as file:
    for row in file:
        row = row.strip("\n")
        row_list = row.split(";")
        glosor.append(Glosor(row_list[0],row_list[1]))


choice=[]
print("Välkommen till vårt glosförhör, detta kan du göra:")
while True:

    print("1. Kolla på glosor\n2. Öva på glosor (Engelska - Svenska)\n3. Öva på glosor (Svenska - Engelska)\n4. Avsluta glosförhöret")

    while(choices:=(input("Vad vill du göra?(välj en siffra)")).lower()) not in ["1","2","3","4"]:
        print("Välj vad du vill göra!")


    if choices == "1":
        print(*glosor, sep="\n")

    elif choices == "2":
        glosa = random.choice(glosor)
        print(glosa.Engelska)
        if (choices:=(input("Vad är ordet på svenska?")).lower()) == glosa.Svenska:
            print("Rätt!")

        else:
            print("Fel!")

    elif choices == "3":
        glosa = random.choice(glosor)
        print(glosa.Svenska)
        if (choices := (input("Vad är ordet på Engelska?")).lower()) == glosa.Engelska:
            print("Rätt!")

        else:
            print("Fel!")


    elif choices == "4":
        print("Hoppas att du har lärt dig något! Ha det bra:)")
        break

