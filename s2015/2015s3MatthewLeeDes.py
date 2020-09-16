data = open("s3.0b.in")
gates = int(data.readline())
numPlanes = int(data.readline())
print()
print("gates=" + str(gates) + " numPlanes=" + str(numPlanes), end=" ")
planes = []
total = 0
for i in range(gates + 1):
    planes.append(0)
    print("planes[" + str(i) + "]=" + str(planes[i]), end=" ")
print()
print()
i = 0
keepGoing = True
while i < numPlanes and keepGoing:
    cPlane = int(data.readline())
    while cPlane > 0 and planes[cPlane] > 0:
        t = planes[cPlane]
        planes[cPlane] = planes[cPlane] + 1
        cPlane = cPlane - t
        print("       t=" + str(t) + " cPlane=" + str(cPlane), end=" ")
        for j in range(gates + 1):
            planes.append(0)
            print("planes[" + str(j) + "]=" + str(planes[j]), end=" ")
        print()
    if cPlane <= 0:
        keepGoing = False
    else:
        planes[cPlane] = 1
        total = total + 1
        print("    planes[" + str(cPlane) + "]=" + str(planes[cPlane]) + " total=" + str(total))
    i = i + 1
    print("i=" + str(i))
print(total)
