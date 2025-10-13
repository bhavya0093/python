num = int(input("Enter Your Number :"))
rev=0

temp = num

while num > 0:
    digit = num % 10
    rev = rev + ( digit * digit * digit )
    num //= 10

if temp==rev:
    print("Armstrong")
else:
    print("Not Armstrong")