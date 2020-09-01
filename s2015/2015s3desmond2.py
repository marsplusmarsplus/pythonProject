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
        for k in range(numGates):
            if gates[k] == temp // pow(numPlanes + 1, i):
                notParked = 0
        if notParked == 1:
            gates[i] = temp // pow(numPlanes + 1, i)
        temp = temp - (temp // pow(numPlanes + 1, i)) * pow(numPlanes + 1, i)
        for j in range(numGates):
            print(str(gates[j]), end=" ")
        print()
        gatesDecimalValue = gatesDecimalValue + 1
