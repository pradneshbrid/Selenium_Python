# #Problem Statement:
# Handle Tuple modification exception with Try Catch
# Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.

# "Rahul", 25, 5.9

# Print the second element of the tuple.

# Attempt to change the name in the tuple to a different name and explain why this will or will not work.


#Code
person = ("Rahul", 25, 5.9)

print("Age:", person[1])  

try:
    person[0] = "Amit"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")