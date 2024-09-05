import math

seasons=("spring","summer","autumn","winter")

print(seasons[(math.ceil(int(input("Enter the number of a month"))/3))-1])