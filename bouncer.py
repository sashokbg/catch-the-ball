from cocos.sprite import Sprite
from cocos.actions import *
from cocos.collision_model import *
import cocos.euclid as eu

class Bouncer(Sprite):

    @property
    def speed(self):
        return self.__speed

    def __init__(self, speed = 120, position = (320, 10)):
        Sprite.__init__(self, 'img/bouncer64x14.png')
        self.__speed = speed
        self.position = position
        center_x, center_y = self.position
        self.cshape = AARectShape(eu.Vector2(center_x, center_y), 32, 7)

    def update(self):
        center_x, center_y = self.position
        self.cshape = AARectShape(eu.Vector2(center_x, center_y), 32, 7)

    def moveLeft(self):
        self.stop()
        self.do(Repeat(MoveBy((-self.speed,0), duration=1)))

    def moveRight(self):
        self.stop()
        self.do(Repeat(MoveBy((self.speed,0), duration=1)))
    
