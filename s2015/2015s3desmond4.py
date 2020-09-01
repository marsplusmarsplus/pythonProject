data = open("s3.0a.in")
maxParkedPlanes = 0
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
    for ii in range(numGates - 1, -1, -1):
        gates[ii] = temp // pow(numPlanes + 1, ii)
        temp = temp - (temp // pow(numPlanes + 1, ii)) * pow(numPlanes + 1, ii)
    numParkedPlanes = 0
    for iii in range(numGates):
        print(str(gates[iii]), end=" ")
        if gates[iii] > 0:
            numParkedPlanes = numParkedPlanes + 1
    print("number of parked planes = " + str(numParkedPlanes))
    if numParkedPlanes > maxParkedPlanes:
        maxParkedPlanes = numParkedPlanes
        print("max number of parked planes = " + str(maxParkedPlanes))
    gatesDecimalValue = gatesDecimalValue + 1
    for hhh in gates:
        if gates.count(hhh) > 1 and hhh != 0:
            print("VOID")
print("max number of parked planes = " + str(maxParkedPlanes))
