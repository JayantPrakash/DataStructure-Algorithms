from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[0:k]
        heapq.heapify(self.heap)
        left_nums = nums[k:]
        for num in left_nums:
            if num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

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