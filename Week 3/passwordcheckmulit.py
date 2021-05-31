usera = "bob"
passa = "password1234"
userb = "fred"
passb = "happyPass122"
userc = 'lock'
passc = "passwithlock44"
login = str(input('Enter Username: '))
if login == usera:
    pass1 = str(input('Enter Password: '))
    if pass1 == passa:
        print ('Access Granted')
    else:
        print ('Invalid Password')
else:
        if login == userb:
            pass2 = str(input('Enter Password: '))
            if pass2 == passb:
                        print ('Access Granted')
            else:
                        print ('Invalid Password')
        else:
            if login == userc:
                pass2 = str(input('Enter Password: '))
                if pass2 == passc:
                        print ('Access Granted')
                else:
                        print ('Invalid Password')
