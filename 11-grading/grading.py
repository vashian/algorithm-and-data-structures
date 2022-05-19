from unittest import result


result = []

for i in range(int(input())):

    grade = int(input())

    if grade < 38:
        result.append(grade)
        continue

    if (5 - (grade % 5)) < 3:
        grade = (5 - (grade % 5)) + grade

    result.append(grade)

print(*result, sep="\n")
