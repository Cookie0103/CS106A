"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    MIN_INTEGER = 10
    MAX_INTEGER = 99
    CORRECT_ROWS = 3
    i = 0 
    while i < CORRECT_ROWS:
        x1 = random.randint(MIN_INTEGER, MAX_INTEGER)
        x2 = random.randint(MIN_INTEGER, MAX_INTEGER)
        problem = print("What is ", x1, " + ", x2, "?")
        expected = float(input("Your answer: "))
        if expected != x1 + x2:
            print("Incorrect. The expected answer is ", x1+x2)
            i = 0
        else:
            i += 1
            print("Correct! You've gotten", i, "correct in a row.")
    print("Congratulations! You mastered addition.")
        


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
