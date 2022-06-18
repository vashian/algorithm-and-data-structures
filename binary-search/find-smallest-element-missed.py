def miss_elem(nums: list, left=None, right=None):

    if left is None and right is None:
        (left, right) = (0, len(nums) - 1)

    if left > right:
        return left

    mid = (left + right) // 2

    if nums[mid] == mid:
        return miss_elem(nums, mid + 1, right)
    else:
        return miss_elem(nums, left, mid - 1)


if __name__ == "__main__":

    nums = [0, 1, 2, 3, 4, 5, 6]

    print('The smallest missing element is', miss_elem(nums))
