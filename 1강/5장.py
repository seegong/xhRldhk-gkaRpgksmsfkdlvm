# 당근 마을을 만드는 코드예요. 아래 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
create_world(5, 5)
rabbit = Rabbit()
rabbit.set_trace('blue')
rabbit.set_pause(0.3)
_time.sleep(0.3)

# 아래에 코드를 작성해 볼까요?
# 1. 먼저 토끼를 1칸 이동시킨 후 왼쪽으로 돌도록 코드를 써봅시다.
rabbit.move()
rabbit.turn_left()

# 2. 토끼를 한 번 더 왼쪽으로 돌게 합니다.
rabbit.turn_left()

# 3. 이제 토끼가 다시 제자리로 돌아오도록 합니다.

rabbit.move()