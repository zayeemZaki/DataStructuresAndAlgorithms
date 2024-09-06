arr = [15, 16, 9, 8, 1]

for i in range(len(arr) - 1):

    smallest_index = i

    for j in range(i + 1, len(arr)):
        if arr[smallest_index] > arr[j]:
            smallest_index = j

    arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

for i in range(len(arr)):
    print(arr[i])

"""
Time complexity = O(n^2)
Space complexity = O(1)

"""
