def binary_search(arr: list, target: int):

    (left, right) = (0, len(arr) - 1)

    while left <= right:

        mid = (left + right) // 2

        if target == arr[mid]:
            return mid

        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return mid if arr[mid] == target else -1


if __name__ == "__main__":

    target = 7
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    index = binary_search(nums, target)

    print(f"Element found at index: {index}") if index != - \
        1 else print(f"Element not found")
