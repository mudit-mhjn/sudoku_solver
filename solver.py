"""
this file takes input a grid with empty spaces marked as '0' and returns a solved grid.
"""

def find_empty_cell(grid, rcrd):
    for row in range(9):
        for coloumn in range(9):
            if grid[row][coloumn] == 0:
                rcrd[0] = row
                rcrd[1] = coloumn
                return True
    return False

def check_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False

def check_coloumn(grid, coloumn, num):
    for i in range(9):
        if grid[i][coloumn] == num:
            return True
    return False

def check_box(grid, row, coloumn, num):
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+coloumn] == num:
                return True
    return False

def check_location(grid, row, coloumn, num):
    return not check_row(grid, row, num) and not check_coloumn(grid, coloumn, num) and not check_box(grid, row-row%3, coloumn-coloumn%3, num)

def solve_sudoku(grid):
    rcrd = [0,0]

    if not (find_empty_cell(grid, rcrd)):
        return True
    row = rcrd[0]
    coloumn = rcrd[1]
    for i in range(1, 10):
        if check_location(grid, row, coloumn, i):
            grid[row][coloumn] = i
            if solve_sudoku(grid):
                return True
            grid[row][coloumn] = 0
    return False

if __name__ == '__main__':
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solve_sudoku(grid):
        for i in range(9):
            print('')
            for j in range(9):
                print(grid[i][j], end = " ")
    else:
        print("No Solution")

                


