"""
binary search
time: O(logn)
space: O(1)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = int(start + (end - start) / 2)

            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid
        
        return start
"""
intuitions
1. peak element must always exist because (think about upward downward slopes)
- no adjacent elements are equal
- boundaries are defined by negative infinity 
2. log(n) -> binary search -> narrowing search range by 1/2 everytime
- compare against neighbor: where would peak element "potentially" be?
- intuition from linear scan

nums = [1,2,1,3,5,6,4]
start = 0
end = len(nums)-1
mid = start + (end - start) / 2
condition while start < end:
if nums[mid] > nums[mid+1]:
    end = mid
else:
    start = mid + 1

"""
