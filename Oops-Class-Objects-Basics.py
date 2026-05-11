class Student:

    college_name = "GCS"

    def __init__(self, name, marks):
        self.n = name
        self.m = marks


s1 = Student(input("Enter Your Name"), input("Enter Your Marks"))


s2 = Student(input("Enter Your Name"), input("Enter Your Marks"))

print(s1.n, s1.m, s1.college_name)
print(s2.n, s2.m, )
