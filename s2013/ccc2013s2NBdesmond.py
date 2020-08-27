file = open("s2.14.in", 'r')
maxW = int(file.readline())
print("max weight = " + str(maxW))
carsN = int(file.readline())
print("number of cars = " + str(carsN))
carW = []
for i in range(carsN):
    carW.append(file.readline().strip())
print("car weights =", end=" ")
for i in range(carsN):
    print(carW[i], end=" ")
print()
currentCar = 0
while currentCar < int(carsN) and \
        ((int(carW[currentCar]) + int(carW[currentCar + 1])
          + int(carW[currentCar + 2]) + int(carW[currentCar + 3])) <= maxW):
    currentCar = currentCar + 1
print("max number of cars = " + str(currentCar + 3))
