from maps import map1, map2, map3
from shops import products
from character import Player
from ennemies import Slime, Goblin, CursedTree, E4, E5, E6, Wormathron, B2, B3
from events import Fight, Buy, Trap
import random as r
import sys

p = Player()
explo = True
adventure = [map1, map2, map3]  #list of maps

s = Slime()
g = Goblin()

#print(map1)

while explo:
    cm = adventure[0]  #current map
    cp = cm[p.y][p.x]  #current pos
    mvt = ""
    p.pos = [p.y, p.x]

    print(cp)
    print(p.pos)

    if cp == 2:
        #mob = r.choice((s, g))
        mob = s
        Fight(p, mob)
    elif cp == 3:
        Buy()
    elif cp == 4:
        Trap()
    elif cp == 5:
        if cm == map1:
            Fight(p, Wormathron)
        elif cm == map2:
            Fight(p, B2)
        elif cm == map3:
            Fight(p, B3)

    while mvt == "":
        print("Choose which direction?\n")
        if p.y != 0 and cm[p.y - 1][p.x] != 0:
            print("W: North")
        if p.x != 0 and cm[p.y][p.x - 1] != 0:
            print("A: West")
        if p.y != 4 and cm[p.y + 1][p.x] != 0:
            print("S: South")
        if p.x != 4 and cm[p.y][p.x + 1] != 0:
            print("D: East")
        mvt = input("> ").upper()
        if mvt == "W" and p.y != 0 and cm[p.y - 1][p.x] != 0:
            p.y -= 1
        elif mvt == "A" and p.x != 0 and cm[p.y][p.x - 1] != 0:
            p.x -= 1
        elif mvt == "S" and p.y != 4 and cm[p.y + 1][p.x] != 0:
            p.y += 1
        elif mvt == "D" and p.x != 4 and cm[p.y][p.x + 1] != 0:
            p.x += 1
        elif mvt == "Q":
            sys.exit()
        else:
            print("the road is blocked or the input is invalid")
            mvt = ""
