# ---------------------------------------------------- USER SITE --------------------------------------------------------

def complaint(name,category,description,status="Pending"):
    complaint_id = 1
    try:
        with open("complaint.txt" ,"r") as f:
            lines = f.readlines()

            lines = [line.strip() for line in lines if line.strip() != ""]

            if lines:
                new_line = lines[-1]
                complaint_id = int(new_line.split("|")[0].strip())+1

    except FileNotFoundError:
        pass

    com_data = f"{complaint_id} | {name} | {category} | {description} | {status} | \n"

    with open("complaint.txt" ,"a") as f:
         f.write(com_data)

    print("----------------------------------")
    print("Complaint Raise Successfully")
    print("----------------------------------")
    print("Your Complaint ID is :",complaint_id)

def search(complaint_id):
    try:
        with open("complaint.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue

                parts = [p.strip() for p in line.split("|")]

                file_id = int(parts[0])

                if file_id == complaint_id:
                    print("---------------------------------------------------------")
                    return line   
                    print("---------------------------------------------------------")
        return "Complaint ID not found "

    except FileNotFoundError:
        return "File not found "
    
def feedback(complaint_id):
    try:
        with open("complaint.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue

                parts = [p.strip() for p in line.split("|")]

                file_id = int(parts[0])

                if file_id == complaint_id:
                    print("---------------------------------------------------------")
                    print(f"Complaint : {parts[2]}")
                    print("---------------------------------------------------------")
                    feed = input("Enter your feedBack :")
                    with open("feedback.txt" ,"a") as f:
                        f.write(f"{complaint_id} | {feed}")
                    return "Feedback saved"
                return "Complaint Id Not Found"
    except FileNotFoundError:
        pass   

# ---------------------------------------------- ADMIN SITE ----------------------------------------------


def login(user_id, pas):
    user_id = user_id.strip()
    pas = pas.strip()

    if user_id == "bhavya" and pas == "123":
        print("------------------")
        print("Login Successfully")
        print("------------------")
        return True
    
        

def record():
    try:
        with open("complaint.txt", "r") as f:
            data = f.readlines()

        if not data:
            print("No complaints found ")
            return

        print("\n---------------- ALL COMPLAINTS ----------------")
        for line in data:
            line = line.strip()
            if line == "":
                continue
            print(line)
        print("------------------------------------------------")

    except FileNotFoundError:
        print("complaint.txt not found ")
 
def update_complain():
    try:
        with open("complaint.txt", "r") as f:
            lines = f.readlines()

        if not lines:
            print(" No complaints found.")
            return

        complaint_id = input("Enter Complaint Id to Update :").strip()

        print("\nSelect New Status")
        print("1. Pending")
        print("2. In Progress")
        print("3. Resolved")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            new_status = "Pending"
        elif choice == "2":
            new_status = "In Progress"
        elif choice == "3":
            new_status = "Resolved"
        else:
            print(" Invalid choice")
            return

        updated_lines = []
        updated = False

        for line in lines:
            data = line.strip().split("|")

            
            if len(data) < 5:
                updated_lines.append(line)
                continue

            file_id = data[0].strip()
            current_status = data[4].strip()

            if file_id == complaint_id:
                if current_status == "Resolved":
                    print("==============================")
                    print(" Complaint already resolved")
                    print("==============================")
                    return

                data[4] = f" {new_status}"
                updated = True
                updated_lines.append("|".join(data) + "\n")
            else:
                updated_lines.append(line)

        if updated:
            with open("complaint.txt", "w") as f:
                f.writelines(updated_lines)

            print("======================================")
            print(" Complaint status updated successfully!")
            print("======================================")
        else:
            print(" Complaint ID not found.")

    except FileNotFoundError:
        print(" complaint.txt file not found.")

def view_status():
    try:
        with open("complaint.txt", "r") as f:
            lines = f.readlines()

        new_id = input("Enter Customer Id :")
        found = False

        for line in lines:
            data = line.strip().split("|")

            if len(data) < 5:
                continue

            file_id = data[0].strip()
            name = data[1].strip()
            status = data[4].strip()

            if file_id == new_id:
                print("==================================")
                print(f"Name : {name} , Status : {status}")
                print("==================================")
                found = True    


    except FileNotFoundError:
         print("complaint.txt file not found.")
        
def find_com():
    try:
        with open("complaint.txt", "r") as f:
            lines = f.readlines()

        new_id = input("Enter Customer Id :")
        found = False
        for line in lines:
            data = line.strip().split("|")

            if len(data) < 5:
                continue

            file_id = data[0].strip()
            name = data[1].strip()
            category = data[2].strip()
            note = data[3].strip()
            status = data[4].strip()

            if file_id == new_id:
                print("============================================================")
                print(f"{file_id} | {name} | {category} | {note} | {status}")
                print("============================================================")
                found = True
                break
        if not found:
            print("Invalid Complaint Id")

    except FileNotFoundError:
         print("complaint.txt file not found.")
        