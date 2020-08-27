file = open("s2.14.in", 'r')
maxW = int(file.readline())
carsN = int(file.readline())
carWeight = [0, 0, 0]
for i in range(carsN):
    carWeight.append(int(file.readline()))
carWeight.append(maxW + 1)
carsAcross = 0
i = 3
totalWeight = carWeight[i - 3] + carWeight[i - 2] + carWeight[i - 1] + carWeight[i]
while totalWeight <= maxW:
    carsAcross = carsAcross + 1
    i = i + 1
    totalWeight = carWeight[i - 3] + carWeight[i - 2] + carWeight[i - 1] + carWeight[i]
print(carsAcross)
