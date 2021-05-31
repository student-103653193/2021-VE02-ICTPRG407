all = []
repeat = []
num = input("Enter some numbers (Press X to stop): ")
while (num != 'x'):
    all.append(num)
    num = input("Enter some numbers (Press X to stop): ")
print(all)

for i in range(len(all)):
    for x in range(i+1,len(all)):
            if all[i] == all[x]:
                repeat.append(all[i])
                break
print (sorted(set(repeat))) #set makes it only appears once