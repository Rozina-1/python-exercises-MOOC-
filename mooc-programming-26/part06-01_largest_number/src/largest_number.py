# import os

def largest():
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(script_dir, "numbers.txt")
    with open("numbers.txt") as new_file:
        greatest = 0
        for line in new_file:
            number1 = int(line.replace("\n", ""))
            if number1 > greatest:
                greatest = number1
    return greatest

if __name__ == "__main__":
    print(largest())