"""
recursion
time: O(n * n!)
space: O(n)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        unseen_set = set(nums)

        def genPermutation(cur_list):
            if len(cur_list) == len(nums):
                return_list.append(cur_list.copy())
            
            for next_num in list(unseen_set):
                unseen_set.remove(next_num)
                cur_list.append(next_num)
                genPermutation(cur_list)
                cur_list.pop()
                unseen_set.add(next_num)

        genPermutation([])
        return return_list
"""
permutation -> recursion
distinct integers -> can simply use set to keep track of unseen items
-> using set to perform add and remove in O(1) time
"""
