"""
dynamic programming
m = len(word1)
n = len(word2)
time: O(mn)
space: O(mn) -> can be optimized to O(m+n)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[float('inf')] * n  for _ in range(m)]
        
        # intialization
        for j in range(n):
            dp[0][j] = j

        for i in range(m):
            dp[i][0] = i

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    # account for all 3 operations
                    # insertion
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    # deletion
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
                    # replacement
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)
                    
        return dp[len(word1)][len(word2)]
"""
dynamic programming
dp[i][j] = min num operations required to convert word1[:i (non inclusive)] to word2[:j (non inclusive)]

intialization:
dp[0][any j] = j
dp[any i][0] = i
intialize all other values float('inf')

i from 1 to len(word1):
    j from 1 to len(word2):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        else:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)

dp[len(word1)][len(word2)]
hor
dl
"""
