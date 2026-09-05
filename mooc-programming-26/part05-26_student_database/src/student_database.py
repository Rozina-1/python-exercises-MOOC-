def add_student(students: dict, name: str):
    students[name] = []

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return 
    if students[name] == []:
        print(f"{name}:")
        print(" no completed courses")
    else:
        print(f"{name}: ")
        print(f" {len(students[name])} completed courses: ")
        total_grade = 0
        for course,grade in students[name]:
                  total_grade += grade
                  print(f"  {course} {grade}")
        average = total_grade/len(students[name])
        print(" average grade", average)
             

def add_course(students: dict, name: str, course: tuple):
        students[name].append(course)

if __name__ == "__main__":  
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")