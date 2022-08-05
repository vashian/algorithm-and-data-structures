def merge(arr1: list, arr2: list) -> list:
    result = []
    arr1Index, arr2Index = 0, 0

    while arr1Index < len(arr1) and arr2Index < len(arr2):

        if arr1[arr1Index] < arr2[arr2Index]:
            result.append(arr1[arr1Index])
            arr1Index += 1

        else:
            result.append(arr2[arr2Index])
            arr2Index += 1

    while arr1Index < len(arr1):
        result.append(arr1[arr1Index])
        arr1Index += 1

    while arr2Index < len(arr2):
        result.append(arr2[arr2Index])
        arr2Index += 1

    return result


if __name__ == "__main__":

    arr1 = [1, 10, 50]
    arr2 = [2, 10, 99, 100]

    result = merge(arr1, arr2)

    print(result)
