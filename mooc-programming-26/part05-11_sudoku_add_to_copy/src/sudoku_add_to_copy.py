def print_sudoku(sudoku):
    for r in range(0,9):
        if r == 3 or r == 6:
            print()
        for c in range(0,9):
            if c == 3 or c == 6:
                print(" ", end = "")
            if sudoku[r][c] == 0:
                print("_", end = " ")
            else:
                print(sudoku[r][c], end = " ")
        print()
def copy_and_add(sudoku, r , c , num):
    sudoku1 = []
    for row in sudoku:
        sudoku1.append(row[:]) 
    sudoku1[r][c] = num
    return sudoku1

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)