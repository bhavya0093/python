marks = int(input("Enter Your Number :"))

if marks > 90:
    print("A Grade")
elif marks >= 70 and marks <= 90:
    print("B Grade")
elif marks >= 55 and marks <= 70:
    print("C Grade")
elif marks >= 35 and marks <= 55:
    print("D Grade")
else:
    print("Fail")