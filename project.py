name = input("Enter Your Name :")
age = int(input("Enter You Age :"))
gdr = input("Enter Your Gender :")


product = input("Enter Product Name :")
gram = int(input("Enter Product gram :"))
current = 11109
total = gram * current

print("----------------------------")
print(f"Total Amount is : {total}")


print("----------------------------")

makingcharge = gram * 845

print(f"Total Making Charge is : {makingcharge}")

print("---------------------------")
totalamount = total + makingcharge
 
print(f"Total Amount : {totalamount}")

print("============================")
print("Discount")

if gdr == 'male':
    if age >= 65:
        if total > 210000 and total < 310000:
         print("Discount is 25%")
         discount = total * 25 / 100
         final = total - discount
         print(f"Final Price is {total} - {discount} = {final}")
        elif total >310000 and total <500000:
            print("Discount is 30%")
            discount = total * 30 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")
        else:
            print("Discount is 35%")
            discount = total * 35 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")
    else:
        if total > 210000 and total < 310000:
            print("Discount is 10%")
            discount = total * 10 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")
        elif total >310000 and total <500000:
                print("Discount is 20%")
                discount = total * 20 / 100
                final = total - discount
                print(f"Final Price is {total} - {discount} = {final}")
        else:
            print("Discount is 25%")
            discount = total * 25 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")        

if gdr == 'female':
    if age >= 65:
        if total > 210000 and total < 310000:
         print("Discount is 20%")
         discount = total * 25 / 100
         final = total - discount
         print(f"Final Price is {total} - {discount} = {final}")
        elif total >310000 and total <500000:
            print("Discount is 35%")
            discount = total * 35 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")
        else:
            print("Discount is 40%")
            discount = total * 40 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")
    else:
        if total > 210000 and total < 310000:
            print("Discount is 15%")
            discount = total * 15 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")
        elif total >310000 and total <500000:
                print("Discount is 25%")
                discount = total * 25 / 100
                final = total - discount
                print(f"Final Price is {total} - {discount} = {final}")
        else:
            print("Discount is 30%")
            discount = total * 30 / 100
            final = total - discount
            print(f"Final Price is {total} - {discount} = {final}")             

