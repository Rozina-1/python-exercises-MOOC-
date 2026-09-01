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

def add_number(sudoku, r, c, num):
    for i in range(0,9):
        for j in range(0,9):
            if i==r and j == c:
                sudoku[r][c] += num

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)