file = open("s2.2.in", 'r')
inputString = file.readline().strip()
print(inputString)
print(len(inputString))
for i in range(0, len(inputString), 2):
    print(inputString[i] + inputString[i + 1], end=" ")
print()
romanArray = []
for i in range(len(inputString)):
    romanArray.append(inputString[i])
for i in range(len(inputString)):
    if romanArray[i] == "I":
        romanArray[i] = 1
    if romanArray[i] == "V":
        romanArray[i] = 5
    if romanArray[i] == "X":
        romanArray[i] = 10
    if romanArray[i] == "L":
        romanArray[i] = 50
    if romanArray[i] == "C":
        romanArray[i] = 100
    if romanArray[i] == "D":
        romanArray[i] = 500
    if romanArray[i] == "M":
        romanArray[i] = 1000
    print(romanArray[i], end=" ")
print()
value = int(romanArray[len(inputString) - 2]) * int(romanArray[len(inputString) - 1])
for i in range(0, len(inputString) - 2, 2):
    if romanArray[i + 3] > romanArray[i + 1]:
        value = value - int(romanArray[i]) * int(romanArray[i + 1])
    else:
        value = value + int(romanArray[i]) * int(romanArray[i + 1])
print(value)
