from typing import List
class Solution:
    # Exploit sorted input: the left pointer raises the sum and the right pointer lowers it.
    # Each pointer moves only inward, giving O(n) time and O(1) space; a solution is assumed.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers) - 1

        while l_ptr!=r_ptr:
            if numbers[l_ptr] + numbers[r_ptr] == target:
                # The problem asks for one-based positions, so convert both zero-based indices.
                return [l_ptr+1,r_ptr+1]
            # A sum that is too large rules out the current right value with every remaining left value.
            elif numbers[l_ptr] + numbers[r_ptr] > target:
                r_ptr -=1
            else:
                l_ptr +=1

                

