# class Student:

#     college_name = "GCS"

#     def __init__(self, name, marks):
#         self.n = name
#         self.m = marks


# s1 = Student(input("Enter Your Name"), input("Enter Your Marks"))


# s2 = Student(input("Enter Your Name"), input("Enter Your Marks"))

# print(s1.n, s1.m, s1.college_name)
# print(s2.n, s2.m, )


# Example 2 | Getting AVG Marks of three Subjects
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print(f"Your Average Marks is {sum / 3}")


s1 = Student("Faseeh", [90, 95, 99])
print(s1.name)
s1.get_avg()
