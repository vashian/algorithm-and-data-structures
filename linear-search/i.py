def linear_search(arr: list, val):
    for i, v in enumerate(arr):
        if v == val:
            return i
    return -1


result = linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)

print(result)
