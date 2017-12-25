from cocos.sprite import Sprite
from cocos.actions import *
import cocos
import cocos.collision_model as cm
import cocos.euclid as eu

class Ball(Sprite):

    def __init__(self, speed=200, position = (320,200)):
        Sprite.__init__(self, 'img/ball_64x64.png')
        self.__speed = speed
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
        self.do(Place((320,200)))
        self.doFall()

    @property
    def speed(self):
        return self.__speed
    
