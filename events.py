from character import Player
from enemies import *
from shops import products
import random
import os
import sys
import math

# p = Player()
# s = Slime()

"""
GAME EVENTS
"""
def Fight(player: Player, enemy: Enemy|Boss) -> None:
    """
    Handles enemy encounters
    :param Player player: Instance of player class
    :param Enemy|Boss enemy: Instance of child of enemy class
    :return: None
    """
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
                # enemy can only attack
                move = 1
            # possible battle actions
            if move == 1:
                dmg = abs(int(random.choice(attacker.att) - (defender.df / 10)))
                print(f"{attacker.__class__.__name__} Dealt {dmg} damage")
                defender.currentHp -= dmg
            elif move == 2: #player only action
                UseItem(player)
                enemy.Stats()
            # end battle conditions
            if enemy.currentHp <= 0:
                ggain = random.choice(enemy.drop)  #gold gain
                print(f"Battle won\n"
                      f"{ggain} gold gained")
                player.gold += ggain
                return
            elif player.currentHp <= 0:
                print("Battle lost")
                sys.exit()

        # intermediate step before clearing screen
        next = input("> ")
        if next == next:
            EndScript(next)
            ClearText()
            # print(next)
            # print(next == next)


def Buy(p):
    """
    Handles shop interactions
    :param p: Instance of player class
    :return: None
    """
    # sort shop products by price
    sortedShop = sorted(products.items(), key=lambda item: item[1][0])
    msg = ""

    while True:
        ClearText()
        index = 1
        print("You've stumbled into a shop!\n"
              "write the input shown inside [brackets] to purchase\n")

        for x, y in sortedShop:
            # display list of products
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
                    # change int meaning price to int meaning nb of items
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
    return


def Trap(p):
    """
    Handles trap
    :param p: Instance of player class
    :return: None
    """
    rng = random.choice(range(1, 21)) / 100
    print("Rng:", rng)
    dmg = math.ceil(p.maxHp * rng) if rng <= .04 else int(p.maxHp * rng)
    print("Dmg:", dmg)
    p.currentHp -= dmg

    if dmg > p.maxHp * .1:
        print("You stepped on a branch. ", end="")
    elif dmg > 1:
        print("You got hit by an interstellar alien laser. ", end="")
    else:
        print("You breathed a little too hard. ", end="")

    print(f"You took {dmg} damage")
    p.Stats()

    if p.currentHp <= 0:
        print("Died of skill issue")
        sys.exit()
    return


def UseItem(p):
    """
    Handles item use
    :param p: Instance of player class
    :return: None
    """
    ClearText()

    if len(p.inventory) == 0:
        # cant use an item that doesn't exist, duh
        print("Inventory empty: no action possible\n")
        return

    print(f"Help:\n"
          "Legend -> [ITEM] (Nb available, 'Description')\n"
          "Input item name to use it\n"
          "Not case sensitive\n"
          "Built-in text matching to avoid writing full name\n"
          "Still lose turn if no item selected\n")

    for el in p.inventory.items():
        # print currently available items from player inv
        print(f"[{el[0].upper()}]\t({el[1][0]}, \'{el[1][1]}\')")

    choice = input("> ").lower()
    EndScript(choice)

    # take list of currently available items from inv
    for item in p.inventory.keys():
        # print(item)

        # match user input with dict key
        if choice in item.lower():
            # print("Item found")
            p.inventory[item][0] -= 1

            # apply item effect
            if item.lower() == "health potion":
                print("You feel healthy")
                p.currentHp = p.maxHp
            elif item.lower() == "protein powder":
                print("You feel a bit stronger")
                p.minDmg += random.choice((1, 2))
            elif item.lower() == "bag of rocks":
                print("Strength cap slightly higher")
                p.maxDmg += random.choice(range(1, 4))
            elif item.lower() == "rings":
                print("Found the sonic fan")
                p.spd += random.choice((1, 2))
            elif item.lower() == "hammer":
                print("It just works!")
                p.df += random.choice((1, 2))
            elif item.lower() == "fat juicy bloody steamy steak":
                print("↑ ↑ ↓ ↓ ← → ← → B A Start Select")
                p.maxHp += random.choice(range(2, 6))
            elif item.lower() == "fighting tactics":
                print("Player learned Rollout!")
                p.chain += random.choice((1, 2))
            elif item.lower() == "mobility training":
                print("Average souls-like gamer")
                p.dodge += random.choice(range(1, 4))
            elif item.lower() == "guide of the Warrior":
                print("Peak damage")
                p.minDmg += random.choice(range(2, 5))
                p.maxDmg += random.choice(range(3, 6))
            elif item.lower() == "guide of the Paladin":
                print("Peak survivability")
                p.maxHp += random.choice(range(3, 8))
                p.df += random.choice(range(2, 4))
            elif item.lower() == "guide of the Hunter":
                print("Peak utility")
                p.chain += random.choice(range(2, 4))
                p.dodge += random.choice(range(3, 5))
            elif item.lower() == "dndice":
                print("LET'S GO GAMBLING")
                p.gold *= random.choice((0, 2))
            # remove item from inv if nb is 0
            if p.inventory[item][0] == 0:
                del p.inventory[item]

            break
        else:
            # print("Item not found")
            pass

    # print(p.inventory)
    return


"""
GENERAL FUNCTIONS
"""
def EndScript(input: str) -> None:
    """
    Shortcut to quickly end program
    :param str input: User input
    :return: None
    """
    if str(input).lower() == "q":
        exec(open("theEnd.py").read())
        sys.exit()
    return


def ClearText() -> None:
    """
    Clear terminal screen
    :return: None
    """
    # cls for windows, clear for linux and mac
    os.system("cls" if os.name == "nt" else "clear")
    return


def ValidInput(input: str, dataType) -> bool:
    """
    Validation process when needing user input to fit specific data type
    :param str input: User input
    :param dataType: Data type to match with
    :return: If input matches desired data type
    :raise ValueError: If type conversion isn't possible
    """
    EndScript(input)

    try:
        type(dataType(input))
    except ValueError:
        return False
    else:
        return True


# Fight(p, s)
# print(ValidInput("true", bool))
# print(bool("true") == bool)
# print(bool("true"))
