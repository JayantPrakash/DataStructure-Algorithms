# Key idea: Track heap ordering and which element is kept at the root.
import heapq
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))
print(h)

# Compute or update the heapsort result for the supplied input.
def heapsort(iterable):
    h = []
    # Process each value from `iterable`.
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))


h = []
heapq.heappush(h, 5)
heapq.heappush(h, 7)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(heapq.heappop(h))
print(h)
