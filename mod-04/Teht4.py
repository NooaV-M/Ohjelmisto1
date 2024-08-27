import random

random_number = random.randint(1, 10)

guess = int(input("Guess the number between 1 and 10: "))

while guess != random_number:
    if guess > 10 or guess < 1:
        guess = int(input("Guess the number between 1 and 10: "))
    elif guess < random_number:
        guess = int(input("Too low\nGuess again:"))
    else:
        guess = int(input("Too high\nGuess again:"))

print(f"{guess} is correct!")