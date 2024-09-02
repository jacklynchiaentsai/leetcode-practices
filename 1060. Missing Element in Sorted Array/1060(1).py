"""
binary search
adjusting boundary updates to avoid infinite loop
time: O(log(n))
space: O(1)
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        # handling when missing number is beyond last element of nums
        if nums[high] - nums[low] - high < k:
            return nums[0] + len(nums) - 1 + k

        while low < high:
            mid = low + (high-low) // 2

            expectedNums = nums[mid] - nums[0] - 1
            actualNums = mid - 1

            missingNums = expectedNums - actualNums
            
            if missingNums >= k:
                high = mid
            else:
                # handling infinite loop case when mid = 0
                # need to adjust upon final answer
                low = mid + 1
        
        # starting point + actual nums + missing nums
        return nums[0] + (low - 1) + k
    
