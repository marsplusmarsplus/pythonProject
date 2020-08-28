def hasCrystal(M, X, Y):
    if M == 1:
        if (X == 1 and Y == 0) or (X == 2 and Y == 0) \
                or (X == 3 and Y == 0) or (X == 2 and Y == 1):
            return "CRYSTAL"
        else:
            return "EMPTY"
    else:
        print(pow(5, M - 1))
        if (X // pow(5, M - 1) == 1 and Y // pow(5, M - 1) == 0) \
                or (X // pow(5, M - 1) == 2 and Y // pow(5, M - 1) == 0) \
                or (X // pow(5, M - 1) == 3 and Y // pow(5, M - 1) == 0) \
                or (X // pow(5, M - 1) == 2 and Y // pow(5, M - 1) == 1):
            return "CRYSTAL"
        else:
            return hasCrystal(M - 1, X % 5, Y % 5)


file = open("s3.6.in", 'r')
inputLine = file.readline().split()
M = int(inputLine[0])
X = int(inputLine[1])
Y = int(inputLine[2])
if (X > pow(5, M) or Y > pow(5, M)):
    print("error")
print(hasCrystal(M, X, Y))
