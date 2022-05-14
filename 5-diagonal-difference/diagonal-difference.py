lines = int(input())

arr = []

for _ in range(lines):
    arr.append(list(map(int, input().rstrip().split())))


left_to_write = 0
write_to_left = 0

for i in range(lines):
    left_to_write += arr[i][i]
    write_to_left += arr[i][-i - 1]


print(abs(left_to_write - write_to_left))
