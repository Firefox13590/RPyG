class Player:
    def __init__(self):
        self.maxHp = 25
        self.currentHp = self.maxHp
        self.maxDmg = 5
        self.minDmg = 3
        self.att = range(self.minDmg, self.maxDmg)
        self.chain = 0 #% to multi hit
        self.df = 10
        self.dodge = 0 #% to negate enemy dmg
        self.spd = 5
        self.gold = 2
        self.x = 0
        self.y = 0
        self.pos = [self.x, self.y]
        self.inventory: dict = {}

    def Stats(self):
        remain = round(20 * (self.currentHp / self.maxHp))
        print(f"{self.__class__.__name__}:\n"
              f"{self.currentHp} HP left\n"
              "[" + "#" * remain + "-" * (20 - remain) + "]")


p = Player()
# p.Stats()
