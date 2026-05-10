"""
File: superguessnumber.py
-------------------------
This program implements a simple guessing game where the computer picks
a random number (integer) between MIN_NUM and MAX_NUM and the user
tries to guess the number.  The computer prompts if the user's guess is
too low or too high.  The user repeatedly guesses until they guess the
right answer.  The program prints out how many guesses the user took
before getting the right number.
"""

import random

MIN_NUM = 1             # lower bound of random number selected by computer
MAX_NUM = 100           # upper bound of random number selected by computer
TIMES_TO_CELEBRATE = 4  # number of times to print celebratory message after winning


def main():
    """
    Select random number and give user introduction, then play game and
    print out a final message when the user wins.
    """
    secret_number = random.randint(MIN_NUM, MAX_NUM)
    intro_message()
    num_guesses = play_game(secret_number)
    print_winning_message(num_guesses, secret_number)


def intro_message():
    """
    Prints an introductory message for the game
    """
    print("I am thinking of a number between " + str(MIN_NUM) + " and " + str(MAX_NUM))


def play_game(number):
    """
    Allow the user to repeatedly guess the number until they are correct.
    Let them know if they guessed too high or too low.
    Returns the number of guesses made by the user before they get the right
    answer.
    """
    num_guesses = 0         # Keep track of number of guesses
    while True:
        guess = int(input("Enter a guess: "))
        num_guesses += 1
        if guess == number:
            break
        if guess < number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print("")           # Prints an empty line
    return num_guesses      # Return number of guesses made by player


def print_winning_message(num_guesses, number):
    """
    Print out a congratulatory celebration message
    """
    print("Congrats! The number was: " + str(number))
    print("You got it in " + str(num_guesses) + " guesses!")
    for i in range(TIMES_TO_CELEBRATE):
        print("You rock!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
