
def search_by_name(filename: str, word: str):
    from pathlib import Path
    script_dir = Path(__file__).parent
    file_path = script_dir/filename
    item = []
    found_recipie = []
    temprecipie = []
    with open(file_path) as new_file:
        for line in new_file:
            line = line.strip("\n")
            if line == "":
                item.append(temprecipie)
                temprecipie = []
            else:
                temprecipie.append(line)
        item.append(temprecipie)
    for block in item:
        if word.lower() in block[0].lower():
            found_recipie.append(block[0])
    return found_recipie

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)