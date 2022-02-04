# Travelbag
elever = ["Dante", "Vigor", "Jesper", "Jubin", "Daniel", "Fabian", "Johan", "Mary", "David", "Jorge", "Lukas",
          "Leonida", "Godson", "Ida", "Ludwig", "Leon", "Noah", "Alexandru", "Martin", "Gibie", "Jalil"]
elever.sort()
print("1. Skriv ut klasslistan\n"
                     "2. Lägg till elev\n"
                     "3. Ta bort en elev\n"
                     "4.Avsluta program\n"
                     "")
while True:
    klassval = input()

    if klassval == "1":
        for elev in elever:
            print(elev)

    elif klassval == "2":
        plus = input("Lägg till en elev")
        elever.append(plus)

    elif klassval == "3":
        bort = input("Vem vill du ta bort?")
        if bort in elever:
            elever.remove(bort)
        else:
            print("Den människan kan inte skrivas ut")


    elif klassval == "4":
        break
