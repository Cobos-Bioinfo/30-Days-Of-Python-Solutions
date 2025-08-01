# Day 7 - 30DaysOfPython Challenge
# Sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Level 1
# 1 - Find the length of the set it_companies
print(len(it_companies))

# 2 - Add 'Twitter' to it_companies
it_companies.add("Twitter")

# 3 - Insert multiple IT companies at once to the set it_companies
it_companies.update(["Meta", "NVIDIA"])

# 4 - Remove one of the companies from the set it_companies
it_companies.pop()

# 5 - What is the difference between remove and discard
"""
remove() --> If the element is not a member, raise a KeyError.
discard() --> Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
"""

# Level 2
# 1 - Join A and B
A.update(B)


# 2 - Find A intersection B
print(A.intersection(B))

# 3 - Is A subset of B
print(A.issubset(B)) # True

# 4 - Are A and B disjoint sets
print(A.isdisjoint(B)) # False

# 5 - Join A with B and B with A
A.update(B) # creates new set
B.update(A) # modifies B in-place

# 6 - What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 7 - Delete the sets completely
del A, B, it_companies

# Level 3
# 1 - Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(f"Age set bigger than age list: {len(age_st) > len(age)}")

# 2 - Explain the difference between the following data types: string, list, tuple and set
""" 
String: Immutable text. 
List: Mutable ordered collection. 
Tuple: Immutable ordered collection. 
Set: Mutable unordered unique elements.
 """

# 3 - I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
print(f"Unique words: {len(set(sentence.split()))}")