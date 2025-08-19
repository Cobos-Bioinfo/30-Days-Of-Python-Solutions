# Day 20 - 30DaysOfPython Challenge
# PIP: Preferred Installer Program
import requests
import string
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mypackage import arithmetic
from bs4 import BeautifulSoup



# 1 - Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# Note: URL was outdated so had to manually retrieve the working one as of 19/08/2025: 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
def read_and_return_common_words(url: str = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt', n: int = 10) -> list[tuple[str, int]]:
    text: str = requests.get(url).text

    # Gutenberg books are always contained in between these START-END statements
    start: int = text.find('*** START OF THE PROJECT GUTENBERG EBOOK ROMEO AND JULIET ***')
    end: int = text.find('*** END OF THE PROJECT GUTENBERG EBOOK ROMEO AND JULIET ***')
    text = text[start:end].lower()

    translator: dict = str.maketrans('', '', string.punctuation + string.digits) # maketrans(x, y, z) -> x: chars to replace (None); y: replace with (None); y: chars to delete (all chars from string.punctuation and string.digits)
    words: list[str] = text.translate(translator).split()

    word_count: dict[str, int] = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:n]

# 2 - Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find:
    # - i. the min, max, mean, median, standard deviation of cats' weight in metric units.
    # - ii. the min, max, mean, median, standard deviation of cats' lifespan in years.
    # - iii. Create a frequency table of country and breed of cats
def analyze_cat_data(url: str = 'https://api.thecatapi.com/v1/breeds') -> dict:
    cats: list[dict] = requests.get(url).json()

    # i.
    weights: list = []
    for cat in cats:
        metric_str: str = cat['weight']['metric'] # weight is also a dict with keys 'metric' and 'imperial'
        low, high = [float(weight_val.strip()) for weight_val in metric_str.split('-')] # weight values are separated by "-" so we save both values as low and high by using split("-") and then we strip() bc there are spaces (["3 ", " 5"])
        avg_weight: float = (low + high) / 2
        weights.append(avg_weight)

    weight_stats: dict[str, float] = {
        'min': min(weights),
        'max': max(weights),
        'mean': arithmetic.calculate_mean(weights),
        'median': arithmetic.calculate_median(weights),
        'std': arithmetic.calculate_std(weights)
    }

    # ii.
    lifespans: list[float] = []
    for cat in cats:
        life_str: str = cat['life_span']
        low, high = [float(life_val.strip()) for life_val in life_str.split('-')]
        avg_life: float = (low + high) / 2
        lifespans.append(avg_life)

    lifespan_stats: dict[str, float] = {
        'min': min(lifespans),
        'max': max(lifespans),
        'mean': arithmetic.calculate_mean(lifespans),
        'median': arithmetic.calculate_median(lifespans),
        'std': arithmetic.calculate_std(lifespans)
    }

    # iii.
    freq_table: dict[str, list[str]] = {}
    for cat in cats:
        country: str = cat.get('origin', 'Unknown')
        breed: str = cat['name']
        if country not in freq_table:
            freq_table[country] = []
        freq_table[country].append(breed)

    return {
        'weight': weight_stats,
        'lifespan': lifespan_stats,
        'frequency_table': freq_table
    }

# 3 - Read the countries API and find
    # i. the 10 largest countries
    # ii. the 10 most spoken languages
    # iii. the total number of languages in the countries API
"""
Countries API (https://restcountries.eu/rest/v2/all) "Not Found"
"""

# 4 - UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
"""
Provided link returns Error 404.
"""