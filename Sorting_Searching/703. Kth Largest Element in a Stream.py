from typing import List
import heapq


# The intended invariant is a min-heap of the k largest stream values; its root is kth largest.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Copy the first k candidates so heap operations do not rearrange the original input list.
        self.heap = nums[0:k]
        heapq.heapify(self.heap)
        left_nums = nums[k:]
        for num in left_nums:
            # Once full, replace the weakest retained value only when a larger candidate arrives.
            if num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    # For a full heap this performs a bounded-heap update in O(log(k + 1)) time.
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        # This is a second independent if: after an underfilled-heap insertion, it can insert val again.
        # That can discard a valid earlier value and duplicate the new one; the underfilled case is not generally correct.
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