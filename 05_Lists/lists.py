# Day 5 - 30DaysOfPython Challenge
# Lists

# Level 1
# 1 - Declare an empty list
lst = []

# 2 - Declare a list with more than 5 items
lst = [1, 2, 3, 4, 5, 6]

# 3 - Find the length of your list
print(len(lst))

# 4 - Get the first item, the middle item and the last item of the list
print(
    f"First item: {lst[0]}\n"
    f"Last item: {lst[-1]}\n"
    f"Middle item: {lst[len(lst)//2]}"
)

# 5 - Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Cobos", 150, 200, "TMI", "Way TMI"]

# 6 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7 - Print the list using print()
print(it_companies)

# 8 - Print the number of companies in the list
print(len(it_companies))

# 9 - Print the first, middle and last company
print(
    f"First company: {it_companies[0]}\n"
    f"Middle company: {it_companies[len(it_companies)//2]}\n"
    f"Last company: {it_companies[-1]}"
)

# 10 - Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

# 11 - Add an IT company to it_companies
it_companies.append("NVIDIA")
print(it_companies)

# 12 - Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, "MiddleCompany")
print(it_companies)

# 13 - Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper() # Lists are modifiable BUT strings are immutable, we need to REASIGN to modify a string inside a list!
print(it_companies)

# 14 - Join the it_companies with a string '#;  '
print(", ".join(it_companies))

# 15 - Check if a certain company exists in the it_companies list.
print("IBM" in it_companies)

# 16 - Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 - Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18 - Slice out the first 3 companies from the list
print(it_companies[:3]) # Prints only 3 first
print(it_companies[3:]) # Prints all but 3 first

# 19 - Slice out the last 3 companies from the list
print(it_companies[len(it_companies)-3:]) # Prints only 3 last
print(it_companies[:-3]) # Prints all but 3 last

# 20 - Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2]) # Prints middle company
print(it_companies[:len(it_companies)//2] + it_companies[len(it_companies) // 2 + 1:]) # Prints all but middle company

# 21 - Remove the first IT company from the list
it_companies.pop(0)

# 22 - Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)

# 23 - Remove the last IT company from the list
it_companies.pop()

# 24 - Remove all IT companies from the list
it_companies.clear()

# 25 - Destroy the IT companies list
del it_companies

# 26 - Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_and_back_end = front_end + back_end # Method A
front_end.extend(back_end) # Method B

# 27 - After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_and_back_end.copy()
full_stack[full_stack.index("Redux")+1 : full_stack.index("Redux")+1] = ["Python", "SQL"] 
print(full_stack)

# Level 2
# 1 - The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age, max_age = ages[0], ages[-1]

# Add the min age and the max age again to the list
ages.extend([min_age, max_age])

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
if len(ages) % 2 == 0:
    print(f"Even, therefore median = {int((ages[len(ages)//2] + ages[len(ages)//2 - 1])/2)}")
else:
    print(f"Odd, therefore median = {ages[len(ages)//2]}")
    
# Find the average age (sum of all items divided by their number )
avg_age = sum(ages)/len(ages)
print(f"Average age: {avg_age}")

# Find the range of the ages (max minus min)
print(f"Range = {ages[-1] - ages[0]}")

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_age - avg_age) == abs(max_age - avg_age))

# Should have cloned the repo...
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'    
]

# Find the middle country(ies) in the countries list
if len(countries) % 2 == 0:
    print(f"Even, therefore 2 middle countries: {countries[len(countries)//2 - 1]}, {countries[len(countries)//2]}")
else:
    print(f"Odd, therefore 1 middle country: {countries[len(countries)//2]}")

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
    print("Even")
    countries1 = countries[:len(countries)//2]
    countries2 = countries[len(countries)//2:]
else:
    print("Odd")
    countries1 = countries[:len(countries)//2 + 1]
    countries2 = countries[len(countries)//2 + 1:]
print(f"n in Countries1: {len(countries1)}\nn in Countries2: {len(countries2)}")

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
mini_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = mini_countries