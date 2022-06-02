def count_down(num: int):
    if num <= 0:
        print("All Done!")
        return
    print(num)
    num -= 1
    count_down(num)


count_down(5)
