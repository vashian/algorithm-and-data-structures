def get_digit(num: int, i: int):
    return num // 10 ** i % 10


print(get_digit(1234, 234))
