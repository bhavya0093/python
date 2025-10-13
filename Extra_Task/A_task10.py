a = int(input("Enter Your Number : "))
b = int(input("Enter Your Number : "))
c = int(input("Enter Your Number : "))

if ( a + b > c )and (b + c > a) and (a + c > b):
    print("Valid Triangle")
else:
    print("Not Valid Triangle")
