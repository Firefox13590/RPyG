from pyglet import *

fenetre = window.Window()

label = text.Label("Hello world!",
                   font_size=16,
                   x=fenetre.width/2,
                   y=fenetre.height/2,
                   anchor_x="center",
                   anchor_y="center")


@fenetre.event
def on_draw():
    fenetre.clear()
    label.draw()


app.run()
