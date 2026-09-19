# Key idea: Track how each state reuses results from smaller subproblems.
from typing import  List
# Group the state and operations used by the min cost climbing stairs implementation.
class Solution:
    # Compute or update the min cost climbing stairs result for the supplied input.
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        cost.append(0)
        min_cost_dict = {}
        # Compute or update the helper result for the supplied input.
        def helper(i: int) -> int:
            # Choose this path when `i in min_cost_dict.keys()` is true.
            if i in min_cost_dict.keys():
                return min_cost_dict[i]
            # Choose this path when `i <= 1` is true.
            if i <= 1:
                min_cost_dict[i] = cost[i]
                return cost[i]
            min_cost = min(helper(i - 1), helper(i - 2)) + cost[i]
            min_cost_dict[i] = min_cost
            return  min_cost

        return helper(len_cost)

sol = Solution()
cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs(cost))    

"""without memoization, 
T(n) = O(2^n)
S(n) = O(n)
"""
"""with memoization, 
T(n) = O(n)
S(n) = O(n)
"""