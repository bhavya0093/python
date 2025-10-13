bill = int(input("Enter Your Amount :"))

if bill > 1000:
    discount = bill * 10 / 100
    total = bill - discount
    print("Total Bill is :",total)