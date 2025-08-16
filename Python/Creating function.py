# #Problem Statement:

# Objective: Create a function that greets the user.

# Instructions:
# Write a function called GreetUser that takes a single argument username.
# The function should print "Hello, [username]! Welcome to the Python course."
# Call the function with username "John".


# Expected Output:
# Hello, John! Welcome to the Python course.

#Code:
def GreetUser(username):
    return(f"Hello, {username}! Welcome to the Python course.")
    
user = GreetUser("John")
print(user)