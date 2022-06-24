# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world("worlds/LeaveHouse1.wlr")
rabbit = Rabbit(carrots = 1)
rabbit.set_trace('red')
rabbit.set_pause(0.1)
_time.sleep(0.1)

# 1. 토끼가 출구가 있는 곳까지 직진하도록 코드를 쓰세요.

for i in range(6):
    rabbit.move()
    

# 2. 굴에서 빠져나오도록 코드를 쓰세요. (왼쪽으로 돌아 앞으로 두 칸 이동!)

rabbit.turn_left()
for i in range(2):
    rabbit.move()
    