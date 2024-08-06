# Existing array
my_array = [1, 2, 3, 4, 2, 5, 2, 6, 2, 7]

# Element to find the frequency of
element_to_find = 2

# Initialize a variable to count the frequency
frequency = 0

# Iterate through the array
for element in my_array:
    if element == element_to_find:
        frequency += 1

# Print the frequency of the element
print(f"The frequency of {element_to_find} in the array is {frequency}" )