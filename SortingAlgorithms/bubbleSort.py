
arr = [ 5, 9, 4, 3, 1]

n = len(arr)

for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if swapped == False:
        break

for elements in arr:
    print(elements)

"""
Time Complexity = O(n^2)
Space complexity = O(1)
"""