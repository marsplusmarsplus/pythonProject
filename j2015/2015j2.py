file = open("j2.1.in", "r")
line = file.readline()
happy = 0
sad = 0
for i in range(len(line) - 2):
    if line[i:i + 3] == ":-)":
        happy = happy + 1
    elif line[i:i + 3] == ":-(":
        sad = sad + 1
print(str(happy) + " happy and " + str(sad) + " sad")
if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("equal happy and sad")
elif happy > sad:
    print("more happy")
else:
    print("more sad")
