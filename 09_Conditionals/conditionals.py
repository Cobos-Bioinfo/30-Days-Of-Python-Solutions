# Day 9 - 30DaysOfPython Challenge
# Conditionals

# Level 1
# 1 - Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))
print("You are old enough to learn to drive.") if age >= 18 else print(f"You must wait {18 - age} years to learn to drive.")

# 2 - Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
diff = int(22 - age)
if diff == 0:
    print("We are the same age!")
else:
    y = "year" if abs(diff) == 1 else "years"
    print(f"You are {abs(diff)} {y} {"younger" if diff > 0 else "older"} than me")
    
# 3 - Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a, b = float(input("Enter number a: ")), float(input("Enter number b: "))
if a == b:
    print(f"a ({a}) is equal to b ({b})")
else:
    adifb = "greater" if a > b else "smaller"
    print(f"a ({a}) is {adifb} than b ({b})")

# Level 2
# 1 - Write a code which gives grade to students according to theirs scores:
score = int(input("Enter score: "))
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# Note: Because I knew that using so many if statements was inefficient, I decided to use an AI LLM to optimize grade calculation through string indexing ("FDCBA") and floor division (score // 10 - 4).
grade = "FDCBA"[min(score // 10 - 4, 4)] if score >= 50 else "F"  
print(f"Score: {score} - Grade: {grade}")

# 2 - Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = str(input("Enter the month: ")).capitalize()
seasons = {
        "January": "Winter",
        "February": "Winter",
        "March": "Spring",
        "April": "Spring",
        "May": "Spring",
        "June": "Summer",
        "July": "Summer",
        "August": "Summer",
        "September": "Fall",
        "October": "Fall",
        "November": "Fall",
        "December": "Winter"
    }
print(f"Month: {month} - Season: {seasons.get(month)}")

# 3 - The following list contains some fruits. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = str(input("Enter a fruit: "))
fruits = ['banana', 'orange', 'mango', 'lemon']
print(f"{fruit} is already in the list!") if fruit in fruits else (fruits.append(fruit), print(f"Added {fruit} to the list: {fruits}"))

# Level 3
# note: In this section I tried to force myself to not use nested conditionals.
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1.1 - Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print(f"Middle skill: {person.get("skills")[len(person.get("skills"))//2]}" if "skills" in person else "Person has no skills!")

# 1.2 - Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print("Python" in person.get("skills", [])) # Empty list as default so in case of not being "skills", "Python" won't be in []
 
# 1.3 If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
skills = set(person.get("skills", []))
print(skills)
if skills == {"JavaScript", "React"}:
    print("Frontend developer")
elif skills == {"Node", "Python", "MongoDB"}:
    print("Backend developer")
elif {"React", "Node", "MongoDB"}.issubset(skills):
    print("Fullstack developer")
else:
    print("Unknown title")
 
# 1.4 - If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
print(f"{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married" if person["is_marred"] and person["country"] == "Finland" else f"{person["first_name"]} {person["last_name"]} either does not live in {person["country"]} or is not married.")