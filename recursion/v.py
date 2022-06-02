def collect_odd_values(arr: list):

    new_arr = []

    if len(arr) == 0:
        return new_arr

    if arr[0] % 2 != 0:
        new_arr.append(arr[0])

    new_arr = new_arr + collect_odd_values(arr[1:])

    return new_arr


print(collect_odd_values([1, 2, 3, 4, 5, 6, 7, 8, 9]))
