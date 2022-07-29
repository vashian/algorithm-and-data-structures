def bubble_sort(nums: list) -> list:

    for i in range(len(nums), 0, -1):
        noSwap = True
        for j in range(i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                noSwap = False
        if noSwap:
            print("No swap")
            break
    return nums


if __name__ == "__main__":

    nums = [8, 1, 2, 3, 4, 5, 6, 7]

    result = bubble_sort(nums)

    print(result)
