class Player:
    def __init__(self):
        self.maxhp = 25
        self.currenthp = self.maxhp
        self.highrol = 5
        self.lowrol = 3
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


inventory = {}
p = Player()
#p.Stats()
