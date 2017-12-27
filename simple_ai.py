from game import Game

class SimpleAI():
    
    def __init__(self):
        self.game = Game(self)
        self.game.start()
    

    def update(self, ball, bouncer):
        if bouncer.position[0] < ball.position[0]:
            self.moveRight()

        if bouncer.position[0] > ball.position[0]:
            self.moveLeft()

    def moveRight(self):
        self.game.bouncer.moveRight()

    def moveLeft(self):
        self.game.bouncer.moveLeft()

def main():
    ai = SimpleAI()

if __name__ == "__main__": main()

