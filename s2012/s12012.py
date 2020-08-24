file = open("s1.3.in", 'r')
J = eval(file.readline())
print(((J - 1) * (J - 2) * (J - 3)) / 6)
