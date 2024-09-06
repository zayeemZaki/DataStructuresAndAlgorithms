arr = [13, 11, 12, 7, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j+1] = key

for element in arr:
    print(element)

"""
Time complexity = O(n^2)
Space Auxiliary = O(1)
"""