# Write the function between the START and END tags
# START
def AddTwoNumbers(a, b):  
    sum = a + b
    return sum

#DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))
print("Test 3 Passed: " + str(AddTwoNumbers(9, 0) != 10))