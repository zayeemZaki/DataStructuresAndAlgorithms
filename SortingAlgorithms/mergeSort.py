def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) / 2
    leftHalf = mergeSort(array[0:mid])
    rightHalf = mergeSort(array[mid:len(array)])

    return merge(leftHalf, rightHalf)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
