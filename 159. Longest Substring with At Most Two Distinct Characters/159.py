"""
time: O(n)
space: O(1)
sliding window: keeping track of last occurence
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        end = 0
        chardict = {}
        maxsize = 0

        while end < len(s):
            currentchar = s[end]
            chardict[currentchar] = end

            if len(chardict) > 2:
                minindex = len(s)
                for key, value in chardict.items():
                    minindex = min(minindex, value)
                del chardict[s[minindex]]
                start = minindex + 1

            maxsize = max(maxsize, end - start + 1)
            end += 1

        return maxsize       


"""
start end
chardict = { char: last index occured}
maxsize
eceba
"""
