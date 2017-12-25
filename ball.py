from cocos.sprite import Sprite
from cocos.actions import *
import cocos
import cocos.collision_model as cm
import cocos.euclid as eu

class Ball(Sprite):

    def __init__(self, speed):
        Sprite.__init__(self, 'ball_64x64.png')
        self.__speed = speed
        center_x, center_y = self.position
        self.cshape = cm.CircleShape(eu.Vector2(center_x, center_y), 32)

    def doFall(self):
        self.do(Repeat(MoveBy((0,-self.__speed), duration=2)))

    @property
    def speed(self):
        return self.__speed
    
