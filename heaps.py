# created by arrays, used to find max/min min is default
import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 0)

# min value is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap)) # popping removes but prints all

print(minHeap)

# no max heaps but multiply by -1 when push and pop
maxHeap = []
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, -5)
heapq.heappush(maxHeap, -3)

print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

#turning array into a heap
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))