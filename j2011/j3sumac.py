previous = eval(input())
current = eval(input())
print(previous, end=" ")
print(current, end=" ")
count = 2
while previous >= current and previous >= 0 and current >= 0:
    count = count + 1
    next = previous - current
    previous = current
    current = next
    print(next, end=" ")
print("= " + str(count) + " terms")
