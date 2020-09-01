data = open("s3.0a.in")
numGates = int(data.readline().strip())
numPlanes = int(data.readline().strip())
print("number of gates = " + str(numGates), end="  ")
gates = []
for i in range(numGates):
    gates.append(0)
print("number of planes = " + str(numPlanes), end="  ")
planesMaxGate = []
for i in range(numPlanes):
    planesMaxGate.append(int(data.readline().strip()))
print("planes max gate = ", end=" ")
for i in range(numPlanes):
    print(str(planesMaxGate[i]), end=" ")
print()
gatesDecimalValue = 0
for j in range(pow(numPlanes + 1, numGates)):
    print("gates status = ", end=" ")
    temp = gatesDecimalValue
    for i in range(numGates - 1, -1, -1):
        notParked = 1
        for l in range(numGates):
            if gates[l] == (temp // pow(numPlanes + 1, l)) and gates[l] > 0:
                notParked = 0
        if notParked == 1:
            gates[i] = temp // pow(numPlanes + 1, i)
            temp = temp - (temp // pow(numPlanes + 1, i)) * pow(numPlanes + 1, i)
    for i in range(numGates):
        print(str(gates[i]), end=" ")
    print()
    gatesDecimalValue = gatesDecimalValue + 1
