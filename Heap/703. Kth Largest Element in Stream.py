# Key idea: Track heap ordering and which element is kept at the root.
from typing import List
import heapq as hp
# Group the state and operations used by the Kth Largest Element in Stream implementation.
class KthLargest:

    # Initialize the state needed by a new instance.
    def __init__(self, k: int, nums: List[int]):
        self._nums = nums
        self._k = k
        hp.heapify(self._nums)
        # Keep processing while `len(self._nums) > k` remains true.
        while(len(self._nums) > k):
            hp.heappop(self._nums)

    # Compute or update the add result for the supplied input.
    def add(self, val: int) -> int:
        hp.heappush(self._nums,val)
        # Choose this path when `len(self._nums) > self._k` is true.
        if len(self._nums) > self._k:
            hp.heappop(self._nums)
        return self._nums[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

A = [4, 5, 8, 2]

kth = KthLargest(3, A)
print(kth.add(3))
print(kth.add(5))
print(kth.add(10))
print(kth.add(9))
print(kth.add(4))




