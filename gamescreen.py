from cocos.layer import Layer

class GameScreen(Layer):

    def __init__(self, game):
        Layer.__init__(self)

        self.game = game
