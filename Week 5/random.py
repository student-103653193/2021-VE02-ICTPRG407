value = ""
numlist = []
while (value != 'x'):
    value = input("Pleae enter some numbers. Press X to stop")
    if (value != 'x'):
        numbList.append(numlist)
repeatedNumbers = []
x = 0
for i in range(len(numbList)):
    for x in range(len(numbist)):
        if (numlist[int(i)] == numbList[x]):
            repeatedNumbers.append(numlist[i])
            break
print(repeatedNumbers)