with open("glosor.txt", "r") as infil:
    for rad in infil:
        rad = rad.strip()

def läsFil (infil):
    lista = []
    for rad in infil:
        rad = rad.strip()
        lista.append(rad)
    infil.close()
    return lista

print("Hej")