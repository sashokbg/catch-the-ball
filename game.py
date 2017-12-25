from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from ball import Ball

class Game():

    def __init__(self):
        director.init()
        self.main_layer = Layer()
        self.ball = Ball(40)
        self.ball.position = 320, 200
    
        self.main_layer.add(self.ball)
    
        self.main_scene = Scene(self.main_layer)

    def update(self, delta_t):
        print("updated {}".format(self.ball.position))

    def start(self):
        self.main_layer.schedule(self.update)
        self.ball.doFall()
        director.run(self.main_scene)

def main():
    game = Game()
    game.start()

if __name__ == '__main__': main()
