sum = 0
num=(int(input("Enter some numbers (Press X to stop): ")))
while (num != 'x'):
    sum=sum+int(num)
    num = input("Enter some numbers (Press X to stop): ")
print(sum)