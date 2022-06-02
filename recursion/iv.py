result = []


def helper(helper_arr: list):

    if len(helper_arr) == 0:
        return

    if helper_arr[0] % 2 != 0:
        result.append(helper_arr[0])

    helper(helper_arr[1:])

    return result


def collect_odd_values(arr: list):
    return helper(arr)


print(collect_odd_values([1, 2, 3, 4, 5, 6, 7, 8, 9]))
