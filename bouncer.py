from cocos.sprite import Sprite
from cocos.actions import *

class Bouncer(Sprite):

    def __init__(self):
        Sprite.__init__(self, 'bouncer64x14.png')

    def moveLeft(self):
        self.stop()
        self.do(Repeat(MoveBy((-30,0), duration=1)))

    def moveRight(self):
        self.stop()
        self.do(Repeat(MoveBy((30,0), duration=1)))
    
