n = int(input("Enter Your Number: "))

a, b = 0, 1

if n >= 1:
    print(a, end=" ")
if n >= 2:
    print(b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
