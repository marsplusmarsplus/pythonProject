file = open("j1.9.in", "r")
month = int(file.readline())
day = int(file.readline())
if month == 2 and day == 18:
    print("Special")
elif month < 2 or (month == 2 and day < 18):
    print("Before")
else:
    print("After")
