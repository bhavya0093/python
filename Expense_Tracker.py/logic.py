from datetime import datetime
import csv
import os

expenses = []
file_name = "expenses.csv"

# ---------------------------------------------- FILE HANDLING (CSV) ----------------------------------------------

def save_all_to_csv():
    """Rewrite full CSV (useful after delete/update)"""
    with open(file_name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category", "note"])
        writer.writeheader()
        writer.writerows(expenses)

def append_one_to_csv(expense):
    """Append a single expense row to CSV"""
    file_exists = os.path.exists(file_name)

    with open(file_name, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category", "note"])

        
        if not file_exists or os.path.getsize(file_name) == 0:
            writer.writeheader()

        writer.writerow(expense)

def load_expenses():
    global expenses
    expenses = []

    if not os.path.exists(file_name):
        return

    with open(file_name, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["amount"] = int(row["amount"])
            except:
                row["amount"] = 0
            expenses.append(row)

# ---------------------------------------------- ADD EXPENSES --------------------------------------------------

def valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_exp():
    while True:
        date = input("Enter Date (YYYY-MM-DD) : ")
        if valid_date(date):
            break
        else:
            print("Invalid Date !")

    while True:
        try:
            amount = int(input("Enter Amount : "))
            if amount > 0:
                break
            else:
                print("Amount must be > 0")
        except:
            print("Enter valid number!")

    category = input("Enter Category : ").strip()
    note = input("Enter Note : ").strip()

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)

    
    append_one_to_csv(expense)

    print("---------------------------")
    print("Data Added Successfully...")
    print("---------------------------")

# ---------------------------------------------- VIEW EXPENSES --------------------------------------------------

def view_exp():
    if len(expenses) == 0:
        print("No expenses found!")
        return

    print(f"{'DATE':<12} {'AMOUNT':<8} {'CATEGORY':<12} NOTE")
    print("-" * 55)
    for e in expenses:
        print(f"{e['date']:<12} {e['amount']:<8} {e['category']:<12} {e['note']}")

# ---------------------------------------------- Total Spending --------------------------------------------------

def t_exp():
    total = 0
    for i in expenses:
        total += i["amount"]

    print("---------------------------")
    print(f"Total Spend : {total}")
    print("---------------------------")

# ---------------------------------------------- Category-Wise Spending --------------------------------------------

def cate_wise():
    if len(expenses) == 0:
        print("No expenses found!")
        return

    c_total = {}

    for i in expenses:
        cat = i["category"]
        amt = i["amount"]

        if cat in c_total:
            c_total[cat] += amt
        else:
            c_total[cat] = amt

    print("=======================")
    print("Category | Total Amount")
    print("-----------------------")
    for c, total in c_total.items():
        print(c, ":", total)

# ---------------------------------------------- Monthly Summary --------------------------------------------------

def valid_month(month_str):
    try:
        datetime.strptime(month_str, "%Y-%m")
        return True
    except:
        return False

def monthly_summary():
    if len(expenses) == 0:
        print("No expenses found!")
        return

    month = input("Enter Month (YYYY-MM) : ").strip()

    if not valid_month(month):
        print("Invalid month format! Example: 2026-01")
        return

    total = 0
    cat_total = {}
    count = 0

    for e in expenses:
        if e["date"].startswith(month):
            count += 1
            total += e["amount"]

            cat = e["category"]
            if cat in cat_total:
                cat_total[cat] += e["amount"]
            else:
                cat_total[cat] = e["amount"]

    if count == 0:
        print("No expenses found in this month!")
        return

    print("\nMonthly Summary:", month)
    print("Total Entries :", count)
    print("Total Spend   :", total)

    print("\nCategory Wise:")
    for c, t in cat_total.items():
        print(c, ":", t)


