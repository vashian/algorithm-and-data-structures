def get_ceil(nums: list, target: int) -> int:

    (left, right) = (0, len(nums) - 1)

    ceil = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return nums[mid]

        elif target < nums[mid]:
            ceil = nums[mid]
            right = mid - 1

        else:
            left = mid + 1

    return ceil


def get_floor(nums: list, target: int) -> int:

    (left, right) = (0, len(nums) - 1)

    floor = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return nums[mid]

        elif target < nums[mid]:
            right = mid - 1

        else:
            floor = nums[mid]
            left = mid + 1

    return floor


if __name__ == "__main__":
    nums = [1, 4, 6, 8, 9]

    for i in range(max(nums) + 2):
        print(
            f"Number {i} -> ceil is {get_ceil(nums, i)}, floor is {get_floor(nums, i)}")
