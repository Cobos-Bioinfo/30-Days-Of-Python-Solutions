# Day 3 - 30DaysOfPython Challenge
# Operators

# 1 - Declare your age as integer variable.
age = int(150) # TMI
# 2 - Declare your height as a float variable.
height = float(200) # TMI
# 3 - Declare a variable that stores a complex number.
complex_num = complex(3 + 5j)

# 4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle.
area_triangle = int(
    0.5 * 
    int(input("Enter base: ")) * 
    int(input("Enter height: "))
)
print("The area of the triangle is =", area_triangle)

# 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle.
perimeter_triangle = int(
    int(input("Enter side a: ")) + 
    int(input("Enter side b: ")) + 
    int(input("Enter side c: "))
)
print("The perimeter of the triangle is =", perimeter_triangle)

# 6 - Get length and width of a rectangle using prompt. Calculate its area and perimeter.
length, width = int(input("Enter length: ")), int(input("Enter width: "))
print("The area of the rectangle is =", length * width)
print("The perimeter of the rectangle =", 2 * (length + width))

# 7 - Get radius of a circle using prompt. Calculate the area and circumference.
radius = int(input("Enter radius: "))
print("The area of the circle =", 3.14 * radius**2)
print("The circumference of the circle =", 2 * 3.14 * radius)

# 8 - Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("Slope = 2")
print("x-intercept = 1")
print("y-intercept = -2")

# 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1, x2, y2 = 2, 2, 6, 10
print("Slope =", int((y2 - y1) / (x2 - x1))) # 2
print(f"Euclidean distance = {((x2-x1)**2 + (y2-y1)**2) ** 0.5:.2f}") # 8.94

# 10 - Compare the slopes in tasks 8 and 9.
print(2 == int((y2 - y1) / (x2 - x1))) # True

# 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-10, 11):
    y = x**2 + 6*x + 9
    if y == 0:
        print("Solution: y is 0 when x =", x)
        break # Solution: y is 0 when x = -3
else:
    print("No solution in tested range.")

# 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") != len("dragon")) # False

# 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon") # True

# 14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon.") # True

# 15 - There is no 'on' in both dragon and python
print("on" not in "python" and "on" not in "dragon") # False

# 16 - Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("python")))) # <class 'str'>

# 17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("Even" if int(input("Enter integer: ")) % 2 == 0 else "Odd")

# 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7)) # True

# 19 - Check if type of '10' is equal to type of 10
print(type('10') == type(10)) # False

# 20 - Check if int('9.8') is equal to 10
print(int(9.8) == 10) # False

# 21 - Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print(f"Your monthly earnings are: {float(input("Enter your weekly work hours: ")) * 
      4 * 
      float(input("Enter your hourly pay rate: "))}")

# 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
print(f"You have lived for {
    int(input("Enter number of years you have lived: ")) * 
    365 * 
    24 * 
    60 * 
    60} seconds")

# 23 - Write a Python script that displays the following table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)