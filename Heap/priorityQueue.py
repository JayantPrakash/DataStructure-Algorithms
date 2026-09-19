import heapq
# heapq removes the smallest priority first; tuple ties fall through to the task text.
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))
# A heap's backing list is only partially ordered; it is not the priority-sorted sequence.
print(h)

# Push all input values into a separate min-heap, then pop them in ascending order.
# O(n log n) time and O(n) extra space; the supplied iterable is not rearranged.
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    # Repeated minimum extraction, rather than iterating the heap, produces sorted output.
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))


h = []
heapq.heappush(h, 5)
heapq.heappush(h, 7)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(heapq.heappop(h))
print(h)
