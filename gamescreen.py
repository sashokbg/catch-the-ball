from cocos.layer import Layer

left = 65361
right = 65363

class GameScreen(Layer):
    is_event_handler = True

    def __init__(self, game):
        Layer.__init__(self)

        self.game = game

    def on_key_press(self, key, modifiers):
        if key == left:
            self.game.bouncer.moveLeft()

        if key == right:
            self.game.bouncer.moveRight()

        print("pressed {}".format(key))

    def on_key_release(self, key, modifiers):
        self.game.bouncer.stop()
