# given = ""
# last = ""
# age = ""
# year = 2020
# while (given == ""):
#     given = input("Please enter your First name:")
#     given = given.strip()
# last = str(input("Please enter your Last name: "))
# last = last.strip()
# age = input("How old are you this year? ")
# age = (year - int(age) - 1)
# names = given.split()
# shortfirstname=""
# for i in range(len(names)):
#     shortfirstname+=names[i][0]
# if last == '':
#     print(shortfirstname.lower() + "@Huawow.io" + "|", given.lower() + "_" + str(age))
# else:
#     namess = (last[0])
#     print(shortfirstname.lower() + str(last.lower()) + "@Huawow.io" + "|", given.lower() + str(namess) + "_" + str(age))

# given = ""
# while (given == ""):
#     given = str(input("Please enter your First name:"))
#     given = given.strip()
# names = given.spilt()
# shortfirstname=""
# for i in range(len(names)):
#     shortfirstname+=names[i][0]
# print(shortfirstname.lower())
given = ""
last = ""
age = ""
year = 2021
while (given == ""):
    given = input("Please enter your First name:")
    given = given.strip()
last = str(input("Please enter your Last name: "))
last = last.strip()
age = input("How old are you this year? ")
age = (year - int(age) - 1)
names = given.split()
shortfirstname=""
for i in range(len(names)):
    shortfirstname+=names[i][0]
if last == '':
    given = given.replace(" ", "")
    print(shortfirstname.lower() + "@Huawow.io" + "|", given.lower() + "_" + str(age))
else:
    namess = (last[0])
    given = given.replace(" ", "")
    print(shortfirstname[0].lower() + str(last.lower()) + "@Huawow.io" + "|", given.lower() + str(namess).upper() + "_" + str(age))