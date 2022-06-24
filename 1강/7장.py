# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
create_world(5, 5)
rabbit = Rabbit()
rabbit.set_trace('blue')
rabbit.set_pause(0.2)
_time.sleep(0.2)

# 우선 아래에 오른쪽으로 돌기 함수를 써볼까요?
def turn_right():
    rabbit.turn_left()
    rabbit.turn_left()
    rabbit.turn_left()
    
    

# 이제 토끼가 움직일 수 있게 코드를 써봅시다.

rabbit.move()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
rabbit.turn_left()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
rabbit.turn_left()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
rabbit.turn_left()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
rabbit.turn_left()
rabbit.turn_left()