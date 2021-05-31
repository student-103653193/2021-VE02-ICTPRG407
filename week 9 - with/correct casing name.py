file1 = open ('names.text','r')
lines = file1.readlines()
print(lines)
new_list = []
for name in lines:
    new_list.append(name.title())
print(new_list)
outfile = open("names-formatted.text","w")
outfile.writelines(new_list)
outfile.close
