# Day 19 - 30DaysOfPython Challenge
# File handling
import re
import json

# Level 1
# 1 - Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def count_lines_words(file_path: str) -> tuple[int, int]:
    with open(file_path, "r") as f:
        lines: list[str] = f.readlines()
        
        return len(lines), sum(len(line.split()) for line in lines)

# 2 - Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(file_path: str, n: int):
    with open(file_path, "r", encoding="utf-8") as f:
        countries = json.load(f)
    language_counts: dict[str, int] = {}
    all_languages = [lang for country in countries for lang in country["languages"]]

    for lang in all_languages:
        language_counts[lang] = language_counts.get(lang, 0) + 1

    return sorted([(count, lang) for lang, count in language_counts.items()], reverse=True)[:n]

# 3 - Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(file_path: str, n: int) -> list[dict[str, int|str]]:
    with open(file_path, "r", encoding="utf-8") as f:
        countries = json.load(f)

    population_list: list[dict[str, int|str]] = [
        {"country": country["name"], "population": country["population"]}
        for country in countries
    ]

    return sorted(population_list, key=lambda x: x["population"], reverse=True)[:n]

# Level 2
# 4 - Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def get_email(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        raw_txt: str = f.read()

    # [\w\.-]+  => letters, numbers, _ , . or - ; ("+" one or more chars)
    # \.        => literal dot before the domain ending
    # \w+       => domain ending (e.g., com, org, edu)
    all_emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", raw_txt)
    return all_emails

# 5 - Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(file_path: str, n: int) -> list[tuple]:
    with open(file_path, "r") as f:
        raw_text:str = f.read().lower()
    
    all_words = re.findall(r"\b[a-z]+\b", raw_text)
    
    word_count: dict[str, int] = {}
    for word in all_words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return sorted([(count, word) for word, count in word_count.items()], reverse=True)[:n]

# This was my original approach. However, when refactoring my code, I came across this much better and elegant approach using set():
def find_most_common_wordsV2(file_path: str, n: int) -> list[tuple]:
    with open(file_path, "r") as f:
        raw_text:str = f.read().lower()
    
    all_words = re.findall(r"\b[a-z]+\b", raw_text)
    
    word_count = {word: all_words.count(word) for word in set(all_words)}
    
    return sorted([(count, word) for word, count in word_count.items()], reverse=True)[:n]

# 6 - Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
print(
    f"Obama's speech 10 most frequent words:\n{find_most_common_wordsV2("./data/obama_speech.txt", 10)}\n"
    f"Michelle's speech 10 most frequent words:\n{find_most_common_wordsV2("./data/michelle_obama_speech.txt", 10)}\n"
    f"Trump's speech 10 most frequent words:\n{find_most_common_wordsV2("./data/donald_speech.txt", 10)}\n"
    f"Melina's speech 10 most frequent words:\n{find_most_common_wordsV2("./data/melina_trump_speech.txt", 10)}")

# 7 - Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
