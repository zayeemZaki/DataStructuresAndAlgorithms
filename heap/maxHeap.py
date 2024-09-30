arr = [2, 6, 7, 3, 4, 8]

maxHeap = []

for element in arr:
    maxHeap.append(element)
    index = len(maxHeap)-1
    while maxHeap[index//2] < maxHeap[index]:
        maxHeap[index//2], maxHeap[index] = maxHeap[index], maxHeap[index//2]
        index = index//2


print(maxHeap)



i=0
while i < len(maxHeap):
    maxHeap[0], maxHeap[len(maxHeap)-(i+1)] = maxHeap[len(maxHeap)-(i+1)], maxHeap[0]

    j=0
    while (j*2 < len(maxHeap)-(i+1) and maxHeap[j] < maxHeap[j*2]) or (j*2+1 < len(maxHeap)-(i+1) and maxHeap[j] < maxHeap[j*2+1]):
        if maxHeap[j] < maxHeap[j*2]:
            maxHeap[j], maxHeap[j*2] = maxHeap[j*2], maxHeap[j]
            j = j*2
        elif maxHeap[j] < maxHeap[j*2+1]:
            maxHeap[j], maxHeap[j*2+1] = maxHeap[j*2+1], maxHeap[j]
            j = j*2+1

    i+=1

print(maxHeap)
