class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curptr = 0
        replaceptr = 0
        
        counter = 0
        curnum = nums[0]
        
        while curptr < len(nums):
            if nums[curptr] == curnum:
                counter += 1
            else:
                counter = 1
                curnum = nums[curptr]

            if counter > 2:
                while curptr < len(nums):
                    if nums[curptr] == curnum:
                        curptr += 1
                    else:
                        counter = 1
                        curnum = nums[curptr]
                        break
            
            if curptr < len(nums):
                nums[replaceptr] = nums[curptr]
            else:
                break
            
            replaceptr += 1
            curptr += 1

        return replaceptr
            
                
            

"""
intuition:
remove in place through pop by index -> O(n) operation for each deletion

two pointers for swapping:
curptr: current index on
replaceptr: index I should replace value with

curptr = replaceptr = 0
counter = 0

nums = [0,0,1,1,2,3,3,1,1]

replaceptr = 4
curptr = 6
"""
