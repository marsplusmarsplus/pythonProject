file = open("j3.4.in", "r")
n = int(file.readline())
antonia = 100
david = 100
for x in range(n):
    roll = file.readline().split()
    a = int(roll[0])
    d = int(roll[1])
    if a < d:
        antonia = antonia - d
    elif d < a:
        david = david - a
    print("roll is " + str(a) + " and " + str(d)
          + " => antonia has " + str(antonia)
          + " points and david has "
          + str(david) + " points")
