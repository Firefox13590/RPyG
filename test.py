import pyglet
from pyglet.window import key

logo = pyglet.resource.image("images/favicon.ico")


fenetre = pyglet.window.Window()
fenetre.set_icon(logo)

keys = key.KeyStateHandler()
fenetre.push_handlers(keys)

states = ["idle", "move"]
currentState = states[0]
idleChar = (" O\n"
            "[|]\n"
            " ^\n")
print(idleChar)


label = pyglet.text.Label("Hello world!",
                   font_size=16,
                   x=fenetre.width/2, y=fenetre.height/2,
                   anchor_x="center", anchor_y="center")

character = pyglet.text.Label(currentState,
                   font_size=16,
                   x=fenetre.width/2, y=fenetre.height/2,
                   anchor_x="center", anchor_y="center")




@fenetre.event
def on_key_press(symbol, modifiers):
    global currentState
    currentState = states[0]

    if keys[key.A] or keys[key.LEFT]:
        character.x -= 16
        currentState = states[1]
        # key.MOTION_LEFT = LEFT
    if keys[key.D] or keys[key.RIGHT]:
        character.x += 16
        currentState = states[1]
    if keys[key.S] or keys[key.DOWN]:
        character.y -= 16
        currentState = states[1]
    if keys[key.W] or keys[key.UP]:
        character.y += 16
        currentState = states[1]

    character.text = currentState
    pass

@fenetre.event
def on_key_release(symbol, modifiers):
    global currentState
    currentState = states[0]

    # if keys[key.A] or keys[key.LEFT]:
    #     character.x -= 16
    #     currentState = states[1]
    #     # key.MOTION_LEFT = LEFT
    # if keys[key.D] or keys[key.RIGHT]:
    #     character.x += 16
    #     currentState = states[1]
    # if keys[key.S] or keys[key.DOWN]:
    #     character.y -= 16
    #     currentState = states[1]
    # if keys[key.W] or keys[key.UP]:
    #     character.y += 16
    #     currentState = states[1]

    character.text = currentState
    pass

@fenetre.event
def on_text_motion(motion):
    global currentState
    currentState = states[0]

    if motion == key.MOTION_LEFT:
        character.x -= 16
        currentState = states[1]
        # character.text = currentState
    if motion == key.MOTION_RIGHT:
        character.x += 16
        currentState = states[1]
    if motion == key.MOTION_DOWN:
        character.y -= 16
        currentState = states[1]
    if motion == key.MOTION_UP:
        character.y += 16
        currentState = states[1]

    character.text = currentState
    pass

@fenetre.event
def on_draw():
    fenetre.clear()
    # label.draw()
    character.draw()
    fenetre.push_handlers(keys)
    pass


pyglet.app.run()
