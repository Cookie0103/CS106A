from karel.stanfordkarel import *

"""
File: DoubleBeepers.py
----------------------
Karel doubles the number of beepers in a pile one step in front of it.
"""


def main():
    """
    Karel moves to the pile on the corner in front of it, doubles the number
    of beepers in the pile and returns to its original position.
    """
    move()
    double_beepers_in_pile()
    move_backward()


def double_beepers_in_pile():
    """
    For every beeper on the current corner, Karel ends up with two
    beepers on the current corner.  It does this by creating a pile
    with twice as many beepers one corner ahead of it and then moving
    that pile back to its original location.
    """
    while beepers_present():
        pick_beeper()
        put_two_beepers_next_door()
    move_pile_next_door_back()


def put_two_beepers_next_door():
    """
    Place two beepers on corner one avenue ahead of Karel
    and move back to starting position/orientation
    """
    move()
    put_beeper()
    put_beeper()
    move_backward()


def move_pile_next_door_back():
    """
    Move all the beepers on the corner in front of Karel
    to the corner Karel is currently on.
    """
    move()
    while beepers_present():
        move_one_beeper_back()
    move_backward()


def move_one_beeper_back():
    """
    Move one beeper from the current corner back one avenue
    and return to the original position/orientation.
    """
    pick_beeper()
    move_backward()
    put_beeper()
    move()


def move_backward():
    """
    Move Karel back one avenue, but facing same direction it started.
    """
    turn_around()
    move()
    turn_around()


def turn_around():
    """
    pre-condition: none
    post-condition: Karel does a 180 degree turn in place
    """
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
