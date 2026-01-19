from logic import *

load_expenses()
status = True
while status:
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category- Wise Total")
        print("5. Monthly Summary")
        print("6. Exit")

        choice = int(input("Choice Your Field :"))


        if choice == 1:
            add_exp()
        elif choice == 2:
            view_exp()
        elif choice == 3:
            t_exp()
        elif choice == 4:
            cate_wise()
        elif choice == 5:
             monthly_summary()
        elif choice == 6:
             exit()