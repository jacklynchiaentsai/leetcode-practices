"""
fibnacci pattern dp
time: O(n)
space: O(n)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mincost = [0] * n

        mincost[0] = cost[0]
        mincost[1] = cost[1]

        for i in range(2, n):
            mincost[i] = min(mincost[i-1], mincost[i-2]) + cost[i]

        return min(mincost[n-1], mincost[n-2])
"""
future decision depends on previous decisions -> dynamic programming

mincost = [0] * len(cost)
-> represents the minimum number of costs to climb at each step i


initialization 
-> steps with index 0 and 1 with their own value

for each step i can only come from one step or two steps before
steps[i] = min(steps[i-1], steps[i-2]) + cost[i]

return steps[len(cost)-1] - cost[len(cost) - 1]
-> don't need to pay the cost of the final step
"""
