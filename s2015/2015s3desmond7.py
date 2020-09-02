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
for j in range(pow(numPlanes + 1, numGates)):  # MAIN LOOP
    temp = gatesDecimalValue
    void = 0
    for ii in range(numGates - 1, -1, -1):  # park planes in gates
        gates[ii] = temp // pow(numPlanes + 1, ii)
        if gates[ii] > planesMaxGate[gates[ii] - 1]:
            void = 111
        temp = temp - (temp // pow(numPlanes + 1, ii)) * pow(numPlanes + 1, ii)
    for hhh in gates:  # any duplicate planes?
        if gates.count(hhh) > 1 and hhh != 0:
            void = 222222
    print("void = " + str(void), end=" ")
    numParkedPlanes = 0
    print("gates status = ", end=" ")
    for iii in range(numGates):  # how many planes were parked?
        print(str(gates[iii]), end=" ")
        if gates[iii] > 0:
            numParkedPlanes = numParkedPlanes + 1
    print("number of parked planes = " + str(numParkedPlanes))
    if numParkedPlanes > maxParkedPlanes and void == 0:
        maxParkedPlanes = numParkedPlanes
        print(str(j) + " max number of parked planes = " + str(maxParkedPlanes))
    gatesDecimalValue = gatesDecimalValue + 1
print("max number of parked planes = " + str(maxParkedPlanes))
