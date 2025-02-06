import pyglet
from pyglet.event import EVENT_HANDLE_STATE
from pyglet.window import key

# source characteres unicodes: https://en.wikipedia.org/wiki/List_of_Unicode_characters

class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__()


        self.set_icon(pyglet.resource.image("images/favicon.ico"))
        self.alive = 1


        self.charText = "O /\\ /\\"
        self.charText2 = f"{chr(160)}O └|{chr(172)} {chr(160) + chr(691)}L"
        self.charText3 = f"{chr(160)}O ⌈|⌋ {chr(160)}ֈ{chr(172)}"
        self.giraffe = r"""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """
        self.savedSide = self.charText2
        self.msgText = "Hello world! We ballin today"
        self.states = ["idle", "move"]
        self.currentState = self.states[0]


        self.label = pyglet.text.Label(self.charText,
                                       multiline=True, font_size=21,
                                       x=self.width//2, y=self.height//2,
                                       width=10, height=10)

        doc = pyglet.text.document.AbstractDocument(self.giraffe)
        self.enemy = pyglet.text.layout.TextLayout(doc,
                                       wrap_lines=True,
                                       x=self.height // 2, y=self.height // 2,
                                       anchor_x="center", anchor_y="center",
                                       width=100, height=self.height)

        self.drawnObjects = [self.label, self.enemy]
        pass

    def on_close(self) -> None:
        self.alive = 0
        pass

    def on_draw(self):
        self.render()
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        mvtKeys = (key.A, key.LEFT, key.D, key.RIGHT, key.S, key.DOWN, key.W, key.UP)
        if symbol == key.ESCAPE:
            self.alive = 0

        if symbol in mvtKeys:
            self.currentState = self.states[1]

        if symbol in mvtKeys[:2]:
            self.label.x -= 32
        if symbol in mvtKeys[2:4]:
            self.label.x += 32
        if symbol in mvtKeys[4:6]:
            self.label.y -= 32
        if symbol in mvtKeys[6:]:
            self.label.y += 32

        if symbol in mvtKeys[:2]:
            self.label.text = self.charText2
            self.savedSide = self.charText2
        elif symbol in mvtKeys[2:4]:
            self.label.text = self.charText3
            self.savedSide = self.charText3
        else:
            self.label.text = self.savedSide

        # self.label.text = self.currentState
        pass

    def on_key_release(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        self.currentState = self.states[0]
        # self.label.text = self.currentState
        self.label.text = self.charText
        pass

    def update(self, dt):
        pass

    def render(self):
        self.clear()

        # for el in self.drawnObjects:
        #     el.draw()

        self.label.draw()
        self.enemy.draw()

        self.flip()
        pass

    def run(self):
        while self.alive == 1:
            self.render()
            event = self.dispatch_events()
        pass


if __name__ == "__main__":
    f = Fenetre()
    f.run()

