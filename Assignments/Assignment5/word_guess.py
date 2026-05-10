"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "TestLexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    # print(secret_word)
    guess_left = INITIAL_GUESSES
    guessed_letters = set()
    print("The word now looks like this: ", "-"*len(secret_word))
    display = check_word("", secret_word, "-"*len(secret_word))
    while True:
        print(f"You have {guess_left} guesses left")
        letter = input("Type a single letter here, then press enter: ")
        
        if len(letter) > 1:
            print("Guess should only be a single character.")
            print("The word now looks like this: ", display)
            continue
        if letter.upper() in guessed_letters:
            print("You already guessed that letter.")
            continue
        display = check_word(letter, secret_word, display)
        if letter.upper() not in secret_word:
            print(f"There are no {letter.upper()}'s in the word")
            print("The word now looks like this: ", display)
            guess_left -= 1
        elif letter.upper() in secret_word:
            print("That guess is correct.")
            print("The word now looks like this: ", display)
        guessed_letters.add(letter.upper())
        
        if guess_left > 0:
            if guess_all(display):
                print("Congratulations, the word is: ", secret_word)
                break
        else:
            print("Sorry, you lost. The secret word was: ", secret_word)
            break            
            
def check_word(letter, secret_word, display):
    if letter == "":
        return "-" * len(secret_word)
    for i in range(len(secret_word)):
        if display[i] == "-":
            if letter.upper() == secret_word[i]:
                display = display[:i] + letter.upper() + display[i+1:]
    return display

def guess_all(display):
    if "-" in display:
        return False
    else:
        return True

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    # index = random.randrange(3)
    # if index == 0:
    #     return 'HAPPY'
    # elif index == 1:
    #     return 'PYTHON'
    # else:
    #     return 'COMPUTER'
    secret_list = []
    with open(LEXICON_FILE, "r") as file:
        for line in file:
            secret_list.append(line.strip())
    
    index = random.randrange(len(secret_list))
    return secret_list[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()