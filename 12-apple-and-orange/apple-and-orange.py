s_and_t = list(map(int, input().strip().split()))

apple_and_orange = list(map(int, input().strip().split()))

number_of_apples_and_oranges = list(map(int, input().strip().split()))

apples_location = list(map(int, input().strip().split()))
orange_location = list(map(int, input().strip().split()))

result = [0, 0]
for i in range(sum(number_of_apples_and_oranges)):

    if (i < len(apples_location)):
        x = apple_and_orange[0] + apples_location[i]

        if x >= s_and_t[0] and x <= s_and_t[1]:
            result[0] += 1

    if (i < len(orange_location)):
        y = apple_and_orange[1] + orange_location[i]

        if y >= s_and_t[0] and y <= s_and_t[1]:
            result[1] += 1

print(*result, sep="\n")
