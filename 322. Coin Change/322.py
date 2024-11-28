"""
dynamic programming (bottom up)
n = len(coins)
m = amount
time: O(mn)
space:O(m)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(1, len(dp)):
                if (i-coin) >=0 and (i-coin) <= amount:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        # print(dp)
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
"""
clarifications
- coin[i] > 0
- amount >= 0 

dynamic programming
dp should have size of amount + 1: i ranges from 0 to amount
-> handle out of bound edge cases
dp[i] = minimum number of coins I need to make up amount i

initialization of dp
dp[i] = float('inf')
dp[0] = 0

for each coin:
    for each index i from smallest to larget in dp where i > 0:
        dp[i] = min(dp[i], dp[i-coin] + 1)

return dp[amount] -> check if infinity then return -1 instead
"""
