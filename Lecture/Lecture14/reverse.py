"""
File: reverse.py
----------------
This program shows an example of reversing a string, character by character,
and by using slices.
"""


def reverse(str):
    """
    Takes a string and returns a reversed copy.  Uses for-each loop.
    >>> reverse('stressed')
    'desserts'
    >>> reverse('hello')
    'olleh'
    """
    result = ''
    for ch in str:
        result = ch + result
    return result


def reverse2(str):
    """
    Takes a string and returns a reversed copy.  Uses for-range loop.
    >>> reverse2('stressed')
    'desserts'
    >>> reverse2('hello')
    'olleh'
    """
    result = ''
    for i in range(len(str)-1, -1, -1):   # counts from len(str)-1 down to 0 (including 0)
        ch = str[i]
        result += ch
    return result


def reverse3(str):
    """
    Takes a string and returns a reversed copy.  Uses slices.
    >>> reverse2('stressed')
    'desserts'
    >>> reverse2('hello')
    'olleh'
    """
    return str[::-1]


def main():
    x = input('Enter a string: ')
    rev = reverse(x)
    print(x + ' spelled backwards is ' + rev)


if __name__ == '__main__':
    main()
