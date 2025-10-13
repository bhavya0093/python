numbers = [1, 2, 2, 3, 4, 4, 5]

for i in numbers:
    count = 0
    for j in numbers:
        if i == j:
            count += 1
    if count == 1:
        print(i, end=" ")
