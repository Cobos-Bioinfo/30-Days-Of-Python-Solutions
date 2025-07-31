# Day 4 - 30DaysOfPython Challenge
# Strings

# 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a, b, c, d = "Thirty", "Days", "Of", "Python"
print(f"{a} {b} {c} {d}")

# 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a, b, c = "Coding", "For", "All"
print(f"{a} {b} {c}")

# 3 - Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4 - Print the variable company using print().
print(company)

# 5 - Print the length of the company string using len() method and print().
print(len(company))

# 6 - Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 - Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(f"{company.capitalize()}\n"
      f"{company.title()}\n"
      f"{company.swapcase()}")

# 9 - Cut(slice) out the first word of Coding For All string.
print(company[7::])
print(company.split(" ", 1)[1]) # Avoids having to manually count index

# 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(f"{company.index("Coding")}\n"
      f"{company.find("Coding")}\n"
      f"{"Coding" in company}")

# 11 - Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# 12 - Change Python for Everyone to Python for All using the replace method or other methods.
print("Python For Everyone".replace("Everyone", "All"))

# 13 - Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# 14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# 15 - What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 - What is the last index of the string Coding For All.
print(len(company) - 1) # 13

# 17 - What character is at index 10 in "Coding For All" string.
print(company[10]) # space

# 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone".split()
print(f"{name[0][0]}{name[1][0]}{name[2][0]}")

# 19 - Create an acronym or an abbreviation for the name 'Coding For All'.
print(f"{company.split()[0][0]}"
      f"{company.split()[1][0]}"
      f"{company.split()[2][0]}")

# 20 - Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# 21 - Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind("l"))

# 23 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because")) # 31

# 24 - Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because")) # 47

# 25 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:47+len("because")+1])
print(sentence.replace("because because because ",""))

# 26 - Duplicate of 23
# 27 - Duplicate of 25

# 28 - Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# 29 - Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

# 30 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# 31 - Which one of the following variables return True when we use the method isidentifier(): 
print(f"{"30DaysOfPython".isidentifier()}\n" # False
      f"{"thirty_days_of_python".isidentifier()}") # True

# 32 - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(lib_list))

# 33 - Use the new line escape sequence to separate the following sentences.
print(f"I am enjoying this challenge\nI just wonder what is next")

# 34 - Use a tab escape sequence to write the following lines.
print(f"Name\tAge\tCountry\tCity\n"
      f"Asabeneh\t250\tFinland\tHelsinki")

# 35 - Use the string formatting method to display the following:
print(f"radius = 10\n"
      f"area = 3.14 * radius ** 2\n"
      f"The area of a circle with radius 10 is 314 meters square.")

# 36 - Make the following using string formatting methods:
print(f"8 + 6 = {8 + 6}\n"
      f"8 - 6 = {8 - 6}\n"
      f"8 * 6 = {8 * 6}\n"
      f"8 / 6 = {8 / 6:.2f}\n"
      f"8 % 6 = {8 % 6}\n"
      f"8 // 6 = {8 // 6}\n"
      f"8 ** 6 = {8 ** 6}\n")