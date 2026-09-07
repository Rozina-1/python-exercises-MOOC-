from pathlib import Path
def read_fruits():
    script_dir = Path(__file__).parent
    file_path = script_dir / "fruits.csv"
    with open(file_path) as new_file:
        fruit = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            price =float( parts[1])
            fruit[name] = price
        return fruit

if __name__ == "__main__":
    print(read_fruits())
            
    