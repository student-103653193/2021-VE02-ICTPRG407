num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
total = num1 + num2
outfile = open("totalsum.text","w")
outfile.write(str(total))
outfile.close()

totals = open("totalsum.text", "r")
contents = totals.read()
print("The total is: " + contents)
