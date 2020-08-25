k = eval(input())
for i in range(k):
    for j in range(k):
        print("*", end="")
    for j in range(k):
        print("X", end="")
    for j in range(k):
        print("*", end="")
    print()
for i in range(k):
    for j in range(k):
        print(" ", end="")
    for j in range(k):
        print("X", end="")
    for j in range(k):
        print("X", end="")
    print()
for i in range(k):
    for j in range(k):
        print("*", end="")
    for j in range(k):
        print(" ", end="")
    for j in range(k):
        print("*", end="")
    print()
