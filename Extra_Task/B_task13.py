num = int(input("Enter Your Number :"))
fact = 1

for i in range(1,num+1):
    fact *= i

    print("Factorial is : ",fact)