age = int(input("Enter Your Age :"))
ticket = 100

if age > 10 and age < 18:
    discount = ticket * 10 / 100
    total = ticket - discount
    print(f"Total Price = {total}")
elif age >= 18 and age <= 60:
    discount = ticket * 5 / 100
    total = ticket - discount
    print(f"Total Price = {total}")
else:
    print("Invalid Age...!!")    

