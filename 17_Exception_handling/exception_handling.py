# Day 17 - 30DaysOfPython Challenge
# Exception handling
""" 
IMPORTANT: Today's exercise was very limited and didn't challenge us to apply most of the key concepts from Day 17. To better reinforce these concepts, I asked an AI assistant to generate additional practice exercises.
"""

# 1 - Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names: list[str] = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(f"Nordic countries: {nordic_countries}\n"
      f"{es}\n{ru}")

# ----- EXTRA ----- #
# 2 - Write a function called safe_get_country(index) that takes an index as input. The function should return the country at the given index from the names list. It should handle potential errors by returning "Index out of range" if an IndexError occurs (when the index is beyond the list length) and "Invalid index type" if a TypeError occurs (when the index is not an integer). Regardless of whether an error occurs or not, the function should always print "Operation completed" in the finally block.
def safe_get_country(index: int) -> str:
    try:
        return names[index]
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Invalid index type"
    finally:
        print("Operation completed")
        
print(safe_get_country(4))

# 3 - Using the enumerate function, create a dictionary called country_ranks where the keys are ranking positions starting at 1, and the values are the corresponding country names from the names list. The enumeration should assign each country a sequential rank number beginning with 1.
country_ranks: dict[int, str] = {rank: country for rank, country in enumerate(names, 1)}

# 4 - Use zip to combine names and codes = ["FI", "SE", "NO", "DK", "IS", "EE", "RU"] into country_code_pairs (a list of tuples).
codes: list[str] = ["FI", "SE", "NO", "DK", "IS", "EE", "RU"]
country_code_pairs: list[tuple] = list(zip(names, codes))

# 5 - Create a new list all_countries by spreading names between "USA" and "Japan"
all_countries: list[str] = ["USA", *names, "Japan"]