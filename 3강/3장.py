# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time

create_world()
rabbit = Rabbit()
rabbit.set_trace('blue')    
_time.sleep(0.0001)
rabbit.set_pause(0.00001)

def go10():
    for a in range(9): 
        rabbit.move()
def aa():
    for b in range(3):
        rabbit.turn_left()

rabbit.turn_left()

go10()
aa()
rabbit.move()
aa()
go10()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
go10()
aa()
rabbit.move()
aa()
go10()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
go10()
aa()
rabbit.move()
aa()
go10()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
go10()
aa()
rabbit.move()
aa()
go10()
rabbit.turn_left()
rabbit.move()
rabbit.turn_left()
go10()
aa()
rabbit.move()
aa()
go10()
