"""
File: first_string_example.py
-----------------------------
This program shows a simple example of creating a string and looping
through it to print out all the characters, one at a time.
"""

def main():
    example = "Hi mom!"

    # example of length function
    length = len(example)
    print(length)  # prints 6

    # example of getting a single character
    first = example[0]
    print(first)  # prints 'H'

    # loop that prints letters one-by-one
    for i in range(len(example)):
        ch = example[i]
        print(i, ch)


if __name__ == '__main__':
    main()
