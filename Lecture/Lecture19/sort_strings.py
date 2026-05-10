"""
File: sort_strings.py
---------------------
This program provides an example of sorting using a custom function
"""


def get_len(s):
    return len(s)


def main():
    strs = ['a', 'bbbb', 'cc', 'zzz']
    sorted_strs = sorted(strs, key=get_len)
    print(sorted_strs)


if __name__ == '__main__':
    main()
