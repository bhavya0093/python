marks = [45, 67, 23, 89, 34, 50, 12]  #

passed = 0
failed = 0

for mark in marks:
    if mark >= 35:
        passed += 1
    else:
        failed += 1

print("Number of students passed:", passed)
print("Number of students failed:", failed)
