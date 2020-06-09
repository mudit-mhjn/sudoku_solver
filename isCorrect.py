"""
This will return 1 if the given grid is possible or not
returns True if grid is valid
returns False if grid is invalid
"""
import numpy as np

def valid_row(row_num, grid):
    temp = grid[row_num]
    temp = list(filter(lambda x: x!=0, temp)) # removing zeroes or empty spaces
    for i in temp:
        if i<0 or i>9:
            return False
    if len(temp) != len(set(temp)):
        return False
    else:
        return True

def valid_coloumn(coloumn_num, grid_transposed):
    temp = grid_transposed[coloumn_num]
    temp = list(filter(lambda x: x!=0, temp))
    for i in temp:
        if i<0 or i>9:
            return False
    if len(temp) != len(set(temp)):
        return False
    else:
        return True

def valid_subsquare(grid):
    for row in range(0, 9, 3):
        for coloumn in range(0, 9, 3):
            temp = []
            for r in range(row, row+3):
                for c in range(coloumn, coloumn+3):
                    if grid[r][c]!=0:
                        temp.append(grid[r][c])
            for i in temp:
                if i>9 or i<0:
                    return False
            if len(temp)!= len(set(temp)):
                return False
    return True

def valid_board(grid):
    grid = np.array(grid)
    for i in range(9):
        check_row = valid_row(i, grid)
        check_coloumn = valid_coloumn(i, grid.T)
    if not (check_row and check_coloumn):
        print("INVALID BOARD")
        return

    check_subgrids = valid_subsquare(grid)
    if check_subgrids:
        return True
    else:
        return False



if __name__ == '__main__':
    grid1 = [[1, 4, 7, 0, 0, 0, 0, 0, 3],
        [2, 5, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 0, 4, 1, 0, 0, 2, 0],
        [9, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 9],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 0, 7]]
    print(valid_board(grid1))
    grid2 = [[1, 4, 4, 0, 0, 0, 0, 0, 3],
         [2, 5, 0, 0, 0, 1, 0, 0, 0],
         [3, 0, 9, 0, 0, 0, 0, 0, 0],
         [0, 8, 0, 0, 2, 0, 0, 0, 4],
         [0, 0, 0, 4, 1, 0, 0, 2, 0],
         [9, 0, 0, 0, 0, 0, 6, 0, 0],
         [0, 0, 3, 0, 0, 0, 0, 0, 9],
         [4, 0, 0, 0, 0, 2, 0, 0, 0],
         [0, 0, 1, 0, 0, 8, 0, 0, 7]]
    print(valid_board(grid2))
    
