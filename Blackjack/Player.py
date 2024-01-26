class Player:
    def __init__(self):
        self.name = None
        self.hand = []
        self.money = 250
        self.cardInfo = {
            "0": 0,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 8,
            "10": 10,
            "11": 10,
            "12": 10,
            "13": 10,
        }
        self.bid = 0
        self.blackJack = False

    def get_value(self, show_All=False):
        value = 0
        card: Card
        for card in self.hand:
            if card.hidden and not show_All:
                continue
            if card.get_value() == 14:
                if value + 10 > 21:
                    value += 1
                else:
                    value += 11
                continue
            value += self.cardInfo[f"{card.get_value()}"]
        return value

    def add_to_hand(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []


class Card:
    def __init__(self, card, hidden=False):
        self.value = card[0]
        self.type = card[1]
        self.types = {
            "Spade": "♠",
            "Heart": "♥",
            "Diamond": "◆",
            "Club": "♣"
        }
        self.cardInfo = {
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "T",
            11: "J",
            12: "Q",
            13: "K",
            14: "A"
        }
        self.hidden = hidden

    def get_ascii(self):
        if not self.hidden:
            type = self.types[self.type]
            value = self.cardInfo[self.value]
            card = [
                "┌───┐",
                f"│ {value} │",
                f"│ {type} │",
                "└───┘"
            ]
        else:
            card = [
                "┌───┐",
                "│ ? │",
                "│ ? │",
                "└───┘"
            ]

        return card

    def get_value(self):
        if not self.hidden:
            return self.value
        else:
            return 0
