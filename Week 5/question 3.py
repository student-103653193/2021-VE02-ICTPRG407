value = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
total = 0
i = 0
while (i <len(value)):
    total = total + value[i]
    i += 1
print ("The total is, ", total)
avg = total / len(value)
print ('The average is', avg)
print('The largest number is: ',max(value))
