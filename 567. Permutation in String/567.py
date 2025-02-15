"""
sliding window + check anagrams
n = len(s1)
m = len(s2)
time: O(m)
space: O(1)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict, s2_dict = {}, {}

        def isSame():
            if len(s1_dict) != len(s2_dict):
                return False
            
            for key, value in s1_dict.items():
                if key not in s2_dict:
                    return False
                if s2_dict[key] != value:
                    return False

            return True

        if len(s1) > len(s2):
            return False
        
        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 0
            s1_dict[char] += 1

        for i in range(0, len(s1)):
            char = s2[i]
            if char not in s2_dict:
                s2_dict[char] = 0
            s2_dict[char] += 1

        start = 0
        end = len(s1) - 1

        while end < len(s2):
            if isSame():
                return True

            s2_dict[s2[start]] -= 1
            if s2_dict[s2[start]] == 0:
                del s2_dict[s2[start]]
            
            if end + 1 < len(s2):
                newchar = s2[end + 1]
                if newchar not in s2_dict:
                    s2_dict[newchar] = 0
                s2_dict[newchar] += 1

            start += 1
            end += 1

        return False

"""
if have sliding window of fixed size each time just have to update start and end pointers
edge case:
if len(s1) > len(s2):
    return False

s1 = "adc", s2 = "dcda"
create s1_dict = {a: 1,  c: 1, d: 1}

iterate from 0 - len(s1) create s2_dict = {d:2, c:1 }
start = 0
end = len(s1) - 1 ->  inclusive

while end < len(s2):
    check if s1_dict the same as s2_dict:
        return True

    update s2_dict to decrease frequency of s2[start]
    make sure to delete when the character's frequency hits 0
    if end + 1 < len(s2):
        update s1_dict to increase frequency of s2[end + 1]
    else:
        break

    start += 1
    end += 1

return False





""" 
