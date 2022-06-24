# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world("worlds/Move.wld")
rabbit = Rabbit()
rabbit.set_trace('blue')
rabbit.set_pause(0.2)
_time.sleep(0.2)


def up():
    rabbit.move()
    rabbit.turn_left()
    rabbit.move()
    rabbit.turn_left()
    rabbit.turn_left()
    rabbit.turn_left()
    
    
    

# 이제 토끼가 움직여 당근을 옮길 수 있도록 아래에 코드를 작성해 볼까요?
up()
up()
rabbit.pick_carrot()

up()
up()
rabbit.drop_carrot()


