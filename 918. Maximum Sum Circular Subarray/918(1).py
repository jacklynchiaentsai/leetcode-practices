"""
kadane dp + prefix sum
time: O(n)
space: O(1)
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # solving for normal sum
        curSum = nums[0]
        bestSum = nums[0]

        for i in range(1, n):
            curSum = max(nums[i], curSum + nums[i])
            bestSum = max(curSum, bestSum)

        # solving for special sum
        # initializing as zero because we only want to keep minsum < 0
        curSum = 0
        bestMinSum = 0
        listsum = 0
        for i, num in enumerate(nums):
            curSum = min(num, curSum + num)
            bestMinSum = min(bestMinSum, curSum)
            listsum += num
        
        # checking for edge case that entire list is negative in that case using bestMinSum results in empty subarray
        if bestMinSum != listsum:
            bestSum = max(bestSum, listsum - bestMinSum)
        

        return bestSum

"""
solving for special sum
trying to find the largest prefix and suffix sum combination
-> essentially trying to find the minimum subarray in list that separates prefix and suffix sum
observation of edge cases:
- largest range the prefix and suffix sum can cover is the entire list
-> i.e. sum of entire list
- would only want to use the minimum subarray to separate prefix and suffix sum when its sum is <0 
"""
