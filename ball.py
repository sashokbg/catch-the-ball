from cocos.sprite import Sprite
from cocos.actions import *
import random
import cocos
import cocos.collision_model as cm
import cocos.euclid as eu

class Ball(Sprite):

    def randomPosition(self):
        return (random.randint(20,620), 300)

    def __init__(self, speed=200, position = None):
        Sprite.__init__(self, 'img/ball_64x64.png')
        self.__speed = speed

        if not position:
            self.position = self.randomPosition()
        else:
            self.position = position

        center_x, center_y = self.position
        self.cshape = cm.CircleShape(eu.Vector2(center_x, center_y), 32)



    def doFall(self):
        self.do(Repeat(MoveBy((0,-self.__speed), duration=2)))

    def update(self, game):
        if self.position[1] < 0:
            game.loosePoint()
            self.reset()
        
        center_x, center_y = self.position
        self.cshape = cm.CircleShape(eu.Vector2(center_x, center_y), 32)

    def reset(self):
        self.stop()
        self.do(Place(self.randomPosition()))
        self.doFall()

    @property
    def speed(self):
        return self.__speed
    
