"""
time: O(n)
space: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            bestSum = max(currentSum, bestSum)

        return bestSum
"""
sliding window? -> no because need a specific criteria to make subarray valid -> too many possibilities
maximum subarray problem -> kadane's algorithm dp
"""
