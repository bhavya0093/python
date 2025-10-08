unit = int(input("Enter Your Units :"))
fixcharge = 50
surcharge = 0
discount = 0
charge = 0

if unit > 0 and unit <= 100:
    if unit < 50:
        discount = unit * 5 / 100
        unit -= discount
        perunit = unit * 5
        mcharge = perunit + fixcharge
        
    else:
        perunit = unit * 5
        mcharge = perunit + fixcharge

elif unit >= 101 and unit <= 200:
    perunit = unit * 7
    mcharge = perunit + fixcharge

elif unit >= 201 and unit <= 300:
    perunit = unit * 10
    mcharge = perunit + fixcharge
else:
    perunit = unit * 15
    mcharge = perunit + fixcharge
    
    if unit > 500:
        surcharge = (perunit * 10) / 100
        mcharge = perunit + surcharge
       

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

if late == "yes":
    late = mcharge + 100
else:
    late_penalty = 0

print("------------------------------------------")

print("-------------Electricity Bill----------------")

print(f"Total Unit : {unit} ")
print(f"Fix Meter Charge : {fixcharge}")
print(f"Total Amount + Surcharge : {surcharge}")
print(f"Total Discount : {discount}")
print(f"Pik Over Use Amount : {charge}")
print(f"Late Charge : {late}")
print(f"Total Amount : {mcharge}")
