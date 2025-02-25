from character import Player
from enemies import Slime, Goblin, CursedTree, E4, E5, E6, Wormathron, B2, B3
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
                defender.currenthp -= dmg
            if enemy.currenthp <= 0:
                ggain = r.choice(enemy.drop)  #gold gain
                print(f"Battle won\n{ggain} gold gained")
                return
            elif player.currenthp <= 0:
                print("Battle lost")
                return

        next = input("> ")
        if next == next:
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            # print(next)
            # print(next == next)


def Buy():
    pass


def Trap():
    pass


# Fight(p, s)
