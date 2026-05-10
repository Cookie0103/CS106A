from karel.stanfordkarel import *

def beeper_column():
    # 往下一直放，然后保证朝east
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()

def reposition():
    # 重新回到这列最高点，然后比原先向下一格，保证向east
    turn_left()
    while beeper_present():
        move()
    turn_around()
    move()
    move()
    turn_left()
    move()

def main():
    # 只要右边是clear
    while right_is_clear():
        beeper_column()
        reposition()
    beeper_column()




# def main():
#     height = count_height()
#     print(height)
#     for i in range(height, 1, -1):
#         climb_wall(i)
#         down_wall()
#         move()
#     climb_wall(1)
#     down_wall()

# def count_height():
#     turn_right()
#     height = 1
#     while front_is_clear():
#         height += 1
#         move()
#     turn_left()
#     return height

# def climb_wall(height):
#     turn_left()
#     for i in range(height):
#         put_beeper()
#         move()

# def down_wall():
#     turn_around()
#     while front_is_clear():
#         move()
#     turn_left()
    
# turn_right and turn_around are provided for convenience, in case you need them

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()