# Day 11 - 30DaysOfPython Challenge
# Functions

# Level 1
# 1 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a+b


# 2 - Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14*r**2

# 3 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    for i in nums:
        if type(i) != int and type(i) != float:
            return f"ERROR: All arguments must be numbers! {i}: {type(i)}"
    return sum(nums) 

# 4 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_C_to_F(c):
    return f"{c}ºC = {(c * 9/5) + 32}ºF"


# 5 - Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
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
    if type(month) != str or month.capitalize() not in seasons:
        return f"Argument must be a month: {month} ({type(month)}"
    else:
        return seasons.get(month.capitalize())

# 6 - Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    if x1 == x2:
        return f"ERROR: x1 ({x1}) = x2 ({x2}), division by zero!"
    else:
        return f"Slope: {(y2 - y1)/(x2 - x1)}"

# 7 - Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# x = (-b ± √(b² - 4ac)) / 2a
def solve_quadratic_eqn(a, b, c):
    discriminant = (b**2 - 4*a*c)**0.5
    x1 = (-b + discriminant) / (2*a)
    x2 = (-b - discriminant) / (2*a)
    return (x1, x2)

# 8 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)

# 9 - Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    r_array = []
    for _ in range(len(array)):
        r_array.append(array.pop())
    return r_array

# 10 - Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    cap_lst = []
    for i in lst:
        cap_lst.append(i.capitalize())
    return cap_lst

# 11 - Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst_added = lst.copy()
    lst_added.append(item)
    return lst_added

# 12 - Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    lst_removed = lst.copy()
    lst_removed.remove(item)
    return lst_removed

# 13 - Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    return n * (n + 1) // 2 # Using Gauss's Sum formula! (way more optimal than using a for loop)

# 14 - Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    return sum(num for num in range(n + 1) if num % 2 != 0)
# Super performant method (AI-assistance I did not know this mathematical property!)
def sum_of_odds(n):
    k = (n + 1) // 2  # Count of odd numbers
    return k**2       # Sum of the first k odd numbers is always k²(e.g., 1+3=4=2², 1+3+5=9=3²)

# 15 - Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(n):
    return sum(num for num in range(n + 1) if num % 2 == 0)
# Super performant method
def sum_of_even(n):
    k = n // 2
    return k * (k + 1)  # Sum = 2(1 + 2 + ... + k) = k(k+1)

# Level 2
# 1 - Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def even_and_odds(n):
    even, odds = 0, 0
    for i in range(n+1):
        if i % 2 == 0:
            even += 1
        else:
            odds += 1
    return f"N of evens: {even}\nN of odds: {odds}"
# Super performant method (combining both previous)
def evens_and_odds(n): # Every pair of numbers has 1 even and 1 odd. The last number (n) marks if there’s an "extra" even.
    if n % 2 == 0:
        even = n // 2 + 1
        odds = n // 2
    else:
        even = odds = (n + 1) // 2
    return f"Number of evens: {even}.\nN of odds: {odds}."

# 2 - Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    fac = 1
    for num in range(2, n+1):
        fac *= num
    return fac

# 3 - Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(item):
    return not item

# 4 - Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 != 0: # Odd-len(list)
        return sorted_lst[mid]
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2

def calculate_mode(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1 # k=arg in list v=0+1 if empty or val+1 if v already in freq{}
    max_count = max(freq.values())
    modes = []
    for k, v in freq.items():
        if v == max_count:
            modes.append(k)
    return modes[0] if len(modes) == 1 else modes

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    total = 0
    for x in lst:
        total += (x - mean) ** 2
    return total / len(lst)

def calculate_std(lst):
    return calculate_variance(lst) ** 0.5

# Level 3
# 1 - Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if type(n) != int or n <= 1:
        return f"{False} - A prime number is defined as a natural number greater than 1. Your number: {n} ({type(n)})"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return f"{False} - For any number n > 1, if there is no whole number i (where 2 ≤ i ≤ √n) such that n ÷ i has no remainder, then n is a prime number."
        else:
            return f"{True} - {n} is prime"

# 2 - Write a functions which checks if all items are unique in the list.
def is_uniq(lst):
    return len(lst) == len(set(lst))


# 3 - Write a function which checks if all the items of the list are of the same data type.
def is_type(lst):
    _type = set()
    for i in lst:
        _type.add(type(i))
    if len(_type) == 1:
        return f"{True} - All items in the list are of the same data type ({type(lst[0])})"
    else:
        return f"{False} - There are {len(_type)} different data types in the list ({_type})"

# Another, more optimal approach that avoids checking all items in lst
def is_type(lst):
    _type = type(lst[0])
    for i in lst:
        if type(i) != _type:
            return f"{False} - Mixed types found (first is {_type}, found {type(i)})"
    return f"{True} - All items are {_type}"
 
# 4 - Write a function which check if provided variable is a valid python variable
# note: I don't think you can check the name of the var itself. Best I can do is if the arg provided could be a valid var name.
def is_valid(name):
    ans = f"{False} - \"{name}\" is not a valid python variable name"
    if type(name) != str:
        return ans
    if not name:
        return ans
    if name[0].isdigit():
        return ans
    for char in name:
        if not (char.isalnum() or char == '_'):
            return ans
    reserved_words = [ # generated list with AI-assistance
        'False', 'None', 'True', 'and', 'as', 'assert', 'break', 
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
        'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
        'return', 'try', 'while', 'with', 'yield', 'str', 'int', 
        'list', 'dict', 'tuple', 'set'
    ]
    if name in reserved_words:
        return ans
    
    return f"{True} - \"{name}\" is a valid python variable name!"
    
# 5 - Go to the data folder and access the countries-data.py file.
import sys
sys.path.append("data")
from countries_data import countries_data as c_data

    # - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(lst):
    language_count = dict()
    for country in lst:
        for language in country["languages"]:
            language_count[language] = language_count.get(language, 0) + 1  # if no language: for loop skips
                    # if language.count[language] is empty (new language) set it to 0 and add 1
                    # if language.count[language] has value, add 1
    
    sorted_languages = sorted(language_count.items(), key=lambda item: item[1], reverse=True)
    top_langs = list()
    for item in sorted_languages[:20]:
        top_langs.append(item)
    
    return f"These are the 20 most spoken languages:\n{top_langs}"

    # - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(lst):
    pop_count = dict()
    for country in lst:
       pop_count[country["name"]] = country["population"] # k for pop_count = v of country["name"] v for pop_count = v for country["population"]
    sorted_pops = sorted(pop_count.items(), key=lambda item: item[1], reverse=True) # reminder: this lambda func is used as key to sort. input=item=(country, population) pairs (as tuple) and output=item[1]=population=int
    top_pops = list()
    for item in sorted_pops[:20]:
        top_pops.append(item)
        
    return f"These are the 20 most populated countries:\n{top_pops}"
