import heapq
h = [10, 20, 15, 30, 40]
heapq.heapify(h)

"""
By deafult heap is stored as min heap, firmst element will be
minimum
"""
# Appending an element
heapq.heappush(h, 5)
print(h)

# Pop the smallest element from the heap
min = heapq.heappop(h)
print("Smallest:", min)
print(h)
print(h[0])

"""
Using Heap as a Max-Heap
By default, Python's heapq implements a min-heap.
To create a max-heap simply invert the values 
(store negative numbers).
"""

import heapq  
nums = [10, 20, 15, 30, 40]  

# Convert into a max-heap by inverting values  
max_heap = [-n for n in nums]  
heapq.heapify(max_heap)  

# Access largest element (invert sign again)  
print("Largest element:", -max_heap[0])

"""
Finding Largest and Smallest Elements
heapq.nlargest() and heapq.nsmallest() 
return the required number of largest 
or smallest elements from an iterable.
"""

h = [10, 20, 15, 30, 40]
heapq.heapify(h)

maxi = heapq.nlargest(3, h)
print("3 largest elements:", maxi)

min = heapq.nsmallest(3, h)
print("3 smallest elements:", min)