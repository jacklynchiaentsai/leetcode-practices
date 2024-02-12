"""
intuition: nums = nums[len(nums)-k:] + nums[0: len(nums) - k - 1]
divide and conquer, reversing list
time: O(n)
space: O(1)
"""
class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])

        
