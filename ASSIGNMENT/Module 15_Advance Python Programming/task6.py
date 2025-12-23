#  Write a Python program to create a class and access its properties using an object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Niyati", 18)

print("Name:", s1.name)
print("Age:", s1.age)
