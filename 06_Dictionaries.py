student = {
    "name": "Ali",
    "age": 22,
    "course": "Data Science"
}
print(student)
# How to Access Elements

print(student["name"])
print(student.get("age"))


# Dictionaries Method
student["age"] = 23
student["City"] = "Lahore"
student.pop("course")

print(student)


# Looping Dictionary
for key, value in student.items():
    print(key, ":", value)
