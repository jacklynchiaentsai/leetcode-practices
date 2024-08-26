"""
time: O(n)
space: O(1)
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        isUpward = True

        for i in range(0, len(nums) - 1):
            first = nums[i]
            second = nums[i+1]

            if (isUpward and first > second) or (not isUpward and first< second):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

            isUpward = not isUpward

        

        
