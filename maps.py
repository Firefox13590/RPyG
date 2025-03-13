
"""
0 = wall
1 = path
2 = enemy
3 = shop
4 = trap
5 = boss
"""

map1 = [[1, 1, 2, 1, 1],
        [0, 0, 0, 0, 2],
        [4, 1, 2, 1, 3],
        [4, 2, 0, 0, 0],
        [4, 2, 1, 3, 5]]
map2 = [[1, 4, 2, 2, 3],
        [1, 0, 0, 1, 0],
        [2, 2, 0, 1, 0],
        [0, 1, 2, 1, 2],
        [3, 4, 4, 0, 5]]
map3 = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
world = (map1, map2, map3)

# print(map1)
# print(map2)
# print(map3)

# for map in world:
#     print("[", end="")
#
#     for i in range(len(map)):
#         print(map[i], end="") if i == len(map) - 1 else print(map[i])
#
#     print("]\n")
