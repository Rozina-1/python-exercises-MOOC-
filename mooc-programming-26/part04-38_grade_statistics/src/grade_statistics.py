total_points_list = []
grades_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
passed_students = 0
total_students = 0

while True:
    user_input = input("Exam points and exercises completed: ")
    
    if user_input == "":
        break
        
    parts = user_input.split()
    exam_points = int(parts[0])
    exercises_completed = int(parts[1])
    
    exercise_points = exercises_completed // 10
    
    total_points = exam_points + exercise_points
    total_points_list.append(total_points)
    total_students += 1
    
    if exam_points < 10:
        grade = 0
    elif 0 <= total_points <= 14:
        grade = 0
    elif 15 <= total_points <= 17:
        grade = 1
    elif 18 <= total_points <= 20:
        grade = 2
    elif 21 <= total_points <= 23:
        grade = 3
    elif 24 <= total_points <= 27:
        grade = 4
    elif 28 <= total_points <= 30:
        grade = 5
        
    grades_distribution[grade] += 1
    if grade > 0:
        passed_students += 1

print("Statistics:")

if total_students > 0:
    points_average = sum(total_points_list) / total_students
    pass_percentage = (passed_students / total_students) * 100
else:
    points_average = 0.0
    pass_percentage = 0.0

print(f"Points average: {points_average:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")

print("Grade distribution:")
for g in grades_distribution:
    stars = "*" * grades_distribution[g]
    print(f"  {g}: {stars}")
