def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b

# Took the funcs from Day 11 and added them here to use at Day 20-2
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