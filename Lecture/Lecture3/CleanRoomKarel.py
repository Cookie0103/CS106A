from karel.stanfordkarel import * 

"""
File: CleanRoomKarel.py
----------------------------
Pick up all the beepers in the world.
"""


def main():
    """
    Karel should be is facing East in bottom row (street) of the world and
    will end up facing East at end of top row, having picked up all the
    beepers in the world.
    """
    while left_is_clear():  # left will only be blocked when we reach top row of world
        clear_row()
        reposition_for_next_row()
    clear_row()             # fence-post issue. Make sure to clean top row.


def clear_row():
    """
    Karel should be facing East on 1st avenue (at the start of a messy row) and
    will end up at the end of the row, having picked up all beepers in row.
    """
    while front_is_clear():
        safe_pick_up()
        move()
    safe_pick_up()          # fence-post issue. Must make sure to clean last corner.


def safe_pick_up():
    """
    Karel will pick up a beeper on the current corner, if there is one.
    """
    if beepers_present():
        pick_beeper()


def reposition_for_next_row():
    """
    Assuming Karel is facing East, it will reposition itself on
    1st avenue, facing East, one row up from the row in which it started
    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()


def move_to_wall():
    """
    Karel will move forward until it reaches a wall.
    """
    while front_is_clear():
        move()


def turn_around():
    """
    pre-condition: none
    post-condition: Karel does a 180 degree turn in place
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Pre-condition:  none
    Post-condition: Karel is facing to the right of whichever
                    direction Karel was facing previously
    """
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
