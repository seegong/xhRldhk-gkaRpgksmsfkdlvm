# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world("worlds/harvest1.wld")
rabbit = Rabbit()
rabbit.set_trace('blue')
rabbit.set_pause(0.1)
_time.sleep(0.1)

rabbit.pick_carrot()

# 1. 앞이 막혀있지 않는 동안 직진하는 반복문을 쓰세요.

#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요
#제발 제발 제발 실행 누르지말고 제출만 누르세요



while rabbit.front_is_clear():
    rabbit.move()


# 2. 당근 뽑고 귀퉁이 돌기

rabbit.pick_carrot()

# 3. 모든 귀퉁이를 돌며 당근을 뽑을 수 있게 위에 썼던 코드들을 다시 사용해보세요.

rabbit.turn_left()

while rabbit.front_is_clear():
    rabbit.move()

rabbit.pick_carrot()

rabbit.turn_left()

while rabbit.front_is_clear():
    rabbit.move()

rabbit.pick_carrot()

