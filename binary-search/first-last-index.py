def first_index(nums: list, target: int):

    (left, right) = (0, len(nums) - 1)

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            result = mid
            right = mid - 1

        elif target < nums[mid]:
            right = mid - 1

        else:
            left = mid + 1
    return result


def last_index(nums: list, target: int):

    (left, right) = (0, len(nums) - 1)

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            result = mid
            left = mid + 1

        elif target > nums[mid]:
            left = mid + 1

        else:
            right = mid - 1
    return result


if __name__ == "__main__":
    nums = [2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    target = 9

    f_index = first_index(nums, target)
    l_index = last_index(nums, target)

    if f_index != -1 and l_index != -1:
        print(f"he first occurrence of {target} is at index {f_index}")
        print(f"The last occurrence of {target} is at index {l_index}")
    else:
        print("Element not found in the array")
