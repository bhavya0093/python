numbers = [10, 20, 5, 30, 20]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number is:", second)
