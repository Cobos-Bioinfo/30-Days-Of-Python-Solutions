# Day 14 - 30DaysOfPython Challenge
# Higher order functions
import sys
sys.path.append("data")
from functools import reduce

countries: list[str] = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countriesV2: list[str] = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', "Chile"] # added a 5 letter country (Chile) to test Level 2.6
names: list[str] = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Level 1
# 1 - Explain the difference between map, filter, and reduce.
"""
map() transforms each element from an iterable, returns iterable
filter() selects elements based on a condition (bool), returns iterable
reduce() combines elements into a single value, returns val
 """
 
# 2 - Explain the difference between higher order function, closure and decorator
"""
higher_order_func() takes or returns a function
closure() nested function remembers vars from outer scope even after outer exits
decorator() wraps a function to modify/extend its behavior without changing its code
"""

# 3 - Define a call function before map, filter or reduce, see examples.
# map
def sqrt(num: int) -> int:
    return num**0.5
print(f"Square root of each int in numbers: {list(map(sqrt, numbers))}")

# filter
def long_names(name: str) -> bool:
    if len(name) > 6:
        return True
    else:
        return False
print(f"Names longer that 6 letters: {list(filter(long_names, names))}")

# reduce
def mult_pairs(a: int, b: int) -> int:
    return a * b
print(f"Sequentially multiplied pairs from list = {reduce(mult_pairs, numbers)}")

# 4 - Use for loop to print each country in the countries list.
for i in countries:
    print(i)

# 5 - Use for to print each name in the names list.
for i in names:
    print(i)

# 6 - Use for to print each number in the numbers list.
for i in numbers:
    print(i)

# Level 2
# 1 - Use map to create a new list by changing each country to uppercase in the countries list
print(list(map(lambda x: x.upper(), countries)))

# 2 - Use map to create a new list by changing each number to its square in the numbers list
print(list(map(lambda x: x**2, numbers)))

# 3 - Use map to change each name to uppercase in the names list
print(list(map(lambda x: x.upper(), names)))

# 4 - Use filter to filter out countries containing 'land'.
print(list(filter(lambda x: "land" not in x, countries)))

# 5 - Use filter to filter out countries having exactly six characters.
print(list(filter(lambda x: len(x) != 6, countries)))

# 6 - Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(lambda x: len(x) < 6, countriesV2)))

# 7 - Use filter to filter out countries starting with an 'E'
print(list(filter(lambda x: x[0] != "E", countries)))

# 8 - Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print(list(map(lambda x: x.upper(), list(filter(lambda x: "land" not in x, countries)))))
# Outputs CAPITALIZED countries filtered to be only "land-less"
# Iterator for map == list output from filter!

# 9 - Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst: list) -> list[str]:
    return list(map(lambda x: str(x), lst))

# 10 - Use reduce to sum all the numbers in the numbers list.
print(reduce(lambda a, b: a+b, numbers))

# 11 - Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print(reduce(lambda acc_countries, next_country: f"{acc_countries}, {next_country}" if next_country != countries[-1] else f"{acc_countries}, and {next_country} are north European countries", countries))
"""
How this reduce() works:
1. Starts with first country (Estonia) as initial accumulator
2. For each next country:
   - If NOT last: adds ", Country" (e.g., ", Finland")
   - If last: adds ", and Country are north European countries"
3. Final output builds the complete sentence
"""

# 12 - Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import countries as cnt

def get_multiWord_countries(country_list: list[str]) -> list[str]:
    return list(filter(lambda x: " " in x or "-" in x, country_list))
# Wanted to practice list comprehension (Day_13):
def get_multiWord_countriesV2(country_list: list[str]) -> list[str]:
    return [country for country in country_list if " " in country or "-" in country]

# 13 - Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def get_country_letter_N(country_list: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    list(map(lambda country: result.update({country[0]: result.get(country[0], 0) + 1}), country_list))
    return result

# 14 - Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(country_list: list[str]) -> list[str]:
    return country_list[:10]

# 15 - Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(country_list: list[str]) -> list[str]:
    return country_list[-10:]

# Level 3
# 1 - Use the countries_data.py file and follow the tasks below:
from countries_data import countries_data as c_data

    # - Sort countries by name, by capital, by population
def sort_name(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["name"])

def sort_capital(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["capital"])

def sort_population(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["population"], reverse = True)

    # - Sort out the ten most spoken languages by location.
def sort_10languages(country_dict: list[dict]) -> list[str]:
    lang_counts: dict = {}
    for country in country_dict:
        for language in country.get("languages", []):
            lang_counts[language] = lang_counts.get(language, 0) + 1 # Count language occurrences

    return [lang for lang, n in sorted(lang_counts.items(), key = lambda item: item[1], reverse = True)][:10]
    # lang_counts.items() gives tuple (language, count) pairs
    # sorted() orders these by count (item[1]) (n) descending
    # [lang for lang, n in...] tuple-unpacks just the language names from the tuple pairs (lang, n); n is not used (by convention should be _), but n helps me visualize it as the count of the language

    # - Sort out the ten most populated countries.
def sort_population10(countries: list[dict]) -> list[dict]:
    return sorted(countries, key=lambda x: x["population"], reverse = True)[:10]