name = {}
exercises = {}
exam_points = {}
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
        exercises[parts[0]] = exercises[parts[0]]//4


with open(file_path3) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        exam_points[parts[0]] = 0
        for value in parts[1:]:
            exam_points[parts[0]] += int(value)

def course_grading():
    total_points = 0
    for key,value in exam_points.items():
        total_points = value + exercises[key]
        if total_points <= 14:
            grade = 0
        elif total_points <= 17:
            grade = 1
        elif total_points <= 20:
            grade = 2
        elif total_points <= 23:
            grade = 3
        elif total_points <= 27:
            grade = 5
        print(name[key], grade)

course_grading()