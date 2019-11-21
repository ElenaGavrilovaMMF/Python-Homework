#Вариант 4

f1 = open('F1.txt', 'r')
f2 = open('F2.txt', 'w')
massWords = []
maxWord = ""
for line in f1:
    if ' ' not in line:
        f2.write(line)
        newLine = line.replace("\n", "")
        if len(newLine) > len(maxWord):
            maxWord = newLine
        massWords.append(newLine)
f1.close()
f2.close()
print(maxWord)
