# Day 6 - 30DaysOfPython Challenge
# Tuples

# Level 1
# 1 - Create an empty tuple
tpl = ()

# 2 - Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Mike", "John")
sisters = ("Maria", "Marta", "Mireia")

# 3 - Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4 - How many siblings do you have?
print(f"You have {len(siblings)} siblings")

# 5 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.extend(["Bob", "Maria"])
family_members = tuple(siblings)

# Level 2
# 1 - Unpack siblings and parents from family_members
*siblings, p1, p2 = family_members # Option A
parents = [p1, p2]

siblings, parents = family_members[:-2], family_members[-2:] # Option B

# 2 - Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("tomato", "apple", "strawberry")
vegetables = ("zucchini", "cucumber")
animal_prod = ("milk", "eggs", "butter")
food_stuff_tp = fruits + vegetables + animal_prod

# 3 - Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_tp) % 2 == 0:
    print(f"Even, {food_stuff_tp[len(food_stuff_tp)//2 - 1]} and {food_stuff_tp[len(food_stuff_tp)//2]} sliced")
else:
    print(f"Odd, {food_stuff_tp[len(food_stuff_tp)//2]} sliced")

# 5 - Slice out the first three items and the last three items from food_staff_lt list
print(f"First 3: {food_stuff_lt[:3]}\n" 
      f"Last 3: {food_stuff_lt[-3:]}"
)

# 6 - Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7 - Check if an item exists in tuple:
    # Check if 'Estonia' is a nordic country
    # Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Is Estonia a nordic country? {"Estonia" in nordic_countries}\n"
      f"Is Iceland a nordic country? {"Iceland" in nordic_countries}"
)