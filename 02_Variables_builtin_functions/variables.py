# Day 2 - 30DaysOfPython Challenge
# Variables & Builtin functions

# Level 1
first_name = "xGUAPI"
last_name = "x"
full_name = first_name + last_name
country = "Spain"
city = "Barcelona"
age = 22
year = 2025
is_married = False
is_true = True
is_light_on = False
gender, language = "Male", "English"

# Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(gender))
print(type(language))

print(len(first_name))

print(len(first_name) > len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = int(input("Insert radius of the circle (must be an integer): ")) # 30
circum_of_circle = 3.14 * 2 * radius
area_of_circle = 3.14 * radius**2
print("The circumference of the circle of radius:", radius, "=", 
      circum_of_circle, "\nThe area of the circle of radius:", 
      radius, "=", area_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your Country of origin: ")
age = int(input("Enter your age (must be an integer): "))

help('keywords')