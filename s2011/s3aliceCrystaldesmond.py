def hasCrystal(M, X, Y):
    if M == 1:
        if X == 1 and Y == 0:
            return "*"
        elif X == 2 and Y == 0:
            return "*"
        elif X == 3 and Y == 0:
            return "*"
        elif X == 2 and Y == 1:
            return "*"
        else:
            return "_"
    else:
        if X // pow(5, M - 1) == 1 and Y // pow(5, M - 1) == 0:
            return "*"
        elif X // pow(5, M - 1) == 2 and Y // pow(5, M - 1) == 0:
            return "*"
        elif X // pow(5, M - 1) == 3 and Y // pow(5, M - 1) == 0:
            return "*"
        elif X // pow(5, M - 1) == 2 and Y // pow(5, M - 1) == 1:
            return "*"
        elif X // pow(5, M - 1) == 1 and Y // pow(5, M - 1) == 1:
            return hasCrystal(M - 1, X % pow(5, M - 1), Y % pow(5, M - 1))
        elif X // pow(5, M - 1) == 3 and Y // pow(5, M - 1) == 1:
            return hasCrystal(M - 1, X % pow(5, M - 1), Y % pow(5, M - 1))
        elif X // pow(5, M - 1) == 2 and Y // pow(5, M - 1) == 2:
            return hasCrystal(M - 1, X % pow(5, M - 1), Y % pow(5, M - 1))
        else:
            return "_"


file = open("s3.6.in", 'r')
inputLine = file.readline().split()
M = int(inputLine[0])
for i in range(pow(5, M) - 1, -1, -1):
    for j in range(pow(5, M)):
        # for j in range(pow(5, M)):
        print(hasCrystal(M, j, i), end="")
    print()
