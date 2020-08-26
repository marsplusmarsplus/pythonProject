file = open("s1.3.in", "r")
k = int(file.readline())
friends = []
for i in range(k):
    friends.append(i + 1)
for i in range(k):
    print(friends[i], end=" ")
print()
m = int(file.readline())
for round in range(m):
    print("round " + str(round + 1))
    r = int(file.readline())
    newfriends = []
    for i in range(len(friends)):
        if (i + 1) % r != 0:
            newfriends.append(friends[i])
    friends = []
    for f in newfriends:
        friends.append(f)
    for i in range(len(friends)):
        print(friends[i], end=" ")
    print()
