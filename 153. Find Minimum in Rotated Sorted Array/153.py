"""
binary search
time: O(log(n))
space: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if mid == 0:
                # special case to avoid out of bounds error
                if nums[mid] > nums[mid + 1]:
                    return nums[mid+1]
                # array is regularly sorted
                elif nums[mid] < nums[-1]:
                    return nums[0]
                else:
                    low = mid + 1
                
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[-1]:
                high = mid - 1
            else:
                low = mid + 1
    
"""
sorted n times -> regular sorted array
-> nums[0]
sorted < n:
-> identify the pivot index
- the last element of my rotated array would be the largest of the rotated part
- if current point < last element -> current point is in the rotated
- otherwise it is not in rotated part

low = 0
high = len(nums) - 1

while low <= high:
    mid
    if mid == 0:
        break
    if nums[mid-1] > nums[mid]:
        return nums[mid]
    elif nums[mid] < nums[-1]:
        high = mid - 1
    else:
        low = mid + 1

regular sorted array
return nums[0]
    
"""
