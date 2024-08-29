def listsum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

numlist = []

query = input("Input numbers one by one, enter nothing to sum and end: ")

while query != "":
    try:
        query = float(query)
        numlist.append(query)
        query = input("Input numbers one by one, enter nothing to sum and end: ")

    except:
        query = input("Input numbers one by one, enter nothing to sum and end: ")

print(listsum(numlist))