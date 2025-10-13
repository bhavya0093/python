num = int(input("Enter Your Number :"))

if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is Divided By 5 and 11")
else:
    print(f"{num} is Not Divided By 5 and 11")