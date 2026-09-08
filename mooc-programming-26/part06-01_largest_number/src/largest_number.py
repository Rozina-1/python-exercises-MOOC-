from pathlib import Path

def largest():
    script_dir = Path(__file__).parent
    file_path = script_dir / "numbers.txt"
    with open(file_path) as new_file:
        greatest = 0
        for line in new_file:
            number = int(line.strip())
            if number > greatest:
                greatest = number
    return greatest

if __name__ == "__main__":
    print(largest())