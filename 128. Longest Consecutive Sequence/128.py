"""
O(1) searching -> set or dictionary
time: O(n)
space: O(n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxlen = 0 
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_len = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_len += 1
                    current_num += 1
                
                maxlen = max(maxlen, current_len)

        return maxlen

"""
edge: if empty return 0
maxlen
intial -> sort -> keep track of previous element and update maxlen

convert nums to set
for num in nums_set:
    if num - 1 not in nums_set:
        current_len = 1
        current_num = num
        repeatedly search for current_num + 1 and update current_len

    update maxlen
"""
