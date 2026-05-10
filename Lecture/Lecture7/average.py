"""
File: average.py
----------------
This program shows an example of using a function to compute
an average of two numbers.
"""


def main():
    mid = average(5.0, 10.2)
    print(mid)


def average(a, b):
    """
    Returns the average value of a and b
    """
    sum = a + b
    return sum / 2


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
