num = int(input("Enter Your Number :"))
flag=False

for i in range(1,11):


    if num >= 1 and num <= 10:
        flag=True
    else:
        flag=False

if flag:
    print("Number Is Range List")
else:
    print("Number Is Not Range List")
    
