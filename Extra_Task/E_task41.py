

correct_pin = 1234
balance = 5000  

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("PIN verified successfully!")
    print("Your current balance is:", balance)
    
    withdraw = int(input("Enter amount to withdraw: "))
    
    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")
else:
    print("Incorrect PIN!")
