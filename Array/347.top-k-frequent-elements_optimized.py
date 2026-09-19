# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import Optional, List
import heapq

# Group the state and operations used by the top k frequent elements optimized implementation.
class Solution:
    # Compute or update the top kfrequent result for the supplied input.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_elem = {}

        # Process each value from `range(len(nums))`.
        for i in range(len(nums)):
            # Choose this path when `nums[i] in dict_elem` is true.
            if nums[i] in dict_elem:
                dict_elem[nums[i]] = dict_elem[nums[i]] + 1
            else:
                dict_elem[nums[i]] = 1

        h = []
        # Process each value from `dict_elem.items()`.
        for key, val in dict_elem.items():
            heapq.heappush(h, (val,key))

            # Choose this path when `len(h) > k` is true.
            if len(h) > k:
                heapq.heappop(h)

        #for i in range(len(h)):
        #    print(h[i])

        result = [heapq.heappop(h)[1] for i in range(k)]        
        return result  


sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent( nums = [1], k = 1))
print(sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))

"""
T(n) = O(nlog(k))
S(n) = O(n+k) # size of heap and dict

Algorithm
Build a frequency map that counts how many times each number appears.
Create an empty min-heap.
For each number in the frequency map:
Push (frequency, number) into the heap.
If the heap size becomes greater than k, pop once to remove the smallest frequency.
After processing all numbers, the heap contains the k most frequent elements.
Pop all elements from the heap and collect their numbers into the result list.
Return the result.

"""
