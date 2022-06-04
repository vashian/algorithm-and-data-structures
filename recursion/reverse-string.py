s = list(input())


def reverse_string(s: list):
    if len(s) == 1:
        return s
    else:
        return [s[-1]] + reverse_string(s[:-1])


print(reverse_string(s))
