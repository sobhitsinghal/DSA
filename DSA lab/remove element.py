# Write a python program to remove an element from a specific location of an existing array
# Existing array
my_array = [1, 2, 3, 4, 5]

# Index of the element to remove
index_to_remove = 2  # This will remove the element at index 2 (3 in this case)

# Check if the index is valid
if 0 <= index_to_remove < len(my_array):
    # Remove the element at the specified index
    updated_array = my_array[:index_to_remove] + my_array[index_to_remove + 1:]
    print("Updated Array:", updated_array)
else:
    print("Invalid index. Element not removed.")

# Print the updated array
print("Original Array:", my_array)
