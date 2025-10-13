
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c

if D > 0:
    print("Roots are real and distinct")
elif D == 0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary")
