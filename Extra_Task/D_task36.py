num = int(input("Enter Your Number: "))
temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10       
    sum_digits += digit     
    temp //= 10             

print("Sum of digits is:", sum_digits)
