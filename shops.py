
# dict{str(product name): tuple(int(price), str(description)}
# (n..m) = possible added stats
products = {"Health potion": (2, "Professionals have standards"), #set hp to max
            "Protein powder": (4, "No pain no gain"), #min dmg (1..2)
            "Bag of rocks": (8, "Dwayne The Rock Johnson approved"),  # max dmg (1..3)
            "Rings": (10, "YOU'RE FAST AS FUCK BOIIIII"), #speed (1..2)
            "Hammer": (15, "Smash your armor to increase resistance... somehow?"), #def (1..2)
            "Fat juicy bloody steamy steak": (25, "9 out of 10 doctors recommend to increase life expectancy"), #max hp (2..5)
            "Fighting tactics": (40, "With a bit of luck, you can hit enemies multiple times"), #chain (1..2)
            "Mobility training": (40, "When fast enough, you can dodge attacks"), #dodge (1..3)
            "Guide of the Warrior": (75, "Anything you want for maximum damage"), #min dmg (2..4); max dmg (3..5)
            "Guide of the Paladin": (75, "Anything you want for maximum survivability"), #max hp (3..7); def (2..3)
            "Guide of the Hunter": (75, "Anything you want for maximum utility"), #chain (2..3); dodge (2..4)
            "DnDice": (99, "99% of gamblers quit before they win BIG")} #50/50 double or nothing with gold

# print(products)
# print(products["Protein powder"])
# print(products["Protein powder"][1])
# print(list(products["Health potion"]))
