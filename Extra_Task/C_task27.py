units = float(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
elif units <= 300:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
else:
    bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00

print("Total electricity bill is: ", bill)
