# In Python Object-Oriented Programming (OOP), inheritance is a mechanism that allows a new class to derive attributes and methods from an existing class.

# Types of Inheritance

# Single Inheritance: A child class inherits from only one parent class.

class Car:
    @staticmethod
    def start():
        print("Car is started")

    @staticmethod
    def stop():
        print("Car is stopped")


class Toyota(Car):
    def __init__(self, name):
        self.name = name


car1 = Toyota("Fortuner")
print(car1.start())
# This was single inheritance that the methods of Car derived from car to Toyota

# Multi-level inheritance is an object-oriented programming concept where a class is derived from another derived class, creating a parent-child-grandchild chain
# for example i can inherit start from Toyota as it has properties of Car


class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type


car2 = Fortuner("Electric")
print(car2.start())

#  Multiple inheritance is an object-oriented programming feature allowing a derived class to inherit properties and behaviors from two or more base classes.

# For Example i have create 3 classes name A B C , Now iam going to print A and B class using C class as you see in the following code:


class A:
    varA = print("This is Class A")


class B:
    varB = print("This is Class B")


class C(A, B):
    varC = print("This is variable C")


text = C()
print(text.varA)
print(text.varB)
print(text.varC)

# Done
