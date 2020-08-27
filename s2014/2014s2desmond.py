file = open ("s2.5b.in", "r")
n = int(file.readline())
first = file.readline().split()
second = file.readline().split()
i = 0
state = "good"
while i < n and state == "good":
    position = first.index(second[i])
    if first[i] != second[position] or position == i:
        state = "bad"
    i = i + 1
print (state)
