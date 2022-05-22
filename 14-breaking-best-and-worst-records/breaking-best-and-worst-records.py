from unittest import result


number_of_records = int(input())

records = list(map(int, input().strip().split()))


minimum = records[0]
maximum = records[0]

result = {max: 0, min: 0}

for record in records:
    if record > maximum:
        maximum = record
        result[max] += 1
    elif record < minimum:
        minimum = record
        result[min] += 1

print(result[max], result[min])
