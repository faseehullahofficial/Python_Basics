# Python Excercise
# Convert the messy Phone number into a clean format with only digits


phone = "+49 (176) 123-4567"
print(phone.replace("+", "00").replace("(", "").replace(")",
      "").replace("-", "").replace(" ", ""))
