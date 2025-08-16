#Problem Statement:

# Create a list named fruits that contains below five different fruit names (strings).
# "apple", "banana", "cherry", "date", "elderberry"
# Print the first and last elements of the list.
# Use slicing to print the second and third fruits from the list.

# Expected Result:
# First fruit: apple
# Last fruit: elderberry
# Fruits from index 1 to 2: ['banana', 'cherry']

#Code:

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


print("Fruits from index 1 to 2:", fruits[0:3])

# Explore tuple

# Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.
# "Rahul", 25, 5.9
# Print the second element of the tuple.

person = ("Rahul", 25, 5.9)
print("Age:", person[1])