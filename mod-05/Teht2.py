from os.path import exists

num = []

inputNum = input("Enter a number, or press enter to exit: ")
while inputNum != '':
    num.append(int(inputNum))

    inputNum = input("Enter a number, or press enter to exit: ")

num.sort(reverse=True)

if len(num) != 0:
    print(str(num[0:5]))