a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
if a == b == c == d:
    print("Fish At Constant Depth")
elif a < b < c < d:
    print(str(a) + " < " + str(b) + " < " + str(c) + " < " + str(d) + " means Fish Rising")
elif a > b > c > d:
    print(str(a) + " > " + str(b) + " > " + str(c) + " > " + str(d) + " means Fish Diving")
else:
    print("No Fish")

