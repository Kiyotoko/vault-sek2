from random import randint

number = randint(1, 10)
trys = 1


def get_number(description: str = "Enter a number: ") -> int:
    try:
        return int(input(description))
    except ValueError:
        print("No number, try again. ")
        return get_number(description)


def guessing():
    guess = get_number()
    global trys
    if(guess == number):
        print("Thats right, you have needed", trys, "trys.")
    else:
        if(guess > number):
            print("Smaller ...")
        else:
            print("Greater ...")
        trys += 1
        guessing()

print("Please guess a number in the range of [1:10]")
guessing()