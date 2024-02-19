"""
n: number of characters in string
time: O(n)
space: O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words_li = s.split()
        return " ".join(reversed(words_li))
