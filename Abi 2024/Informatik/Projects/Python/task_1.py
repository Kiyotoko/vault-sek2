from math import perm, comb, atan2, hypot


FUNCTIONS = {
    'perm': perm,
    'comb': comb,
    'atan2': atan2,
    'hypot': hypot
}


def get_number(description: str = "Enter a number: ") -> int:
    try:
        return int(input(description))
    except ValueError:
        print("No number, try again. ")
        return get_number(description)


def get_function(description: str = "Enter a function: "):
    key = input(description)
    val = FUNCTIONS.get(key)
    if(val != None):
        return val
    else:
        print(key, " is not a valid function, try again. ")
        return get_function(description)


n = get_number()
k = get_number()
f = get_function()
print(f(n, k))