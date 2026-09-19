# Key idea: Track how values move toward their final sorted positions.
from typing import List
# Group the state and operations used by the two sum ii input array is sorted implementation.
class Solution:
    # Compute or update the two sum result for the supplied input.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers) - 1

        # Keep processing while `l_ptr != r_ptr` remains true.
        while l_ptr!=r_ptr:
            # Choose this path when `numbers[l_ptr] + numbers[r_ptr] == target` is true.
            if numbers[l_ptr] + numbers[r_ptr] == target:
                return [l_ptr+1,r_ptr+1]
            # Choose this path when `numbers[l_ptr] + numbers[r_ptr] > target` is true.
            elif numbers[l_ptr] + numbers[r_ptr] > target:
                r_ptr -=1
            else:
                l_ptr +=1

                

