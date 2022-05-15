# First solution

array_length = int(input())

array_content = list(map(int, input().split()))

only_positive = [num for num in array_content if num >= 1]
only_negative = [num for num in array_content if num <= -1]

zero = len(array_content) - (len(only_positive) + len(only_negative))

print(format(len(only_positive) / len(array_content), '.6f'))
print(format(len(only_negative) / len(array_content), '.6f'))
print(format(zero / len(array_content), '.6f'))

# Second solution

# array_length = int(input())
# array_content = [1 if int(num) > 0 else -1 if int(num)
#                  < 0 else 0 for num in input().split()]

# print("{0:.6f}".format(array_content.count(1)/array_length))
# print("{0:.6f}".format(array_content.count(-1)/array_length))
# print("{0:.6f}".format(array_content.count(0)/array_length))
