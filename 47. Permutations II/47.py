import collections
"""
time: O(n * n!)
-> takes n steps to generate a single permutation with n! possible permutation worst case when all numbers are unique
space: O(n)
-> dictionary and recursion
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        count_dict = collections.Counter(nums)
        
        def permutation(cur_list):
            # base case if reached length of permutation
            if len(cur_list) == len(nums):
                # list is mutable so need to create a copy otherwise value would be altered!!
                return_list.append(cur_list.copy())
                return
            
            for key, value in count_dict.items():
                # consider only keys with frequency >0 that I can consider
                if value > 0:
                    # remove next_char from unseen count_dict as we're using it as our next item in list
                    count_dict[key] -= 1
                    cur_list.append(key)
                    permutation(cur_list)
                    # add it back to the unseen count_dict as we're using a different key for next iteration
                    cur_list.pop()
                    count_dict[key] += 1

        permutation([])
        return return_list

            

        
"""
permutation that might contain duplicates
- recursion
- count_dict to obtain unique elements by key yet uses count to keep track of availability

iterate through all possible options (keys) in count_dict
"""
