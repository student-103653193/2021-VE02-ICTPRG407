# def isAuthorized():
#   username = input("Enter your username: ").strip()
#   password = input("Enter your password: ").strip()

#   with open("logins.text", "r") as f:
#     for line in f:
#       loginInfo = line.strip().split(",")
#       print(loginInfo)
#       if username == loginInfo[0] and password == loginInfo[1]:
#         return True
#     return False

# if isAuthorized():
#   input("Access Granted! \t Press any key to continue: ")
# else:
#   input("Access Denied")
import getpass

credentials = {}                                                            
with open('logins.text', 'r') as f:                                       
    for line in f:  
        username, delim, password = line.strip().partition(':')                        
        credentials[username] = password.split(';')   

while True:
    username = input("Please enter your username: ")                     
    password = getpass.getpass("Please enter your password: ")      
    if username in credentials and password == credentials[username][0]:
        print ("Access Granted")  
        break
    else:
        print ("Login incorrect!")