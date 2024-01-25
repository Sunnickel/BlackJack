import itertools
import random

from Player import *

players = []
bank: Player = Player()
playing = True
deck = None


def get_deck():
    global deck
    deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
    random.shuffle(deck)
    return deck


def start():
    player_num = 0
    while not int(player_num) > 0:
        player_num = input("How many players are playing? $ ")
        if not player_num.isdigit():
            player_num = 0
    for i in range(int(player_num)):
        players.append(Player())
    bank.name = "Bank"
    players.append(bank)
    for i in range(2):
        for player in players:
            give_card(player)
    for i in range(len(players)):
        if (players[i]).name is None:
            (players[i]).name = input(f"What's your name Player{i + 1}? $ ")


def give_card(player: Player, hidden=False):
    player.add_to_hand(Card(deck[0], hidden=hidden))
    deck.pop(0)


def print_hand(player: Player):
    print(player.name)
    hand = player.hand
    output = ""
    for i in range(4):
        card: Card
        for card in hand:
            output += card.get_ascii()[i]
        output += "\n"
    print(output)
    print(f"Value: {player.get_value()}")


def over_21(player: Player):
    return player.get_value(True) > 21


def bid_money():
    for player in players:
        if player.name == "Bank":
            continue
        if player.money == 0:
            players.remove(player)
        print(players)
        print(f"{player.name}'s Money: {player.money}")
        has_enough = False
        if len(players) == 1:
            exit("All players are broke af")
        while not has_enough:
            player.bid = int(input(f"Set your bids {player.name} $ "))
            if player.bid > player.money:
                print("You don't have enough money!")
            elif player.bid <= 0:
                print("You need to bids at least 1$!")
            else:
                has_enough = True


def end_round(player: Player, ending: str):
    if ending == "push":
        player.money += player.bid
    elif ending == "win":
        player.money += player.bid * 2
    elif ending == "blackJack":
        player.money += player.bid * 2.5


def pause():
    for i in range(20):
        print("\n")


def play_game():
    player: Player
    bid_money()
    pause()
    for player in players:
        player.money -= player.bid
        for player1 in players:
            print_hand(player1)
        if player == bank or bank.get_value() == 21:
            bank_logic()
            print_hand(bank)
            player2: Player
            for player2 in players:
                if player2 == bank:
                    continue
                print(f"{player2.name}'s Value: {player2.get_value(True)}")
            continue
        turn = True
        if player.get_value(True) == 21:
            player.blackJack = True
            continue
        while turn:
            print("Options:\n"
                  "     [0] Double\n"
                  "     [1] Split\n"
                  "     [2] Stand\n"
                  "     [3] Hit\n")  # Options
            choice = input(f"{player.name} $ ")
            if choice == "0":
                player.bid *= 2
                give_card(player, True)
                turn = False
                pause()

            elif choice == "1":
                print("Hab keine Lust auf dieses Feature :D")

            elif choice == "2":
                turn = False
                pause()

            elif choice == "3":
                give_card(player)
                if over_21(player):
                    turn = False
                    continue
                pause()
            pause()
            for player1 in players:
                print_hand(player1)


def bank_logic():
    while bank.get_value() < 17:
        give_card(bank)
    player: Player
    for player in players:
        if player.blackJack:
            end_round(player, "blackJack")
        elif player.get_value() > 21:
            continue
        elif bank.get_value() < player.get_value(True):
            end_round(player, "win")
        elif bank.get_value() == player.get_value(True):
            end_round(player, "push")
    pause()


if __name__ == '__main__':
    deck = get_deck()
    start()
    while playing:
        play_game()
        if len(players) == 1:
            playing = False
