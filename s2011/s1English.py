file = open("s1.4.in", 'r')
totalLines = file.readlines(10000)
countS = 0
countT = 0
for line in totalLines:
    for i in range(0, len(line)):
        if line[i] == "s" or line[i] == "S":
            countS = countS + 1
        elif line[i] == "t" or line[i] == "T":
            countT = countT + 1
    print("S=" + str(countS) + " T=" + str(countT))
if countT > countS:
    print("T > S means English")
elif countS > countT:
    print("S > T means French")
else:
    print("S = T means ??????")
file.close()
