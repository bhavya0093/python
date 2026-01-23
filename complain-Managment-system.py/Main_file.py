from mymodule import *
from admin import *
from user import *

print("--------- COMPLAIN MANAGMENT SYSTEM ----------")

print("1. Admin Site")
print("2. User Site")
print("3. Exit")

choice = int(input("Choose Your Field :"))

if choice == 1:
    print("=================== WELCOME ADMIN-SITE ===================")
    print(menu_admin())

elif choice == 2:
    print("=================== WELCOME USER-SITE ===================")
    print(menu())

elif choice == 3:
    exit("Thank For Visit...")




