def binary_search(arr: list, elem):
    start = 0
    end = len(arr) - 1
    middle = (start + end) // 2

    while arr[middle] != elem and start <= end:
        if elem < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

        middle = (start + end) // 2

    return middle if arr[middle] == elem else -1


result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
print(result)
