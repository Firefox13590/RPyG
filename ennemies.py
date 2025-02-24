#abstract class for ennemies
class Ennemy:
    def __init__(self):
        self.maxhp = 0
        self.currenthp = self.maxhp
        self.att = 0
        self.df = 0
        self.spd = 0
        self.drop = 0
        pass

    def Sprite(self):
        pass

    def Stats(self):
        remain = round(20 * (self.currenthp / self.maxhp))
        print(f"{self.__class__.__name__}:")
        self.Sprite()
        print("[" + "#" * remain
              + "-" * (20 - remain) + "]")

    pass


#ennemies
class Slime(Ennemy):
    def __init__(self):
        super().__init__()
        self.maxhp = 10
        self.currenthp = self.maxhp
        self.att = 3
        self.df = 5
        self.spd = 3
        self.drop = range(3)

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


class Goblin(Ennemy):
    def __init__(self):
        super().__init__()
        self.maxhp = 15
        self.currenthp = self.maxhp
        self.att = 5
        self.df = 3
        self.spd = 5
        self.drop = range(6)

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


class CursedTree(Ennemy):
    def __init__(self):
        super().__init__()
        self.maxhp = 30
        self.currenthp = self.maxhp
        self.att = 2
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


class E4(Ennemy):
    pass


class E5(Ennemy):
    pass


class E6(Ennemy):
    pass


#abstract class for bosses
class Boss(Ennemy):
    pass


#bosses
class Wormathron(Boss):
    def __init__(self):
        super().__init__()
        self.maxhp = 30
        self.currenthp = self.maxhp
        self.att = 10
        self.df = 10
        self.spd = 10
        self.drop = range(10, 20)

    def Sprite(self):
        print(r'''
               ________ __
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
