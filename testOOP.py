import pyglet
from pyglet.event import EVENT_HANDLE_STATE
from pyglet.window import key

logo = pyglet.resource.image("images/favicon.ico")


class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__()

        self.set_icon(logo)
        self.alive = 1

    def on_draw(self) -> EVENT_HANDLE_STATE:
        self.render()

    def render(self):
        self.clear()
        self.flip()

    def run(self):
        while self.alive == 1:
            self.render()
            event = self.dispatch_event()


# Fenetre.run(Fenetre)