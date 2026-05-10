"""
File: compiledict.py
--------------------
Provides an example of the kind of problem that might be on the final exam.

Given a dictionary of dictionaries where the inner dictionaries may have some matching
keys, return a dictionary that contains all the keys of inner dictionaries where the
value is the sum over all the values in the inner dictionary with the same key.
"""


def compile_dict(dict):
    result = {}

    # loop over all keys in outer dictionary
    for outer_key in dict:
        # Get the inner dictionary associated with key from outer dictionary
        inner_dict = dict[outer_key]

        # Loop over all keys in inner dictionary
        for inner_key in inner_dict:
            value = inner_dict[inner_key]

            if inner_key in result:
                # If the inner key is already in the result dictionary, then
                # add the current value to the value associated with that key
                # in the result dictionary.
                result[inner_key] += value
            else:
                # Otherwise, the inner key is not in the result dictionary, so
                # add the current value with the inner key to the result dictionary.
                result[inner_key] = value

    return result


def main():
    example_dict1 = {
        'Mehran': {
            'age': 52,
            'height': 70,
            'goatees': 1
        },
        'Juliette': {
            'age': 23,
            'height': 68
        },
    }

    example_dict2 = {
        'CA': {
            'zipcodes': 1741,
            'area codes': 36,
            'population': 39000000
        },
        'OR': {
            'zipcodes': 411,
            'area codes': 4
        },
        'TX': {
            'zipcodes': 1930,
            'area codes': 27,
            'population': 29000000
        },
    }

    print('Compilation for first example:', compile_dict(example_dict1))
    print('Compilation for second example:', compile_dict(example_dict2))


if __name__ == '__main__':
    main()
