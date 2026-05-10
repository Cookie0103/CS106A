"""
File: palindrome.py
-------------------
This program determines if a string is a palindrome or not.
"""


# A few examples of palindromes and one that's not
PANAMA = 'A man, a plan, a canal, Panama!'
KOREAN = '여보, 안경 안보여'
OWL = 'Mr. Owl ate my metal worm.'
HINDI = 'कडक'
NOT_PALINDROME = 'Have a nice day!'


def is_palindrome(str):
    """
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('Abba!')
    True
    >>> is_palindrome('mehran')
    False
    """
    normalized = normalize(str)
    rev = reverse(normalized)
    return normalized == rev


def normalize(str):
    """
    This function returns a "normalized" version of the string passed in.
    The normalized string only includes alphabetic characters (in any Unicode
    supported alphabet).  For examples, whitespace, punctuation, and digits
    would not be included in the normalized string.
    >>> normalize('abc 1!2 def')
    'abcdef'
    >>> normalize('여보, 안경')
    '여보안경'
    """
    normalized = ''
    for ch in str:
        if ch.isalpha():
            normalized += ch.lower()
    return normalized


def reverse(str):
    """
    This function returns a reversed copy of the string passed in.
    >>> reverse('stressed')
    'desserts'
    >>> reverse('hello')
    'olleh'
    """
    return str[::-1]    # oh yeah, feel the power of slices!


def main():
    original = PANAMA
    print(original)

    if is_palindrome(original):
        print('Is a palindrome of length ' + str(len(original)) + ' characters')
    else:
        print('Is not a palindrome...')


if __name__ == '__main__':
    main()
