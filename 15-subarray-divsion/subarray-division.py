n = int(input())

s = list(map(int, input().strip().split()))

first_multiple_input = input().rstrip().split()
d, m = int(first_multiple_input[0]), int(first_multiple_input[1])


possible_checks = n - m + 1

result = 0
for i in range(possible_checks):
    if sum(s[i:i+m]) == d:
        result += 1


print(result)
