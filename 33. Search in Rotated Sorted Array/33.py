"""
modified + multiple binary search
time: O(logn)
space: O(1)
"""
class Solution:
    def binsearch(self, nums, target, start, end):
        while start<= end:
            mid = int(start + (end-start)/2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        pivot = -1
        
        if nums[start] > nums[end]:
            while start <= end:
                mid = int(start + (end-start)/2)
                # consider the edge case where the pivot is at the 0th index
                if (mid ==0 and nums[mid] > nums[mid+1]) or (nums[mid] > nums[mid-1] and nums[mid]> nums[mid+1]):
                    pivot = mid
                    break
                # comparing with last value because each side of pivot is either greater or smaller than last element
                # pivot is at the right of mid
                elif nums[mid] > nums[-1]:
                    start = mid + 1
                else:
                    end = mid - 1
                
        if pivot == -1:
            return self.binsearch(nums, target, 0, len(nums)-1)
        else:
            firstsearch = self.binsearch(nums, target, 0, pivot) 
            if firstsearch != -1:
                return firstsearch
            secondsearch = self.binsearch(nums, target, pivot+1, len(nums)-1) 
            if secondsearch != -1:
                return secondsearch
            else:
                return -1

        
"""
binary search
1) single upward sloping
2) two non continuous upward sloping

start = 0
end = len(nums) - 1
-> mid = start + (end- start)/ 2

[4,5,6,7,0,1,2] target = 0
1) search for pivot index
2) search for target

"""
