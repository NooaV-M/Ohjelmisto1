def gallonconvert(gallons):
    return float(gallons*3.78541178)

gallons_amount = (input("Enter number of gallons to convert: "))

while True:
    try:
        gallons_amount = int(gallons_amount)
    except:
        gallons_amount = (input("Enter number of gallons to convert: "))
    else:
        break

while float(gallons_amount) >= 0:
    print(f"{round(gallonconvert(float(gallons_amount)),2)} liters")
    gallons_amount = (input("Enter gallons to convert: "))
    while True:
        try:
            gallons_amount = int(gallons_amount)
        except:
            gallons_amount = (input("Enter number of gallons to convert: "))
        else:
            break
