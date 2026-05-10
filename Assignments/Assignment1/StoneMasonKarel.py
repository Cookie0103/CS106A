from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


# def main():
#     """
#     You should write your code to make Karel do its task in
#     this function. Make sure to delete the 'pass' line before
#     starting to write your own code. You should also delete this
#     comment and replace it with a better, more descriptive one.
#     """
#     while front_is_clear():
#         ascend_wall()
#         descend_wall()
#         move_4_wall()
#     ascend_wall()
#     descend_wall()

# def move_4_wall():
#     for i in range(4):
#         move()
        
# def ascend_wall():
#     turn_left()
#     while front_is_clear():
#         if beepers_present():
#             move()
#         else:
#             put_beeper()
#     if not beepers_present():
#         put_beeper()

# def turn_around():
#     turn_left()
#     turn_left()

# def descend_wall():
#     turn_around()
#     while front_is_clear():
#         move()
#     turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
