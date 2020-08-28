file = open("s2.5b.in", "r")
N = int(file.readline())
firstArray = []
firstArray = file.readline().split()
secondArray = []
secondArray = file.readline().split()
resultsArray = []
for i in range(N):
    resultsArray.append("good")
for i in range(N):
    for j in range(N):
        if firstArray[i] == secondArray[j] and firstArray[j] != secondArray[i]:
            resultsArray[i] = "bad"
        if firstArray[i] == secondArray[j] and i == j:
            resultsArray[i] = "bad"
for i in range(N):
    print(firstArray[i] + " + " + secondArray[i] + " => " + resultsArray[i])
