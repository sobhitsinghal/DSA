#Write a Python program to append an element in an existing array
def append_element(arr, element):
    arr.append(element)
    print("Element appended successfully!")

# Example array
my_array = [1, 2, 3, 4, 5]

# Element to append
new_element = 6

# Append the element
append_element(my_array, new_element)

print("Updated Array:", my_array)
