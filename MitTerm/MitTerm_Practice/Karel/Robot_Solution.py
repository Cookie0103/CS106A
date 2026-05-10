from karel.stanfordkarel import *

def next_position():
    # 站到下一个放置点的前一个位置
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    
def handle_border():
    # 先动一步，然后先放置（注意要判断是有存在）再动
    move()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()

def move_up_row():
    # 站到起始位置
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def main():
    # 站到起始位置，循环4次
    move_up_row()
    for i in range(4):
        handle_border()
        next_position()


if __name__ == "__main__":
    run_karel_program()