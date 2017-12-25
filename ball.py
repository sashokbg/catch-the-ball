from cocos.sprite import Sprite
import cocos
from cocos.actions import *

class Ball(Sprite):

    def __init__(self, speed):
        Sprite.__init__(self, 'ball_64x64.png')
        self.__speed = speed

    def doFall(self):
        self.do(Repeat(MoveBy((0,-self.__speed), duration=2)))

    @property
    def speed(self):
        return self.__speed
    
