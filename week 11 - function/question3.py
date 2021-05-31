# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya

# Write the function between the START and END tags
# START

def FibonacciAdder(n) :
    if (n < 0) :
        return 0
  
    fibo =[0] * (n+1)
    fibo[1] = 1
  
    # Initialize result
    sm = fibo[0] + fibo[1]
  
    # Add remaining terms
    for i in range(2,n) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        sm = sm + fibo[i]
         
    return sm

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
# print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
# print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
# print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))
print("Test 1 Passed: " + str(FibonacciAdder(2)))
print("Test 2 Passed: " + str(FibonacciAdder(5)))
print("Test 3 Passed: " + str(FibonacciAdder(10)))