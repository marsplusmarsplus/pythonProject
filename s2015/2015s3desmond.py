data = open("s3.0d.in")
numGates = int(data.readline().strip())
numPlanes = int(data.readline().strip())
print("number of gates = " + str(numGates))
takenGates = 0
print("taken gates = " + str(takenGates))
gates = []
gates.append(0)
for i in range(numGates):
    gates.append(0)
for i in range(numGates):
    print("gate " + str(i + 1) + " status = " + str(gates[i + 1]))
print("number of planes = " + str(numPlanes))
planes = []
planes.append(0)
for i in range(numPlanes):
    planes.append(int(data.readline().strip()))
for i in range(numPlanes):
    print("plane " + str(i + 1) + " max gate = " + str(planes[i + 1]))
for gateNum in range(numGates):
    print(gateNum + 1)
    for planeNum in range(numPlanes):
        print(planeNum, end=" ")
    print()
