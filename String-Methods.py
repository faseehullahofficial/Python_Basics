# In this file you can see multiple strings methods

# 01 How to check type of var

x = 9

print(type(x))

name = "Faseeh"
print(type(name))


# 02 How to check length and count of string
# We have String name

print(len(name))

# Now Lets see what is .count
# As I have a list of multiple students name and some of them are repeating in the list so i can count them by using this However len() will show you how much the number of properties are in your list

Student_name = ["Faseeh", "Saif", "Huzaifa",
                "Abdul Sami", "Shahmeer", "Bilal", "Abdul Razzaq", "Ayan", "Anas", "Saif"]

print(Student_name.count("Saif"))
print(len(Student_name))


# 03 Transformations


# 3.1 replace() We can change the specific value of our string by using this

# The folllowing code output without dash and brackets just phone Number digits

phone = "+49 (176) 123-4567"
print(phone.replace("+", "00").replace("(", "").replace(")",
      "").replace("-", "").replace(" ", ""))


# 3.2 Storing 1 Name and last name as Full Name OR A + B = AB
first_name = "Muhammad Faseeh"
Last_Name = "Ullah"

# # method 1
print(first_name + + Last_Name)

FullName = first_name + " " + Last_Name

# print(FullName)


# ------------------Examples-----------------
name = FullName
age = 18
is_student = True

# Making Sentences through these variables
# method 1
print("My name is " + FullName + "My age is " +
      str(age) + " and student status is " + str(is_student) + ".")


# 3.3 Using F String
# By using F String We can also add mathematical rules easily in Double quotes No need to add + name + age

print(
    f"My Name is {name}, I am {age} years old, and student status {is_student}.")


print(f"2 + 2 = {2 + 2}")


# ------------------------------------------------

# 3.4 Split Method
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))


# 3.5 Repeatition of Text
print("ha" * 7)  # This wil Print "ha" for 7 times like "hahahahahahaha.."
print("=" * 20)  # This will Print = Symbol 10 Times


# ---------------------------------------------
# 3.5 Extractions of String by Index
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


# -------------------------------------------------------------


# 04 Cleaning

# 4.1 Whitespace cleanup

text = " Pakistan".lstrip()
print(text)

text = "Pakistan ".rstrip()
print(text)

text = " Pakistan ".strip()
print(text)


text = "###Pakistan####".strip("#")
print(text)

text = "  Pakistan"
print(len(text))
print(len(text.strip()))

print(len(text) - len(text.strip()))


# 4.2 Case Converstations

text = "Faseeh Ullah"

print(text.lower())
print(text.upper())


# ---------------PYTHON CHALLENGE-----------------

text = "968-Maria, ( D@t@ Engineer ) ;; 27y  "

print(text
      .lower()
      .replace("968-", "name: ")
      .replace("@", "a")
      .replace(",", " |")
      .replace("(", "role:")
      .replace(")", "|")
      .replace(";;", "age:")
      .replace("27y", "27")


      )


# 05-----------------Searching in Python---------------------------
date = "2026-Sep-12"


# 5.1 startswith()
print(date.startswith("2026"))
print(date.startswith("2024"))

# 5.2 endswith()
print(date.endswith("13"))
print(date.endswith("12"))

# 5.3 in
print("Mar" in date)
print("Sep" in date)

# 5.4 Finding in Python
print(date.find("-"))

# Examples printing just Month and date by this method
print(date[date.find("-")+1:])


# 06-------------------Validation in Python -----------------------

# 6.1 isalpha() check the wether its string or not
country = "Pakistan"
print(country.isalpha())

country = "Pakistan001"
print(country.isalpha())

# 6.2 isnumeric() check the wether its numeric or not

number = "001-Pakistan"
print(number.isnumeric())

number = "001"
print(number.isnumeric())


# ------------STRINGS METHODS ARE COMPLETED------------
