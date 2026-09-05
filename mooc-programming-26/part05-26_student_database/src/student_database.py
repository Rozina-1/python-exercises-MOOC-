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
        if course[1] == 0:
            return
        for i,(cour, grade) in enumerate(students[name]):
            if cour == course[0]:
                if course[1] > grade:
                    students[name][i] = course
                return

        students[name].append(course)

def summary(students: list):
    print(f"students {len(students)}")
    most_course = 0
    nam = ""
    total_grade = 0
    best_average = 0
    for name,course in students.items():
        if len(course) > most_course:
            most_course = len(course)
            nam = name
    print(f"most courses completed {most_course} {nam}")

    for name, courses in students.items():
        for course,grade in courses:
            total_grade += grade
            average = total_grade/len(students[name])
            if average > best_average:
                best_average = average
                na = name
    # for course, grade in courses:
    #     total_grade += grade
    #     average = total_grade/len(students[name])
    #     if average > best_average:
    #         best_average = average
    #         na = name
    print(f"best average grade {best_average} {na}")  



if __name__ == "__main__":  
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 2))
    # print_student(students, "Peter")
     
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)
