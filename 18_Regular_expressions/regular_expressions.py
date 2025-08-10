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