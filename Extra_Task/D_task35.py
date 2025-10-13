num = int(input("Enter Your Number: "))

if num <= 1:
    print("Number is Not Prime")
else:
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

    if flag:
        print("Number is Prime")
    else:
        print("Number is Not Prime")

