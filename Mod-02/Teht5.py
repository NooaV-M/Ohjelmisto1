Talents_grams=(float(input("Enter Talents:"))*20*32*13.3)
Pounds_grams=(float(input("Enter Pounds:"))*32*13.3)
Lots_grams=(float(input("Enter Lots:"))*13.3)

grams=Talents_grams+Pounds_grams+Lots_grams

print(f"The weight in modern units:\n{(grams)//1000} Kilograms\nand\n{grams%1000:.2f} Grams")
