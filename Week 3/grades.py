#Simon Trinh, Seeing your grade
grade = float(input("Enter your grade: "))
if (grade >= 90 and grade <=100):
    print("High Distinction")
elif(grade >= 80 and grade <=89):
    print("Distinction")
elif(grade >=70 and grade <=79):
    print("Credit")
elif(grade >=60 and grade <=69):
    print("Pass")
elif(grade >=0 and grade <=59):
    print("Fail")
else:
    print ("Incorrect amount entered")
