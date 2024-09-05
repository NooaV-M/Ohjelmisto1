names = set()

nameinput = input("Enter a name, or enter an empty string to end program: ")

while nameinput != '':
    for i in names:
        if nameinput == i:
            print("Existing name")
            break
    else:
        print("New name")
        names.add(nameinput)
    nameinput = input("Enter a name, or enter an empty string to end program: ")

for i in names:
    print(i)