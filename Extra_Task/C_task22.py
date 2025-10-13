num1 = int(input("Enter Your Number :"))
num2 = int(input("Enter Your Number :"))
num3 = int(input("Enter Your Number :"))

if num1 >= num2:
    if num1 > num3:
        print(f"{num1} is Grater {num2} and {num3}")
    else:
        print(f"{num3} is Grater {num1} and {num2}")
else:
    if num2 >= num3:        
         print(f"{num2} is Grater {num1} and {num3}")
    else:
        print(f"{num3} is Grater {num1} and {num2}")