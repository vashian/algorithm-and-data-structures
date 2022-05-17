from array import array


array_number = sorted(list(map(int, input().split())))

print(sum(array_number[:-1]), sum(array_number[1:]))
