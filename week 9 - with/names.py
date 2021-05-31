names = []
name = input("Please enter a name: ")
while (name != ''):
    names.append(name + "\n")
    name = input("Please enter a name: ")
outfile = open("allnames.text","w")
outfile.writelines(names)
outfile.close
