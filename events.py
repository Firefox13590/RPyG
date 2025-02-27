from character import Player
from enemies import *
import random as r
import os
import sys
from shops import products

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
            defender.Stats()

            if attacker == player:
                player.Stats()
                move = input("\nWhat to do?\n"
                             "[1]: Attack\n"
                             "[2]: Use item\n"
                             "[3]: Leave\n> ")

                while not move.isdigit():
                    EndScript(move)

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
                p.gold += ggain
                return
            elif player.currentHp <= 0:
                print("Battle lost")
                sys.exit()

        next = input("> ")
        if next == next:
            EndScript(next)

            ClearText()
            # print(next)
            # print(next == next)
    pass

def Buy():
    sortedShop = sorted(products.items(), key=lambda item: item[1][0])
    msg = ""

    while True:
        ClearText()
        index = 1

        for x, y in sortedShop:
            print(f"[{index}]\t{x}: {y[0]}g, \"{y[1]}\"")
            index += 1

        print(f"[Other input]\tNothing: free, \"Social interaction is scary\"\n\n")
        print(msg)
        print(f"Gold remaining: {p.gold}g")
        purchase = input("What to buy?\n> ")
        EndScript(purchase)

        if purchase.isdigit():
            purchase = int(purchase)
        else:
            print("You're out")
            break

        if purchase in range(1, 13): #if input match options
            # print(sortedShop[purchase - 1][1][0])
            if p.gold < sortedShop[purchase - 1][1][0]:
                msg = "Too poor to afford item"
            else:
                if sortedShop[purchase - 1][0] not in p.inventory: #add item in inv
                    # print("not in inv")
                    # print(sortedShop[purchase - 1])
                    p.inventory[sortedShop[purchase - 1][0]] = sortedShop[purchase - 1][1][:2] #set (key, value) pair
                    # change int for price to int for nb of items
                    info = list(p.inventory[sortedShop[purchase - 1][0]])
                    info[0] = 1
                    # print(info)
                    p.inventory[sortedShop[purchase - 1][0]] = info
                    # print(p.inventory)
                    pass
                else: #increase item count in inv
                    # print("in inv")
                    p.inventory[sortedShop[purchase - 1][0]][0] += 1
                    pass
                # print(f"\n{p.inventory}") #player inv
                # print(sortedShop[purchase - 1][0]) #key part
                # print(p.inventory[sortedShop[purchase - 1][0]]) #value part
                # print(f"{p.inventory[sortedShop[purchase - 1][0]][0]}\n") #nb of items
                msg = "item bought succesfully"
                p.gold -= sortedShop[purchase - 1][1][0]
        else:
            print("You're out")
            break
    pass


def Trap():
    pass


def Item():
    pass


def EndScript(input):
    if str(input).upper() == "Q":
        sys.exit()
    pass


def ClearText():
    os.system("cls" if os.name == "nt" else "clear")
    pass

# Fight(p, s)
