# Day 13 - 30DaysOfPython Challenge
# List comprehension

# 1 - Filter only negative and zero in the list using list comprehension
def filter_list(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num > 0]

# 2 - Flatten the following list of lists of lists to a one dimensional list:
"""
3-level nested list: We have to unpack twice to access num
list_lists[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
sub1[0] = [[1, 2, 3]]
sub2[0] = [1, 2, 3]
"""
def flaten_3nested_list(list_lists: list[list[list]]) -> list[int]:
    return [num for sub1 in list_lists for sub2 in sub1 for num in sub2]

# 3 - Using list comprehension create the following list of tuples:
# list_of_tuples: list[tuple] = [(n, 1, )]
list_of_tuples = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
# I knew there had to be a better alternative so I used tuple unpacking (Day_06) to unpack the generator (i**n for n in range(1,6)) directly into the tuple!
def generate_list_of_tuples() -> list[tuple]:
    return [(i, 1, *(i**n for n in range(1,6))) for i in range(11)]

# 4 - Flatten the following list to a new list:
"""
Now we only have to flatten twice (since we want to maintain the pairs)
list_list_tuple = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list1[0] = [('Finland', 'Helsinki')]
_tuple = ('Finland', 'Helsinki')
_tuple[0] = 'Finland'
"""
def flatten_2list1tuple(list_list_tuple: list[list[tuple]]) -> list[list[str]]:
    return [[_tuple[0].upper(), _tuple[0].upper()[:3], _tuple[1].upper()] for list1 in list_list_tuple for _tuple in list1]

# 5 - Change the following list to a list of dictionaries:
"""
list_list_tuple = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list1[0] = [('Finland', 'Helsinki')]
_tuple = ('Finland', 'Helsinki')
_tuple[0] = 'Finland'
We define the dict inside the list --> return [{}]
Inside the dict we assign k: v where k is simply the desired string and v is the corresponding _tuple[index]
"""
def list_to_listDicts(list_list_tuple: list[list[tuple]]) -> list[dict]:
    return [{"country":_tuple[0].upper(), "city":_tuple[1].upper()} for list1 in list_list_tuple for _tuple in list1]

# 6 - Change the following list of lists to a list of concatenated strings:
# list_list_tuple = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
def list_to_listStrings(list_list_tuple: list[list[tuple]]) -> list[str]:
    return [f"{_tuple[0]} {_tuple[1]}" for list1 in list_list_tuple for _tuple in list1]

# 7 - Write a lambda function which can solve a slope or y-intercept of linear functions.
lamb_slope = lambda x1, x2, y1, y2: (y2 - y1)/(x2 - x1)
lamb_yIntercept = lambda x1, y1, x2, y2: y1 - lamb_slope(x1, x2, y1, y2) * x1