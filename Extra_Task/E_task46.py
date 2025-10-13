text = input("Enter a string: ")

words = 1
digits = 0
special = 0
letters = 0

for char in text:
    if char == " ":
        words += 1
    elif char >= '0' and char <= '9':
        digits += 1
    elif (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
        letters += 1
    else:
        special += 1

print("Words:", words)
print("Digits:", digits)
print("Special characters:", special)
