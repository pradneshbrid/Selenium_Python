#Problem Statement:

#Create three variables: age, height, and favorite_color. Assign them values 25, 5.9, blue:
#age: an integer (e.g., 25)
# height: a float (e.g., 5.9)
# favorite_color: a string (e.g., "blue")
# Use the print function to display each variable and its type using the type() function.

# Expected Result:

# Age: 25 | Type: <class 'int'>
# Height: 5.9 | Type: <class 'float'>
# Favorite Color: blue | Type: <class 'str'>

#Code:

age = 25
height = 5.9
favorite_color = "blue"
age_type = type(age)
height_type = type(height)
fav_type = type(favorite_color)

print(f"Age: {age} | Type: {age_type}")
print(f"Height: {height} | Type: {height_type}")
print(f"Favorite Color: {favorite_color} | Type: {fav_type}")