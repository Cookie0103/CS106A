"""
File: use_counter.py
--------------------
This program provides an example of using Counter objects
"""

from counter import Counter     # import the Class


def count_two_times(count):
    """
    Get and prints next two numbers in a Counter object
    """
    for i in range(2):
        print(count.next_value())


def main():
    count1 = Counter()      # Create a new Counter object
    count2 = Counter()      # Create another new Counter object

    print('Count1: ')
    count_two_times(count1)

    print('Count2: ')
    count_two_times(count2)

    print('Count1: ')
    count_two_times(count1)


if __name__ == '__main__':
    main()
