"""
File: indexalphabet.py
----------------------
This program determines the position/index of letters in the alphabet.  For example,
'a' is 0, 'B' is 1, etc.  This is really a program to show examples of functions
on individual characters.
"""


def index_in_alphabet(ch):
    """
    This function is passed a character (string) representing a letter and
    returns it's index in the alphabet (regardless of case).  It returns -1
    if the character passed in is not a letter.
    >>> index_in_alphabet('a')
    0
    >>> index_in_alphabet('D')
    3
    >>> index_in_alphabet('!')
    -1
    """
    if ch.isalpha():
        lowercase = ch.lower()
        return ord(lowercase) - ord('a')
    else:
        return -1


def main():
    x = input('Enter a letter: ')
    index = index_in_alphabet(x)
    if index != -1:
        print('That letter is at index:', index)
    else:
        print(x, 'is not a letter.')


if __name__ == '__main__':
    main()
