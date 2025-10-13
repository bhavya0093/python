num = int(input("Enter Your Number :"))
rev=0


while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reverse Number Is :",rev)