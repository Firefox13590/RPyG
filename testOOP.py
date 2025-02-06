import pyglet
from pyglet.event import EVENT_HANDLE_STATE
from pyglet.window import key


class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__()

        self.set_icon(pyglet.resource.image("images/favicon.ico"))
        self.alive = 1

        self.charText = "O /|\\ /\\"
        self.charText2 = ""
        self.msgText = "Hello world! We ballin today"
        self.states = ["idle", "move"]
        self.currentState = self.states[0]

        self.label = pyglet.text.Label(self.currentState,
                                       multiline=True, font_size=21,
                                       x=self.width//2, y=self.height//2,
                                       width=10, height=10)
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
            self.label.x -= 16
        if symbol in mvtKeys[2:4]:
            self.label.x += 16
        if symbol in mvtKeys[4:6]:
            self.label.y -= 16
        if symbol in mvtKeys[6:]:
            self.label.y += 16

        self.label.text = self.currentState
        pass

    def on_key_release(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        self.currentState = self.states[0]
        self.label.text = self.currentState
        pass

    def update(self, dt):
        pass

    def render(self):
        self.clear()

        self.label.draw()

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

