"""
File: reverse_dict.py
---------------------
This program shows an example of reversing a dictionary.  The result
is a dictionary where for each key there is a list for the value.  That
list contains the keys from the original dictionary that shared the same
value that is now the key in the reversed dictionary.
"""

def reverse(original):
    """
    This function creates and returns a new dictionary where
    the values of the original dictionary are the keys.  And
    the keys in the original dictionary are included in lists
    that are the values in the reversed dictionary.
    """
    reversed = {}
    for key in original:
        value = original[key]

        # Need to create an empty list if the value associated with
        # the key in the original dictionary has not yet been added
        # as a key in the reversed dictionary.
        if value not in reversed:
            reversed[value] = []

        reversed[value].append(key)

    return reversed


def main():
    birth_year = {'Mehran Sahami': 1970,
                  'Chris Piech': 1988,
                  'Queen Latifah': 1970,
                  'Jamie Chang': 2003,
                  'Jennifer Connelly': 1970,
                  'Pat Jones': 2003
                  }

    print('Forward:')
    print(birth_year)

    reversed = reverse(birth_year)

    print('Reversed:')
    print(reversed)


if __name__ == '__main__':
    main()
