def oddremover(list):
    evenlist = []
    for i in list:
        if i % 2 == 0:
            evenlist.append(i)
    return evenlist

numlist = []


query = 0

while query != "":
    query = input("Input whole numbers one by one, enter nothing to sum and end: ")
    try:
        query = int(query)
        numlist.append(query)
    except:
        print("Please enter only numbers")

print(oddremover(numlist))

