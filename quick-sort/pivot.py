def swap(arr: list, i: int, j: int) -> None:
    """
    Swaps the elements at index i and j in the list.
    """
    arr[i], arr[j] = arr[j], arr[i]


def pivot(nums: list) -> int:
    """
    Returns the index of the pivot element in the list.
    """
    start = 0
    end = len(nums)

    pivot = nums[start]
    swap_index = start

    for i in range(start + 1, end):
        if nums[i] < pivot:
            swap_index += 1
            swap(nums, swap_index, i)

    swap(nums, start, swap_index)

    return swap_index


if __name__ == "__main__":

    nums = [4, 8, 2, 1, 5, 7, 6, 3]

    result = pivot(nums)

    print(result)
