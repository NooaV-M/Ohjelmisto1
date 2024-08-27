number = float(input("Enter number of inches:"))

while number >= 0:
    print(f"{2.54*number} centimeters.")
    number = float(input("Enter number of inches:"))

print("Invalid value.")