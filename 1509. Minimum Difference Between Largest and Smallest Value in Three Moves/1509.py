"""
greedy + math
time: O(nlogn)
space: O(1)
"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        four_largest = nums[len(nums) - 4: len(nums)]
        four_smallest = nums[:4]

        mindiff = 1e18
        for i in range(4):
            mindiff = min(mindiff, four_largest[i] - four_smallest[i])

        return mindiff

"""
intuition:
changing the largest and smallest value also redefines the largest and smallest value

len(nums) <= 4:
return 0

len(nums) > 4:
given limitation of 3 steps evaluate the mindiff
4thlargest, 3rdlargest, 2ndlargest, largest 
smallest, 2ndsmallest, 3rdsmallest, 4thsmallest

1,2,3,4,5
2,3,4,5
1,2,3,4
"""
