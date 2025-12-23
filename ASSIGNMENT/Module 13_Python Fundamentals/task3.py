# This program demonstrates creation of variables of various data types

# Integer type
age = 18

# Float type
height = 5.7

# String type
name = "Aarav"

# Boolean type
is_student = True

# List type
subjects = ["Math", "Science", "English"]

# Tuple type
marks = (85, 90, 88)

# Dictionary type
student_info = {"name": "Aarav","age": 18,"grade": "A"}

# Set type
unique_numbers = {1, 2, 3, 3, 2}

# Display all variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Subjects:", subjects)
print("Marks (Tuple):", marks)
print("Student Info (Dictionary):", student_info)
print("Unique Numbers (Set):", unique_numbers)


#How does the Python code structure work? 
# This is a simple Python program to greet a user and check their age

# Step 1: Take input from the user
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# Step 2: Print a welcome message
print("Hello,", user_name + "!")

# Step 3: Use control structure (if-else) to give a message based on age
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#how to create variable in python?
# Creating variables of different types
student_name = "Niyati"
student_age = 18
student_grade = "A"
is_passed = True

# Displaying the values
print("Name:", student_name)
print("Age:", student_age)
print("Grade:", student_grade)
print("Passed:", is_passed)


#how to take user input using the input() function
name = input("Enter your name: ")
print("Hello,", name)


#How to check the type of a variable dynamically using type(). 
name = "Aarav"
age = 18
height = 5.6
is_student = True

# Check and print types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

