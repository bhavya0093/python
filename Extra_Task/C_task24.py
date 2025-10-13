year = 2025

if year % 100 == 0:
    if year % 400 == 0 :
        print("Century leap Year")
    else:
        print("Century BU is Not leap Year")
else:
    print("Century Not Leap Year")        