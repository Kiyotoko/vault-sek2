FUNCTIONS = {
    'add': lambda a, b: a+b,
    'sub': lambda a, b: a+b,
    'mul': lambda a, b: a*b,
    'div': lambda a, b: a/b,
    'pow': lambda a, b: a**b
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


a = get_number()
b = get_number()
f = get_function()
print(f(a, b))