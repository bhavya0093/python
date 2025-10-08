unit = int(input("Enter Your Units :"))
fixcharge = 50
discount = 0
charge = 0

if unit > 0 and unit <= 100:
    if unit < 50:
        price = (unit * 5) + fixcharge
        discount = unit * 5 / 100
        unit -= discount
        perunit = unit * 5
             
    else:
        price = (unit * 5) + fixcharge
        perunit = unit * 5
        
elif unit >= 101 and unit <= 200:
    extra = unit - 100
    _1to100 = 100 * 5
    price = _1to100 + (extra * 7) + fixcharge
    perunit = unit * 7

elif unit >= 201 and unit <= 300:
    extra = unit - 200
    _1to100 = 100 * 5
    _101to200 = 100 * 7
    price = _1to100 + _101to200 + (extra * 10) + fixcharge
    perunit = unit * 10
    
else:
    extra = unit - 300
    _1to100 = 100 * 5
    _101to200 = 100 * 7
    _201to300 = 100 * 10
    price = _1to100 + _101to200 + _201to300 + (extra * 15) + fixcharge
    
    if unit > 500:
        surcharge = unit * 10 / 100
        price = surcharge + price
    
peak = int(input("Enter Your Pik Over Use :"))    

if peak > 50:
    extra = peak - 50
    charge = extra * 2

elif peak <= 50:
    print(f"{peak} Unit Is Low")
elif peak > 50 and peak < 200:
    print(f"{peak} Unit Is Medium")
else:
    print(f"{peak} Unit Is High consumption")     

late = input("Is the payment delayed? (yes/no):")    

if late == 'yes':
    latePrice = 100
else:
    latePrice = 0

print("------------------------------------------")

print("-------------Electricity Bill----------------")

print(f"Total Unit : {unit} ")
print(f"Fix Meter Charge : {fixcharge}")
print(f"Total Amount + Surcharge : {price}")
print(f"Total Discount : {discount}")
print(f"Pik Over Use Amount : {charge}")
print(f"Late Charge : {latePrice}")
print(f"Total Amount : {price + latePrice + charge}")
