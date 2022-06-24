# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world("worlds/iterate1.wld")
rabbit = Rabbit()
rabbit.set_pause(0.2)
_time.sleep(0.2)
rabbit.set_trace('blue')

# 아래에 코드를 작성해 볼까요? 
for i in range(9):
    rabbit.move()