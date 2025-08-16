# #Problem Statement:
# Objective: Calculate the average of three numbers.

# Instructions:
# Create a function called CalculateAverage that takes three parameters: num1, num2, and num3.
# Use the numbers 10,20,30 as input to functions
# The function should return the average of these three numbers.

# Expected Output:
# The average of 10, 20, and 30 is 20.0

#Code
def CalculateAverage(num1, num2, num3):
    average = (num1 + num2 + num3)/3
    return(average)
    
averagecheck = CalculateAverage(10,20,30)
print("The average of 10, 20, and 30 is", averagecheck)