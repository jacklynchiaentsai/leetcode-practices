"""
sliding window
n = len(s)
m = size of character set
time: O(n)
space: O(min(m, n))
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start, end = 0, 0
        maxlen = 0
        index_dict = {}

        while end < len(s):
            cur_char = s[end]

            if cur_char in index_dict and index_dict[cur_char] >= start:
                start = index_dict[cur_char] + 1

            index_dict[cur_char] = end
            maxlen = max(maxlen, end - start + 1)
            end += 1

        return maxlen
"""
string is empty -> 0
start, end = 0
maxlen = 0
index_dict = {char: last_seen_index}

while end < len(s):
    get s[end]
    last_seen = index[s[end]]
    if last_seen >= start:
        move start to index_dict[s[end]] + 1

    update s[end] to index_dict

    update maxlen = max(maxlen, end-start+1)
    end += 1


    

"""
