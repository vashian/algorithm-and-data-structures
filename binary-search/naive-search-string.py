from itertools import count


def naive_search(long: str, short: str):
    count = 0
    for i in range(len(long)):
        for j in range(len(short)):
            if short[j] != long[i+j]:
                break
            if j == len(short) - 1:
                count += 1
    return count


print(naive_search("lsumorem ipsum", "sum"))
