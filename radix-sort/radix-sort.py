import math


def get_digit(num: int, i: int) -> int:
    return num // 10 ** i % 10


def count_digit(num: int) -> int:
    return len(str(num))


def count_digit_math(num: int) -> int:
    if num == 0:
        return 1

    return int(math.log10(num)) + 1


def most_digits(nums: list) -> int:

    max_digits = 0
    for num in nums:
        max_digits = max(max_digits, count_digit_math(num))

    return max_digits


def radix_sort(nums: list) -> list:
  max_digit_count = most_digits(nums)

  for i in range(max_digit_count):
    digit_buckets = [ [], [], [], [], [], [], [], [], [], []]

    for n in range(len(nums)):
      digit_buckets[get_digit(nums[n], i)].append(nums[n])
    
    nums = [ item for elem in digit_buckets for item in elem]

  return nums


if __name__ == "__main__":
  nums = [23, 345, 5467, 12, 2345, 9852]

  result = radix_sort(nums)

  print(result)
