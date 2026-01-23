from mymodule import *

def menu():
    while True:
        print("1. Register New Complaint")
        print("2. View Complaint Status")
        print("3. Submit FeedBack")
        print("4. Exit")
  


        choice = int(input("Enter Your Field :"))

        if choice == 1:
            try:
                name = input("Enter Name : ").strip()
                category = input("Enter Category : ").strip()
                Des = input("Enter Description : ").strip()

                if name == "" or category == "" or Des == "":
                    print("Please Fill All Data.....!")
                else:
                    complaint(name, category, Des)
                    print("Complaint Registered...!")

            except Exception as e:
                print("Error:", e)


        elif choice == 2:
            id = int(input("Enter Customer Id :"))
            print(search(id))

        elif choice == 3:
            id = int(input("Enter Customer Id :"))
            print(feedback(id))

        else:

            exit("Thank You.....")

