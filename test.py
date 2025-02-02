import pyglet
from pyglet.window import key

logo = pyglet.resource.image("images/favicon.ico")


fenetre = pyglet.window.Window()
fenetre.set_icon(logo)


label = pyglet.text.Label("Hello world!",
                   font_size=16,
                   x=fenetre.width/2, y=fenetre.height/2,
                   anchor_x="center", anchor_y="center")


@fenetre.event
def on_key_press(symbol, modifiers):
    if symbol in (key.A, key.LEFT):
        label.x -= 16
    if symbol in (key.D, key.RIGHT):
        label.x += 16
    if symbol in (key.S, key.DOWN):
        label.y -= 16
    if symbol in (key.W, key.UP):
        label.y += 16
    pass

@fenetre.event
def on_draw():
    fenetre.clear()
    label.draw()
    pass


pyglet.app.run()
