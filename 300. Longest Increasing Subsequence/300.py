"""
dynamic programming

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)
"""
dynamic programming
dp[i] = length fo longest strictly increasing subsequence that ends in nums[i]

initialization:
dp[0] = 1
i should be range of indices for nums

for i from 1 to len(nums):
    dp[i] = length of longest strictly increasing subsequence that ended in j < i  + 1 where nums[j] < nums[i]
    for j from 0 to i:
        if nums[j] < nums[i]
            dp[i] = max(dp[j] + 1, dp[i])

return max(dp)
"""
