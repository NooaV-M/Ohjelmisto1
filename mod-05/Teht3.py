num = (input("Enter a whole number or press enter to end program: "))

while num != "":

    for i in range(2,(int(num))):
        if int(num) % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")


    num = (input("Enter a whole number or press enter to end program: "))
