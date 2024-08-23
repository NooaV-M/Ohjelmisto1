cabin_class = input("Please enter a cabin class")

while True:
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
        break
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
        break
    elif cabin_class == "B":
        print("windowless cabin above the car deck.")
        break
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
        break
    else:
        print("Invalid cabin class.")
        cabin_class = input("Please enter a valid cabin class")
