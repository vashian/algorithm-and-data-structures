

def bubble_sort(nums: list) -> list:
    for i in range(len(nums), 0, -1):
        for j in range(i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


if __name__ == "__main__":

    nums = [37, 45, 29, 8]

    result = bubble_sort(nums)

    print(result)
