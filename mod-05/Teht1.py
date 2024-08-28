import random

dicerolls_amount = int(input("Enter number of dice to roll: "))
dicerolls_total = 0

for i in range(dicerolls_amount):
    dicerolls_total = dicerolls_total + random.randint(1,6)

print(f"The total result of all {dicerolls_amount} dice rolled is {dicerolls_total}")