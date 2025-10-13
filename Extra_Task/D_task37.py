word = input("Enter a word: ")

vowels = 0
consonants = 0

for char in word:
    if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
        vowels += 1
    else:
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
