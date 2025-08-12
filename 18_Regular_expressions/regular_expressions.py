# Day 18 - 30DaysOfPython Challenge
# Regular expressions

import re
# Level 1
# 1 - What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
def most_frequent_word(txt: str) -> list[tuple[int, str]]:
    all_words = re.findall(r"\b\w+\b", txt, re.I) # \b
    
    word_count: dict[str, int] = {}
    for word in all_words:
        word_count[word] = word_count.get(word, 0) + 1
    
    count_word_pairs: list[tuple[int, str]] = sorted([(count, word) for word, count in word_count.items()], reverse=True)
    
    return count_word_pairs

# 2 - The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
def get_max_particle_distance(text: str) -> int:
    numbers = re.findall(r"-?\d+", text) # Optional minus sign (-?); followed by one or more digits (\d+)
    all_points: list[int] = [int(num) for num in numbers]
    return max(all_points) - min(all_points)

# Level 2
# 1 - Write a pattern which identifies if a string is a valid python variable
def is_valid_python_variable(var: str) -> bool:
    PYTHON_KEYWORDS = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
        'try', 'while', 'with', 'yield'
    }
    if not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", var): 
        return False
    
    return var not in PYTHON_KEYWORDS

# Level 3
# 1 - Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt: str) -> str:
    return re.sub(r"[^a-zA-Z\s]", "", txt) # when "^" inside [] means "match anything NOT these charracters; "\s" = any whitespace character

def most_frequent_words(clean_txt: str) -> list[tuple[int, str]]:
    words_count = {}
    words = re.findall(r"\b\w+\b", clean_txt.lower())
    
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    
    return sorted([(count, word) for word, count in words_count.items()], reverse=True)[:3]