from character import Player
from enemies import *
from shops import products
import random as r
import os
import sys

# p = Player()
# s = Slime()

"""
GAME EVENTS
"""
def Fight(player, enemy):
    move = ""
    next = ""
    order = [player, enemy] if player.spd >= enemy.spd else [enemy, player]

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

                while not (ValidInput(move, int) and (move in ("1", "2", "3"))):
                    move = input("Need a Number from 1 to 3 as input\n> ")

                move = int(move)
            else:
                move = 1
            # possible battle actions
            if move == 1:
                dmg = r.choice(attacker.att)
                print(f"{attacker.__class__.__name__} Dealt {dmg} damage")
                defender.currentHp -= dmg
            elif move == 2: #player only action
                UseItem(player)
                enemy.Stats()
            # end battle conditions
            if enemy.currentHp <= 0:
                ggain = r.choice(enemy.drop)  #gold gain
                print(f"Battle won\n"
                      f"{ggain} gold gained")
                player.gold += ggain
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

def Buy(p):
    sortedShop = sorted(products.items(), key=lambda item: item[1][0])
    msg = ""

    while True:
        ClearText()
        index = 1
        print("You've stumbled into a shop!\n"
              "write the input shown inside [brackets] to purchase\n")

        for x, y in sortedShop:
            print(f"[{index}]\t{x}: {y[0]}g, \"{y[1]}\"")
            index += 1

        print(f"[Other input]\tNothing: free, \"Social interaction is scary\"\n\n"
              f"{msg}\n"
              f"Gold remaining: {p.gold}g")
        purchase = input("What to buy?\n> ")

        if ValidInput(purchase, int):
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
                    p.inventory[sortedShop[purchase - 1][0]] = sortedShop[purchase - 1][1] #add (key, value) pair
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


def UseItem(p):
    ClearText()

    if len(p.inventory) == 0:
        print("Inventory empty: no action possible\n")
        return

    print(f"Help:\n"
          "Legend -> [ITEM] (Nb available, 'Description')\n"
          "Input item name to use it\n"
          "Not case sensitive\n"
          "Built-in text matching to avoid writing full name\n"
          "Still lose turn if no item selected")
    print()

    for el in p.inventory.items():
        print(f"[{el[0].upper()}]\t({el[1][0]}, \'{el[1][1]}\')")

    choice = input("> ").lower()
    EndScript(choice)

    for item in p.inventory.keys():
        print(item)

        if choice in item.lower():
            print("Item found")
            p.inventory[item][0] -= 1

            if item.lower() == "health potion":
                print("Used Health potion")
                p.currentHp = p.maxHp
                p.Stats()
            if p.inventory[item][0] == 0:
                del p.inventory[item]

            break
        else:
            print("Item not found")

    print(p.inventory)
    pass


"""
GENERAL FUNCTIONS
"""
def EndScript(input: object) -> None:
    """
    Helps with testing by exiting the program
    :param object input: User input
    :return: None
    """
    if str(input).lower() == "q":
        sys.exit()
    pass


def ClearText():
    os.system("cls" if os.name == "nt" else "clear")
    pass


def ValidInput(input: str, dataType) -> bool:
    """

    :param str input: User input
    :param dataType: Data type to match with
    :return: bool
    """
    EndScript(input)

    try:
        type(dataType(input))
    except ValueError:
        return False
    else:
        return True
    # if type(dataType(input)) == dataType:
    #     return True
    # else:
    #     return False


# Fight(p, s)
# print(ValidInput("true", bool))
# print(bool("true") == bool)
# print(bool("true"))
