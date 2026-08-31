def sudoku_grid_correct(sudoku):
    for r in range(9):
        if not row_correct(sudoku, r):
            return False
    for c in range(9):
        if not column_correct(sudoku,c):
            return False
    for r in range(0,9,3):
        for c in range(0,9,3):
            if not block_correct(sudoku, r, c):
                return False
    return True
def block_correct(sudoku, row, col):
    new_row = []
    i = 0
    j = 0
    for i in range(row, row + 3):
      for j in range(col, col + 3):
           if sudoku[i][j] in new_row and sudoku[i][j]>0:
                return False
           new_row.append(sudoku[i][j])
    return True   
def column_correct(sudoku: list, column_no: int):
    new_row = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in new_row:
            return False
        new_row.append(row[column_no])
    return True
def row_correct(sudoku , row):
    new_row = []
    for item in sudoku[row]:
        if item != 0:
            if item in new_row:
                return False
            new_row.append(item)
    return True 
if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))