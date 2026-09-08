
from pathlib import Path
def read_matrix():
    matrix = []
    script_dir = Path(__file__).parent
    file_path = script_dir/"matrix.txt"
    with open(file_path) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            int_row = []
            string_row = line.split(",")
            for value in string_row:
                int_row.append(int(value))
            matrix.append(int_row)
    return matrix



def matrix_sum():
    matrix = read_matrix()
    sum = 0
    for row in matrix:
        for column in row:
            sum += column
    return sum

def matrix_max():
    matrix = read_matrix()
    max = 0
    for row in matrix:
        for column in row:
            if column > max:
                max = column
    return max

def row_sums():
    matrix = read_matrix()
    rowSum = []
    for row in matrix:
        temp = 0
        for column in row:
            temp += column
        rowSum.append(temp)
    return rowSum

if __name__ == "__main__" :
    matrix = []
    read_matrix()
    print("matrix sum is: ", matrix_sum())
    print("maximum value is: ", matrix_max())
    print("sum of individual row is: ", row_sums())
