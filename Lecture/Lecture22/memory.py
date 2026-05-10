"""
File: memory.py
---------------
Shows how memory is used when dealing with variables and parameters
in Python.
"""


def main():
    x = ['a', 'b', 'c']
    print(x)
    update_in_list(x)
    print(x)
    update_list(x)
    print(x)


def update_in_list(x):
    x[0] = 'z'
    x[1] = 'z'
    x[2] = 'z'


def update_list(x):
    x = ['m', 'n', 'o']


if __name__ == '__main__':
    main()
