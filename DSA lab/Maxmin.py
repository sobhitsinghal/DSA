def find_max_min(arr, low, high):
    # If there is only one element
    if low == high:
        return arr[low], arr[low]

    # If there are two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # If there are more than two elements
    mid = (low + high) // 2
    max1, min1 = find_max_min(arr, low, mid)
    max2, min2 = find_max_min(arr, mid + 1, high)

    return max(max1, max2), min(min1, min2)


# Example usage
arr = [1, 3, 7, 5, 9, 13, 18 ,20]
max_element, min_element = find_max_min(arr, 0, len(arr) - 1)
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")
