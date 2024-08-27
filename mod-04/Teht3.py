number = (input("Enter a number, or enter an empty string to end program:"))
if number != "":
    number = float(number)

    num_lowest = number
    num_highest = number

    while number != "":
        number = float(number)

        if number < num_lowest:
            num_lowest = number
        if number > num_highest:
            num_highest = number

        number = (input("Enter a number, or enter an empty string to end program "))

    print(f"Program ended.\nLargest number: {num_highest}\nSmallest number: {num_lowest}")
else:
    print("program ended.")