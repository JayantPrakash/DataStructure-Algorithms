# Key idea: Track heap ordering and which element is kept at the root.
import heapq
from typing import List


# Group the state and operations used by the Kth Largest Element in an Array implementation.
class Solution:
    # Compute or update the find kth largest result for the supplied input.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        # Process each value from `nums`.
        for num in nums:
            # Choose this path when `len(heap) < k` is true.
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                # Choose this path when `num > heap[0]` is true.
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]

