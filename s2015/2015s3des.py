# input number of gates and number of planes
data = open("s3.0b.in")
numGates = int(data.readline().strip())
numPlanes = int(data.readline().strip())
print(str(numGates) + " gates and ", end=" ")
print(str(numPlanes) + " planes", end="  ")
print()

# input max gate for each plane
planesMaxGate = []
for i in range(numPlanes):
    planesMaxGate.append(int(data.readline().strip()))
for i in range(numPlanes):
    print("plane " + str(i + 1) + " => gates = ", end=" ")
    for j in range(planesMaxGate[i]):
        print(j + 1, end=" ")
    print()

# initially, gates are all empty
gates = []
for i in range(numGates):
    gates.append(0)
    print("gate " + str(i + 1) + " = " + str(gates[i]), end="  ")
print()
