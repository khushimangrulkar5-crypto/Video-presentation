def binary_search(arr, first, last, num):
    # If the search range is invalid, element is not found
    if first > last:
        return -1
    
    # Find the middle index of the current range
    mid = (first + last) // 2
    
    # Check if the middle element is the target
    if num == arr[mid]:
        return mid
    
    # If target is greater, search in the right half
    elif num > arr[mid]:
        return binary_search(arr, mid + 1, last, num)
    
    # If target is smaller, search in the left half
    else:
        return binary_search(arr, first, mid - 1, num)


# Take input from user and convert it into a list of integers
arr = list(map(int, input("Enter the elements (space-separated): ").split()))

# Take the number to search
num = int(input("Enter the number to search: "))

# Call the function
result = binary_search(arr, 0, len(arr) - 1, num)

# Display result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
