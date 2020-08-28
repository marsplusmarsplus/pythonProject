file = open("s2.1.in", "r")
numJ = int(file.readline())
numA = int(file.readline())
print("number of athletes = " + str(numA))
jerseyArray = []
for i in range(numJ):
    jerseyArray.append(file.readline().strip())
print(str(numJ) + " jerseys available => ", end=" ")
for i in range(numJ):
    print(jerseyArray[i], end=" ")
print()
requestsSatisfied = 0
for line in file:
    number = int(line[2:], 10) - 1
    line = line[0]
    if jerseyArray[number] != 'T':
        if line == 'S' or \
                line == jerseyArray[number] or \
                (line == 'M' and jerseyArray[number] == 'L'):
            requestsSatisfied = requestsSatisfied + 1
            jerseyArray[number] = 'T'
print(requestsSatisfied)
