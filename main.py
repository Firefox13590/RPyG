from maps import map1, map2, map3
from shops import products
from character import Player
from enemies import *
from events import *
import random
import sys
import os

p = Player()
adventure = [map1, map2, map3]  #list of maps
progress = 0 #map progress
#print(map1)

while True:
    ClearText()
    cm = adventure[progress]  #current map
    cp = cm[p.y][p.x]  #current pos
    mvt = ""
    p.pos = [p.y, p.x]
    # print(cp)
    # print(p.pos)

    if cp == 2:
        if cm == map1:
            mob = random.choice((Slime(), Goblin(), CursedTree()))
        elif cm == map2:
            mob = random.choice((E4(), E5(), E6()))
        elif cm == map3:
            mob = random.choice((E7(), E8(), E9()))
        mob.currentHp = mob.maxHp
        Fight(p, mob)
    elif cp == 3:
        Buy(p)
    elif cp == 4:
        Trap(p)
    elif cp == 5:
        # print(cm)
        # print(map1)
        # print(cm == map1)
        if cm == map1:
            Fight(p, Wormathron())
        elif cm == map2:
            Fight(p, B2())
        elif cm == map3:
            Fight(p, B3())
            break
        if progress < 2:
            progress += 1

        p.x, p.y = (0, 0)

    while mvt == "":
        print("Choose which direction?\n")

        # direction available
        if p.y != 0 and cm[p.y - 1][p.x] != 0:
            print("W: North")
        if p.x != 0 and cm[p.y][p.x - 1] != 0:
            print("A: West")
        if p.y != 4 and cm[p.y + 1][p.x] != 0:
            print("S: South")
        if p.x != 4 and cm[p.y][p.x + 1] != 0:
            print("D: East")

        mvt = input("M: Show map\n> ").upper()

        # movement
        if mvt == "W" and p.y != 0 and cm[p.y - 1][p.x] != 0:
            p.y -= 1
        elif mvt == "A" and p.x != 0 and cm[p.y][p.x - 1] != 0:
            p.x -= 1
        elif mvt == "S" and p.y != 4 and cm[p.y + 1][p.x] != 0:
            p.y += 1
        elif mvt == "D" and p.x != 4 and cm[p.y][p.x + 1] != 0:
            p.x += 1
        elif mvt == "M":
            showMap(cm)
            pass
        else:
            EndScript(mvt)
            print("The road is blocked or the input is invalid")
            mvt = ""

# print("Thank you so much a-for-to playing my game!\n:D")
