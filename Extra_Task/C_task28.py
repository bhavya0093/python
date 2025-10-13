age = int(input("Enter Your Age :"))

if age < 14:
    print("Child")
elif age >= 14 and age <18:
    print("teenager")
elif age >= 18 and age < 60:
    print("Adult")
else:
    print("Senior Citizen")