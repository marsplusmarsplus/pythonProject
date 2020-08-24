def distinct(y):
    s = str(y)
    for digit in s:
        if s.count(digit) > 1:
            return False
    return True
file = open("s1.15.in", 'r')
year = int(file.readline()) + 1
while not distinct(year):
    year = year + 1
print(year)
