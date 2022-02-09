class Glosor:

    def __init__(self, English, Swedish):
        self.English = English
        self.Swedish = Swedish

    def __str__(self):
        return f"English: {self.English} Swedish: {self.Swedish}"

glosor = []
with open("glosor.txt", "r",encoding="utf8") as file:
    for row in file:
        row = row.strip("\n")
        row_list = row.split(";")
        glosor.append(Glosor(row_list[0],row_list[1]))
print(*glosor,sep="\n")

