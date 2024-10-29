'''
two pointer approach: fast and slow runner
remove elements in array in place: keep track of next point to replace
time: O(n)
space: O(1)
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        overwrite_index = 0

        for i in range(0, len(nums)):

            if (i != 0) and (nums[i] == nums[i-1]):
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[overwrite_index] = nums[i]
                overwrite_index += 1

        return overwrite_index

