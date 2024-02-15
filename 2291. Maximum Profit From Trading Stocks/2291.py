"""
time: O(n^2)
space: O(n+m)
m: budget
"""
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        profit = [future[i] - present[i] for i in range(n)]
        dp = [0] * (budget+1)

        for i in range(n):
            for b in range(budget, present[i]-1, -1):
                dp[b] = max(dp[b], profit[i] + dp[b-present[i]])
        
        return dp[budget]

"""
dynamic programming
can buy each stock at most once
dp =[] 0-budget size: budget+1: maximum profit I can make given budget =i
initialize dp[0] = 

profit[i] = future[i]- present[i]
dp[budget]
"""
