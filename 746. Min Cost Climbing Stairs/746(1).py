"""
fibnacci pattern dp
time: O(n)
space: O(1)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        two_steps = cost[0]
        one_steps = cost[1]

        for i in range(2, n):
            current_cost = min(one_steps, two_steps) + cost[i]
            two_steps = one_steps
            one_steps = current_cost


        return min(one_steps, two_steps)
"""
can further reduce it to constant space as we only need to know one and two steps before each time
"""
