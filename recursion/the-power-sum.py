x = int(input())

n = int(input())


def power_sum(x: int, n: int, arr: list):

    s = sum(i**n for i in arr)

    if s == x:
        return 1

    else:
        result = 0
        y = arr[-1] + 1 if arr else 1

        while y**n + s <= x:
            result += power_sum(x, n, arr + [y])
            y += 1

        return result


print(power_sum(x, n, []))
