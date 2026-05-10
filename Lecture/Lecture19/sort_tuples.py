"""
File: sort_tuples.py
--------------------
This program provides an example of sorting a list of tuples a custom function
"""


def get_count(food):
    # returns the second element of the tuple food
    return food[1]


def main():
   foods = [('apple', 5), ('banana', 2), ('chocolate', 137)]
   sort_names = sorted(foods)
   print(sort_names)
   sort_count = sorted(foods, key=get_count)
   print(sort_count)
   rev_sort_count = sorted(foods, key=get_count, reverse=True)
   print(rev_sort_count)


if __name__ == '__main__':
    main()
