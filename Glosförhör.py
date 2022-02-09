dict = {}
with open("glosor.txt", "r") as infil:
    for rad in infil:
        rad = rad.strip()
        rad = rad.split(";")
        dict[rad[0]] = rad[1]

print(dict)



def läsFil (infil):
    lista = []
    for rad in infil:
        rad = rad.strip()
        lista.append(rad)
    infil.close()
    return lista