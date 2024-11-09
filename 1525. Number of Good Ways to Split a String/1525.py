"""
use dictionary and set to count character frequency
time: O(n)
space: O(n)
"""

class Solution:
    def numSplits(self, s: str) -> int:
        right_dict = {}
        left_set = set()
        num_good = 0

        for char in s:
            if char not in right_dict:
                right_dict[char] = 0
            right_dict[char] += 1
        
        for i in range(0, len(s) - 1):
            char = s[i]
            left_set.add(char)
            right_dict[char] -= 1

            if right_dict[char] == 0:
                del right_dict[char]
            
            if len(left_set) == len(right_dict):
                num_good += 1

        return num_good


"""
intuition: (brute force)
go through indices 0 ~ len(s) - 2 and examine distinct integers
left_set = set()
right_dict = {char: freq > 0}

1st iteration to populate right_dict
2nd iteration:
and at each index from 0 ~ len(s) - 2 
update left_set, right_dict (decrement, make sure to remove freq = 0)
-> determine if it is good split
"""
