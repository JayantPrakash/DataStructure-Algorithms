from typing import  List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        cost.append(0)
        min_cost_dict = {}
        def helper(i: int) -> int:
            if i in min_cost_dict.keys():
                return min_cost_dict[i]
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