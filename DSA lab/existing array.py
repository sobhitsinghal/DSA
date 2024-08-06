#Write a Python program to insert an element to a specific location in  an existing array
def insert_element(arr, element, index):
    if index < 0 or index > len(arr):
        print("Invalid index")
        return
    
    arr.insert(index, element)
    print("Element inserted successfully!")

# Example array
my_array = [1, 2, 3, 4, 5]

# Element to insert
new_element = 10

# Index where the element should be inserted
insert_index = 2

# Insert the element
insert_element(my_array, new_element, insert_index)

print("Updated Array:", my_array)