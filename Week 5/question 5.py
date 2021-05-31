nums = []
num = input("Enter some numbers (Press X to stop): ")
while (num != 'x'):
    nums.append(num)
    num = input("Enter some numbers (Press X to stop): ")
print(nums)