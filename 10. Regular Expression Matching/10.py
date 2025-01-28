"""
top down dynamic programming + memoization
m = len(s)
n = len(p)
going through all possible combinations of s_idx and p_idx only once
time: O(m*n)
space: O(m*n)
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {} # (s_idx, p_idx): result

        def dp(s_idx, p_idx):
            if (s_idx, p_idx) in cache:
                return cache[(s_idx, p_idx)]
            
            if s_idx >= len(s) and p_idx >= len(p):
                return True
            elif p_idx >= len(p):
                return False

            match = (s_idx < len(s)) and (s[s_idx] == p[p_idx] or p[p_idx] == '.')

            if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
                cache[(s_idx, p_idx)] = (match and dp(s_idx + 1, p_idx)) or dp(s_idx, p_idx + 2)
            else:
                if match:
                    cache[(s_idx, p_idx)] = dp(s_idx + 1, p_idx + 1)
                else:
                    cache[(s_idx, p_idx)] = False

            return cache[(s_idx, p_idx)]

        return dp(0, 0)

            


            
"""
edge cases
- s is empty p would have to be empty or _*
- if p is empty then s would have to be empty to return true otherwise false

s_idx, p_idx

aba
a*a*b
c*a*b

consider sometimes where choosing to add preceding element might not be best choice even though there is a direct match:
a*.b
ab

whenever we encounter a star we can either choose to add the preceding element or not 
-> current decision will determine the string we can form and therefore impact our future decisions
-> dynamic programming problem

if next element of the p_idx is *:
    if p[p_idx] == s[s_idx] (consider . to be a match):
        s_idx += 1, p_idx be same
    or:
        s_idx, p_idx += 2

"""
