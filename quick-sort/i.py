def swap(arr: list, i: int, j: int) -> None:
    """
    Swaps the elements at index i and j in the list.
    """
    arr[i], arr[j] = arr[j], arr[i]


def pivot(nums: list, start: int, end: int) -> int:
    """
    Returns the index of the pivot element in the list.
    """

    pivot = nums[start]
    swap_index = start

    for i in range(start + 1, end):
        if nums[i] < pivot:
            swap_index += 1
            swap(nums, swap_index, i)

    swap(nums, start, swap_index)

    return swap_index


def quick_sort(nums: list, start: int, end: int) -> list:
    """
    Returns a sorted list.
    """
    if start < end:
        pivot_index = pivot(nums, start, end)

        # Sort the left side of the pivot.
        quick_sort(nums, start, pivot_index)

        # Sort the right side of the pivot.
        quick_sort(nums, pivot_index + 1, end)

    return nums


if __name__ == "__main__":

    nums = [4, 8, 2, 1, 5, 7, 6, 3]

    result = quick_sort(nums, 0, len(nums))

    print(result)
