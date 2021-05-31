# date = (input("Please enter Date?"))
# month = (input("Please enter Month? "))
# year = (input("Please enter Year? "))
# full = date + "/" + month + "/" + "/" + year
# print (full)

date = input("Please enter the date in the form dd/mm/yy: ")
se = date.split("/")
print("Date: ", se[0])
print("Month: ", se[1])
print("Year: ", se[2])
