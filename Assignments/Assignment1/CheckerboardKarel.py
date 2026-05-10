from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    start_with_beeper = True
    fill_one_row(start_with_beeper)
    while next_row_exist():
        start_with_beeper = not start_with_beeper
        fill_one_row(start_with_beeper)

def fill_one_row(has_beeper):
    if has_beeper:
        put_beeper()
    while front_is_clear():
        move()
        if not has_beeper:
            put_beeper()
        has_beeper = not has_beeper

def next_row_exist():
    turn_left()
    if front_is_clear():
        move()
        turn_left()
        while front_is_clear():
            move()
        turn_around()
        return True
    return False

def turn_around():
    turn_left()
    turn_left()
    
    
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
