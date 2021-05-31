given = "" 
last = "" 
age = ""
year = 2021
given = input("Please enter your First name:")
while (given != ''):
  last = str(input("Please enter your Last name: "))
  given = given.strip() 
  last = last.strip()
  while True: 
    try:
      age = int(input('How old are you currently? '))
    except ValueError:
      print('Invalid input detected')
      continue
    break
  age = (year - int(age) - 1)
  names = given.split()
  shortfirstname=""
  for i in range(len(names)):
      shortfirstname+=names[i][0]
  if last == '':
      given = given.replace(" ", "")
      last = last.replace(" ","")
      print("Your username and password is as follows:")
      print(shortfirstname.lower() + "@Huawow.io" + "|", given.lower() + "_" + str(age))
      shortfirstname.lower() + "@Huawow.io" + "|", given.lower() + "_" + str(age)
  else:
      namess = (last[0])
      given = given.replace(" ", "")
      last = last.replace(" ","")
      print("Your username and password is as follows:")
      print(shortfirstname[0].lower() + str(last.lower()) + "@Huawow.io" + "|", given.lower() + str(namess).upper() + "_" + str(age))
      shortfirstname[0].lower() + str(last.lower()) + "@Huawow.io" + "|", given.lower() + str(namess).upper() + "_" + str(age)
  given = input("Please enter your First name:")


    