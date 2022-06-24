# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world("worlds/harvest1.wld")
rabbit = Rabbit()
rabbit.set_trace('red')
rabbit.set_pause(0.1)
_time.sleep(0.1)

# 토끼가 오른쪽으로 돌기 위한 함수예요. 수정하지 마세요.
def aa():
    rabbit.turn_left()
    rabbit.turn_left()
    rabbit.turn_left()
    
# 이제 토끼가 길을 따라 움직이며 당근을 뽑을 수 있도록 해봅시다.

def bb():
    for a in range(5):
        rabbit.move()
        rabbit.pick_carrot()
        
def cc():
    rabbit.pick_carrot()
    rabbit.turn_left()
    rabbit.move()
    
    
    
    
def dd():
    for g in range(4):
        rabbit.move()
        rabbit.pick_carrot()

def gg():
    rabbit.turn_left()
    rabbit.move()
    rabbit.pick_carrot()
    rabbit.turn_left()


rabbit.move()
rabbit.pick_carrot()
bb()
gg()
bb()
aa()
rabbit.move()
aa()
rabbit.pick_carrot()
bb()
gg()
bb()
aa()
rabbit.move()
aa()
rabbit.pick_carrot()
bb()
gg()
bb()
aa()
rabbit.move()
aa()




