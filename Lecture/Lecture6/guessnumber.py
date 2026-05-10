"""
File: guessnumber.py
--------------------
This program implements a simple guessing game where the computer picks
a random number (integer) between MIN_NUM and MAX_NUM and the user
tries to guess the number.  The computer prompts if the user's guess is
too low or too high.  The user repeatedly guesses until they guess the
right answer.
"""

import random

MIN_NUM = 1             # lower bound of random number selected by computer
MAX_NUM = 100           # upper bound of random number selected by computer
TIMES_TO_CELEBRATE = 4  # number of times to print celebratory message after winning


def main():
    # Select random number and give user introduction
    secret_number = random.randint(MIN_NUM, MAX_NUM)
    print("I am thinking of a number between " + str(MIN_NUM) + " and " + str(MAX_NUM))

    # Allow the user to repeatedly guess the number until they are correct
    while True:
        guess = int(input("Enter a guess: "))
        if guess == secret_number:
            break
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print("")                       # print an empty line

    # Print out a congratulatory celebration message
    print("Congrats! The number was: " + str(secret_number))
    for i in range(TIMES_TO_CELEBRATE):
        print("You rock!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
