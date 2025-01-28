"""
recursion + backtracking
n = len(nums)
time: O(n* 2^n) n: copying to output list
space: O(n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution_set = []
        def findsubset(curIndex, curSubset):
            if curIndex >= len(nums):
                solution_set.append(curSubset.copy())
                return
            
            curSubset.append(nums[curIndex])
            findsubset(curIndex + 1, curSubset)
            curSubset.pop()
            findsubset(curIndex + 1, curSubset)

        findsubset(0,[])
        return solution_set
"""
solution_set = set()

def findsubset(curIndex, curSubSet):
    if curIndex is out of bounds:
        add curSubSet.copy() to solution_set
    
    curSubset.append(nums[curIndex])
    findsubset(curIndex + 1, curSubset)
    curSubset.pop()
    findsubset(curIndex + 1, curSubset)
"""
