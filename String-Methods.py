
first_name = "Muhammad Faseeh"
Last_Name = "Ullah"

# # method 1
# print(first_name + + Last_Name)

FullName = first_name + " " + Last_Name

# print(FullName)


# -----------------------------------
name = FullName
age = 18
is_student = True

# Making Sentences through these variables
# method 1
print("My name is " + FullName + "My age is " +
      str(age) + " and student status is " + str(is_student) + ".")


# Method 2 Using F String

print(
    f"My Name is {name}, I am {age} years old, and student status {is_student}.")

# By using F String We can also add mathematical rules easily in Double quotes

print(f"2 + 2 = {2 + 2}")


# Transformations
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))

# Repeatition of Text
print("ha" * 7)  # This wil Print "ha" for 7 times like "hahahahahahaha.."
print("=" * 20)  # This will Print = Symbol 10 Times


# Extractions of String by Index
text = "Python"
print(text[0:4])

print(text[-5:-2])

print(text[2:4])

print(text[2:])

print(text[2:])

print(text[0:4:1])


# Extracting Positve Character
print(text[0])
print(text[1])
print(text[2])
# : Means not to stopped go to end


# Some Examples of printing Date
date = "2026-09-12"
print(date[0:4])
print(date[:4])  # Not need to define where to start

# Just Print 2026
# Now following just printing the Months
print(date[5:7])
# By Negative values
print(date[-4])
print(date[-5:-3])
