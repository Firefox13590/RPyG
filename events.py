from character import Player
from ennemies import Slime, Goblin, CursedTree, E4, E5, E6, Wormathron, B2, B3
import random as r
import os
import sys

p = Player()
s = Slime()


def Fight(player, ennemy):
    tord = []  #turn order
    if player.spd >= ennemy.spd:
        tord.append(player)
        tord.append(ennemy)
    else:
        tord.append(ennemy)
        tord.append(player)

    while True:
        ennemy.Stats()
        move = input("\nWhat to do?\n"
                     "[1]: Attack\n"
                     "[2]: Use item\n"
                     "[3]: Leave\n> ")

        while not move.isdigit():
            if move.upper() == "Q":
                sys.exit()

            move = input("Need a Number as input\n> ")
            if int(move) not in (1, 2, 3):
                print("Not a valid number")
                move = ""

        os.system('cls' if os.name == 'nt' else "printf '\033c'")

        if move == "1":
            dmg = r.choice(player.att)
            print(f"\nDealt {dmg} damage")
            ennemy.currenthp -= dmg

        if ennemy.currenthp <= 0:
            ggain = r.choice(ennemy.drop)  #gold gain
            print(f"Battle won\n{ggain} gold gained")
            break
        elif player.currenthp <= 0:
            print("Battle lost, loser")
            break

    return


def Buy():
    pass


def Trap():
    pass


Fight(p, s)
