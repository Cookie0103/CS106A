"""
File: gridswap.py
-----------------
This program shows an example of swapping items
in a list of lists (grid).
"""


def swap(grid, row1, col1, row2, col2):
    """
    This function swaps the elements at locations (row1, col1)
    and (row2, col2) in the grid passed in.
    """
    temp = grid[row1][col1]
    grid[row1][col1] = grid[row2][col2]
    grid[row2][col2] = temp


def main():
    my_grid = [[10, 20, 30], [40, 50, 60]]
    print("Original grid:")
    print(my_grid)

    swap(my_grid, 0, 1, 1, 2)
    print("Grid after swapping two elements:")
    print(my_grid)


if __name__ == '__main__':
    main()
