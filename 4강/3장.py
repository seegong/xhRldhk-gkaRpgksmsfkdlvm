# 토끼와 당근밭을 불러올 모듈을 호출합니다.
from elicerabbits import *
import time as _time

# 가로, 세로 5 길이의 엘리스월드를 소환합니다.
create_world(avenues=5, streets=5)

# 당근 10000개를 들고 있는 토끼를 소환합니다.
rabbit = Rabbit(carrots = 10000)
rabbit.set_pause(0.1)
_time.sleep(0.1)


# H를 쓰는 함수를 정의해주세요.
def drawH(rabbit):
    rabbit.turn_left()
    go_straight_with_carrot(rabbit)
    for _ in range(2):
        rabbit.turn_left()
    for _ in range(2):
        rabbit.move()
    rabbit.turn_left()
    go_straight_with_carrot(rabbit)
    rabbit.turn_left()
    go_straight_with_carrot(rabbit)
    for _ in range(2):
        rabbit.turn_left()
    go_straight_with_carrot(rabbit)

# E를 쓰는 함수를 정의해주세요.
def drawE(rabbit):
    rabbit.turn_left()
    go_straight_with_carrot(rabbit)
    turn_right(rabbit)
    go_straight_with_carrot(rabbit)
    turn_right(rabbit)
    for _ in range(2):
        rabbit.move()
    turn_right(rabbit)
    go_straight_with_carrot(rabbit)
    rabbit.turn_left()
    for _ in range(2):
        rabbit.move()
    rabbit.turn_left()
    go_straight_with_carrot(rabbit)

# L을 쓰는 함수를 정의해주세요.
def drawL(rabbit):
    rabbit.turn_left()
    go_straight_with_carrot(rabbit)
    return_to_base(rabbit)
    go_straight_with_carrot(rabbit)

# O를 쓰는 함수를 정의해주세요.
def drawO(rabbit):
    for _ in range(4):
        go_straight_with_carrot(rabbit)
        rabbit.turn_left()

# 토끼가 우회전하는 코드입니다.
# 이 함수는 수정하지 않으셔야 합니다.
def turn_right(rabbit) :
    for i in range(3) :
        rabbit.turn_left()

def safe_pick_carrot(rabbit) :
    while rabbit.on_carrot() :
        rabbit.pick_carrot()

def drop_carrot_only_one(rabbit) :
    while not rabbit.on_carrot() :
        rabbit.drop_carrot()

def go_straight_with_carrot(rabbit) :
    while rabbit.front_is_clear():
        drop_carrot_only_one(rabbit)
        rabbit.move()
    drop_carrot_only_one(rabbit)


# 알파벳을 쓰기 위해 심은 당근을 모두 줍는 함수를 작성해보세요.
# 이 함수는 채점되지 않습니다. 
def clear_world(rabbit):
    def clear_left_to_right() :
        while rabbit.front_is_clear():
            safe_pick_carrot(rabbit)
            rabbit.move()
        safe_pick_carrot(rabbit)
        rabbit.turn_left()
        
        if rabbit.front_is_clear() :
            rabbit.move()
            
        rabbit.turn_left()
        
    def clear_right_to_left() :
        while rabbit.front_is_clear():
            safe_pick_carrot(rabbit)
            rabbit.move()
        safe_pick_carrot(rabbit)
        turn_right(rabbit)
                
        if rabbit.front_is_clear() :
            rabbit.move()
            
        turn_right(rabbit)
    
    clear_left_to_right()
    clear_right_to_left()
    clear_left_to_right()
    clear_right_to_left()
    clear_left_to_right()
    
    return_to_base(rabbit)


# 본래의 지점인 (1, 1)로 돌아오는 함수입니다.
# 이 함수는 수정하지 않으셔야 합니다.
# 이 함수는 채점되지 않습니다.
def return_to_base(rabbit):
    while not rabbit.facing_north():
        rabbit.turn_left()
    rabbit.turn_left()
    while rabbit.front_is_clear():
        rabbit.move()
    rabbit.turn_left()
    while rabbit.front_is_clear():
        rabbit.move()
    rabbit.turn_left()
    

# 위 6개의 함수를 이용해 토끼가 HELLO를 쓰는 함수를 정의해보세요.
def draw_alphabets(rabbit):
    mvLs = [ drawH, drawE, drawL, drawL, drawO ]
    for f in mvLs:
        f(rabbit)
        return_to_base(rabbit)
        clear_world(rabbit)

draw_alphabets(rabbit)