# def PrintBoxByWidth(height, width):
#     # if height is even number, add 1 to make it becomes odd number
#     # if not height & 1: # this is to demonstrate bitwise operation to check for even number
#     if (height % 2 == 0):
#         height += 1
#     middle_row = height // 2 # or use bitwise operator height >> 1 
    
#     for row in range(height):
#         for col in range(width):
#             if row in (0, height-1) or col in(0,width-1):
#                 print("x", end='')
#             elif row == middle_row:
#                 print("o", end='')
#             else:
#                 print(" ", end='')
#         print("")

# PrintBoxByWidth(5,60)

myFile = open("allnames.text", "r")
names = open("names.txt", "w")
info = myFile.readline().strip()

for line in myFile:
    line = line.strip()
    value = line.split(",")
    if(len(value[0]) > 3):
        names.write(value[0].title())
        names.write("\n")
    print("Name: " + value[0])

names.close()
myFile.close()