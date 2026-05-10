"""
File: listswap.py
-----------------
This program shows examples of buggy and successful ways
of swapping two elements in a list.
"""


def swap_elements_buggy(elem1, elem2):
    """
    This function tries to swap the two elements passed it.
    This code is BUGGY!
    """
    temp = elem1
    elem1 = elem2
    elem2 = temp


def swap_elements_working(alist, index1, index2):
    """
    This function successfully swaps the two elements at
    positions index1 and index2 in the list (alist) passed in.
    """
    temp = alist[index1]
    alist[index1] = alist[index2]
    alist[index2] = temp


def main():
    my_list = [10, 20, 30]
    print("Original list:")
    print(my_list)

    swap_elements_buggy(my_list[0], my_list[1])
    print("List after buggy attempt at swap:")
    print(my_list)

    print("List after successful attempt at swap:")
    swap_elements_working(my_list, 0, 1)
    print(my_list)


if __name__ == '__main__':
    main()
