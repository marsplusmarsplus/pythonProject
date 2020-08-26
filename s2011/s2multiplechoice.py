file = open("s2.4.in", 'r')
N = eval(file.readline())
studentResponses = []
studentArray = ""
for i in range(N):
    studentResponses.append(file.readline())
    studentArray = studentArray + studentResponses[i].rstrip() + " "
print(studentArray)
correctAnswers = []
studentArray = ""
for i in range(N):
    correctAnswers.append(file.readline())
    studentArray = studentArray + correctAnswers[i].rstrip() + " "
print(studentArray)
score = 0
studentArray = ""
for i in range(N):
    if studentResponses[i] == correctAnswers[i]:
        studentArray = studentArray + "* "
        score = score + 1
    else:
        studentArray = studentArray + "  "
print(studentArray)
print(str(score) + " out of " + str(N) + " correct")
file.close()
