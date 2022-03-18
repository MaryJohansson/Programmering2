class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other

        elif isinstance(other, str):
            return self.suit < other

        elif isinstance(other, Card):
            if self.value < other.value:
                return True
            elif self.value > other.value:
                return False

    def __gt__(self, other):
        if isinstance(other, int):
            return self.value > other

        elif isinstance(other, str):
            return self.suit > other

        elif isinstance(other, Card):
            if self.value > other.value:
                return True
            elif self.value < other.value:
                return False

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other

        elif isinstance(other, str):
            return self.suit == other

        elif isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit


suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = []
for value in range(1, 14):
    for suit in suits:
        card = Card(value, suit)
        cards.append(card)

for c in cards:
    if c == 10:
        print(c)

print("")

for c in cards:
    if c == 11 and c == "Diamonds":
        print("Jack of Diamonds")
    elif c == 12 and c == "Diamonds":
        print("Queen of Diamonds")
    elif c == 13 and c == "Diamonds":
        print("King of Diamonds")

print("")

card = Card(5, "Diamonds")
for c in cards:
    if c == card:
        print(c)

for c in cards:
    if c == 5 and c > card:
        print(c)
