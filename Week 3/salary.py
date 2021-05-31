print ("Welcome to the Loan Checker Machine")
salary = float(input("Firstly, please enter your salary: $"))
if (salary < 50000):
    print ("Sorry your income is to low")
else:
    time = float(input("Great! Now please enter how long have you worked for: "))
    if (time < 3):
        print ("Sorry, you haven't worked long enough for a loan to be approved")
    else:
        print ("Your loan has been approved")

