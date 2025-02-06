import pyglet


class Fenetre(pyglet.window.Window):
    def __init__(self):
        super().__init__()

        self.set_icon(pyglet.resource.image("images/favicon.ico"))
        self.alive = 1

        self.charText = "O /|\\ /\\"
        self.msgText = "Hello world! We ballin today"
        self.label = pyglet.text.Label(self.charText,
                                       multiline=True, font_size=21,
                                       x=self.width//2, y=self.height//2,
                                       width=10, height=10)

    def on_draw(self):
        self.clear()
        self.label.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass

    def update(self, dt):
        pass


if __name__ == "__main__":
    f = Fenetre()
    pyglet.app.run()