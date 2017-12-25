from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
import ball

def main():
    director.init()
    main_layer = Layer()
    ball_ = ball.Ball(40)
    ball_.position = 320, 200

    main_layer.add(ball_)

    main_scene = Scene(main_layer)
    
    ball_.doFall()

    director.run(main_scene)

if __name__ == '__main__': main()
