from typing import List
import heapq as hp
# Keep only the k largest values in a min-heap; its smallest value is the kth largest overall.
# Duplicates count as separate stream elements.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Reuse nums directly: heap construction and pruning mutate the caller's list.
        self._nums = nums
        self._k = k
        hp.heapify(self._nums)
        # Remove small values until at most k candidates remain; no future small value can improve the top k.
        while(len(self._nums) > k):
            hp.heappop(self._nums)

    # Push the new candidate and discard the minimum if capacity is exceeded: O(log(k + 1)) per update.
    def add(self, val: int) -> int:
        hp.heappush(self._nums,val)
        if len(self._nums) > self._k:
            hp.heappop(self._nums)
        # The root is the kth largest once at least k values have arrived; before that it is the minimum seen.
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




