"""
dynamic programming (bottom up)
n = len(nums)
t = total
time: O(n*t)
space: O(t)
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        prevdp = {}

        # edge case if target is not possible
        if target < (-1) * total or target > total:
            return 0

        for i in range((-1) * total, total+1):
            prevdp[i] = 0

        firstnum = nums[0]
        # consider the case of 0 where negation would be the same value
        prevdp[firstnum] += 1
        prevdp[(-1) * firstnum] += 1

        for i in range(1, len(nums)):
            curdp = {}
            for j in range((-1) * total, total+1):
                curdp[j] = 0
            
            for cursum, numWays in prevdp.items():
                plussum = cursum + nums[i]
                minussum = cursum - nums[i]
                if plussum >= (-1) * total and plussum <= total:
                    curdp[plussum] += numWays
                if minussum >= (-1) * total and minussum <= total:
                    curdp[minussum] += numWays

            prevdp = curdp

        return prevdp[target]

        


        

"""
dynamic programming whether or not I can achieve target after examining all the integers in nums depends on my earlier decisions

total = totals sum of list
sum range: -total to total
dp[i][sum] = numOfWays we can make up sum given nums[:i (inclusive)]
-> only depend on i-1 so can update prevdp
dp = {sum: numOfWays given previous array}

firstnum
initialize dp
dp[firstnum] = 1
dp[-firstnum] = 1
for all the remaining values if it does not exist in dp we assume as 0

traverse throught rest of nums
nums[i]
    traverse through dp -> key: cursum, value: numWays 
    dp[cursum + nums[i]] += numWays
    dp[cursum - nums[i]] += numWays

return dp[target]

"""
