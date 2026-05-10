def diagonal_line(grid):
    x, y = check_location(grid)
    grid = draw_diagonal(grid, x, y)
    return grid

def check_location(grid):
    rows, cols = rows_cols(grid)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return i, j

def draw_diagonal(grid, x, y):
    if check_edge(grid, x, y):
        return grid
    else:
        grid = draw_up_half(grid, x, y)
        grid = draw_down_half(grid, x, y)
        return grid


def check_edge(grid, x, y):
    rows, cols = rows_cols(grid)
    if x == 0 and y == cols - 1:
        return True
    elif x == rows - 1 and y == 0:
        return True
    else:
        return False

def rows_cols(grid):
    return len(grid), len(grid[0])

def draw_up_half(grid, x, y):
    rows, cols = rows_cols(grid)
    while True:
        x -= 1
        y -= 1
        if x >= 0 and x < rows and y >= 0 and y < cols:
            grid[x][y] = 1
        else:
            break
    return grid

def draw_down_half(grid, x, y):
    rows, cols = rows_cols(grid)
    while True:
        x += 1
        y += 1
        if x >= 0 and x < rows and y >= 0 and y < cols:
            grid[x][y] = 1
        else:
            break
    return grid


grid1 = [[0,0,0],[0,0,0],[0,0,0],[0,1,0]]
grid2 = [[0,0,1],[0,0,0],[0,0,0]]
print(diagonal_line(grid1))
print(diagonal_line(grid2))