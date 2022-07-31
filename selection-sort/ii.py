def find_smallest(nums: list) -> int:

  smallest = nums[0]
  smallest_index = 0

  for i in range(1, len(nums)):
    if nums[i] < smallest:
      smallest = nums[i]
      smallest_index = i
  return smallest_index

def selection_sort(nums: list) -> list:
  
  result = []

  for i in range(len(nums)):

    result.append(nums.pop(find_smallest(nums)))

  return result


if __name__ == "__main__": 
    nums = [8, 1, 2, 3, 4, 5, 6, 7]

    result = selection_sort(nums)

    print(result)