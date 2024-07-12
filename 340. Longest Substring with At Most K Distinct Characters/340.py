"""
sliding window
n = len(s)
time: O(n)
space: O(k) -> k is maximum number of distinct numbers O(k+1)
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k ==0:
            return 0
        start = 0
        end = 0
        visited_char = {s[start]: 1}
        max_len = 0

        while end < len(s):
            while len(visited_char) <= k:
                end += 1
                if end >= len(s):
                    break
                cur_char = s[end]
                if cur_char not in visited_char:
                    visited_char[cur_char] = 0
                
                visited_char[cur_char] += 1
            
            max_len = max(max_len, end - start)

            while len(visited_char) > k and start < end:

                cur_char = s[start]
                visited_char[cur_char] -= 1
                
                if visited_char[cur_char] == 0:
                    del visited_char[cur_char]

                start += 1

        return max_len
