h = eval(input())
M = eval(input())
t = 1
A = -6 * t * t * t * t + h * t * t * t + 2 * t * t + t
print("time=" + str(t) + " Altitude=" + str(A))
while t < M and A > 0:
    t = t + 1
    A = -6 * pow(t, 4) + h * pow(t, 3) + 2 * t * t + t
    print("time=" + str(t) + " Altitude=" + str(A))
if A > 0:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon touches ground at time:", t)
