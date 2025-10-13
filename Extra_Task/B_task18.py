num = int(input("Enter Your Number :"))
rev=0

temp = num

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
