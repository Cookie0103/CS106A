# def is_valid_grid(grid):
#     appear = []
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if not grid[i][j] in appear:
#                 appear.append(grid[i][j])
#             else:
#                 return False
#     return True

# grid1 = [[7,5,4], [3,2,1], [6,9,6]]
# p = is_valid_grid(grid1)
# print(p)
# grid2 = [[1,2,3], [5,6,8], [9,7,4]]
# p = is_valid_grid(grid2)
# print(p)

def is_value_present(grid, value):
    # 遍历grid是否等于value，是就返回True
    for row in grid:
        for num in row:
            if num == value:
                return True
    return False
    
def is_valid_grid(grid):
    # 遍历1-9
    for i in range(1, 10):
        if not is_value_present(grid, i):
            return False
    return True