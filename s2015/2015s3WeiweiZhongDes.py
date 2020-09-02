root = [0 for i in range(100001)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def merge(x, y):
    root[find(x)] = find(y)


file = open("s3.0b.in")
numGates = int(file.readline())
numPlanes = int(file.readline())
for i in range(1, numGates + 1):
    root[i] = i
i = 0
keepgoing = True
while i < numPlanes and keepgoing:
    gateWanted = int(file.readline())
    gateWantedRoot = find(gateWanted)
    if gateWantedRoot == 0:
        print(i)
        keepgoing = False
    merge(gateWantedRoot, gateWantedRoot - 1)
    i = i + 1
if keepgoing:
    print(numPlanes)
