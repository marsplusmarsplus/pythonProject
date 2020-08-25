file = open("j3.1.in", "r")
word = file.readline()
print(str(word)+" => ", end="")
for letter in word:
    print(str(letter), end="")
    if str(letter) == "b":
        print("ac", end="")
    if str(letter) == "c":
        print("ad", end="")
    if str(letter) == "d":
        print("ef", end="")
    if str(letter) == "f":
        print("eg", end="")
    if str(letter) == "g":
        print("eh", end="")
    if str(letter) == "h":
        print("ij", end="")
    if str(letter) == "j":
        print("ik", end="")
    if str(letter) == "k":
        print("il", end="")
    if str(letter) == "l":
        print("im", end="")
    if str(letter) == "m":
        print("on", end="")
    if str(letter) == "n":
        print("op", end="")
    if str(letter) == "p":
        print("oq", end="")
    if str(letter) == "q":
        print("or", end="")
    if str(letter) == "r":
        print("os", end="")
    if str(letter) == "s":
        print("ut", end="")
    if str(letter) == "t":
        print("uv", end="")
    if str(letter) == "v":
        print("uw", end="")
    if str(letter) == "w":
        print("ux", end="")
    if str(letter) == "x":
        print("uy", end="")
    if str(letter) == "y":
        print("uz", end="")
    if str(letter) == "z":
        print("uz", end="")
