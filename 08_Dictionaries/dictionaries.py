# Day 8 - 30DaysOfPython Challenge
# Dictionaries


# 1 - Create an empty dictionary called dog
dog = {}

# 2 - Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Cuqui"
dog["color"] = "Brown"
dog["breed"] = "Beagle"
dog["legs"] = "Short"
dog["age"] = 13

# 3 - Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Maria",
    "last_name": "Carey",
    "gender": "Female",
    "age": 50,
    "marital_status": "TMI",
    "skills": ["singing", "dancing", "acting", "performing"],
    "country": "USA",
    "adress": "IDK"
}

# 4 - Get the length of the student dictionary
print(len(student))

# 5 - Get the value of skills and check the data type, it should be a list
print(f"Skills: {student.get("skills")} data type: {type(student.get("skills"))}")


# 6 - Modify the skills values by adding one or two skills
student["skills"].append("welcoming Christmas")

# 7 - Get the dictionary keys as a list
print(list(student.keys()))

# 8 - Get the dictionary values as a list
print(list(student.values()))

# 9 - Change the dictionary to a list of tuples using items() method
print(list(student.items()))


# 10 - Delete one of the items in the dictionary
del student["marital_status"] # Option A
student.pop("age") # Option B

# 11 - Delete one of the dictionaries
del dog