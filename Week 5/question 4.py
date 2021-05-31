name = input("Please enter your full name: ")
names = name.split()
initals=""
for i in range(len(names)):
    initals+=names[i][0]
print("names:",name)
print("Initals:",initals)