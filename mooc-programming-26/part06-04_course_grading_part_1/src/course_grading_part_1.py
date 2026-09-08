name = {}
from pathlib import Path

file_name1 = input("Student information: ")
file_name2 = input("Excercises completed: ")
script_dir = Path(__file__).parent
file_path1 = script_dir / file_name1
file_path2 = script_dir / file_name2
with open(file_path1) as new_file:
    for line in new_file:
        line = line.replace("\n","")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        name[parts[0]] = parts[1] + " " + parts[2]

excercises = {}
with open(file_path2) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        excercises[parts[0]] = 0
        for value in parts[1:]:
            excercises[parts[0]] += int(value)


for key,value in excercises.items():
    print(name[key], value)