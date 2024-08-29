import random
from random import randint

DxSides = int(input("Enter the number of sides on the die: "))

def dxroll(sides):
    return randint(1, int(sides))

current_result = 0

while current_result != DxSides:
    current_result = dxroll(DxSides)
    print(current_result)

