def diagonal_line(grid):
    # 找到1的位置，然后直接遍历行找对应列
    row0, col0 = 0, 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                row0, col0 = row, col
    
    for row in range(len(grid)):
        col =  col0 - row0 + row
        if col >= 0 and col < len(grid[0]):
            grid[row][col] = 1
    print(grid)


grid1 = [[0,0,0],[0,0,0],[0,0,0],[0,1,0]]
grid2 = [[0,0,1],[0,0,0],[0,0,0]]
diagonal_line(grid1)
diagonal_line(grid2)