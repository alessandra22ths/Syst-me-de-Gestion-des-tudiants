def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, age, grades = line.strip().split("|")
                if grades:
                    grades_list = [float(g) for g in grades.split(",")]
                else:
                    grades_list = []
                students.append({
                    "name": name,
                    "age": age,
                    "grades": grades_list
                })
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            grades = ",".join(str(g) for g in student["grades"])
            file.write(f"{student['name']}|{student['age']}|{grades}\n")

def export_to_csv(students):
    import csv
    with open("students_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Average", "Grades"])
        for student in students:
            if student["grades"]:
                average = sum(student["grades"]) / len(student["grades"])
            else:
                average = 0
            grades_str = ",".join(str(g) for g in student["grades"])
            writer.writerow([student["name"], student["age"], f"{average:.2f}", grades_str])
    print("Report exported to students_report.csv")

students = load_students()

print("Student Management System")

while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. View students")
    print("3. Add grade")
    print("4. Edit student")
    print("5. Delete student")
    print("6. Search student")
    print("7. View ranking")
    print("8. Exit")
    print("9. Export report to CSV")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Student name: ")
        age = input("Student age: ")
        student = {"name": name, "age": age, "grades": []}
        students.append(student)
        print("Student added!")

    elif choice == "2":
        if not students:
            print("No students yet.")
        else:
            for index, student in enumerate(students, start=1):
                if student["grades"]:
                    average = sum(student["grades"]) / len(student["grades"])
                    print(f"{index}. {student['name']} - Age: {student['age']} - Average: {average:.2f}")
                else:
                    print(f"{index}. {student['name']} - Age: {student['age']} - No grades yet")

    elif choice == "3":
        if not students:
            print("No students available.")
        else:
            for index, student in enumerate(students, start=1):
                print(f"{index}. {student['name']}")
            student_number = input("Choose student number: ")
            if student_number.isdigit():
                student_number = int(student_number)
                if 1 <= student_number <= len(students):
                    grade_input = input("Enter grade (0-100): ")
                    if grade_input.replace(".", "", 1).isdigit():
                        grade = float(grade_input)
                        if 0 <= grade <= 100:
                            students[student_number - 1]["grades"].append(grade)
                            print("Grade added!")
                        else:
                            print("Grade must be between 0 and 100.")
                    else:
                        print("Invalid grade. Enter a number.")
                else:
                    print("Invalid student number.")
            else:
                print("Enter a valid number.")

    elif choice == "4":
        if not students:
            print("No students to edit.")
        else:
            for index, student in enumerate(students, start=1):
                print(f"{index}. {student['name']} - Age: {student['age']}")
            student_number = input("Choose student number to edit: ")
            if student_number.isdigit():
                student_number = int(student_number)
                if 1 <= student_number <= len(students):
                    student = students[student_number - 1]
                    new_name = input(f"New name ({student['name']}): ")
                    new_age = input(f"New age ({student['age']}): ")
                    if new_name:
                        student["name"] = new_name
                    if new_age:
                        student["age"] = new_age
                    print("Student updated!")
                else:
                    print("Invalid student number.")
            else:
                print("Enter a valid number.")

    elif choice == "5":
        if not students:
            print("No students to delete.")
        else:
            for index, student in enumerate(students, start=1):
                print(f"{index}. {student['name']}")
            student_number = input("Choose student number to delete: ")
            if student_number.isdigit():
                student_number = int(student_number)
                if 1 <= student_number <= len(students):
                    confirm = input(f"Are you sure you want to delete {students[student_number-1]['name']}? (y/n): ")
                    if confirm.lower() == "y":
                        removed = students.pop(student_number - 1)
                        print(f"Deleted student: {removed['name']}")
                    else:
                        print("Deletion canceled.")
                else:
                    print("Invalid student number.")
            else:
                print("Enter a valid number.")

    elif choice == "6":
        search_name = input("Enter student name to search: ").lower()
        found = False
        for index, student in enumerate(students, start=1):
            if search_name in student["name"].lower():
                found = True
                if student["grades"]:
                    average = sum(student["grades"]) / len(student["grades"])
                    print(f"{index}. {student['name']} - Age: {student['age']} - Average: {average:.2f}")
                else:
                    print(f"{index}. {student['name']} - Age: {student['age']} - No grades yet")
        if not found:
            print("No student found with that name.")

    elif choice == "7":
        if not students:
            print("No students yet.")
        else:
            ranking = []
            for student in students:
                if student["grades"]:
                    average = sum(student["grades"]) / len(student["grades"])
                else:
                    average = 0
                ranking.append((student["name"], average))
            ranking.sort(key=lambda x: x[1], reverse=True)
            print("\nRanking of students by average:")
            for i, (name, avg) in enumerate(ranking, start=1):
                print(f"{i}. {name} - Average: {avg:.2f}")

    elif choice == "8":
        save_students(students)
        print("Goodbye!")
        break

    elif choice == "9":
        if not students:
            print("No students yet.")
        else:
            export_to_csv(students)

    else:
        print("Invalid option")