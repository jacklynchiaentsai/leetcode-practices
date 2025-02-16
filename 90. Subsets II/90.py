"""
sort + backtracking
time: O(n*2^n) n because of deep copy of the subset
space: O(n)
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_subsets = set()
        nums.sort()
        def create_subset(curIndex, curSubset):
            if curIndex >= len(nums):
                tup = tuple(curSubset)
                all_subsets.add(tup)
                return

            curSubset.append(nums[curIndex])
            create_subset(curIndex + 1, curSubset)
            curSubset.pop()
            create_subset(curIndex + 1, curSubset)

        create_subset(0, [])

        ans = []
        for element in all_subsets:
            ans.append(element)

        return ans
"""
O(2^n)
all_subsets = set() -> each element in subset should be in a sorted order

sort nums
def create_subset(curIndex, curSubset):
    if curIndex goes out of bounds:
        convert curSubset to tup
        add tup to all_subsets
        return
    
    curSubset.append(curElement)
    create_subset(curIndex + 1, curSubset)
    curSubset.pop()
    create_subset(curIndex + 1, curSubset)

create_subset(0, [])

""" 
