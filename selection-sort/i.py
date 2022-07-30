def selection_sort(nums: list) -> list:

    for i in range(len(nums)):
        lowest = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest]:
                lowest = j

        if lowest != i:
            nums[i], nums[lowest] = nums[lowest], nums[i]

    return nums


if __name__ == "__main__":

    nums = [8, 1, 2, 3, 4, 5, 6, 7]

    result = selection_sort(nums)

    print(result)
