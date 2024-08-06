# Determine the frequency of a given element in an existing array
def find_frequency(arr, element):
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count

my_list = [1, 2, 3, 4, 5, 1, 2, 3]

element_to_find = 2

frequency = find_frequency(my_list, element_to_find)

print(f"The frequency of {element_to_find} in the list is {frequency}")