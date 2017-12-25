from cocos.sprite import Sprite
from cocos.actions import *

class Bouncer(Sprite):

    @property
    def speed(self):
        return self.__speed

    def __init__(self, speed = 120, position = (320, 10)):
        Sprite.__init__(self, 'img/bouncer64x14.png')
        self.__speed = speed
        self.position = position

    def moveLeft(self):
        self.stop()
        self.do(Repeat(MoveBy((-self.speed,0), duration=1)))

    def moveRight(self):
        self.stop()
        self.do(Repeat(MoveBy((self.speed,0), duration=1)))
    
