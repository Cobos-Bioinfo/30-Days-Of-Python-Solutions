# Day 12 - 30DaysOfPython Challenge
# Modules
# Note: I recently learned about type annotations and will be implementing them from now on (or at least trying)

# Level 1
# 1 - Write a function which generates a six digit/character random_user_id.
import string, random

def random_user_id() -> str:
    chars: str = string.ascii_letters + string.digits
    user_id: str = "".join(random.choices(chars, k = 6))
    
    return user_id

# 2 - Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user() -> list[str]:
    n_chars: int = int(input("How many characters per ID? "))
    n_ids: int = int(input("How many IDs to generate? "))
    users_id: list[str] = []
    chars: str = string.ascii_letters + string.digits
    for _ in range(n_ids):
        users_id.append("".join(random.choices(chars, k = n_chars)))
        
    return users_id

# 3 - Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen() -> str:
    r, g, b = random.choices(range(256), k = 3)
    return f"rgb({r},{g},{b})"

# Level 2
# 1 - Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n_colors: int) -> list[str]:
    lst_hexa_colors: list[str] = []
    chars: str = string.hexdigits[:16] # 0123456789abcdef| ABCDEF
    for _ in range(n_colors):
        hex_color: str = "#" + "".join(random.choices(chars, k = 6))
        lst_hexa_colors.append(hex_color)
        
    return lst_hexa_colors

# 2 - Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n_rgb: int) -> list[str]:
    lst_rgb_colors: list[str] = []
    for _ in range(n_rgb):
        r, g, b = random.choices(range(256), k = 3)
        rgb_color: str = f"rgb({r}, {g}, {b})"
        lst_rgb_colors.append(rgb_color)
    
    return lst_rgb_colors

# 3 - Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(_type: str, n_colors: int) -> list[str] | str:
    if _type == "hexa":
        return list_of_hexa_colors(n_colors)
    elif _type == "rgb":
        return list_of_rgb_colors(n_colors)
    else:
        return f"ERROR: {_type = } must be \"hexa\" or \"rgb\"" # Really cool f-string trick I learned from Indentyl's video on F-Strings: https://youtu.be/EoNOWVYKyo0?si=kqsLmFSFTQQUlJks

# Tried to implement error handling
def generate_colorsV2(_type: str, n_colors: int) -> list[str] | str:
    if _type not in ("hexa", "rgb") or type(n_colors) != int:
        return f"ERROR: {_type = } must be \"hexa\" or \"rgb\"\n AND/OR {n_colors = } --> {type(n_colors)} must be an integer"
    if _type == "hexa":
        return list_of_hexa_colors(n_colors)
    return list_of_rgb_colors(n_colors) # No else needed because all invalid cases are caught first, leaving only valid options

# Level 3
# 1 - Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst: list) -> list:
    shuffled_lst = lst.copy()
    random.shuffle(shuffled_lst)
    
    return shuffled_lst

# 2 - Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_array_7() -> set[int]:
    a: set = set()
    while len(a) < 7:
        a.add(random.randint(0, 9))
    
    return a

# Was happy with my first approach but wanted to explore further the random module:
def random_array_V2() -> list[int]:
    return random.sample(range(10), 7)