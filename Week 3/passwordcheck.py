#Basic Username and password checker
#storing the correct username and password
usera = "bob"
passa = "password1234"
#checking login
login = str(input('Enter Username: '))
if login == usera: #checking if username matches our username on file
    pass1 = str(input('Enter Password: '))
    if pass1 == passa: # checking if username entered matches password on file
        print ('Access Granted')
    else: #incorrect password entered
        print ('Invalid Password')
else: #If incorrect login is entered
    print ('Incorrect Login')
