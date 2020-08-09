def linear_search(arr, target):
    # Your code here
    for element in array:
        if element == target:
            return True

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(array, target):

    # Your code here
    start = 0
    end = len(array) - 1

    found = False

    while not found:
        middle = (start + end) // 2

        if array[middle] == target:
            found = True
        else:
            if value < array[middle]:
                end = middle - 1
            else:
                start = middle + 1
    return found

    return -1  # not found
