"""
dictionary
n = len(s) = len(t)
time: O(n)
space: O(n)
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 0

            char_dict[char] += 1
        
        for char in t:
            if char in char_dict:
                char_dict[char] -= 1

                if char_dict[char] ==0:
                    del char_dict[char]
            
        numSteps = 0
        for key, value in char_dict.items():
            numSteps += value
        
        return numSteps

"""
char_dict = {char: freq} -> update with s
for char in t
-> exists in char_dict => freq -= 1
-> freq == 0 -> remove from char_dict

s = bab
t = aba

"""
