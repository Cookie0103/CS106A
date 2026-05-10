"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    num = int(input("Enter a numbers: "))
    i = 0
    while num != 1:
        if num % 2 == 0:
            old = num
            num = num // 2
            print(int(old), "is even, so I take half: ", int(num))
        else:
            old = num
            num = 3* num + 1
            print(int(old), "is odd, so I make 3n+1: ", int(num))
        i += 1
    print("The process took ", i, " steps to reach 1")
            


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
