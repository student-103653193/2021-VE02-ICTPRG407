# counter = 0
# total = 0
# number = 0
# while number >= 0:
#     number = int(input("Enter a positive number\nor a negative to exit: "))
#     total += number
#     counter += 1
# average = total / counter
# print(average)

punctuation = "#()*+,-/:;<=>? \\@^_`{|}~[]"
print()
print("***")
print()
input_string = input("Enter a text string: ")
output_string = ' '
space_flagged = False
for char in input_string:
    if char == '.':
        print(output_string)
        output_string = ' '
    elif char not in punctuation:
        output_string += char
        space_flagged = False
else:
    if not space_flagged:
        output_string += ' '
        space_flagged = True
print(output_string)
print()
print("***")
print()