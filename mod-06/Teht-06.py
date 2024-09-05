import math

def pizza_price_calculator (diameter,price):
    result = (math.pi*((float(diameter)/100)/2)**2)/float(price)
    return result


parameters1=[]

parameters1.append(input("Enter diameter of pizza in centimeters."))
parameters1.append(input("Enter price of pizza in Euros."))

parameters2=[]

parameters2.append(input("Enter diameter of pizza in centimeters."))
parameters2.append(input("Enter price of pizza in Euros."))

pizza1price = pizza_price_calculator(parameters1[0],parameters1[1])
pizza2price = pizza_price_calculator(parameters2[0],parameters2[1])

if pizza1price == pizza2price:
    print("The two pizza are of equal value")
elif pizza1price > pizza2price:
    print("The first pizza provides better value")
else:
    print("The second pizza provides better value")
