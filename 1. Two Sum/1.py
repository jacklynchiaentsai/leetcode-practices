"""
dictionary
time: O(n)
space: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} # num: index

        for i, num in enumerate(nums):
            find_num = target - num
            if find_num in nums_dict:
                return [nums_dict[find_num], i]
            
            nums_dict[num] = i
