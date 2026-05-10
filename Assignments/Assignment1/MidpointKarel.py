from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    i = 1
    while front_is_clear():
        move()
        i += 1
    if i % 2 == 1:
        steps = (i+1) // 2 - 1
        back_to_beeper(steps)
    else:
        steps = i // 2
        back_to_beeper(steps)

def turn_around():
    turn_left()
    turn_left()

def back_to_beeper(steps):
    turn_around()
    for s in range(steps):
        move()
    put_beeper()
    



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
