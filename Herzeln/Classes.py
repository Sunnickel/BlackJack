class Card:
    def __init__(self, card):
        self.value = card[0]
        self.type = card[1]
        self.types = {"Spade": "♠", "Heart": "♥", "Diamond": "◆", "Club": "♣"}
        self.cardInfo = {7: "7",
                         8: "8",
                         9: "9",
                         10: "T",
                         11: "J",
                         12: "Q",
                         13: "K",
                         14: "A"}

        def get_ascii(self):
            type = self.types[self.type]
            value = self.cardInfo[self.value]
            card = ["┌───┐",
                    f"│ {value} │",
                    f"│ {type} │",
                    "└───┘"]

            return card

        def get_value(self):
            return self.value
