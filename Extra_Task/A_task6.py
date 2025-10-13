num1 = int(input("Enter Your Number :"))
num2 = int(input("Enter Your Number :"))
num3 = int(input("Enter Your Number :"))


if num1 < num2 and num1 < num3:
    print(f"{num1} is small {num2} and {num3}") 
elif num2 < num1 and num2 < num3 :
    print(f"{num2} is Small {num1} and {num3}")
else:
    print(f"{num3} is small {num1} and {num2}")