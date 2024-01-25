import itertools, random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

from Player import *

players = []
playing = True
deck = None


def get_deck():
    deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    return deck


def start():
    bank = Player()
    playerNum = ""
    while not playerNum.isnumeric():
        playerNum = input("How many players are playing? $ ")
    for i in range(int(playerNum)):
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
    player.set_hand(Card(deck[0][0], deck[0][1], hidden=hidden))
    deck.pop(0)


def print_hand(player: Player, hidden=True):
    print(player.name)
    hand = player.hand
    output = ""
    for i in range(4):
        for card in hand:
            output += card.get_ascii()[i]
        output += "\n"
    print(output)
    if hidden:
        print(f"Value: {player.get_value()}")
    else:
        print(f"Value: {player.get_full_value()}")


def over_21(player: Player):
    if player.get_full_value() > 21:
        return True


def bid_money(player: Player):
    if player.name == "Bank":
        return
    hasEnough = False
    while not hasEnough:
        player.bid = (int)(input(f"Set your bids {player.name} $ "))
        if player.bid > player.money:
            print("You don't have enough money!")
        elif player.bid <= 0:
            print("You need to bids at least 1$!")
        else:
            hasEnough = True


def push(player: Player):
    player.money += player.bid


def win(player: Player):
    player.money += player.bid * 2


def black_jack(player: Player):
    player.money += player.bid * 2.5


def pause():
    for i in range(20):
        print("\n")


def play_game():
    for player in players:
        if player.name == "Bank":
            continue
        if player.money == 0:
            players.remove(player)
        print(f"{player.name}'s Money: {player.money}")
        bid_money(player)
    pause()
    for player in players:
        player.money -= player.bid
        for player1 in players:
            print_hand(player1)
        if player.name == "Bank" or players[-1].get_full_value() == 21:
            bank_logic()
            print_hand(player, False)
            for player2 in players:
                if player2.name == "Bank":
                    continue
                print(f"{player2.name}'s Value: {player2.get_full_value()}")
            for player3 in players:
                if player3.name == "Bank":
                    continue

            continue
        turn = True
        if player.get_value() == 21:
            # TODO: BLACKJACK
            player.blackJack = True
            continue
        while turn:
            name = player.name

            print("Options:\n"
                  "     [0] Double\n"
                  "     [1] Split\n"
                  "     [2] Stand\n"
                  "     [3] Hit\n")
            choice = input(f"{name} $ ")
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
    bank: Player = players[-1]
    while bank.get_full_value() < 17:
        give_card(bank, False)
    for player in players:
        if player.blackJack:
            black_jack(player)
        elif player.get_full_value() > 21:
            continue
        elif bank.get_value() < player.get_full_value():
            win(player)
        elif bank.get_value() == player.get_full_value():
            push(player)
    pause()


if __name__ == '__main__':
    deck = get_deck()
    start()
    while playing:
        play_game()
        if len(players) == 1:
            playing = False
