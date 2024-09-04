"""
case handling and logical deduction
time: O(n)
space: O(1)
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) == 1:
            s_index = 0
            t_index = 0
            encountered = False
            while s_index < len(s) and t_index < len(t):
                if s[s_index] != t[t_index] and encountered:
                    return False
                elif s[s_index] != t[t_index] and not encountered:
                    encountered = True
                    if len(s) > len(t):
                        s_index += 1
                    else:
                        t_index += 1
                    if s[s_index] != t[t_index]:
                        return False
                
                s_index += 1
                t_index += 1

            return True

        elif len(s) == len(t) and s != t:
            encountered = False
            
            for i in range(len(s)):
                if s[i] != t[i] and not encountered:
                    encountered = True
                elif s[i] != t[i] and encountered:
                    return False
            
            return True

        else:
            return False
