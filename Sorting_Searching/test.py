# Key idea: Track how values move toward their final sorted positions.
import heapq
heap = []
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)
heapq._heappop_max(listForTree) # pop from maxheap

print(listForTree)
heapq._heappush_max(heap, (5, (1,3)))
heapq._heappush_max(heap, (1, (2,3)))
heapq._heappush_max(heap, (2, (5,3)))
print("Items in the heap:")
# Process each value from `heap`.
for a in heap:
	print(a)
print("----------------------")
print("The smallest item in the heap:")
print(heap[0])
print("----------------------")
print("Pop the smallest item in the heap:")
heapq.heappop(heap)
# Process each value from `heap`.
for a in heap:
	print(a)
