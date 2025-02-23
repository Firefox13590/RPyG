class Player:
    def __init__(self):
        self.maxhp = 25
        self.currenthp = self.maxhp
        self.highrol = 5
        self.lowrol = 2
        self.att = range(self.lowrol, self.highrol)
        self.chain = 0
        self.df = 10
        self.dodge = 0
        self.spd = 5
        self.gold = 0
        self.x = 0
        self.y = 0
        self.pos = [self.x, self.y]

    def Stats(self):
        remain = round(20 * (self.currenthp / self.maxhp))
        print(f"{self.__class__.__name__}:")
        print(f"{self.currenthp} HP left\n[" + "#" * remain
              + "-" * (20 - remain) + "]")


inventory = [["Health potion", 0, "Professionals have standards"],
             ["Bag of rock", 0, "Pretty heavy"],
             ["Protein powder", 0, "No pain no gain"],
             ["Rings", 0, "YOU'RE FAST AS FUCK BOIIIII"],
             ["Scissors", 0, "Cut your armor to become more resilient to attacks"],
             ["Fat juicy bloody steamy steak", 0, "9 out of 10 doctors recommend to increase life expectancy"],
             ["Fighting tactics", 0, "With a bit of luck, you can hit ennemies multiple times"],
             ["Mobility training", 0, "When fast enough, you can dodge attacks"],
             ["Guide of the Warrior", 0, "Anything you want for maximum damage"],
             ["Guide of the Paladin", 0, "Anything you want for maximum survivability"],
             ["Guide of the Hunter", 0, "Anything you want for maximum utility"],
             ["DnDice", 0, "99% of people quit before they win"]]
p = Player()
#p.Stats()
