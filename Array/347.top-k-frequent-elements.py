# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
from typing import Optional, List
# Group the state and operations used by the top k frequent elements implementation.
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


        dict_elem = dict(sorted(dict_elem.items(),
                                key = lambda item : item[1], reverse = True))

        keys = list(dict_elem.keys())
        return keys[0:k]    


sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent( nums = [1], k = 1))
print(sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))