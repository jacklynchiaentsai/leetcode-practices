"""
time: O(n)
space: O(1)
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums) - 1):
            num = nums[i]
            nextnum = nums[i+1]

            numMissing = nextnum - num - 1

            if numMissing >= k:
                return num + k
            else:
                k -= numMissing

        return nums[len(nums) - 1] + k
