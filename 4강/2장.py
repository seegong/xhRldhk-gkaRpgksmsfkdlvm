# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world( "worlds/trash1.wld" )
rabbit = Rabbit()
rabbit.set_trace("blue")
_time.sleep(0.1)
rabbit.set_pause(0.1)

# 1. 토끼가 토끼굴의 처음부터 끝까지 움직이는 코드입니다. 수정하지 마세요!
for i in range(10):
    if i == 9:
        rabbit.turn_left()
        rabbit.turn_left()
    else:
        rabbit.move()
    # 2. 토끼가 당근 위에 있을 때 당근을 줍는 반복문을 쓰세요.
    
        
    
# 3. 당근을 들고 창고에 가는 코드입니다.수정하지 마세요.
for i in range(9):

    while rabbit.on_carrot():
        rabbit.pick_carrot()
    rabbit.move()
rabbit.turn_left()
rabbit.turn_left()
rabbit.turn_left()
rabbit.move()





# 4. 창고에 갔으면 토끼가 당근을 갖고 있으면 당근을 놓는 반복문을 쓰세요.



# 5. 당근을 모두 놓았으면 제자리로 돌아와요.
while rabbit.carries_carrots():
    rabbit.drop_carrot()

rabbit.turn_left()

rabbit.turn_left()

rabbit.move()
rabbit.turn_left()
