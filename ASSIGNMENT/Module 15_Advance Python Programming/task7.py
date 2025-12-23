# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.)
# single inheritance

class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")


c = Child()
c.show_parent() 
c.show_child()   



# multiple inheritance

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Father:
    def show_father(self):
        print("This is Father class")

class Child(Mother, Father):
    def show_child(self):
        print("This is Child class")

c = Child()
c.show_mother()
c.show_father()
c.show_child()


# multilevel inheritance

class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

c = Child()
c.show_grandparent()  
c.show_parent()        
c.show_child()        


# hierarchical inheritance

class Parent:
    def show_parent(self):
        print("This is Parent class")
    
class Child1(Parent):
    def show_child1(self):
        print("This is Child1 class")

class Child2(Parent):
    def show_child2(self):
        print("This is Child2 class")

c1 = Child1()
c1.show_parent()
c1.show_child1()
c2 = Child2()
c2.show_parent()
c2.show_child2()


# hybrid inheritance

class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent")


class Parent1(Grandparent):
    def show_parent1(self):
        print("This is Parent1")


class Parent2:
    def show_parent2(self):
        print("This is Parent2")


class Child(Parent1, Parent2):
    def show_child(self):
        print("This is Child")


c = Child()
c.show_grandparent()  
c.show_parent1()      
c.show_parent2()     
c.show_child()        
