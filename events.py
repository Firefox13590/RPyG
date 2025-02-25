from character import Player
from enemies import *
import random as r
import os
import sys

p = Player()
s = Slime()


def Fight(player, enemy):
    move = ""
    next = ""
    order = [player, enemy] if player.spd >= enemy.spd else [enemy, player]
    # if player.spd >= enemy.spd:
    #     order.append(player)
    #     order.append(enemy)
    # else:
    #     order.append(enemy)
    #     order.append(player)

    while True:
        for attacker in order:
            # print(attacker.__class__.__name__)
            defender = enemy if attacker == player else player
            # if attacker == player:
            #     defender = enemy
            #
            # else:
            #     defender = player

            defender.Stats()
            if attacker == player:
                player.Stats()
                move = input("\nWhat to do?\n"
                             "[1]: Attack\n"
                             "[2]: Use item\n"
                             "[3]: Leave\n> ")

                while not move.isdigit():
                    if move.upper() == "Q":
                        sys.exit()

                    move = input("Need a Number as input\n> ")
                    if int(move) not in (1, 2, 3):
                        print("Not a Number")
                        move = ""
            else:
                move = 1
            if int(move) == 1:
                dmg = r.choice(attacker.att)
                print(f"{attacker.__class__.__name__} Dealt {dmg} damage")
                defender.currentHp -= dmg
            if enemy.currentHp <= 0:
                ggain = r.choice(enemy.drop)  #gold gain
                print(f"Battle won\n{ggain} gold gained")
                return
            elif player.currentHp <= 0:
                print("Battle lost")
                sys.exit()

        next = input("> ")
        if next == next:
            if next.upper() == "Q":
                sys.exit()

            os.system("cls" if os.name == "nt" else "clear")
            # print(next)
            # print(next == next)
    pass

def Buy():
    pass


def Trap():
    pass


def Item():
    pass


# Fight(p, s)
