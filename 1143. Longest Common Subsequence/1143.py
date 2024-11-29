"""
multidimensional bottom up DP
n = len(text1)
m = len(text2)
time: O(mn)
space: O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]

"""
edge cases : if either string is empty then lcs == 0
dynamic programming: subsequebce constructed depends on which characters I chose or left off previously

dp[i][j] = length of the lcs that can be formed from text1[:i], text2[:j]
end point non inclusive
i would range from 0 to len(text1), j would range from 0 to len(text2)

intialization:
dp[0][any j] = 0
dp[any i][0] = 0
intialize all values to be 0

i would range from 0 to len(text1):
    j would range from 0 to len(text2):
        check for out of bounds error
        if text1[i-1] == text2[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        
        this would work because they are previously calculated values
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
i = 3
j = 3

dp[len(text1)][len(text2)]
"""
