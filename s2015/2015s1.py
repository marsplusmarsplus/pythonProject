file = open("s1.6.in", "r")
k = int(file.readline())
list = []
for i in range(k):
    n = int(file.readline())
    if n > 0:
        list.append(n)
    else:
        list.pop()
    for j in range(len(list)):
        print(list[j], end=" ")
    print()
sum = 0
for i in range(len(list)):
    sum = sum + list[i]
print("sum=" + str(sum))
