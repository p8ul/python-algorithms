def binary_search(array, left, right, x):
    # Check base case
    if right >= left:

        mid = left + (right - left) // 2

        # If element is present at the middle itself
        if array[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif array[mid] > x:
            return binary_search(array, left, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search(array, mid + 1, right, x)

    else:
        # Element is not present in the array
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr) - 1, x)
print("%d is present at index % d" % (result, x)) if result != -1 else print('Element not found')
