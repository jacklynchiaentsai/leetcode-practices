"""
sort + two pointer (two sum)
time: O(n^2)
space: O(1)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        prevnum = None
        nums.sort()

        for i in range(0, len(nums)-2):
            firstnum = nums[i]

            if firstnum == prevnum:
                continue

            if firstnum > 0:
                break
            
            left = i + 1
            right = len(nums) - 1
            targetsum = 0 - nums[i]

            while left< right:
                sumval = nums[left] + nums[right]

                if sumval == targetsum:
                    # avoid duplicate solutions
                    if nums[left] != nums[left - 1] or (left- 1) == i:
                        res.append([firstnum, nums[left],  nums[right]])
                    right -= 1
                    left += 1
                elif sumval > targetsum:
                    right -= 1
                else:
                    left += 1
            
            prevnum = firstnum

        return res

"""
nums = [-1,0,1,2,-1,-4]
[-4, -1, -1, -1, 2, 2]

res = []
prevnum = None
go through each numi in nums all the way up to third to last number:
    if numi == prevnum:
        continue
    
    use two pointer approach to find two numbers 
    that sum to (0 - numi)
    left = curIndex + 1
    right = end of list
        while left < right:
            
            if sum of left right pointer values > (0 - numi):
                right -= 1
            elif smaller:
                left += 1
            else:
                add solution to res

    prevnum = numi
""" 
