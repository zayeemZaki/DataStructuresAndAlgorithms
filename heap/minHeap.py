arr = [3, 7, 1, 9, 4, 7]

minHeap = []

for element in arr:
    minHeap.append(element)
    index = len(minHeap)-1
    while minHeap[index//2] > minHeap[index]:
        minHeap[index//2], minHeap[index] = minHeap[index], minHeap[index//2]
        index = index//2

print(minHeap)   