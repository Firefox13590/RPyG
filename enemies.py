#abstract class for enemies
class Enemy:
    def __init__(self):
        self.maxHp = 0
        self.currentHp = self.maxHp
        self.att = 0
        self.df = 0
        self.spd = 0
        self.drop = 0 #gold dropped
        pass

    def Sprite(self):
        pass

    def Stats(self):
        remain = round(20 * (self.currentHp / self.maxHp))
        print(f"{self.__class__.__name__}:")
        self.Sprite()
        print("[" + "#" * remain
              + "-" * (20 - remain) + "]")

    pass


#enemies
class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHp = 10
        self.currentHp = self.maxHp
        self.att = range(3)
        self.df = 5
        self.spd = 3
        self.drop = range(1, 3)

    def Sprite(self):
        print(r'''
                /---\
             /--     ---\
            |   O    O   |
             \    \/    /
              \________/
        ''')
        pass

    pass


class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHp = 15
        self.currentHp = self.maxHp
        self.att = range(5)
        self.df = 3
        self.spd = 5
        self.drop = range(2, 6)

    def Sprite(self):
        print(r'''
          ----        ----
           /\   /    / /\
           \/  /    /  \/
              |____|_/
                \______/
        ''')
        pass

    pass


class CursedTree(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHp = 20
        self.currentHp = self.maxHp
        self.att = range(1, 2)
        self.df = 20
        self.spd = 1
        self.drop = range(4, 10)

    def Sprite(self):
        print(r'''
            \ \/ \/ // /
             |        |  
             |  |  |  |
             |   __   |
            /          \ 
        ''')
        pass

    pass


class E4(Enemy):
    pass


class E5(Enemy):
    pass


class E6(Enemy):
    pass


#abstract class for bosses
class Boss(Enemy):
    pass


#bosses
class Wormathron(Boss):
    def __init__(self):
        super().__init__()
        self.maxHp = 20
        self.currentHp = self.maxHp
        self.att = range(2, 5)
        self.df = 10
        self.spd = 10
        self.drop = range(10, 20)

    def Sprite(self):
        print(r'''
               _______ ___
             /V V V V \    \
            |          |    |
             \_A_A_A_A/     /
              \            /
               |          /
               |         /__/\
                \____________/
        ''')
        pass

    pass


class B2(Boss):
    pass


class B3(Boss):
    pass


"""
mob = Slime()
mob.Stats()
mob = Goblin()
mob.Stats()
mob = CursedTree()
mob.Stats()
mob = Wormathron()
mob.Stats()
"""
