file = open("j3.5.in", "r")
word = file.readline()
consonant = "bcdfghjklmnpqrstvwxyz"
closestVowel = "aaeeeiiiiooooouuuuuuu"
nextConsonant = "cdfghjklmnpqrstvwxyzz"
newWord = ""
for i in range(len(word)):
    j = consonant.find(word[i])
    newWord = newWord + word[i]
    if j > -1:
        newWord = newWord + closestVowel[j] + nextConsonant[j]
print(newWord)
