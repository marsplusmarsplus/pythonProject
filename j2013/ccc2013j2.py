word = input()
rotate = "IOSHZXN"
answer = "CAN ROTATE ALL LETTERS"
for letter in word:
    if letter not in rotate:
        answer = "CANNOT ROTATE THE LETTER "+letter
print (answer)
