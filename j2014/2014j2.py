file = open("j2.4a.in", "r")
v = int(file.readline())
votes = file.readline()
acount = 0
for letter in votes:
    if letter == "A":
        acount = acount + 1
bcount = v - acount
print(str(v) + " votes: " + str(acount) + " for A and " + str(bcount) + " for B")
if acount > bcount:
    print("A wins")
elif bcount > acount:
    print("B wins")
else:
    print("Tie")
