"""
File: maxmax.py
---------------
This program shows an example of using a function to compute
the maximum of two numbers.
"""


def main():
    larger = max(5, 1)
    print(larger)


def max(num1, num2):
    """
    Returns the maximum value of num1 and num2
    """
    if num1 >= num2:
        return num1

    return num2


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
