import heapq
heap = []
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#heapq.heapify(listForTree)             # for a min heap
# This experiment uses private heapq helpers; availability can vary by Python version.
heapq._heapify_max(listForTree)
heapq._heappop_max(listForTree) # pop from maxheap

print(listForTree)
# Tuple max-heap priority is the first value, with remaining tuple fields breaking ties.
heapq._heappush_max(heap, (5, (1,3)))
heapq._heappush_max(heap, (1, (2,3)))
heapq._heappush_max(heap, (2, (5,3)))
print("Items in the heap:")
# Iteration shows the heap's internal layout, not a sorted priority sequence.
for a in heap:
	print(a)
print("----------------------")
print("The smallest item in the heap:")
# For a max-heap this root is the largest, despite the printed label saying smallest.
print(heap[0])
print("----------------------")
print("Pop the smallest item in the heap:")
# This is the min-heap pop operation applied to max-heap storage, so the heap conventions are inconsistent.
heapq.heappop(heap)
# Iteration shows the heap's internal layout, not a sorted priority sequence.
for a in heap:
	print(a)
