# Day 19 - 30DaysOfPython Challenge
# File handling

# Level 1
# 1 - Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def count_lines_words(file_path: str) -> tuple[int, int]:
    with open(file_path, "r") as f:
        lines: list[str] = f.readlines()
        
        return len(lines), sum(len(line.split()) for line in lines)

# 2 - Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

def most_spoken_languages(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        countries = json.load(f)
    language_counts: dict[str, int] = {}
    all_languages = [lang for country in countries for lang in country["languages"]]

    for lang in all_languages:
        language_counts[lang] = language_counts.get(lang, 0) + 1

    top_10 = sorted([(count, lang) for lang, count in language_counts.items()], reverse=True)
    return top_10[:10]

# 3 - Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        countries = json.load(f)
    population_counts: dict[str, int] = {}
    all_populations = [population for country in countries for population in country["population"]]

    for population in all_populations:
        population_counts[population] = population_counts.get(population, 0) + 1

    top_10 = sorted([(count, population) for population, count in population_counts.items()], reverse=True)
    return top_10[:10]
most_populated_countries("./data/countries_data.json")