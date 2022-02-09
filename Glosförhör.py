"""with open("glosor.txt", "r") as infil:
    for rad in infil:
        rad = rad.strip()

def läsFil (infil):
    lista = []
    for rad in infil:
        rad = rad.strip()
        lista.append(rad)
    infil.close()
    return lista
"""
glosor = []
with open("glosor.txt", "r") as file:
    for row in file:
        row = row.strip("\n")
        row_list = row.split(",")
        print(type(row_list), row_list)
