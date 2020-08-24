file = open("s2.7.in", 'r')
N = eval(file.readline())

studentResponses = []
for i in range(N):
    studentResponses.append(file.readline())

correctAnswers = []
for i in range(N):
    correctAnswers.append(file.readline())

score = 0
for i in range(0, N):
    if studentResponses[i] == correctAnswers[i]:
        score = score + 1
        print("question " + str(i + 1) + " is correct")
print(str(score) + " out of " + str(N) + " correct")
file.close()
