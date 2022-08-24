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


print(most_digits([1, 11, 111, 982734]))
