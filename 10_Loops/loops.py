# Day 10 - 30DaysOfPython Challenge
# Loops

# Level 1
# 1 - Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(f"For loop: {i}")

i = 0
while i < 11:
    print(f"While loop: {i}")
    i += 1

# 2 - Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(f"For loop: {i}")

i = 10
while i > -1:
    print(f"While loop: {i}")
    i -= 1

# 3 - Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1,8):
    print("#"*i)

# 4 - Use nested loops to create the following:
for _ in range(8):
    for _ in range(8):
        print("#", end=" ")
    print()
# note: there is no need for a nested loop for this:
for _ in range(8):
    print("# "*8)

# 5 - Print the following pattern:
for i in range(0,11):
    print(f"{i} x {i} = {i*i}")

# 6 - Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst: 
    print(i)

# 7 - Use for loop to iterate from 0 to 100 and print only even numbers
for n in range(0,101,2):
    print(n)

for n in range(101):
    if n % 2 == 0:
        print(n)

# 8 - Use for loop to iterate from 0 to 100 and print only odd numbers
for n in range(1,101,2):
    print(n)

for n in range(101):
    if n % 2 != 0:
        print(n)

# Level 2
# 1 - Use for loop to iterate from 0 to 100 and print the sum of all numbers.
i = 0
for n in range(101):
    i += n
print(f"The sum of all numbersis : {i}")

# 2 - Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
e, o = 0, 0
for n in range(101):
    if n % 2 == 0:
        e+=n
    else:
        o+=n
print(f"The sum of all evens is: {e}\nThe sum of all Odds is: {o}")

# Level 3

# 1 - Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import sys
sys.path.append("data")
from countries import countries

for i in countries:
    if "land" in i:
        print(i)

# 2 - This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
r_fruits = []
for _ in range(len(fruits)):
    r_fruits.append(fruits.pop())

# 3 - Go to the data folder and use the countries_data.py file.
from countries_data import countries_data as c_data

    # What are the total number of languages in the data
n_lang = 0
for i in c_data:
    n_lang += len(i["languages"])
print(n_lang)

    # Find the ten most spoken languages from the data
    # I used AI assistance for this one
# 1. Count languages
language_counts = {}
for country in c_data:
    for language in country["languages"]:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

# 2. Sort languages by count (descending)
sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
# Used this opportunity to learn about Lambda functions. In this case the lambda function takes one argument {item} (e.g., ("English", 91)) and returns {item[1]} (91).

# 3. Get top 10 & Print results
for language, count in sorted_languages[:10]:
    print(f"{language}: {count} countries")

    # Find the 10 most populated countries in the world
population_counts = {}
for country in c_data:
    population_counts[country["name"]] = country["population"]

sorted_pops = sorted(population_counts.items(), key=lambda item: item[1], reverse=True)

for k, v in sorted_pops[:10]:
    print(f"{k}: {v} inhabitants")