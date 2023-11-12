import random

number = random.randint(1, 50)

user_guess = int(input("Guess a number between 1 and 50: "))

while  user_guess != number:
    if user_guess > number:
        print("The guess is too high!, try again")
    else:
        print("The guess is too low!, try again")
    user_guess = int(input("Guess a number between 1 and 50: "))
print("You guessed it right!, the number was", number)
