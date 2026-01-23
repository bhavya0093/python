from mymodule import *

def menu_admin():
    loggin = False
    while True:
            print("1. Admin Login Page")
            print("2. View All Complaints")
            print("3. Update Complaint Status")
            print("4. View Complaints by Status")
            print("5. Search Complaint")
            print("6. Logout")

            choice = int(input("Choose Your Field :"))

            if choice == 1:
                user_id = input("Enter Admin ID: ")
                pas = input("Enter Password: ")

                if login(user_id, pas):
                    loggin = True   
                else:
                    print("---------------------------")
                    print("Invalid Id and Password...!")
                    print("---------------------------")

            elif choice == 2:
                 if not  loggin:
                      print("----------------------")
                      print("Please Login First...!")
                      print("----------------------")
                      continue
                 print(record())

            elif choice == 3:
                 if not  loggin:
                      print("----------------------")
                      print("Please Login First...!")
                      print("----------------------")
                      continue
                 print(update_complain())

            elif choice == 4:
                 if not  loggin:
                      print("----------------------")
                      print("Please Login First...!")
                      print("----------------------")
                      continue
                 print(view_status())
            elif choice == 5:
                 if not  loggin:
                      print("----------------------")
                      print("Please Login First...!")
                      print("----------------------")
                      continue
                 print(find_com())
            elif choice == 6:
                 if loggin:
                    loggin = False
                    print("-------------------------")
                    print("Admin Logout Successfully")
                    print("-------------------------")
                    menu_admin()

           
                        
                  
