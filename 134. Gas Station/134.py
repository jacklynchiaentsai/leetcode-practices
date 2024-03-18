"""
greedy
- finding valid subsequence
time: O(n)
space: O(1)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank_total = 0
        curr_tank = 0
        start_idx = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            curr_tank += diff
            tank_total += diff

            if curr_tank < 0:
                start_idx = i+1
                curr_tank = 0
        
        if tank_total < 0:
            return -1
        else:
            return start_idx
"""
gas = [1,2,3,4,5], cost = [3,4,5,1,2]
diff = [-2, -2, -2, 3, 3]

diff = [4, -5, 1, -3, 2, 1]

tank_total = 
curr_tank = 
curr_start = 
"""
