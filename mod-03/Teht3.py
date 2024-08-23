gender = input("Please enter your gender (male/female):")

while True:
    if gender == "male" or gender == "female":
        break
    else:
        gender = input("Please enter your gender (male/female):")

hg_value = int(input("Please enter your hemoglobin value (in grams per liter):"))

#Male options
if gender == "male":
    if hg_value > 155:
        print("High hemoglobin levels")
    elif hg_value > 116:
        print("Normal hemoglobin levels")
    else:
        print("Low hemoglobin levels")
#Female options
if gender == "female":
    if hg_value > 167:
        print("High hemoglobin levels")
    elif hg_value > 116:
        print("Normal hemoglobin levels")
    else:
        print("Low hemoglobin levels")

