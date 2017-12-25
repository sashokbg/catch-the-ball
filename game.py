from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from ball import Ball
from bouncer import Bouncer
from gamescreen import GameScreen
from cocos.collision_model import *
from cocos.text import Label

class Game():

    def __init__(self):
        director.init()
        self.main_layer = GameScreen(self)

        self.ball = Ball()
        self.main_layer.add(self.ball)
    
        self.bouncer = Bouncer()
        self.main_layer.add(self.bouncer)

        self.score = 0
        self.score_label = Label("Score: 0", font_size = 32)
        self.score_label.position = 20, 400
        self.main_layer.add(self.score_label)

        self.main_scene = Scene(self.main_layer)
        self.collision_manager = CollisionManagerGrid(0,640,0,400,5,5)
        self.collision_manager.add(self.ball)
        self.collision_manager.add(self.bouncer)

    def update(self, delta_t):
        self.ball.update(self)
        self.bouncer.update()

        if self.collision_manager.they_collide(self.ball, self.bouncer):
            print("collision")
            self.winPoint()
            self.ball.reset()

    def loosePoint(self):
        print("-1 points")
        self.score-=1
        self.score_label.element.text = "Score: {}".format(self.score)
    def winPoint(self):
        print("+1 points")
        self.score+=1
        self.score_label.element.text = "Score: {}".format(self.score)

    def start(self):
        self.main_layer.schedule(self.update)
        self.ball.doFall()
        director.run(self.main_scene)

def main():
    game = Game()
    game.start()

if __name__ == '__main__': main()
