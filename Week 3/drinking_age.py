#Determining current age
year = int(input("What is your year of birth? "))
age = (2021 - year)
#Age determined, now checking whether they are 18 or over
print ('You are ',age )
if age >= 18:
    print ('Come in and have a drink')
else:
    print ('Go away. Child')