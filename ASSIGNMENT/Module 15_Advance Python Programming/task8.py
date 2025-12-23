# Write Python programs to demonstrate method overloading and method overriding.

class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        print("This is Child class method")

p = Parent()
p.show()  

c = Child()
c.show() 
