# Create a mini-project where students combine conditional statements, loops, and functions to create a basic Python application

students = []

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'


def add_student():
    name = input("Enter student name: ")
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            grade = calculate_grade(marks)
            students.append({'name': name, 'marks': marks, 'grade': grade})
            print("Student added successfully!")
        else:
            print("Invalid marks! Must be between 0 and 100.")
    except ValueError:
        print("Please enter valid numeric marks.")


def display_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for student in students:
            print(f"Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}")
        print()

def main():
    while True:
        print("Grade Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

main()
