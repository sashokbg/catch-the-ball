from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from ball import Ball
from bouncer import Bouncer
from gamescreen import GameScreen

class Game():

    def __init__(self):
        director.init()
        self.main_layer = GameScreen(self)

        self.ball = Ball()
        self.main_layer.add(self.ball)
    
        self.bouncer = Bouncer()
        self.main_layer.add(self.bouncer)

        self.main_scene = Scene(self.main_layer)

    def update(self, delta_t):
        self.ball.update(self)

    def loosePoint(self):
        print("-1 points")

    def winPoint(self):
        print("+1 points")

    def start(self):
        self.main_layer.schedule(self.update)
        self.ball.doFall()
        director.run(self.main_scene)

def main():
    game = Game()
    game.start()

if __name__ == '__main__': main()
