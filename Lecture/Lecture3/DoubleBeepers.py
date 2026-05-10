from karel.stanfordkarel import *


def main():
    move()
    double_beepers_in_pile()
    move_backward()

def move_backward():
    turn_around()
    move()
    turn_around()

def double_beepers_in_pile():
    while beepers_present():
        pick_beeper()
        put_two_beepers_next_door()
    move_pile_next_door_back()

def put_two_beepers_next_door():
    move()
    put_beeper()
    put_beeper()
    move_backward()

def move_pile_next_door_back():
    move()
    while beepers_present():
        move_one_beeper_back()
    move_backward()

def move_one_beeper_back():
    pick_beeper()
    move_backward()
    put_beeper()
    move()

def turn_around():
    """
    pre-condition: none
    post-condition: Karel does a 180 degree turn in place
    """
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
