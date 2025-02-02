import pyglet
from pyglet.window import key

logo = pyglet.resource.image("images/favicon.ico")


fenetre = pyglet.window.Window()
fenetre.set_icon(logo)

keys = key.KeyStateHandler()
fenetre.push_handlers(keys)


label = pyglet.text.Label("Hello world!",
                   font_size=16,
                   x=fenetre.width/2, y=fenetre.height/2,
                   anchor_x="center", anchor_y="center")




# @fenetre.event
# def on_key_press(symbol, modifiers):
#     if keys[key.A] or keys[key.LEFT]:
#         print("left")
#         label.x -= 16
#     if keys[key.D] or keys[key.RIGHT]:
#         label.x += 16
#     if keys[key.S] or keys[key.DOWN]:
#         label.y -= 16
#     if keys[key.W] or keys[key.UP]:
#         label.y += 16
#     pass


@fenetre.event
def on_draw():
    fenetre.clear()
    label.draw()
    # fenetre.push_handlers(keys)
    pass

@fenetre.event
def on_text_motion(motion):
    if motion == key.MOTION_LEFT:
        label.x -= 16
    if motion == key.MOTION_RIGHT:
        label.x += 16
    if motion == key.MOTION_DOWN:
        label.y -= 16
    if motion == key.MOTION_UP:
        label.y += 16
    pass


pyglet.app.run()
