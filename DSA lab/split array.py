# Write a python program to split an existing array in two specific length
# Existing array
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lengths of the two sub-arrays
length1 = 3
length2 = 6

# Check if the lengths are valid
if length1 + length2 == len(my_array):
    # Split the array into two sub-arrays
    sub_array1 = my_array[:length1]
    sub_array2 = my_array[length1:length1 + length2]
    print("Sub-Array 1:", sub_array1)
    print("Sub-Array 2:", sub_array2)
else:
    print("Invalid lengths. Cannot split the array.")

# Print the original array
print("Original Array:", my_array)
