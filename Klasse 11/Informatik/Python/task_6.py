from random import randint

value = randint(1, 10)

trys = 0
while trys < 3:
    guess = int(input("Please enter a number: "))
    if guess == value:
        print("You are right!")
    else:
        print("You are false!.\nYou have", 2-trys,"trys left.")
    trys+=1