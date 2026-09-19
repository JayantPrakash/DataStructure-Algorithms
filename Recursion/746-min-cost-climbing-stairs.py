from typing import  List
class Solution:
    # helper(i) is the cheapest cost to reach and pay for step i; the top has cost zero.
    # Memoization gives O(n) time and O(n) cache/stack space.
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        # Add the top as a zero-cost destination; this changes the caller's list.
        cost.append(0)
        min_cost_dict = {}
        def helper(i: int) -> int:
            if i in min_cost_dict.keys():
                return min_cost_dict[i]
            # Either of the first two steps may be the starting step, so its own cost is sufficient.
            if i <= 1:
                min_cost_dict[i] = cost[i]
                return cost[i]
            # Arrive from one or two steps below, choose the cheaper route, then pay the current step.
            min_cost = min(helper(i - 1), helper(i - 2)) + cost[i]
            min_cost_dict[i] = min_cost
            return  min_cost

        # Request the dummy top at the original list length, not the last paid step.
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