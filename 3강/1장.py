# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world("worlds/Move1.wld")
rabbit = Rabbit()
rabbit.set_trace('blue')
rabbit.set_pause(0.1)
_time.sleep(0.1)

# 토끼를 오른쪽 귀퉁이로 데려가 봅시다.


# 당근이 있는지 확인하고 있으면 당근을 뽑는 코드를 작성해 봅시다.


# 당근이 없으면 다음 귀퉁이로 이동해야겠죠?


for i in range(4):
    rabbit.move()
rabbit.turn_left()
if rabbit.on_carrot():
    rabbit.pick_carrot()
for i in range(4):
    rabbit.move()
rabbit.turn_left()
if rabbit.on_carrot():
    rabbit.pick_carrot()
for i in range(4):
    rabbit.move()
rabbit.turn_left()
if rabbit.on_carrot():
    rabbit.pick_carrot()
for i in range(4):
    rabbit.move()
rabbit.turn_left()
if rabbit.on_carrot():
    rabbit.pick_carrot()

rabbit.drop_carrot()


