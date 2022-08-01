def insertion_sort(nums: list) -> list:

  for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and key < nums[j]:
      nums[j+1] = nums[j]
      j -= 1

    nums[j + 1] = key

  return nums


if __name__ == "__main__":

  nums = [9, 5, 1, 4, 3]

  result = insertion_sort(nums)

  print(result)