# Key idea: Track heap ordering and which element is kept at the root.
from typing import List
import heapq


# Group the state and operations used by the Kth Largest Element in a Stream implementation.
class KthLargest:

    # Initialize the state needed by a new instance.
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[0:k]
        heapq.heapify(self.heap)
        left_nums = nums[k:]
        # Process each value from `left_nums`.
        for num in left_nums:
            # Choose this path when `num > self.heap[0]` is true.
            if num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    # Compute or update the add result for the supplied input.
    def add(self, val: int) -> int:
        # Choose this path when `len(self.heap) < self.k` is true.
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        # Choose this path when `val > self.heap[0]` is true.
        if val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
#kthLargest = KthLargest(3, [4, 5, 8, 2]);

kthLargest = KthLargest(5,[1,2,3,4,5,-1,-5,50,80])
kthLargest.add(-1);
kthLargest.add(-5);

"""
kthLargest.add(10);
kthLargest.add(9);
kthLargest.add(4);
"""