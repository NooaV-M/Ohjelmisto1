while True:

    try:

        Fish_length=float(input("Enter the length of the zander in centimeters:"))

        break
    except:

        print("Please enter only a number")

if Fish_length < 42:
    print(f"Specimen is {42-Fish_length}cm below the legal limit and must be released.")
else:
    print("Legal size requirements met.")