name = {}
exercises = {}
exam_points = {}
exercises_points = {}

from pathlib import Path

file_name1 = input("Student information: ")
file_name2 = input("Exercises completed: ")
file_name3 = input("Exam points: ")

script_dir = Path(__file__).parent
file_path1 = script_dir / file_name1
file_path2 = script_dir / file_name2
file_path3 = script_dir / file_name3

with open(file_path1) as new_file:
    for line in new_file:
        line = line.replace("\n","")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        name[parts[0]] = parts[1] + " " + parts[2]

with open(file_path2) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        exercises[parts[0]] = 0
        for value in parts[1:]:
            exercises[parts[0]] += int(value)
        exercises_points[parts[0]] = exercises[parts[0]] // 4

with open(file_path3) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        exam_points[parts[0]] = 0
        for value in parts[1:]:
            exam_points[parts[0]] += int(value)

print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}grade")

for key, value in exam_points.items():
    total_points = value + exercises_points[key]
    if total_points <= 14:
        grade = 0
    elif total_points <= 17:
        grade = 1
    elif total_points <= 20:
        grade = 2
    elif total_points <= 23:
        grade = 3
    elif total_points <= 27:
        grade = 4
    else:
        grade = 5
        
    print(f"{name[key]:<30}{exercises[key]:<10}{exercises_points[key]:<10}{exam_points[key]:<10}{total_points:<10}{grade}")
